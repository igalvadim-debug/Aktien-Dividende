#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Докачивает недостающие иконки в папку icons.

Порядок источников для каждой бумаги без иконки:
  1. ETF: иконка эмитента (iShares / VanEck / Amundi / Vanguard), если она уже лежит в icons
  2. Finnhub: логотип компании по ISIN
  3. Сайт компании (Yahoo Finance): apple-touch-icon, затем favicon (Google / DuckDuckGo)

Иконки сохраняются как PNG 128x128 на белом фоне под именем, указанным в stocks.json.
Неудачные попытки запоминаются на 7 дней (_cache/icons_failed.json), чтобы не
долбить сайты при каждом запуске.

Автоматически запускается в фоне из launch_dashboard.py. Вручную:
    stock-sentiment\\Scripts\\python.exe icon_fetcher.py
"""
import io
import json
import re
import shutil
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests

ROOT = Path(__file__).resolve().parent
ICONS_DIR = ROOT / "icons"
CACHE_DIR = ROOT / "_cache"
FAILED_FILE = CACHE_DIR / "icons_failed.json"
RETRY_AFTER = 7 * 24 * 3600
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}

ISSUERS = [
    ("ishares", "_ISSUER_iShares.png"),
    ("vaneck", "_ISSUER_VanEck.png"),
    ("amundi", "_ISSUER_Amundi.png"),
    ("vanguard", "_ISSUER_Vanguard.png"),
]
# Если Yahoo не знает сайт компании — домен подсказываем вручную
EXTRA_SITES = {"LIN.DE": "linde.com", "MTX.DE": "mtu.de", "QIA.DE": "qiagen.com",
               "SY1.DE": "symrise.com", "SWRD.L": "ssga.com"}
ETF_DOMAINS = {"spdr": "ssga.com", "state street": "ssga.com", "xtrackers": "dws.com", "lyxor": "amundietf.com"}


def _load_failed():
    try:
        return json.loads(FAILED_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _save_failed(data):
    try:
        CACHE_DIR.mkdir(exist_ok=True)
        FAILED_FILE.write_text(json.dumps(data), encoding="utf-8")
    except Exception:
        pass


def _normalize_and_save(content, target, min_side=40):
    """Картинка -> PNG 128x128 на белом фоне. Возвращает True, если иконка нормальная."""
    from PIL import Image
    try:
        img = Image.open(io.BytesIO(content))
        img.load()
    except Exception:
        return False
    img = img.convert("RGBA")
    if min(img.size) < min_side:
        return False
    box = 104
    img.thumbnail((box, box), Image.LANCZOS)
    canvas = Image.new("RGBA", (128, 128), (255, 255, 255, 255))
    canvas.alpha_composite(img, ((128 - img.size[0]) // 2, (128 - img.size[1]) // 2))
    canvas.convert("RGB").save(target, "PNG")
    return True


def _get(url, **kw):
    try:
        r = requests.get(url, headers=UA, timeout=12, **kw)
        if r.status_code == 200 and r.content:
            return r
    except Exception:
        pass
    return None


def _finnhub_logo(isin, ticker, env):
    key = env.get("NEXT_PUBLIC_FINNHUB_API_KEY")
    base = env.get("FINNHUB_BASE_URL", "https://finnhub.io/api/v1")
    if not key:
        return None
    for params in ({"isin": isin}, {"symbol": ticker}):
        try:
            r = requests.get(f"{base}/stock/profile2", params={**params, "token": key}, timeout=10)
            if r.status_code == 200:
                logo = (r.json() or {}).get("logo")
                if logo:
                    g = _get(logo)
                    if g:
                        return g.content
        except Exception:
            pass
    return None


def _website(ticker):
    try:
        import yfinance as yf
        return (yf.Ticker(ticker).info or {}).get("website")
    except Exception:
        return None


def _site_icons(site):
    """Кандидаты: apple-touch-icon с сайта, затем favicon-сервисы."""
    out = []
    if not site:
        return out
    if not site.startswith("http"):
        site = "https://" + site
    host = urlparse(site).netloc.replace("www.", "")
    page = _get(site)
    if page is not None:
        html = page.text[:200000]
        for m in re.finditer(r"<link[^>]+rel=[\"'](?:apple-touch-icon[^\"']*)[\"'][^>]*>", html, re.I):
            h = re.search(r"href=[\"']([^\"']+)[\"']", m.group(0), re.I)
            if h:
                out.append(("apple", urljoin(page.url, h.group(1))))
    out.append(("google", f"https://www.google.com/s2/favicons?domain={host}&sz=128"))
    out.append(("ddg", f"https://icons.duckduckgo.com/ip3/{host}.ico"))
    return out


def fetch_one(stock, env, log=print):
    target = ICONS_DIR / (stock.get("icon") or f"{stock['isin']}.png")
    name_l = stock["name"].lower()

    # 1) эмитент ETF
    if stock.get("kind") == "etf":
        for key, fname in ISSUERS:
            if key in name_l and (ICONS_DIR / fname).exists():
                shutil.copyfile(ICONS_DIR / fname, target)
                return "эмитент " + key
        for key, domain in ETF_DOMAINS.items():
            if key in name_l:
                for src, url in _site_icons("https://" + domain):
                    g = _get(url)
                    if g and (src != "google" or len(g.content) > 1500) and _normalize_and_save(g.content, target):
                        return f"сайт {domain} ({src})"

    # 2) Finnhub
    if stock.get("kind") != "etf":
        data = _finnhub_logo(stock["isin"], stock["ticker"], env)
        if data and _normalize_and_save(data, target):
            return "Finnhub"

    # 3) сайт компании
    candidates = _site_icons(_website(stock["ticker"]))
    if stock["ticker"] in EXTRA_SITES:
        candidates += _site_icons("https://" + EXTRA_SITES[stock["ticker"]])
    for src, url in candidates:
        g = _get(url)
        if not g:
            continue
        if src == "google" and len(g.content) < 1500:
            continue  # заглушка-глобус
        if _normalize_and_save(g.content, target, min_side=32 if src != "apple" else 60):
            return f"сайт ({src})"
    return None


def ensure_icons(stocks, env, log=print):
    ICONS_DIR.mkdir(exist_ok=True)
    failed = _load_failed()
    now = time.time()
    got, miss = [], []
    for s in stocks:
        fname = s.get("icon") or f"{s['isin']}.png"
        if (ICONS_DIR / fname).exists():
            continue
        if now - failed.get(s["isin"], 0) < RETRY_AFTER:
            continue
        try:
            how = fetch_one(s, env, log)
        except Exception as e:  # одна бумага не должна ронять остальные
            how = None
            log(f"[иконки] {s['ticker']}: ошибка {e}")
        if how:
            got.append((s["ticker"], how))
            log(f"[иконки] {s['ticker']}: получена ({how})")
            failed.pop(s["isin"], None)
        else:
            miss.append(s["ticker"])
            failed[s["isin"]] = now
    _save_failed(failed)
    if got or miss:
        log(f"[иконки] готово: {len(got)} добавлено, {len(miss)} не найдено" + (f" ({', '.join(miss)})" if miss else ""))
    return got, miss


def load_env(path=ROOT / ".env"):
    env = {}
    try:
        text = Path(path).read_text(encoding="utf-8-sig")
    except OSError:
        return env
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip().strip("\"'")
    return env


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    stocks = json.loads((ROOT / "stocks.json").read_text(encoding="utf-8"))
    if "--retry" in sys.argv and FAILED_FILE.exists():
        FAILED_FILE.unlink()
    ensure_icons(stocks, load_env())
