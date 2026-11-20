---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-20 20:22 UTC (Fri Nov 20, 03:22 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🟢 open (Fri 15:22) · Tokyo 🔴 closed (Sat 05:22) · Korea 🔴 closed (Sat 05:22) · Hong Kong 🔴 closed (Sat 04:22) · Xetra 🔴 closed (Fri 21:22) · Euronext Amsterdam 🔴 closed (Fri 21:22)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$758,047** | $304,017 (40%) | $454,030 (60%) | -24.20% | -78.00% | 🔴 Risk-off (-22.7%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $758,047), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| ADD | **MRVL**<br><small>Marvell Technology</small> | 353 | 123.14 USD | $43,470 | Executed (paper) | analyst α +0.85 · momentum +0.41 · ⚠️ oversold, rich valuation |
| SELL (exit) | **NVDA**<br><small>NVIDIA</small> | 268 | 128.30 USD | $34,384 | Executed (paper) | quality +0.21 · momentum -0.20 · ⚠️ oversold |
| TRIM | **MU**<br><small>Micron Technology</small> | 52 | 596.09 USD | $30,997 | Executed (paper) | momentum +0.53 · quality +0.06 · ⚠️ oversold, cycle-peak P/E |
| ADD | **INTC**<br><small>Intel</small> | 365 | 52.70 USD | $19,236 | Executed (paper) | analyst α +0.66 · momentum +0.30 · ⚠️ oversold, rich valuation, high σ(e) |
| ADD | **AMAT**<br><small>Applied Materials</small> | 62 | 303.83 USD | $18,837 | Executed (paper) | analyst α +0.48 · momentum +0.07 |
| ADD | **TER**<br><small>Teradyne</small> | 88 | 204.82 USD | $18,024 | Executed (paper) | analyst α +0.55 · trend -0.25 · ⚠️ oversold |
| TRIM | **KLAC**<br><small>KLA Corp</small> | 118 | 126.94 USD | $14,979 | Executed (paper) | quality +0.24 · analyst α +0.15 |
| ADD | **LRCX**<br><small>Lam Research</small> | 78 | 183.04 USD | $14,277 | Executed (paper) | analyst α +0.36 · trend -0.14 |
| ADD | **Infineon**<br><small>IFX.DE</small> | 180 | 45.56 EUR | $8,997 | Queued · Xetra closed | analyst α +0.23 · momentum +0.05 |
| ADD | **ASX**<br><small>ASE Technology</small> | 205 | 26.54 USD | $5,441 | Executed (paper) | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +2.65 | **MRVL**<br><small>Marvell Technology</small> | 123.14 USD | +139% | +14.5% | +175% | -35% | 28 | -0.12 | 9.8% → 9.8% | ADD 353 | analyst α +0.85 · momentum +0.41 · ⚠️ oversold, rich valuation |
| 🟢🟢 Strong Buy | +1.41 | **MU**<br><small>Micron Technology</small> | 596.09 USD | – | +0.0% | +280% | -23% | 30 | +0.12 | 5.0% → 5.0% | TRIM 52 | momentum +0.53 · quality +0.06 · ⚠️ oversold, cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.26 | **INTC**<br><small>Intel</small> | 52.70 USD | +121% | +10.0% | +143% | -40% | 29 | -0.62 | 4.1% → 4.1% | ADD 365 | analyst α +0.66 · momentum +0.30 · ⚠️ oversold, rich valuation, high σ(e) |
| 🟢🟢 Strong Buy | +1.21 | **AMAT**<br><small>Applied Materials</small> | 303.83 USD | +110% | +8.1% | +61% | -32% | 31 | +0.03 | 5.9% → 5.9% | ADD 62 | analyst α +0.48 · momentum +0.07 |
| 🟢🟢 Strong Buy | +1.15 | **SK hynix**<br><small>000660.KS</small> | 1,101,000 KRW | – | +0.0% | +102% | -28% | 37 | +0.62 | 4.4% → 3.9% | – | quality +0.33 · momentum +0.20 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢 Buy | +0.66 | **TER**<br><small>Teradyne</small> | 204.82 USD | +118% | +9.8% | +84% | -41% | 29 | -0.31 | 3.3% → 3.3% | ADD 88 | analyst α +0.55 · trend -0.25 · ⚠️ oversold |
| 🟢 Buy | +0.66 | **ASX**<br><small>ASE Technology</small> | 26.54 USD | +92% | +1.8% | +171% | -23% | 31 | -0.68 | 3.5% → 3.5% | ADD 205 | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.64 | **Infineon**<br><small>IFX.DE</small> | 45.56 EUR | +90% | +2.5% | +59% | -21% | 36 | -0.04 | 2.4% → 3.6% | ADD 180 | analyst α +0.23 · momentum +0.05 |
| 🟢 Buy | +0.62 | **LRCX**<br><small>Lam Research</small> | 183.04 USD | +105% | +6.5% | +55% | -35% | 30 | +0.02 | 3.3% → 3.3% | ADD 78 | analyst α +0.36 · trend -0.14 |
| 🟢 Buy | +0.47 | **KLAC**<br><small>KLA Corp</small> | 126.94 USD | +84% | +1.7% | +27% | -30% | 33 | +0.51 | 2.5% → 2.5% | TRIM 118 | quality +0.24 · analyst α +0.15 |
| 🟢 Buy | +0.37 | **Advantest**<br><small>6857.T</small> | 24,255 JPY | +76% | -1.0% | +63% | -18% | 33 | +0.33 | 2.0% → 1.4% | – | analyst α -0.19 · quality +0.16 · ⚠️ rich valuation |
| ⚪ Hold | +0.24 | **GFS**<br><small>GlobalFoundries</small> | 36.16 USD | +110% | +7.8% | +32% | -34% | 33 | -0.21 | 0.0% → 0.0% | – | analyst α +0.41 · quality -0.13 |
| ⚪ Hold | +0.08 | **Samsung**<br><small>005930.KS</small> | 182,600 KRW | – | +0.0% | +119% | -23% | 35 | -0.26 | 8.2% → 8.2% | – | momentum +0.23 · quality -0.16 · ⚠️ cycle-peak P/E |
| ⚪ Hold | +0.08 | **TSM**<br><small>TSMC</small> | 321.19 USD | +72% | -1.2% | +48% | -20% | 29 | +0.58 | 5.4% → 5.4% | – | quality +0.28 · analyst α -0.23 · ⚠️ oversold |
| ⚪ Hold | +0.05 | **Tokyo Electron**<br><small>8035.T</small> | 8,347 JPY | +83% | +1.1% | +55% | -20% | 37 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · analyst α +0.12 |
| ⚪ Hold | -0.01 | **ARM**<br><small>Arm Holdings</small> | 154.38 USD | +87% | +0.2% | +53% | -34% | 32 | +0.04 | 0.0% → 0.0% | – | trend -0.10 · analyst α +0.08 · ⚠️ rich valuation, high σ(e) |
| ⚪ Hold | -0.16 | **AMD**<br><small>Advanced Micro Devices</small> | 426.67 USD | +45% | -9.1% | +127% | -1% | 39 | -0.15 | 0.0% → 0.0% | – | analyst α -0.48 · momentum +0.26 |
| ⚪ Hold | -0.24 | **ASML**<br><small>ASML Holding</small> | 1,268.26 USD | +65% | -3.3% | +51% | -21% | 29 | +0.42 | 0.0% → 0.0% | – | analyst α -0.27 · quality +0.18 · ⚠️ oversold |
| 🔴 Sell | -0.25 | **Disco**<br><small>6146.T</small> | 41,390 JPY | +97% | +5.0% | +7% | -36% | 35 | +0.06 | 0.0% → 0.0% | – | analyst α +0.27 · momentum -0.26 |
| 🔴 Sell | -0.46 | **NVDA**<br><small>NVIDIA</small> | 128.30 USD | – | +0.0% | +14% | -37% | 16 | +0.47 | 0.0% → 0.0% | SELL 268 | quality +0.21 · momentum -0.20 · ⚠️ oversold |
| 🔴 Sell | -0.53 | **ASMI**<br><small>ASM.AS</small> | 642.00 EUR | +76% | -1.0% | +52% | -21% | 38 | -0.10 | 0.0% → 0.0% | – | analyst α -0.15 · quality -0.06 |
| 🔴 Sell | -0.73 | **TXN**<br><small>Texas Instruments</small> | 266.39 USD | +22% | -13.4% | +81% | +1% | 37 | +0.24 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -0.75 | **ENTG**<br><small>Entegris</small> | 125.62 USD | +38% | -9.9% | +74% | -10% | 39 | -0.02 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.16 |
| 🔴🔴 Strong Sell | -0.78 | **AVGO**<br><small>Broadcom</small> | 304.27 USD | +75% | -0.6% | -8% | -17% | 41 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.12 |
| 🔴🔴 Strong Sell | -0.87 | **QCOM**<br><small>Qualcomm</small> | 153.06 USD | +27% | -12.5% | +6% | -10% | 37 | +0.70 | 0.0% → 0.0% | – | analyst α -0.66 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.88 | **SNPS**<br><small>Synopsys</small> | 400.43 USD | +42% | -8.7% | +9% | -9% | 32 | +0.14 | 0.0% → 0.0% | – | analyst α -0.41 · momentum -0.23 |
| 🔴🔴 Strong Sell | -1.06 | **Shin-Etsu**<br><small>4063.T</small> | 5,273 JPY | +47% | -7.1% | +32% | -17% | 32 | -0.20 | 0.0% → 0.0% | – | analyst α -0.31 · momentum -0.12 |
| 🔴🔴 Strong Sell | -1.08 | **CDNS**<br><small>Cadence Design Systems</small> | 283.58 USD | +43% | -8.4% | +1% | -14% | 32 | +0.31 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.35 |
| 🔴🔴 Strong Sell | -1.43 | **SMIC**<br><small>0981.HK</small> | 49.12 HKD | +95% | +5.4% | -36% | -25% | 48 | -0.99 | 0.0% → 0.0% | – | momentum -0.53 · quality -0.33 |
| 🔴🔴 Strong Sell | -2.30 | **AMKR**<br><small>Amkor Technology</small> | 30.48 USD | – | +0.0% | +25% | -46% | 34 | -1.00 | 0.0% → 0.0% | – | quality -0.43 · trend -0.32 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +2.65"
    **ADD 353 sh** → target 9.8% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 293.88 USD vs 123.14 USD (+139%, 43 analysts); de-biased α +14.5% vs CAPM hurdle 14.1%. Downtrend -35% vs 200-day avg; 12-1 mom +175%; RSI 28. Quality z -0.12 (ROE 19%). ⚠️ oversold; price implies 78% stage-1 growth (reverse DCF).

??? success "MU (MU) — 🟢🟢 Strong Buy, score +1.41"
    **TRIM 52 sh** → target 5.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). No reliable analyst target: α set to 0. Downtrend -23% vs 200-day avg; 12-1 mom +280%; RSI 30. Quality z +0.12 (ROE 17%). ⚠️ oversold; cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "INTC (INTC) — 🟢🟢 Strong Buy, score +1.26"
    **ADD 365 sh** → target 4.1% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 116.37 USD vs 52.70 USD (+121%, 43 analysts); de-biased α +10.0% vs CAPM hurdle 14.0%. Downtrend -40% vs 200-day avg; 12-1 mom +143%; RSI 29. Quality z -0.62 (ROE -0%). ⚠️ oversold; price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "AMAT (AMAT) — 🟢🟢 Strong Buy, score +1.21"
    **ADD 62 sh** → target 5.9% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 303.83 USD (+110%, 36 analysts); de-biased α +8.1% vs CAPM hurdle 11.6%. Downtrend -32% vs 200-day avg; 12-1 mom +61%; RSI 31. Quality z +0.03 (ROE 36%).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.15"
    Within rebalance band of target 3.9%: no trade. No reliable analyst target: α set to 0. Downtrend -28% vs 200-day avg; 12-1 mom +102%; RSI 37. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "TER (TER) — 🟢 Buy, score +0.66"
    **ADD 88 sh** → target 3.3% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 446.47 USD vs 204.82 USD (+118%, 15 analysts); de-biased α +9.8% vs CAPM hurdle 12.3%. Downtrend -41% vs 200-day avg; 12-1 mom +84%; RSI 29. Quality z -0.31 (ROE 20%). ⚠️ oversold.

