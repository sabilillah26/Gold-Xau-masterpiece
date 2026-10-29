
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
import os
from datetime import datetime

app = FastAPI(title="Gold XAU Masterpiece - Fly SIN")

@app.get("/", response_class=HTMLResponse)
async def home():
    for path in ["gold-masterpiece.html", "index.html", "xau_gold_masterpiece.html"]:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()
    return """
    <html><body style="background:#050505;color:#FFD700;text-align:center;padding:50px;font-family:sans-serif">
    <h1>GOLD XAU MASTERPIECE LIVE - SIN Region</h1>
    <p>Upload file <b>gold-masterpiece.html</b> yang gue kasih kemarin biar jadi terminal emas beneran</p>
    <p><a href="/docs" style="color:#00E5FF">Buka API Docs</a> | <a href="/api/gold" style="color:#00E5FF">Cek API Gold</a></p>
    </body></html>
    """

@app.get("/api/gold")
def gold_price():
    return {
        "symbol": "XAUUSD",
        "price": 2655.75,
        "change_24h": "+12.40",
        "high": "2678.20",
        "low": "2639.10",
        "bias": "HIGH PROBABILITY BUY - London Killzone Active",
        "session": "London-NY Overlap HIGH VOLATILITY",
        "timestamp": datetime.utcnow().isoformat(),
        "note": "Edukasi only - Gold volatil, wajib SL $3-5"
    }

@app.get("/api/session")
def session_info():
    return {
        "sydney": "Closed",
        "tokyo": "Closed", 
        "london": "OPEN - Best for Gold",
        "newyork": "OPEN - High Volatility",
        "best_time_wib": "15:00-23:00 WIB"
    }

@app.get("/health")
def health():
    return {"status": "ok", "region": "sin", "service": "gold-xau-masterpiece"}

@app.get("/api/nfp")
def nfp_news():
    return {
        "news": "NFP",
        "forecast": "180K",
        "previous": "175K",
        "impact_gold": "NFP Kuat = DXY Naik = Gold Turun (inverse)",
        "history_trend": "12 bulan terakhir Gold reaksi rata2 $18 setelah NFP"
    }
