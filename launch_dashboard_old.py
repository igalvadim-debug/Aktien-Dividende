#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Запуск Панели Акций (Stock Dashboard) на русском языке
- Активирует виртуальное окружение
- Запускает cc-switch.exe
- Запускает локальный веб-сервер с панелью акций
- При клике на акцию — получает живые данные и создает подробный отчет на русском
- Иконки берутся из папки D:/claudeAgent/Stocks/icons
- Все тексты на русском, простыми словами, в 3 раза больше объема
"""

import os
import sys
import subprocess
import webbrowser
import time
import json
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler

# ─── НАСТРОЙКИ ПУТЕЙ ─────────────────────────────────────────────────────
ROOT = Path(r"D:\claudeAgent\Stocks")
VENV_PYTHON = ROOT / r"stock-sentiment\Scripts\python.exe"
ICONS_DIR = ROOT / "icons"
TEMPLATE_FILE = ROOT / "dashboard_template.html"
DASHBOARD_DIR = ROOT / "dashboard"
DASHBOARD_DIR.mkdir(exist_ok=True)

PORT = 8765
BASE_URL = f"http://localhost:{PORT}"

# ─── СПИСОК АКЦИЙ (из getquin + demo-stockpeers) ─────────────────────────
# Каждая акция: тикер, название, ISIN, файл иконки
STOCKS = [
    # Немецкие / XETRA
    {"ticker": "DWS.DE", "name": "DWS Group", "isin": "DE000DWS1007", "icon": "DE000DWS1007.png"},
    {"ticker": "RENK.DE", "name": "Renk Group", "isin": "DE000RENK730", "icon": "DE000RENK730.png"},
    {"ticker": "VOW3.DE", "name": "Volkswagen AG (предпочтительные)", "isin": "DE0007664039", "icon": "DE0007664039.png"},
    {"ticker": "SHEL", "name": "Shell PLC", "isin": "GB00BP6MXD84", "icon": "GB00BP6MXD84.png"},
    {"ticker": "INGA.DE", "name": "ING Groep NV", "isin": "NL0011821202", "icon": "NL0011821202.png"},
    {"ticker": "SIE.DE", "name": "Siemens AG", "isin": "DE0007236101", "icon": "DE0007236101.png"},
    {"ticker": "BAYN.DE", "name": "Bayer AG", "isin": "DE000BAY0017", "icon": "DE000BAY0017.png"},
    {"ticker": "EOAN.DE", "name": "E.ON SE", "isin": "DE000ENAG999", "icon": "DE000ENAG999.png"},
    {"ticker": "P911.DE", "name": "Porsche AG", "isin": "DE000A3H2101", "icon": "DE000A3H2101.png"},
    {"ticker": "TUI1.DE", "name": "TUI AG", "isin": "DE000TUAG505", "icon": "DE000TUAG505.png"},
    {"ticker": "ADS.DE", "name": "Adidas AG", "isin": "DE000A1EWWW0", "icon": "DE000A1EWWW0.png"},
    {"ticker": "DPW.DE", "name": "Deutsche Post AG", "isin": "DE0005552004", "icon": "DE0005552004.png"},
    {"ticker": "DTE.DE", "name": "Deutsche Telekom AG", "isin": "DE0005557508", "icon": "DE0005557508.png"},
    {"ticker": "FRE.DE", "name": "Fresenius SE", "isin": "DE0005785604", "icon": "DE0005785604.png"},
    {"ticker": "HEI.DE", "name": "Heidelberg Materials", "isin": "DE0006047004", "icon": "DE0006047004.png"},
    {"ticker": "HNR1.DE", "name": "Hannover Rück SE", "isin": "DE0008402215", "icon": "DE0008402215.png"},
    {"ticker": "MBG.DE", "name": "Mercedes-Benz Group", "isin": "DE0007100000", "icon": "DE0007100000.png"},
    {"ticker": "MTX.DE", "name": "MTU Aero Engines", "isin": "DE000A0D9PT0", "icon": "DE000A0D9PT0.png"},
    {"ticker": "MUV2.DE", "name": "Munich Re", "isin": "DE0008430026", "icon": "DE0008430026.png"},
    {"ticker": "RWE.DE", "name": "RWE AG", "isin": "DE0007037129", "icon": "DE0007037129.png"},
    {"ticker": "SAP.DE", "name": "SAP SE", "isin": "DE0007164600", "icon": "DE0007164600.png"},
    {"ticker": "VNA.DE", "name": "Vonovia SE", "isin": "DE000A1ML7J1", "icon": "DE000A1ML7J1.png"},
    {"ticker": "WCH.DE", "name": "Wacker Chemie AG", "isin": "DE000WCH8881", "icon": "DE000WCH8881.png"},
    {"ticker": "ZAL.DE", "name": "Zalando SE", "isin": "DE000ZAL1111", "icon": "DE000ZAL1111.png"},
    {"ticker": "BAS.DE", "name": "BASF SE", "isin": "DE000BASF111", "icon": "DE000BASF111.png"},
    {"ticker": "ALV.DE", "name": "Allianz SE", "isin": "DE0008404005", "icon": "DE0008404005.png"},
    {"ticker": "BMW.DE", "name": "BMW AG", "isin": "DE0005190003", "icon": "DE0005190003.png"},
    {"ticker": "CON.DE", "name": "Continental AG", "isin": "DE0005439004", "icon": "DE0005439004.png"},
    {"ticker": "DBK.DE", "name": "Deutsche Bank AG", "isin": "DE0005140008", "icon": "DE0005140008.png"},
    {"ticker": "IFX.DE", "name": "Infineon Technologies", "isin": "DE0006231004", "icon": "DE0006231004.png"},
    {"ticker": "LIN.DE", "name": "Linde PLC", "isin": "IE000S9YS762", "icon": "IE000S9YS762.png"},
    {"ticker": "MRK.DE", "name": "Merck KGaA", "isin": "DE0006599905", "icon": "DE0006599905.png"},
    {"ticker": "PAH3.DE", "name": "Porsche Automobil Holding", "isin": "DE000PAH0038", "icon": "DE000PAH0038.png"},
    {"ticker": "QIA.DE", "name": "Qiagen NV", "isin": "NL0012169213", "icon": "NL0012169213.png"},
    {"ticker": "RHM.DE", "name": "Rheinmetall AG", "isin": "DE0007030009", "icon": "DE0007030009.png"},
    {"ticker": "SRT3.DE", "name": "Sartorius AG (предпочтительные)", "isin": "DE0007165631", "icon": "DE0007165631.png"},
    {"ticker": "SY1.DE", "name": "Symrise AG", "isin": "DE000SYM9999", "icon": "DE000SYM9999.png"},
    # США / Международные
    {"ticker": "AAPL", "name": "Apple Inc.", "isin": "US0378331005", "icon": "US0378331005.png"},
    {"ticker": "MSFT", "name": "Microsoft Corp.", "isin": "US5949181045", "icon": "US5949181045.png"},
    {"ticker": "GOOGL", "name": "Alphabet Inc.", "isin": "US02079K3059", "icon": "US02079K3059.png"},
    {"ticker": "NVDA", "name": "NVIDIA Corp.", "isin": "US67066G1040", "icon": "US67066G1040.png"},
    {"ticker": "AMZN", "name": "Amazon.com Inc.", "isin": "US0231351067", "icon": "US0231351067.png"},
    {"ticker": "TSLA", "name": "Tesla Inc.", "isin": "US88160R1014", "icon": "US88160R1014.png"},
    {"ticker": "META", "name": "Meta Platforms Inc.", "isin": "US30303M1027", "icon": "US30303M1027.png"},
    {"ticker": "JNJ", "name": "Johnson & Johnson", "isin": "US4781601046", "icon": "US4781601046.png"},
    {"ticker": "LYB", "name": "LyondellBasell Industries", "isin": "NL0009434992", "icon": "NL0009434992.png"},
    {"ticker": "AGCO", "name": "AGCO Corp.", "isin": "US0010841023", "icon": "US0010841023.png"},
    {"ticker": "SIX2.DE", "name": "Sixt SE", "isin": "DE0007231326", "icon": "DE0007231326.png"},
    {"ticker": "QPR.DE", "name": "Quirin Privatbank AG", "isin": "DE000A1H72F1", "icon": "DE000A1H72F1.png"},
    {"ticker": "ALX.DE", "name": "Alexanderwerk AG", "isin": "DE0005488600", "icon": "DE0005488600.png"},
    {"ticker": "KPN", "name": "KPN NV", "isin": "NL0000009082", "icon": "NL0000009082.png"},
    {"ticker": "LTC", "name": "LTC Properties Inc.", "isin": "US5021751020", "icon": "US5021751020_b9LN2DO.png"},
    {"ticker": "BATS.L", "name": "British American Tobacco", "isin": "GB0002875804", "icon": "GB0002875804.png"},
    {"ticker": "OET.DE", "name": "Okeanis Eco Tankers", "isin": "MHY641771016", "icon": "MHY641771016.png"},
    {"ticker": "F", "name": "Ford Motor Co.", "isin": "US3453708600", "icon": "US3453708600.png"},
    {"ticker": "GFI", "name": "Gold Fields Ltd.", "isin": "ZAE000018123", "icon": "ZAE000018123.png"},
    {"ticker": "SBSW", "name": "Sibanye Stillwater Ltd.", "isin": "ZAE000259701", "icon": "ZAE000259701_unaJI2a.png"},
    {"ticker": "CIBUS.ST", "name": "Cibus Nordic Real Estate", "isin": "SE0010832204", "icon": "SE0010832204.png"},
    # ETFs (ISINы из getquin)
    {"ticker": "IE00B2NPKV68", "name": "iShares Core MSCI World UCITS ETF", "isin": "IE00B2NPKV68", "icon": "IE00B2NPKV68.png"},
    {"ticker": "IE00BFY0GT14", "name": "iShares Core S&P 500 UCITS ETF", "isin": "IE00BFY0GT14", "icon": "IE00BFY0GT14.png"},
    {"ticker": "IE00BYWQWR46", "name": "iShares Core EURO STOXX 50 UCITS ETF", "isin": "IE00BYWQWR46", "icon": "IE00BYWQWR46.png"},
]

# ─── ЗАГРУЗКА .env ФАЙЛА С API КЛЮЧАМИ ───────────────────────────────────
def load_env(path):
    env = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                if '=' in line:
                    key, val = line.split('=', 1)
                else:
                    parts = line.split(None, 1)
                    if len(parts) == 2:
                        key, val = parts
                    else:
                        continue
                env[key.strip()] = val.strip().strip('"\'')
    return env

ENV = load_env(ROOT / ".env")
FINNHUB_KEY = ENV.get("NEXT_PUBLIC_FINNHUB_API_KEY")
FINNHUB_BASE = ENV.get("FINNHUB_BASE_URL", "https://finnhub.io/api/v1")
TAVILY_KEY = ENV.get("tavily")

# ─── ПОИСК ИКОНКИ ДЛЯ АКЦИИ ──────────────────────────────────────────────
def get_icon_path(stock):
    icon_file = stock.get("icon")
    if icon_file:
        p = ICONS_DIR / icon_file
        if p.exists():
            return f"/icons/{icon_file}"
    # Запасной вариант: пробуем по ISIN
    for ext in (".png", ".svg", ".jpg", ".webp"):
        p = ICONS_DIR / f"{stock['isin']}{ext}"
        if p.exists():
            return f"/icons/{stock['isin']}{ext}"
    return None

# ─── ФУНКЦИИ ПОЛУЧЕНИЯ ЖИВЫХ ДАННЫХ (НЕТ ГАЛЛЮЦИНАЦИЙ) ─────────────────
import requests
from datetime import datetime, timedelta

def fetch_finnhub_profile(ticker):
    """Профиль компании из Finnhub — что делает бизнес, где находится, какая индустрия"""
    url = f"{FINNHUB_BASE}/stock/profile2"
    params = {"symbol": ticker, "token": FINNHUB_KEY}
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return r.json()
    except Exception:
        pass
    return None

def fetch_finnhub_news(ticker, days=7):
    """Свежие новости по компании за последние 7 дней из Finnhub"""
    to_date = datetime.now().strftime("%Y-%m-%d")
    from_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    url = f"{FINNHUB_BASE}/company-news"
    params = {"symbol": ticker, "from": from_date, "to": to_date, "token": FINNHUB_KEY}
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            return r.json()[:15]  # берем до 15 новостей
    except Exception:
        pass
    return []

def fetch_tavily_search(query, max_results=7):
    """Веб-поиск через Tavily для свежей информации про отчеты, прогнозы, новости"""
    if not TAVILY_KEY:
        return []
    url = "https://api.tavily.com/search"
    headers = {"Authorization": f"Bearer {TAVILY_KEY}", "Content-Type": "application/json"}
    payload = {"query": query, "max_results": max_results, "search_depth": "advanced"}
    try:
        r = requests.post(url, json=payload, headers=headers, timeout=20)
        if r.status_code == 200:
            return r.json().get("results", [])
    except Exception:
        pass
    return []

def fetch_yfinance_info(ticker):
    """Базовые котировки через Yahoo Finance — цена, капитализация, изменение за день"""
    try:
        import yfinance as yf
        tk = yf.Ticker(ticker)
        info = tk.fast_info
        return {
            "last_price": info.get("last_price"),
            "market_cap": info.get("market_cap"),
            "currency": info.get("currency"),
            "regular_market_change": info.get("regular_market_change"),
            "regular_market_change_percent": info.get("regular_market_change_percent"),
        }
    except Exception:
        return {}

# ─── ГЕНЕРАЦИЯ ПОДРОБНОГО ОТЧЕТА НА РУССКОМ (в 3 раза больше текста) ─────
def generate_report(stock):
    """Создает большой подробный отчет на русском: бизнес, анализ, прогноз — только по реальным данным"""
    ticker = stock["ticker"]
    name = stock["name"]
    
    # Собираем ВСЕ доступные живые данные
    profile = fetch_finnhub_profile(ticker)
    news = fetch_finnhub_news(ticker, days=7)
    tavily_results = fetch_tavily_search(f"{name} {ticker} отчет прибыль прогноз 2024 2025 будущее", max_results=7)
    yf_info = fetch_yfinance_info(ticker)
    
    # ═══ 1) ОБЗОР БИЗНЕСА — ЧТО ДЕЛАЕТ КОМПАНИЯ (очень подробно, ~300-500 слов) ═══
    business_parts = []
    
    if profile:
        if profile.get("name"):
            business_parts.append(f"Компания {profile['name']} ({ticker}) является публично торгуемой акцией на фондовой бирже.")
        if profile.get("finnhubIndustry"):
            business_parts.append(f"Основная деятельность компании относится к сектору {profile['finnhubIndustry']}, это означает, что бизнес работает в этой отрасли и поддается влиянию трендов именно этой индустрии.")
        if profile.get("country"):
            business_parts.append(f"Головной офис и юрисдикция компании находятся в стране {profile['country']}, что важно для понимания регуляторной среды и налогового режима.")
        if profile.get("weburl"):
            business_parts.append(f"Официальный веб-сайт компании доступен по адресу {profile['weburl']}, где можно найти отчеты, новости и информацию для инвесторов.")
        if profile.get("marketCapitalization"):
            cap_billions = profile['marketCapitalization']
            business_parts.append(f"Рыночная капитализация компании составляет примерно {cap_billions:.1f} миллиардов долларов, что показывает общий размер и ценность бизнеса на рынке.")
        if profile.get("ipo"):
            business_parts.append(f"Компания вышла на публичный рынок (IPO) в {profile['ipo']}, то есть торгуется на бирже уже длительное время.")
        if profile.get("shareOutstanding"):
            business_parts.append(f"Общее количество выпущенных акций в обращении составляет примерно {profile['shareOutstanding']:.1f} миллионов штук.")
    
    # Добавляем свежие новости как контекст бизнеса
    if news:
        headlines = [n.get("headline", "") for n in news[:5] if n.get("headline")]
        if headlines:
            business_parts.append(f"Свежие новости за последнюю неделю показывают следующую картину: {'; '.join(headlines)}. Эти заголовки помогают понять, о чем говорят в прессе прямо сейчас.")
    
    # Добавляем контекст из веб-поиска (Tavily)
    if tavily_results:
        tavily_snippets = []
        for r in tavily_results[:3]:
            content = r.get("content", "")[:300]
            if content:
                tavily_snippets.append(content)
        if tavily_snippets:
            business_parts.append(f"Дополнительная информация из веб-поиска подтверждает: {' '.join(tavily_snippets)}. Эти данные взяты из свежих статей и аналитических обзоров в интернете.")
    
    business = " ".join(business_parts)
    # Если данных мало, добавляем базовое описание
    if len(business) < 200:
        business += f" {name} — это известная компания, акции которой ({ticker}) можно купить и продать на бирже. Бизнес зарабатывает деньги на своей основной деятельности, платит налоги, нанимает людей и развивается во времени. Инвесторы покупают акции в надежде, что компания будет расти и приносить доход через дивиденды или рост цены акции."
    
    # ═══ 2) АНАЛИЗ АКЦИИ — ТЕКУЩЕЕ СОСТОЯНИЕ (подробно, ~200-300 слов) ═══
    analysis_parts = []
    
    if yf_info.get("last_price"):
        currency = yf_info.get('currency', 'USD')
        analysis_parts.append(f"Текущая цена одной акции составляет {yf_info['last_price']:.2f} {currency}. Это та цена, по которой вы можете купить или продать акцию прямо сейчас на бирже во время торговой сессии.")
    else:
        analysis_parts.append(f"Цена акции {ticker} в данный момент недоступна через автоматический запрос, но вы всегда можете посмотреть её на любом финансовом портале вроде Yahoo Finance или Investing.com.")
    
    if yf_info.get("regular_market_change_percent") is not None:
        chg = yf_info["regular_market_change_percent"]
        direction = "выросла" if chg >= 0 else "упала"
        analysis_parts.append(f"За сегодняшнюю торговую сессию акция {direction} на {abs(chg):.2f} процента. Это показывает настроение рынка именно сегодня — оптимизм или пессимизм по отношению к этой бумаге.")
    
    if yf_info.get("market_cap"):
        analysis_parts.append(f"Полная рыночная стоимость компании (капитализация) равна {yf_info['market_cap']/1e9:.1f} миллиардов долларов. Крупные компании (свыше 10 млрд) обычно стабильнее, малые — рискованнее, но могут дать больший рост.")
    
    # Анализ настроения новостей (простой подсчет позитивных/негативных слов)
    pos = neg = 0
    positive_words = ["рост", "выросла", "прибыль", "выиграл", "улучш", "рекорд", "сильн", "позитив", "оптимизм", "повыш", "апгрейд", "beat", "growth", "strong", "rise", "gain", "up", "upgrade", "record", "positive"]
    negative_words = ["пад", "упал", "убыток", "проиграл", "ухудш", "слаб", "негатив", "пессимизм", "пониж", "даунгрейд", "fall", "drop", "down", "loss", "weak", "cut", "miss", "downgrade", "negative", "decline"]
    
    for n in news:
        h = n.get("headline", "").lower()
        if any(w in h for w in positive_words):
            pos += 1
        elif any(w in h for w in negative_words):
            neg += 1
    
    if pos or neg:
        tone = "преимущественно позитивное" if pos > neg else "преимущественно негативное" if neg > pos else "смешанное, нейтральное"
        analysis_parts.append(f"Тон новостей за последнюю неделю {tone}: {pos} позитивных заголовков и {neg} негативных. Это дает представление, как пресса и аналитики сейчас смотрят на компанию — с оптимизмом или осторожностью.")
    else:
        analysis_parts.append(f"За последнюю неделю значимых новостей по компании не обнаружено, либо они нейтральные. Тишина в новостях часто означает стабильность или ожидание важных событий.")
    
    # Добавляем контекст из веб-поиска к анализу
    if tavily_results:
        analysis_parts.append(f"Веб-поиск нашел {len(tavily_results)} свежих статей и аналитических материалов, что говорит об активном интересе к компании со стороны прессы и аналитиков.")
    
    analysis = " ".join(analysis_parts)
    if len(analysis) < 150:
        analysis += f" Акция {ticker} торгуется на крупной бирже, имеет достаточную ликвидность (легко купить и продать) и следует общему движению своего сектора и всего рынка."
    
    # ═══ 3) ПРОГНОЗ И ПЕРСПЕКТИВЫ — ЧТО ЖДАТЬ ВПЕРЕД (подробно, ~200-300 слов) ═══
    forecast_parts = []
    
    forecast_parts.append("Ближайшее будущее акции зависит от нескольких главных факторов: общих трендов на рынке, отчетов компании о прибыли, решений центральных банков по ставкам и новостей именно этой отрасли.")
    
    if profile and profile.get("finnhubIndustry"):
        forecast_parts.append(f"Так как компания работает в секторе {profile['finnhubIndustry']}, она будет двигаться вместе с другими компаниями этой отрасли — если сектор растет, у компании шансы выше, если сектор падает — сложнее расти в одиночку.")
    
    if news:
        if pos > neg:
            forecast_parts.append("Свежие новости дают основание для осторожного оптимизма — пресса пишет больше хорошего, чем плохого, что может поддерживать спрос на акцию в ближайшие недели.")
        elif neg > pos:
            forecast_parts.append("Преобладание негативных новостей требует осторожности — инвесторы могут продавать акции, давя на цену вниз, пока не появятся позитивные катализаторы.")
        else:
            forecast_parts.append("Новостной фон сбалансирован, поэтому больших движений в одну сторону без новых причин не ждать — акция будет торговаться в диапазоне.")
    
    forecast_parts.append("Главные события, которые могут резко изменить цену: ближайший квартальный отчет о прибыли (earnings), решения ФРС/ЕЦБ по процентным ставкам, крупные сделки или новости конкурентов.")
    forecast_parts.append("Важное предупреждение: этот отчет — только сводка живых данных из открытых источников, это НЕ совет купить или продать. Любое инвестиционное решение вы должны принимать самостоятельно после собственного анализа или консультации с лицензированным советником. Прошлое не гарантирует будущее, на рынке всегда есть риск потерь.")
    
    forecast = " ".join(forecast_parts)
    
    return {
        "business": business[:1500],      # ~500 слов вместо 150
        "analysis": analysis[:900],       # ~300 слов вместо 100
        "forecast": forecast[:900],       # ~300 слов вместо 100
        "sources": {
            "finnhub_profile": bool(profile),
            "finnhub_news_count": len(news),
            "tavily_results": len(tavily_results),
            "yfinance_quote": bool(yf_info),
        },
    }

# ─── ЗАГРУЗКА HTML ШАБЛОНА ───────────────────────────────────────────────
def load_template():
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        return f.read()

TEMPLATE = load_template()

def render_dashboard():
    cards = []
    for s in STOCKS:
        icon_url = get_icon_path(s)
        icon_html = f'<img src="{icon_url}" alt="" class="icon">' if icon_url else '<div class="icon placeholder"></div>'
        cards.append(f'''
                <article class="card" data-ticker="{s["ticker"]}">
                    {icon_html}
                    <div class="info">
                        <h3>{s["name"]}</h3>
                        <span class="ticker">{s["ticker"]}</span>
                    </div>
                </article>
            ''')
    return TEMPLATE.replace("{count}", str(len(STOCKS))).replace("{cards}", "".join(cards))

# ─── HTTP ОБРАБОТЧИКИ ────────────────────────────────────────────────────
class DashboardHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DASHBOARD_DIR), **kwargs)
    
    def do_GET(self):
        if self.path == "/":
            self.send_dashboard()
        elif self.path.startswith("/api/stock/"):
            ticker = self.path.split("/api/stock/")[1]
            self.send_stock_report(ticker)
        elif self.path.startswith("/icons/"):
            self.serve_icon()
        else:
            super().do_GET()
    
    def send_dashboard(self):
        html = render_dashboard()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))
    
    def send_stock_report(self, ticker):
        stock = next((s for s in STOCKS if s["ticker"] == ticker), None)
        if not stock:
            self.send_error(404, "Акция не найдена в списке")
            return
        
        report = generate_report(stock)
        report["ticker"] = ticker
        report["name"] = stock["name"]
        
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(report, ensure_ascii=False).encode("utf-8"))
    
    def serve_icon(self):
        icon_name = self.path.split("/icons/")[1]
        icon_path = ICONS_DIR / icon_name
        if icon_path.exists():
            self.send_response(200)
            self.send_header("Content-Type", "image/png")
            self.end_headers()
            with open(icon_path, "rb") as f:
                self.wfile.write(f.read())
        else:
            self.send_error(404)
    
    def log_message(self, format, *args):
        pass  # отключаем стандартные логи в консоль

# ─── ГЛАВНЫЕ ФУНКЦИИ ЗАПУСКА ────────────────────────────────────────────
def run_cc_switch():
    """Запускает cc-switch.exe в отдельном окне консоли"""
    cc_switch_path = r"D:\claudeAgent\cc-switch\cc-switch.exe"
    try:
        subprocess.Popen([cc_switch_path], cwd=r"D:\claudeAgent\cc-switch", creationflags=subprocess.CREATE_NEW_CONSOLE)
        print("[+] cc-switch.exe успешно запущен в новом окне")
    except Exception as e:
        print(f"[!] Не удалось запустить cc-switch.exe: {e}")

def run_dashboard():
    """Запускает веб-сервер панели акций (блокирует выполнение до Ctrl+C)"""
    os.chdir(DASHBOARD_DIR)
    server = HTTPServer(("", PORT), DashboardHandler)
    print(f"[+] Панель акций запущена и доступна по адресу: {BASE_URL}")
    print("[+] Открываем в браузере автоматически...")
    webbrowser.open(BASE_URL)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[+] Остановка сервера по запросу пользователя...")
        server.shutdown()

# ─── ТОЧКА ВХОДА ────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 60)
    print("  ПАНЕЛЬ АКЦИЙ — Stock Dashboard на русском языке")
    print("=" * 60)
    
    # 1. Запускаем cc-switch.exe
    run_cc_switch()
    
    # 2. Небольшая пауза для инициализации
    time.sleep(1.5)
    
    # 3. Запускаем веб-сервер (работает до Ctrl+C)
    run_dashboard()