??? success "ASX (ASX) — 🟢 Buy, score +0.66"
    **ADD 205 sh** → target 3.5% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 51.00 USD vs 26.54 USD (+92%, 1 analysts); de-biased α +1.8% vs CAPM hurdle 11.9%. Downtrend -23% vs 200-day avg; 12-1 mom +171%; RSI 31. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.64"
    **ADD 180 sh** → target 3.6% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 86.74 EUR vs 45.56 EUR (+90%, 23 analysts); de-biased α +2.5% vs CAPM hurdle 14.1%. Downtrend -21% vs 200-day avg; 12-1 mom +59%; RSI 36. Quality z -0.04 (ROE 6%).

??? success "LRCX (LRCX) — 🟢 Buy, score +0.62"
    **ADD 78 sh** → target 3.3% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 375.06 USD vs 183.04 USD (+105%, 31 analysts); de-biased α +6.5% vs CAPM hurdle 12.6%. Downtrend -35% vs 200-day avg; 12-1 mom +55%; RSI 30. Quality z +0.02 (ROE 65%).

??? success "KLAC (KLAC) — 🟢 Buy, score +0.47"
    **TRIM 118 sh** → target 2.5% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 233.77 USD vs 126.94 USD (+84%, 26 analysts); de-biased α +1.7% vs CAPM hurdle 11.1%. Downtrend -30% vs 200-day avg; 12-1 mom +27%; RSI 33. Quality z +0.51 (ROE 87%).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.37"
    Within rebalance band of target 1.4%: no trade. Analyst target 42,686 JPY vs 24,255 JPY (+76%, 21 analysts); de-biased α -1.0% vs CAPM hurdle 13.4%. Downtrend -18% vs 200-day avg; 12-1 mom +63%; RSI 33. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "GFS (GFS) — ⚪ Hold, score +0.24"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 36.16 USD (+110%, 22 analysts); de-biased α +7.8% vs CAPM hurdle 12.4%. Downtrend -34% vs 200-day avg; 12-1 mom +32%; RSI 33. Quality z -0.21 (ROE 8%).

