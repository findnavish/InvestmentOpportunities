"""Fetch and cache raw market/fundamental data for the silicon supply chain universe."""
import io, json, time, zipfile, warnings
from pathlib import Path
import pandas as pd
import requests
import yfinance as yf
from universe import UNIVERSE, BENCH, FX, RATES

warnings.filterwarnings("ignore")
DATA = Path(__file__).parent / "data"
DATA.mkdir(exist_ok=True)


def prices():
    syms = list(UNIVERSE) + list(BENCH) + [v[0] for v in FX.values()] + list(RATES)
    df = yf.download(syms, period="6y", interval="1d", auto_adjust=True, progress=False, threads=True)["Close"]
    df.to_csv(DATA / "prices_daily.csv")
    yf.download("TWD=X", period="6y", auto_adjust=True, progress=False)["Close"].to_csv(DATA / "twd.csv")
    print("prices", df.shape, "missing cols:", [c for c in syms if c not in df or df[c].dropna().empty])


INFO_KEYS = ["longName", "currency", "financialCurrency", "marketCap", "enterpriseValue", "currentPrice", "trailingPE",
             "forwardPE", "pegRatio", "trailingPegRatio", "priceToBook", "priceToSalesTrailing12Months",
             "enterpriseToEbitda", "enterpriseToRevenue", "returnOnEquity", "returnOnAssets", "profitMargins",
             "operatingMargins", "grossMargins", "ebitdaMargins", "revenueGrowth", "earningsGrowth", "dividendYield",
             "payoutRatio", "debtToEquity", "currentRatio", "quickRatio", "totalCash", "totalDebt", "freeCashflow",
             "operatingCashflow", "trailingEps", "forwardEps", "bookValue", "sharesOutstanding", "totalRevenue",
             "ebitda", "netIncomeToCommon", "beta", "targetMeanPrice", "targetHighPrice", "targetLowPrice",
             "recommendationKey", "numberOfAnalystOpinions", "fiftyTwoWeekHigh", "fiftyTwoWeekLow",
             "heldPercentInstitutions", "shortPercentOfFloat"]

STMT_ROWS = {
    "inc": ["Total Revenue", "Gross Profit", "Operating Income", "EBIT", "Pretax Income", "Tax Provision",
            "Net Income", "Interest Expense", "Research And Development", "Reconciled Depreciation"],
    "bal": ["Total Assets", "Stockholders Equity", "Total Debt", "Cash And Cash Equivalents", "Working Capital"],
    "cf": ["Operating Cash Flow", "Capital Expenditure", "Free Cash Flow", "Cash Dividends Paid", "Repurchase Of Capital Stock"],
}


def fundamentals():
    info, stmts, iv = {}, {}, {}
    for t in UNIVERSE:
        for attempt in range(3):
            try:
                tk = yf.Ticker(t)
                i = tk.info
                info[t] = {k: i.get(k) for k in INFO_KEYS}
                s = {}
                for key, frame in (("inc", tk.income_stmt), ("bal", tk.balance_sheet), ("cf", tk.cashflow)):
                    f = frame.reindex(STMT_ROWS[key]) if frame is not None and not frame.empty else pd.DataFrame()
                    s[key] = {str(c.date()): {r: (None if pd.isna(v) else float(v)) for r, v in f[c].items()}
                              for c in f.columns[:4]} if not f.empty else {}
                stmts[t] = s
                if "." not in t:  # US-listed options: ATM implied vol ~30-60 days out
                    iv[t] = atm_iv(tk, i.get("currentPrice"))
                print("ok", t)
                break
            except Exception as e:
                print("retry", t, e)
                time.sleep(3 * (attempt + 1))
        time.sleep(0.8)
    json.dump(info, open(DATA / "info.json", "w"), indent=1, default=str)
    json.dump(stmts, open(DATA / "statements.json", "w"), indent=1, default=str)
    json.dump(iv, open(DATA / "implied_vol.json", "w"), indent=1, default=str)


def atm_iv(tk, spot):
    try:
        exps = tk.options
        today = pd.Timestamp.today()
        pick = [e for e in exps if 25 <= (pd.Timestamp(e) - today).days <= 70] or exps[:1]
        ch = tk.option_chain(pick[0])
        out = {}
        for side, df in (("call", ch.calls), ("put", ch.puts)):
            df = df[(df.volume.fillna(0) + df.openInterest.fillna(0)) > 0]
            j = (df.strike - spot).abs().idxmin()
            out[side] = float(df.loc[j, "impliedVolatility"])
        out["expiry"] = pick[0]
        return out
    except Exception as e:
        return {"error": str(e)}


def fama_french():
    base = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/"
    for name in ("F-F_Research_Data_5_Factors_2x3_CSV.zip", "F-F_Momentum_Factor_CSV.zip"):
        r = requests.get(base + name, timeout=60)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        txt = z.read(z.namelist()[0]).decode("latin1")
        (DATA / name.replace(".zip", ".txt")).write_text(txt)
        print("ff", name, len(txt))


def patch_last():
    """Yahoo daily bars can lag for the latest US session; capture last traded price for US listings."""
    syms = [t for t in UNIVERSE if "." not in t] + list(BENCH)
    out = {}
    for t in syms:
        try:
            out[t] = float(yf.Ticker(t).fast_info["last_price"])
        except Exception as e:
            print("patch fail", t, e)
    now = pd.Timestamp.now(tz="America/New_York")
    session = now.normalize() if now.hour * 60 + now.minute >= 16 * 60 + 15 else now.normalize() - pd.Timedelta(days=1)
    session = pd.offsets.BDay().rollback(session.tz_localize(None))  # last completed US session (holidays not handled)
    json.dump({"date": str(session.date()), "prices": out}, open(DATA / "last_us_prices.json", "w"), indent=1)
    print("patched", len(out))


if __name__ == "__main__":
    import sys
    steps = sys.argv[1:] or ["prices", "patch", "fundamentals", "ff"]
    if "prices" in steps: prices()
    if "patch" in steps: patch_last()
    if "ff" in steps: fama_french()
    if "fundamentals" in steps: fundamentals()
