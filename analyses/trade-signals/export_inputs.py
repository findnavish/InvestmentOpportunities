"""Export the slow-moving model inputs (weekly) that the hourly signal engine needs."""
import json, sys
from pathlib import Path
import numpy as np
import pandas as pd

HERE = Path(__file__).parent
SRC = HERE.parent / "silicon-supply-chain"
sys.path.insert(0, str(SRC))
from universe import UNIVERSE  # noqa: E402

R = pd.read_pickle(SRC / "output" / "results.pkl")
S = R["sheets"]
info = json.load(open(SRC / "data" / "info.json"))
idx, f, sc, v, A = S["Index_Model_CAPM_Ch8_9"], S["Fundamentals_DuPont_Ch19"], S["Scorecard"], S["Valuation_Ch18"], S["Assumptions"]["value"]


GROUP = {"IP": "IP/EDA", "EDA": "IP/EDA", "Foundry": "Foundry/IDM", "IDM": "Foundry/IDM"}


def clean(x):
    if x is None:
        return None
    try:
        x = float(x)
    except (TypeError, ValueError):
        return None
    return None if np.isnan(x) else x


out = {"as_of": str(A["price_date"]), "rf_1y": clean(R["rf"]), "mrp": clean(A["market_risk_premium"]), "tickers": {}}
for t, (name, seg, country, ccy) in UNIVERSE.items():
    i = info.get(t, {})
    out["tickers"][t] = {
        "name": name, "segment": seg, "group": "Memory" if t == "005930.KS" else GROUP.get(seg.split(" - ")[0].split(" & ")[0], seg.split(" - ")[0]), "country": country, "ccy": ccy,
        "beta_adj": clean(idx.loc[t, "beta_adj_blume"]), "resid_sd": clean(idx.loc[t, "resid_sd_ann"]),
        "target_mean": clean(i.get("targetMeanPrice")), "n_analysts": clean(i.get("numberOfAnalystOpinions")),
        "div_yield": clean(f.loc[t, "div_yield"]) or 0.0, "quality_z": clean(sc.loc[t, "Quality"]) or 0.0,
        "roe": clean(f.loc[t, "roe_dupont"]), "fwd_pe": clean(v.loc[t, "forward_pe"]),
        "implied_g": clean(v.loc[t, "implied_stage1_growth"]), "pvgo_share": clean(v.loc[t, "PVGO_share_of_price"]),
    }
(HERE / "state").mkdir(exist_ok=True)
json.dump(out, open(HERE / "state" / "model_inputs.json", "w"), indent=1)
print("model inputs exported", len(out["tickers"]), "as of", out["as_of"])
