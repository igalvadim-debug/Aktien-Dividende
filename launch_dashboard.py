#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Панель акций (Stock Dashboard) на русском языке.

Запускает локальный веб-сервер (только на этом компьютере, http://localhost:8765).
При клике на акцию собирает живые данные ПАРАЛЛЕЛЬНО и строит отчёт:
  - Yahoo Finance : котировка, профиль, история дивидендов
  - QVeris        : объявленные дивиденды (даты ex-Tag и выплаты), кэш 24 ч (тратит кредиты!)
  - Finnhub       : профиль компании и новости (новости — только для US-тикеров)
  - Tavily        : свежие статьи из интернета

Список бумаг лежит в stocks.json, иконки — в папке icons (недостающие докачиваются
в фоне модулем icon_fetcher.py).
"""
import hashlib
import json
import logging
import mimetypes
import re
import statistics
import sys
import threading
import time
import webbrowser
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote

import requests
from requests.adapters import HTTPAdapter

try:
    import yfinance as yf
    logging.getLogger("yfinance").setLevel(logging.CRITICAL)  # без спама про 404
except Exception:  # pragma: no cover
    yf = None

# ─── НАСТРОЙКИ ───────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent
ICONS_DIR = ROOT / "icons"
TEMPLATE_FILE = ROOT / "dashboard_template.html"
STOCKS_FILE = ROOT / "stocks.json"
CACHE_DIR = ROOT / "_cache"
CACHE_DIR.mkdir(exist_ok=True)

HOST = "127.0.0.1"          # только этот компьютер, из сети недоступно
PORT = 8765
BASE_URL = f"http://localhost:{PORT}"

REPORT_TTL = 15 * 60         # готовый отчёт кэшируем на 15 минут
QV_TTL = 24 * 3600           # дивиденды QVeris — на сутки (экономим кредиты)
QV_FAIL_TTL = 6 * 3600       # неудачу тоже помним, чтобы не ждать повторно

# ─── .env С КЛЮЧАМИ ──────────────────────────────────────────────────────
def load_env(path):
    env = {}
    try:
        text = Path(path).read_text(encoding="utf-8-sig")
    except OSError:
        return env
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        # Ключ QVeris записан в виде «https://qveris.ai/account?page=api-key sk-…»
        m = re.search(r"\b(sk-[A-Za-z0-9_\-]{16,})", line)
        if "qveris" in line.lower() and m:
            env["QVERIS_KEY"] = m.group(1)
            continue
        if "=" in line:
            k, v = line.split("=", 1)
        else:
            parts = line.split(None, 1)
            if len(parts) != 2:
                continue
            k, v = parts
        env[k.strip()] = v.strip().strip("\"'")
    return env


ENV = load_env(ROOT / ".env")
FINNHUB_KEY = ENV.get("NEXT_PUBLIC_FINNHUB_API_KEY")
FINNHUB_BASE = ENV.get("FINNHUB_BASE_URL", "https://finnhub.io/api/v1")
TAVILY_KEY = ENV.get("tavily") or ENV.get("TAVILY_API_KEY")
QVERIS_KEY = ENV.get("QVERIS_KEY")

# ─── СПИСОК БУМАГ ────────────────────────────────────────────────────────
def load_stocks():
    return json.loads(STOCKS_FILE.read_text(encoding="utf-8"))


STOCKS = load_stocks()
STOCK_BY_TICKER = {s["ticker"]: s for s in STOCKS}

# ─── HTTP-СЕССИЯ И КЭШ ───────────────────────────────────────────────────
SESSION = requests.Session()
SESSION.mount("https://", HTTPAdapter(pool_connections=10, pool_maxsize=30))
SESSION.headers.update({"User-Agent": "StockDashboard/2.0"})


class TTLCache:
    def __init__(self):
        self._d = {}
        self._lock = threading.Lock()

    def get(self, key, ttl):
        with self._lock:
            item = self._d.get(key)
        if item and time.time() - item[0] < ttl:
            return item[1]
        return None

    def set(self, key, value):
        with self._lock:
            self._d[key] = (time.time(), value)


REPORT_CACHE = TTLCache()

# Защита от «thundering herd»: пока один поток собирает отчёт по тикеру,
# остальные ждут его результат, а не дублируют платные/тяжёлые запросы.
_BUILD_LOCKS = {}
_BUILD_LOCKS_GUARD = threading.Lock()


def _build_lock(ticker):
    with _BUILD_LOCKS_GUARD:
        lk = _BUILD_LOCKS.get(ticker)
        if lk is None:
            lk = _BUILD_LOCKS[ticker] = threading.Lock()
        return lk


_ICON_EXT_CACHE = {}  # {isin: "file.png" | None} — чтобы не статить диск при каждом рендере страницы


def _find_icon_file(isin):
    hit = _ICON_EXT_CACHE.get(isin)
    if hit is not None:
        return hit
    for ext in (".png", ".svg", ".jpg", ".webp"):
        if (ICONS_DIR / f"{isin}{ext}").exists():
            _ICON_EXT_CACHE[isin] = ext
            return ext
    _ICON_EXT_CACHE[isin] = ""
    return None


def get_icon_path(stock):
    icon_file = stock.get("icon")
    if icon_file and (ICONS_DIR / icon_file).exists():
        return f"/icons/{icon_file}"
    ext = _find_icon_file(stock["isin"])
    if ext:
        return f"/icons/{stock['isin']}{ext}"
    return None


# ─── FINNHUB ─────────────────────────────────────────────────────────────
def _fh_get(path, **params):
    if not FINNHUB_KEY:
        return None
    params["token"] = FINNHUB_KEY
    try:
        r = SESSION.get(f"{FINNHUB_BASE}/{path}", params=params, timeout=10)
        if r.status_code == 200:
            return r.json()
    except Exception:
        pass
    return None


def _is_us_symbol(sym):
    return "." not in sym  # Finnhub (бесплатно) даёт новости/профиль по символу только для США


def fetch_finnhub_profile(stock):
    if stock.get("kind") == "etf":
        return None
    p = _fh_get("stock/profile2", symbol=stock["ticker"]) if _is_us_symbol(stock["ticker"]) else None
    if not p:
        p = _fh_get("stock/profile2", isin=stock["isin"])
    return p or None


def fetch_finnhub_news(stock, days=7):
    if stock.get("kind") == "etf" or not _is_us_symbol(stock["ticker"]):
        return []
    to_date = date.today()
    news = _fh_get("company-news", symbol=stock["ticker"],
                   **{"from": (to_date - timedelta(days=days)).isoformat(), "to": to_date.isoformat()})
    return (news or [])[:15]


# ─── TAVILY ──────────────────────────────────────────────────────────────
def fetch_tavily(query, max_results=6):
    if not TAVILY_KEY:
        return []
    try:
        r = SESSION.post("https://api.tavily.com/search",
                         headers={"Authorization": f"Bearer {TAVILY_KEY}", "Content-Type": "application/json"},
                         json={"query": query, "max_results": max_results, "search_depth": "basic"},
                         timeout=20)
        if r.status_code == 200:
            return r.json().get("results", [])
    except Exception:
        pass
    return []


# ─── QVERIS (дивиденды: даты ex-Tag и выплаты) ───────────────────────────
QV_BASE = "https://qveris.ai/api/v1"
QV_TOOL = "qveris_finance.mkt_dividends"
QV_SESSION_ID = "stock-dashboard"
QV_CACHE_FILE = CACHE_DIR / "qveris_dividends.json"
_qv_lock = threading.Lock()
_qv_state = {"search_id": None, "credits": None}
_qv_disk = {}
try:
    _qv_disk = json.loads(QV_CACHE_FILE.read_text(encoding="utf-8"))
except Exception:
    _qv_disk = {}

_MISS = object()


def _qv_headers():
    return {"Authorization": f"Bearer {QVERIS_KEY}", "Content-Type": "application/json"}


def _qv_cache_get(sym):
    with _qv_lock:
        e = _qv_disk.get(sym)
    if not e:
        return _MISS
    ttl = QV_TTL if e.get("data") is not None else QV_FAIL_TTL
    return e["data"] if time.time() - e["ts"] < ttl else _MISS


def _qv_cache_set(sym, data):
    with _qv_lock:
        _qv_disk[sym] = {"ts": time.time(), "data": data}
        try:
            QV_CACHE_FILE.write_text(json.dumps(_qv_disk, ensure_ascii=False), encoding="utf-8")
        except Exception:
            pass


def _qv_search_id():
    if _qv_state["search_id"]:
        return _qv_state["search_id"]
    r = SESSION.post(f"{QV_BASE}/search", headers=_qv_headers(),
                     json={"query": QV_TOOL, "limit": 1, "session_id": QV_SESSION_ID}, timeout=20)
    j = r.json()
    sid = j.get("search_id")
    if j.get("remaining_credits") is not None:
        _qv_state["credits"] = j["remaining_credits"]
    if sid and sid != "srch_failed":
        _qv_state["search_id"] = sid
        return sid
    return None


def eod_symbol(yf_symbol):
    """Символ Yahoo -> формат QVeris/EODHD (Xetra = .XETRA, Лондон = .LSE)."""
    for a, b in ((".DE", ".XETRA"), (".L", ".LSE")):
        if yf_symbol.endswith(a):
            return yf_symbol[:-len(a)] + b
    return yf_symbol


def fetch_qveris_dividends(yf_symbol, kind="stock"):
    """Список объявленных/прошедших дивидендов: [{ex, amount, pay, ann, currency}] или None."""
    if not QVERIS_KEY:
        return None
    sym = eod_symbol(yf_symbol)
    cached = _qv_cache_get(sym)
    if cached is not _MISS:
        return cached
    if _qv_state["credits"] is not None and _qv_state["credits"] < 20:
        return None  # бережём остаток кредитов
    data = None
    try:
        sid = _qv_search_id()
        if sid:
            r = SESSION.post(f"{QV_BASE}/tools/execute", params={"tool_id": QV_TOOL}, headers=_qv_headers(),
                             json={"search_id": sid, "session_id": QV_SESSION_ID,
                                   "parameters": {"symbol": sym,
                                                  "start_date": (date.today() - timedelta(days=3 * 365)).isoformat()},
                                   "max_response_size": 40000},
                             timeout=45)
            j = r.json()
            if j.get("remaining_credits") is not None:
                _qv_state["credits"] = j["remaining_credits"]
            rows = ((j.get("result") or {}).get("data")) if j.get("success") else None
            if isinstance(rows, list):
                data = []
                for x in rows:
                    if x.get("ex_date") and x.get("amount") is not None:
                        data.append({"ex": x["ex_date"], "amount": float(x["amount"]),
                                     "pay": x.get("payment_date"), "ann": x.get("announcement_date"),
                                     "currency": x.get("currency")})
    except Exception:
        data = None
    _qv_cache_set(sym, data)
    return data


# ─── YAHOO FINANCE ───────────────────────────────────────────────────────
_TTL_15MIN = 15 * 60
_TTL_6H = 6 * 3600
_YF_QUOTE_CACHE = TTLCache()   # котировка — живая, кэшируем недолго
_YF_INFO_CACHE = TTLCache()    # профиль компании меняется редко
_YF_DIV_CACHE = TTLCache()     # история дивидендов — раз в 6 часов
_YF_TICKERS = {}               # {sym: Ticker} — переиспользуем объект, yfinance перечитывает кэш с диска зря


def _yf_ticker(sym):
    t = _YF_TICKERS.get(sym)
    if t is None:
        t = _YF_TICKERS[sym] = yf.Ticker(sym)
    return t


def fetch_yf_quote(sym):
    if yf is None:
        return {}
    cached = _YF_QUOTE_CACHE.get(sym, _TTL_15MIN)
    if cached is not None:
        return cached
    try:
        fi = _yf_ticker(sym).fast_info

        def g(key):
            try:
                return fi[key]
            except Exception:
                return None

        last, prev = g("last_price"), g("previous_close")
        change = (last / prev - 1) * 100 if last and prev else None
        res = {"price": last, "prev_close": prev, "change_pct": change,
               "currency": g("currency"), "market_cap": g("market_cap")}
        if any(v is not None for v in res.values()):
            _YF_QUOTE_CACHE.set(sym, res)
        return res
    except Exception:
        return {}


def fetch_yf_info(sym):
    if yf is None:
        return {}
    cached = _YF_INFO_CACHE.get(sym, _TTL_6H)
    if cached is not None:
        return cached
    keys = ("longName", "shortName", "sector", "industry", "country", "website", "longBusinessSummary",
            "dividendRate", "payoutRatio", "exDividendDate", "quoteType")
    try:
        info = _yf_ticker(sym).info or {}
        res = {k: info.get(k) for k in keys}
        if any(res.values()):
            _YF_INFO_CACHE.set(sym, res)
        return res
    except Exception:
        return {}


def fetch_yf_dividends(sym):
    if yf is None:
        return []
    cached = _YF_DIV_CACHE.get(sym, _TTL_6H)
    if cached is not None:
        return cached
    try:
        s = _yf_ticker(sym).dividends
        if s is None or len(s) == 0:
            return []  # пустой результат не кэшируем — вдруг данные появятся
        res = [(idx.date(), float(v)) for idx, v in s.items()]
        _YF_DIV_CACHE.set(sym, res)
        return res
    except Exception:
        return []


# ─── АНАЛИЗ ДИВИДЕНДОВ ───────────────────────────────────────────────────
FREQ_LABELS = {
    1: "1 раз в год (ежегодно)",
    2: "2 раза в год (раз в полгода)",
    3: "3 раза в год",
    4: "4 раза в год (ежеквартально)",
    6: "6 раз в год (раз в 2 месяца)",
    12: "12 раз в год (ежемесячно)",
}


def _to_date(v):
    try:
        return date.fromisoformat(str(v)[:10])
    except Exception:
        return None


def analyze_dividends(yf_divs, qv_divs, price, currency, info):
    today = date.today()
    events = {}
    for d, a in yf_divs:
        events[d] = {"ex": d, "amount": a, "pay": None, "ann": None, "src": "Yahoo"}

    for q in qv_divs or []:
        d = _to_date(q.get("ex"))
        if not d:
            continue
        match = next((e for k, e in events.items() if abs((k - d).days) <= 4), None)
        if match:
            match["pay"] = match["pay"] or q.get("pay")
            match["ann"] = match["ann"] or q.get("ann")
            match["src"] = "Yahoo + QVeris"
        else:
            qc = (q.get("currency") or "")
            if not currency or qc == currency:  # не смешиваем разные валюты (GBP/GBp и т.п.)
                events[d] = {"ex": d, "amount": q["amount"], "pay": q.get("pay"), "ann": q.get("ann"),
                             "src": "QVeris"}

    # Yahoo иногда знает ближайшую ex-дату раньше, чем она попала в историю
    ex_ts = info.get("exDividendDate")
    if isinstance(ex_ts, (int, float)) and ex_ts > 0:
        d = datetime.fromtimestamp(ex_ts, timezone.utc).date()
        if d > today and not any(abs((k - d).days) <= 4 for k in events):
            events[d] = {"ex": d, "amount": None, "pay": None, "ann": None, "src": "Yahoo"}

    evs = sorted(events.values(), key=lambda e: e["ex"])
    past = [e for e in evs if e["ex"] <= today]
    future = [e for e in evs if e["ex"] > today]

    if not past and not future:
        return {"has_data": False,
                "note": "Выплат дивидендов в данных не найдено: компания их не платит, "
                        "либо это накопительный фонд (доход реинвестируется внутри фонда)."}

    res = {"has_data": True, "currency": currency, "sources": sorted({e["src"] for e in evs})}
    notes = []

    # периодичность по медианному интервалу между последними выплатами
    recent = [e for e in past if e["ex"] >= today - timedelta(days=5 * 365)]
    gaps = [(recent[i]["ex"] - recent[i - 1]["ex"]).days for i in range(1, len(recent))][-8:]
    freq, gap_days = None, None
    if gaps:
        gap_days = statistics.median(gaps)
        raw = 365 / max(gap_days, 1)
        freq = min((1, 2, 3, 4, 6, 12), key=lambda f: abs(f - raw))

    last = past[-1] if past else None
    active = True
    if last:
        expected_gap = 365 / freq if freq else 365
        if (today - last["ex"]).days > expected_gap * 1.5 + 30:
            active = False
            notes.append(f"Последняя выплата была давно ({last['ex'].strftime('%d.%m.%Y')}) — "
                         "похоже, дивиденды приостановлены или прекращены.")

    if freq and active:
        res["frequency"] = FREQ_LABELS[freq]
        res["per_year"] = freq
    elif last and not freq:
        res["frequency"] = "данных мало — по истории была 1 выплата"
    elif not active:
        res["frequency"] = "не выплачиваются в последнее время"
    else:
        res["frequency"] = "не определена"

    # годовой дивиденд = сумма последних N выплат (N = число выплат в год)
    if past and active:
        n = freq or 1
        res["annual_amount"] = round(sum(e["amount"] for e in past[-n:]), 4)
        if price:
            res["yield_pct"] = round(res["annual_amount"] / price * 100, 2)
    rate = info.get("dividendRate")
    if rate and price:
        res["yahoo_rate"] = rate
        res["yahoo_yield_pct"] = round(rate / price * 100, 2)
    if info.get("payoutRatio"):
        res["payout_ratio_pct"] = round(info["payoutRatio"] * 100, 1)

    if last:
        res["last"] = {"ex": last["ex"].isoformat(), "amount": last["amount"],
                       "pay": last.get("pay")}

    # ближайшая ex-дата: объявленная или оценка по прошлому ритму
    nxt = None
    if future:
        f = future[0]
        nxt = {"ex": f["ex"].isoformat(), "amount": f["amount"], "pay": f.get("pay"),
               "kind": "объявлена"}
    elif last and active and freq:
        gap = int(round(gap_days)) if gap_days else int(round(365 / freq))
        d = last["ex"] + timedelta(days=gap)
        if d < today - timedelta(days=20):
            notes.append("Ожидаемая по ритму выплата в этом цикле в данных не найдена — возможно, дивиденд "
                         "отменён или сокращён, либо данные ещё не обновились. Дата ниже — оценка на следующий цикл.")
        while d <= today:
            d += timedelta(days=gap)
        nxt = {"ex": d.isoformat(), "amount": last["amount"], "pay": None, "kind": "оценка"}
        notes.append("Ближайшая ex-дата — ОЦЕНКА по датам прошлых выплат (±несколько недель), "
                     "компания её пока не объявила.")
    if nxt:
        res["next"] = nxt

    history = [e for e in reversed(evs)][:10]
    res["history"] = [{"ex": e["ex"].isoformat(), "amount": e["amount"], "pay": e.get("pay"),
                       "future": e["ex"] > today} for e in history]
    res["notes"] = notes
    return res


# ─── ТОНАЛЬНОСТЬ НОВОСТЕЙ ────────────────────────────────────────────────
POS_RE = re.compile(r"\b(rise[sn]?|rose|gains?|beats?|record|upgrad\w*|surg\w*|jumps?|growth|strong\w*|"
                    r"raises?|boost\w*|profit\w*|outperform\w*|buyback)\b|рост|выросл|прибыл|рекорд|повыш|улучш", re.I)
NEG_RE = re.compile(r"\b(fall[s]?|fell|drops?|dropped|loss(?:es)?|weak\w*|cuts?|miss(?:es|ed)?|downgrad\w*|"
                    r"declin\w*|plunge\w*|slump\w*|warning|lawsuit|probe|recall)\b|убыт|упал|падени|сниж|ухудш|понижен", re.I)


def news_tone(titles):
    pos = neg = 0
    for t in titles:
        p, n = bool(POS_RE.search(t)), bool(NEG_RE.search(t))
        if p and not n:
            pos += 1
        elif n and not p:
            neg += 1
    return pos, neg


def trim(text, limit):
    """Обрезка по границе предложения, а не посреди слова."""
    text = " ".join(str(text or "").split())
    if len(text) <= limit:
        return text
    cut = text[:limit]
    idx = max(cut.rfind(". "), cut.rfind("! "), cut.rfind("? "))
    return (cut[:idx + 1] if idx > limit * 0.4 else cut.rsplit(" ", 1)[0] + "…")


def fmt_money(x, cur=""):
    return f"{x:,.2f} {cur}".replace(",", " ").strip()


def fmt_date(iso):
    d = _to_date(iso)
    return d.strftime("%d.%m.%Y") if d else "—"


# ─── ГЕНЕРАЦИЯ ОТЧЁТА ────────────────────────────────────────────────────
def _safe(fut, default):
    try:
        v = fut.result()
        return default if v is None else v
    except Exception:
        return default


def generate_report(stock):
    ticker, name = stock["ticker"], stock["name"]
    cached = REPORT_CACHE.get(ticker, REPORT_TTL)
    if cached:
        return cached

    # Один поток собирает отчёт, остальные ждут его и берут из кэша —
    # иначе каждый параллельный запрос дублировал бы все внешние API.
    with _build_lock(ticker):
        cached = REPORT_CACHE.get(ticker, REPORT_TTL)
        if cached:
            return cached
        report = _build_report(stock)
        REPORT_CACHE.set(ticker, report)
        return report


def _build_report(stock):
    ticker, name = stock["ticker"], stock["name"]
    year = date.today().year
    with ThreadPoolExecutor(max_workers=7) as ex:
        f_quote = ex.submit(fetch_yf_quote, ticker)
        f_info = ex.submit(fetch_yf_info, ticker)
        f_divs = ex.submit(fetch_yf_dividends, ticker)
        f_qv = ex.submit(fetch_qveris_dividends, ticker, stock.get("kind", "stock"))
        f_prof = ex.submit(fetch_finnhub_profile, stock)
        f_news = ex.submit(fetch_finnhub_news, stock)
        f_web = ex.submit(fetch_tavily, f"{name} {ticker} stock outlook analyst forecast dividend {year}")
        quote = _safe(f_quote, {})
        info = _safe(f_info, {})
        yf_divs = _safe(f_divs, [])
        qv_divs = _safe(f_qv, None)
        profile = _safe(f_prof, {})
        news = _safe(f_news, [])
        web = _safe(f_web, [])

    price, cur = quote.get("price"), quote.get("currency")
    div = analyze_dividends(yf_divs, qv_divs, price, cur, info)

    # ── 1. Бизнес
    biz = []
    industry = profile.get("finnhubIndustry") or info.get("industry") or info.get("sector")
    if industry:
        biz.append(f"Отрасль: {industry}.")
    country = profile.get("country") or info.get("country")
    if country:
        biz.append(f"Страна: {country}.")
    site = profile.get("weburl") or info.get("website")
    if site:
        biz.append(f"Сайт: {site}.")
    if profile.get("ipo"):
        biz.append(f"На бирже с {fmt_date(profile['ipo'])}.")
    if profile.get("shareOutstanding"):
        biz.append(f"Акций в обращении: около {profile['shareOutstanding']:,.0f} млн.".replace(",", " "))
    if info.get("longBusinessSummary"):
        biz.append("Чем занимается (описание Yahoo Finance, на английском): "
                   + trim(info["longBusinessSummary"], 450))
    business = " ".join(biz) or ("Подробного профиля в источниках не нашлось."
                                 + (f" ({stock['note']})" if stock.get("note") else ""))

    # ── 2. Анализ
    ana = []
    if price:
        ana.append(f"Цена: {fmt_money(price, cur or '')}.")
        if quote.get("change_pct") is not None:
            ch = quote["change_pct"]
            ch = 0.0 if abs(ch) < 0.005 else ch  # без «-0.00%»
            ana.append(f"Изменение к предыдущему закрытию: {'+' if ch >= 0 else ''}{ch:.2f}%.")
    else:
        ana.append("Котировка сейчас недоступна на Yahoo Finance"
                   + (f" ({stock['note']})." if stock.get("note") else "."))
    mc = quote.get("market_cap") or (profile.get("marketCapitalization") and profile["marketCapitalization"] * 1e6)
    if mc:
        ana.append(f"Рыночная капитализация: примерно {mc / 1e9:,.1f} млрд {cur or profile.get('currency', '')}.".replace(",", " "))
        if (cur or profile.get("currency")) in ("USD", "EUR"):
            b = mc / 1e9
            size = ("мега-кап: обычно стабильнее рынка в целом" if b > 200 else
                    "крупная компания" if b > 50 else
                    "средняя по размеру компания: колебания цены сильнее" if b > 10 else
                    "небольшая компания: цена может резко меняться на новостях")
            ana.append(f"По размеру это {size}.")
    titles = [n.get("headline", "") for n in news if n.get("headline")] or \
             [w.get("title", "") for w in web if w.get("title")]
    if titles:
        pos, neg = news_tone(titles)
        tone = "в основном позитивный" if pos > neg else "в основном негативный" if neg > pos else "смешанный"
        ana.append(f"Тон заголовков ({len(titles)} шт.): {tone} — позитивных {pos}, негативных {neg}.")
    else:
        ana.append("Свежих новостей по бумаге в источниках не найдено.")
    analysis = " ".join(ana)

    # ── 3. Перспективы (только то, что есть в данных)
    fc = []
    if div.get("has_data") and div.get("next"):
        n = div["next"]
        fc.append(f"Ближайшая экс-дивидендная дата ({n['kind']}): {fmt_date(n['ex'])}. "
                  "Чтобы получить этот дивиденд, акцию нужно купить до этой даты.")
    if web:
        snippets = [f"«{trim(w.get('title', ''), 90)}»: {trim(w.get('content', ''), 200)}"
                    for w in web[:3] if w.get("title") and w.get("content")]
        if snippets:
            fc.append("Что пишут в интернете (Tavily): " + " ".join(snippets))
    if not fc:
        fc.append("Конкретных объявленных событий (отчёт, дивиденд) в источниках не найдено — "
                  "даты отчётов смотрите в календаре на Yahoo Finance или на сайте компании.")
    fc.append("Это сводка данных, а не рекомендация купить или продать. Риск потерь реален.")
    forecast = " ".join(fc)

    news_items = []
    for n in news[:6]:
        if n.get("headline") and n.get("url"):
            news_items.append({"title": n["headline"], "url": n["url"], "source": n.get("source", ""),
                               "date": datetime.fromtimestamp(n["datetime"]).strftime("%d.%m.%Y") if n.get("datetime") else ""})
    web_items = [{"title": w.get("title", ""), "url": w.get("url", "")} for w in web[:6] if w.get("url")]

    report = {
        "ticker": ticker,
        "name": name,
        "icon": get_icon_path(stock),
        "kind": stock.get("kind", "stock"),
        "quote": {"price": price, "currency": cur, "change_pct": quote.get("change_pct"),
                  "market_cap": mc},
        "dividends": div,
        "business": trim(business, 1400),
        "analysis": trim(analysis, 1000),
        "forecast": trim(forecast, 1200),
        "news": news_items,
        "web": web_items,
        "sources": {
            "yahoo_quote": bool(price),
            "yahoo_dividends": len(yf_divs),
            "qveris_dividends": None if qv_divs is None else len(qv_divs),
            "finnhub_profile": bool(profile),
            "finnhub_news": len(news),
            "tavily": len(web),
        },
        "generated_at": datetime.now().isoformat(timespec="seconds"),
    }
    return report


# ─── ШАБЛОН И HTTP ───────────────────────────────────────────────────────
_DASH_CACHE = {"key": None, "html": None}


def render_dashboard():
    # Рендер кэшируется; перечитываем шаблон и пересобираем страницу только
    # когда файл шаблона изменился на диске — правки всё ещё видны без перезапуска.
    try:
        sig = TEMPLATE_FILE.stat().st_mtime_ns
    except OSError:
        sig = 0
    if _DASH_CACHE["html"] is not None and _DASH_CACHE["key"] == sig:
        return _DASH_CACHE["html"]

    template = TEMPLATE_FILE.read_text(encoding="utf-8")
    esc = lambda s: str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
    cards = []
    for s in STOCKS:
        icon_url = get_icon_path(s)
        label = esc(s["ticker"].split(".")[0][:5])
        icon_html = (f'<img src="{icon_url}" alt="" class="icon" loading="lazy">' if icon_url
                     else f'<div class="icon placeholder">{label}</div>')
        cards.append(
            f'<article class="card" data-ticker="{esc(s["ticker"])}" '
            f'data-search="{esc((s["name"] + " " + s["ticker"]).lower())}">{icon_html}'
            f'<div class="info"><h3>{esc(s["name"])}</h3><span class="ticker">{esc(s["ticker"])}</span></div></article>')
    html = template.replace("{count}", str(len(STOCKS))).replace("{cards}", "".join(cards))
    _DASH_CACHE["key"] = sig
    _DASH_CACHE["html"] = html
    return html


def _maybe_gzip(body_bytes, accept_encoding):
    """Сжимаем ответ gzip'ом, если браузер его принимает и это выгодно."""
    if len(body_bytes) < 860 or "gzip" not in (accept_encoding or ""):
        return body_bytes, False
    import gzip as _gz
    return _gz.compress(body_bytes, 5), True


class DashboardHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"  # keep-alive: браузер переиспользует соединения для иконок

    def _send(self, code, body, ctype, gzipped=False, extra_headers=()):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        if gzipped:
            self.send_header("Content-Encoding", "gzip")
            self.send_header("Vary", "Accept-Encoding")
        self.send_header("Cache-Control", "no-store" if code != 200 or ctype.startswith("application/json") else "max-age=3600")
        for k, v in extra_headers:
            self.send_header(k, v)
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def do_HEAD(self):
        self.do_GET(head_only=True)

    def do_GET(self, head_only=False):
        path = self.path.split("?", 1)[0]
        try:
            if path in ("/", "/index.html"):
                body = render_dashboard().encode("utf-8")
                etag = '"' + hashlib.md5(body).hexdigest() + '"'
                if head_only:
                    self._send(200, b"", "text/html; charset=utf-8", extra_headers=[("ETag", etag)])
                    return
                if etag in (self.headers.get("If-None-Match") or ""):
                    self.send_response(304)
                    self.send_header("ETag", etag)
                    self.end_headers()
                    return
                body, gz = _maybe_gzip(body, self.headers.get("Accept-Encoding"))
                self._send(200, body, "text/html; charset=utf-8", gz, [("ETag", etag)])
            elif path.startswith("/api/stock/"):
                ticker = unquote(path[len("/api/stock/"):])
                stock = STOCK_BY_TICKER.get(ticker)
                if not stock:
                    err = json.dumps({"error": "Акция не найдена в списке"}, ensure_ascii=False).encode()
                    if head_only:
                        self._send(404, b"", "application/json; charset=utf-8")
                    else:
                        self._send(404, err, "application/json; charset=utf-8")
                    return
                body = json.dumps(generate_report(stock), ensure_ascii=False, default=str).encode("utf-8")
                if head_only:
                    self._send(200, b"", "application/json; charset=utf-8")
                    return
                body, gz = _maybe_gzip(body, self.headers.get("Accept-Encoding"))
                self._send(200, body, "application/json; charset=utf-8", gz)
            elif path.startswith("/icons/"):
                f = ICONS_DIR / Path(unquote(path[len("/icons/"):])).name  # .name = защита от «../»
                if f.is_file():
                    data = f.read_bytes()
                    etag = '"%s-%d"' % (hashlib.md5(data).hexdigest(), len(data))
                    headers = [("ETag", etag)]
                    if etag in (self.headers.get("If-None-Match") or ""):
                        self.send_response(304)
                        self.send_header("ETag", etag)
                        self.send_header("Cache-Control", "max-age=86400")
                        self.end_headers()
                        return
                    ctype = mimetypes.guess_type(f.name)[0] or "application/octet-stream"
                    if head_only:
                        self._send(200, b"", ctype, extra_headers=headers)
                        return
                    self._send(200, data, ctype, extra_headers=headers)
                else:
                    self._send(404, b"" if head_only else b"Not found", "text/plain")
            elif path == "/favicon.ico":
                self._send(204, b"", "image/x-icon")
            else:
                self._send(404, b"" if head_only else b"Not found", "text/plain")
        except (BrokenPipeError, ConnectionResetError):
            pass
        except Exception as e:
            try:
                err = json.dumps({"error": f"{type(e).__name__}: {e}"}, ensure_ascii=False).encode()
                self._send(500, b"" if head_only else err, "application/json; charset=utf-8")
            except Exception:
                pass

    def log_message(self, format, *args):
        pass


# ─── ЗАПУСК ──────────────────────────────────────────────────────────────
def _icons_in_background():
    try:
        import icon_fetcher
        icon_fetcher.ensure_icons(STOCKS, ENV, log=lambda m: print(m, flush=True))
    except Exception as e:
        print(f"[иконки] пропущено: {e}", flush=True)


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    print("=" * 60)
    print("  ПАНЕЛЬ АКЦИЙ — Stock Dashboard")
    print("=" * 60)
    try:
        server = ThreadingHTTPServer((HOST, PORT), DashboardHandler)
    except OSError:
        print(f"[i] Порт {PORT} уже занят — панель, вероятно, уже запущена. Открываю браузер.")
        webbrowser.open(BASE_URL)
        return
    server.daemon_threads = True
    print(f"[+] Панель: {BASE_URL}   (остановка: Ctrl+C или закрыть окно)")
    print(f"[+] Ключи: Finnhub={'да' if FINNHUB_KEY else 'НЕТ'}, Tavily={'да' if TAVILY_KEY else 'НЕТ'}, "
          f"QVeris={'да' if QVERIS_KEY else 'НЕТ'}")
    threading.Thread(target=_icons_in_background, daemon=True).start()
    threading.Timer(0.6, lambda: webbrowser.open(BASE_URL)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[+] Остановка сервера...")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