??? note "Samsung (005930.KS) — ⚪ Hold, score +0.08"
    Hold zone: keep any existing position, no new money. No reliable analyst target: α set to 0. Downtrend -23% vs 200-day avg; 12-1 mom +119%; RSI 35. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? note "TSM (TSM) — ⚪ Hold, score +0.08"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 321.19 USD (+72%, 20 analysts); de-biased α -1.2% vs CAPM hurdle 10.8%. Downtrend -20% vs 200-day avg; 12-1 mom +48%; RSI 29. Quality z +0.58 (ROE 35%). ⚠️ oversold.

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.05"
    Hold zone: not owned, no entry. Analyst target 15,275 JPY vs 8,347 JPY (+83%, 23 analysts); de-biased α +1.1% vs CAPM hurdle 12.8%. Downtrend -20% vs 200-day avg; 12-1 mom +55%; RSI 37. Quality z -0.28 (ROE 29%).

??? note "ARM (ARM) — ⚪ Hold, score -0.01"
    Hold zone: not owned, no entry. Analyst target 288.70 USD vs 154.38 USD (+87%, 40 analysts); de-biased α +0.2% vs CAPM hurdle 19.6%. Downtrend -34% vs 200-day avg; 12-1 mom +53%; RSI 32. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? note "AMD (AMD) — ⚪ Hold, score -0.16"
    Hold zone: not owned, no entry. Analyst target 619.51 USD vs 426.67 USD (+45%, 50 analysts); de-biased α -9.1% vs CAPM hurdle 14.9%. Downtrend -1% vs 200-day avg; 12-1 mom +127%; RSI 39. Quality z -0.15 (ROE 7%).

