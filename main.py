from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1 style='background:black;color:gold;padding:40px;text-align:center'>
    GOLD XAU MASTERPIECE LIVE - SIN Region<br>
    Deploy Success bos!
    </h1>
    <p style='text-align:center'><a href='/docs'>Buka API Docs</a></p>
    """

@app.get("/api/gold")
def gold_price():
    return {"XAUUSD": 2655.75, "status": "LIVE", "region": "sin"}