??? note "ASML (ASML) — ⚪ Hold, score -0.24"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,268.26 USD (+65%, 16 analysts); de-biased α -3.3% vs CAPM hurdle 12.3%. Downtrend -21% vs 200-day avg; 12-1 mom +51%; RSI 29. Quality z +0.42 (ROE 50%). ⚠️ oversold.

??? failure "Disco (6146.T) — 🔴 Sell, score -0.25"
    Avoid: not owned. Analyst target 81,730 JPY vs 41,390 JPY (+97%, 20 analysts); de-biased α +5.0% vs CAPM hurdle 11.5%. Downtrend -36% vs 200-day avg; 12-1 mom +7%; RSI 35. Quality z +0.06 (ROE 25%).

??? failure "NVDA (NVDA) — 🔴 Sell, score -0.46"
    **SELL (exit) 268 sh** → target 0.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). No reliable analyst target: α set to 0. Downtrend -37% vs 200-day avg; 12-1 mom +14%; RSI 16. Quality z +0.47 (ROE 101%). ⚠️ oversold.

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.53"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 642.00 EUR (+76%, 19 analysts); de-biased α -1.0% vs CAPM hurdle 13.2%. Downtrend -21% vs 200-day avg; 12-1 mom +52%; RSI 38. Quality z -0.10 (ROE 19%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.73"
    Avoid: not owned. Analyst target 324.71 USD vs 266.39 USD (+22%, 31 analysts); de-biased α -13.4% vs CAPM hurdle 10.8%. Uptrend +1% vs 200-day avg; 12-1 mom +81%; RSI 37. Quality z +0.24 (ROE 30%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.75"
    Avoid: not owned. Analyst target 173.36 USD vs 125.62 USD (+38%, 11 analysts); de-biased α -9.9% vs CAPM hurdle 11.0%. Downtrend -10% vs 200-day avg; 12-1 mom +74%; RSI 39. Quality z -0.02 (ROE 6%).

??? failure "AVGO (AVGO) — 🔴🔴 Strong Sell, score -0.78"
    Avoid: not owned. Analyst target 531.31 USD vs 304.27 USD (+75%, 47 analysts); de-biased α -0.6% vs CAPM hurdle 11.2%. Downtrend -17% vs 200-day avg; 12-1 mom -8%; RSI 41. Quality z +0.26 (ROE 31%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.87"
    Avoid: not owned. Analyst target 194.13 USD vs 153.06 USD (+27%, 30 analysts); de-biased α -12.5% vs CAPM hurdle 11.9%. Downtrend -10% vs 200-day avg; 12-1 mom +6%; RSI 37. Quality z +0.70 (ROE 23%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.88"
    Avoid: not owned. Analyst target 569.78 USD vs 400.43 USD (+42%, 26 analysts); de-biased α -8.7% vs CAPM hurdle 10.3%. Downtrend -9% vs 200-day avg; 12-1 mom +9%; RSI 32. Quality z +0.14 (ROE 7%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.06"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,273 JPY (+47%, 17 analysts); de-biased α -7.1% vs CAPM hurdle 10.8%. Downtrend -17% vs 200-day avg; 12-1 mom +32%; RSI 32. Quality z -0.20 (ROE 10%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.08"
    Avoid: not owned. Analyst target 405.47 USD vs 283.58 USD (+43%, 26 analysts); de-biased α -8.4% vs CAPM hurdle 10.0%. Downtrend -14% vs 200-day avg; 12-1 mom +1%; RSI 32. Quality z +0.31 (ROE 22%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.43"
    Avoid: not owned. Analyst target 95.99 HKD vs 49.12 HKD (+95%, 21 analysts); de-biased α +5.4% vs CAPM hurdle 7.3%. Downtrend -25% vs 200-day avg; 12-1 mom -36%; RSI 48. Quality z -0.99 (ROE 3%).

??? failure "AMKR (AMKR) — 🔴🔴 Strong Sell, score -2.30"
    Avoid: not owned. No reliable analyst target: α set to 0. Downtrend -46% vs 200-day avg; 12-1 mom +25%; RSI 34. Quality z -1.00 (ROE 9%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MRVL | Marvell Technology | 601 | 123.14 USD | $74,010 | 9.8% | Strong Buy |
| 005930.KS | Samsung Electronics | 458 | 182,600 KRW | $62,142 | 8.2% | Hold |
| AMAT | Applied Materials | 146 | 303.83 USD | $44,358 | 5.9% | Strong Buy |
| TSM | TSMC | 127 | 321.19 USD | $40,791 | 5.4% | Hold |
| MU | Micron Technology | 64 | 596.09 USD | $38,150 | 5.0% | Strong Buy |
| 000660.KS | SK hynix | 41 | 1,101,000 KRW | $33,542 | 4.4% | Strong Buy |
| INTC | Intel | 595 | 52.70 USD | $31,357 | 4.1% | Strong Buy |
| ASX | ASE Technology | 1,010 | 26.54 USD | $26,805 | 3.5% | Buy |
| TER | Teradyne | 123 | 204.82 USD | $25,193 | 3.3% | Buy |
| LRCX | Lam Research | 136 | 183.04 USD | $24,893 | 3.3% | Buy |
| KLAC | KLA Corp | 150 | 126.94 USD | $19,041 | 2.5% | Buy |
| IFX.DE | Infineon Technologies | 369 | 45.56 EUR | $18,444 | 2.4% | Buy |
| 6857.T | Advantest | 100 | 24,255 JPY | $15,305 | 2.0% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-11-20 20:22 UTC | ADD | INTC | 365 | 52.70 | $19,236 |
| 2026-11-20 20:22 UTC | ADD | MRVL | 353 | 123.14 | $43,470 |
| 2026-11-20 20:22 UTC | ADD | ASX | 205 | 26.54 | $5,441 |
| 2026-11-20 20:22 UTC | ADD | TER | 88 | 204.82 | $18,024 |
| 2026-11-20 20:22 UTC | ADD | LRCX | 78 | 183.03 | $14,277 |
| 2026-11-20 20:22 UTC | ADD | AMAT | 62 | 303.82 | $18,837 |
| 2026-11-20 20:22 UTC | TRIM | MU | -52 | 596.09 | $30,997 |
| 2026-11-20 20:22 UTC | TRIM | KLAC | -118 | 126.94 | $14,979 |
| 2026-11-20 20:22 UTC | SELL (exit) | NVDA | -268 | 128.30 | $34,384 |
| 2026-11-20 11:54 UTC | ADD | IFX.DE | 144 | 46.65 | $7,364 |
| 2026-11-17 03:55 UTC | TRIM | 000660.KS | -47 | 1,144,000.00 | $40,195 |
| 2026-11-16 20:30 UTC | ADD | ASX | 231 | 32.86 | $7,591 |
| 2026-11-16 20:30 UTC | ADD | INTC | 78 | 55.61 | $4,338 |
| 2026-11-16 20:30 UTC | TRIM | NVDA | -69 | 155.52 | $10,731 |
| 2026-11-13 16:26 UTC | ADD | NVDA | 79 | 159.94 | $12,635 |
| 2026-11-13 16:26 UTC | ADD | AMAT | 23 | 357.03 | $8,212 |
| 2026-11-13 16:26 UTC | TRIM | ASX | -290 | 34.86 | $10,109 |
| 2026-11-13 00:26 UTC | TRIM | 005930.KS | -104 | 214,000.00 | $16,663 |
| 2026-11-12 18:57 UTC | ADD | NVDA | 79 | 164.84 | $13,022 |
| 2026-11-12 18:57 UTC | ADD | AMAT | 20 | 386.98 | $7,740 |
| 2026-11-11 15:13 UTC | TRIM | AMAT | -32 | 387.02 | $12,385 |
| 2026-11-11 15:13 UTC | TRIM | MRVL | -76 | 165.15 | $12,551 |
| 2026-11-11 15:13 UTC | TRIM | INTC | -83 | 61.66 | $5,118 |
| 2026-11-11 06:23 UTC | ADD | 000660.KS | 38 | 1,277,000.00 | $36,371 |
| 2026-11-10 17:51 UTC | ADD | ASX | 552 | 34.76 | $19,188 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 66.7%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
