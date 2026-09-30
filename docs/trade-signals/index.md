---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-09-30 13:45 UTC (Wed Sep 30, 09:45 AM ET) · refreshes hourly · weekly model inputs as of 2026-09-25
**Markets:** NYSE/Nasdaq 🟢 open (Wed 09:45) · Tokyo 🔴 closed (Wed 22:45) · Korea 🔴 closed (Wed 22:45) · Hong Kong 🔴 closed (Wed 21:45) · Xetra 🟢 open (Wed 15:45) · Euronext Amsterdam 🟢 open (Wed 15:45)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$1,011,977** | $109,199 (11%) | $902,777 (89%) | +1.20% | +0.81% | 🟢 Risk-on (+26.2%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $1,011,977), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **Infineon**<br><small>IFX.DE</small> | 347 | 59.55 EUR | $23,474 | Executed (paper) | analyst α +0.31 · trend -0.09 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.11 | **SK hynix**<br><small>000660.KS</small> | 1,787,000 KRW | +78% | +11.8% | +405% | +27% | 52 | +0.63 | 9.7% → 10.0% | – | analyst α +0.66 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.22 | **Samsung**<br><small>005930.KS</small> | 270,000 KRW | +77% | +12.5% | +245% | +20% | 53 | -0.25 | 9.6% → 10.0% | – | analyst α +0.85 · momentum +0.35 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.07 | **MU**<br><small>Micron Technology</small> | 1,072.03 USD | +41% | +2.7% | +486% | +59% | 60 | +0.06 | 9.7% → 10.0% | – | momentum +0.53 · trend +0.25 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.67 | **Advantest**<br><small>6857.T</small> | 34,090 JPY | +25% | -1.2% | +149% | +25% | 55 | +0.33 | 8.6% → 9.1% | – | quality +0.16 · momentum +0.12 · ⚠️ rich valuation |
| 🟢 Buy | +0.54 | **NVDA**<br><small>NVIDIA</small> | 230.55 USD | +42% | +2.9% | +22% | +15% | 60 | +0.48 | 10.2% → 10.0% | – | analyst α +0.27 · quality +0.21 |
| 🟢 Buy | +0.40 | **Infineon**<br><small>IFX.DE</small> | 59.55 EUR | +46% | +3.9% | +67% | +8% | 55 | -0.04 | 8.1% → 8.1% | TRIM 347 | analyst α +0.31 · trend -0.09 |
| 🟢 Buy | +0.31 | **AVGO**<br><small>Broadcom</small> | 355.88 USD | +49% | +5.6% | +14% | -3% | 47 | +0.27 | 6.0% → 6.6% | – | analyst α +0.41 · momentum -0.26 |
| 🟢 Buy | +0.30 | **TSM**<br><small>TSMC</small> | 456.49 USD | +21% | -1.4% | +53% | +19% | 65 | +0.58 | 8.4% → 7.4% | – | quality +0.28 · analyst α -0.08 |
| 🟢 Buy | +0.28 | **AMAT**<br><small>Applied Materials</small> | 515.00 USD | +24% | -0.9% | +125% | +21% | 64 | +0.03 | 4.6% → 4.9% | – | momentum +0.07 · trend +0.07 |
| 🟢 Buy | +0.27 | **Tokyo Electron**<br><small>8035.T</small> | 11,860 JPY | – | +0.0% | +153% | +24% | 67 | -0.28 | 5.2% → 4.8% | – | quality -0.18 · momentum +0.14 · ⚠️ rich valuation |
| ⚪ Hold | +0.20 | **Disco**<br><small>6146.T</small> | 57,610 JPY | +43% | +4.0% | +47% | -11% | 55 | +0.07 | 0.0% → 0.0% | – | analyst α +0.36 · trend -0.25 |
| ⚪ Hold | +0.12 | **ASX**<br><small>ASE Technology</small> | 44.66 USD | +14% | -1.7% | +235% | +48% | 63 | -0.68 | 0.0% → 0.0% | – | momentum +0.30 · quality -0.28 · ⚠️ rich valuation |
| ⚪ Hold | +0.05 | **ASML**<br><small>ASML Holding</small> | 1,828.83 USD | +16% | -3.1% | +77% | +19% | 62 | +0.42 | 0.0% → 0.0% | – | analyst α -0.23 · quality +0.18 |
| ⚪ Hold | -0.01 | **KLAC**<br><small>KLA Corp</small> | 197.39 USD | +18% | -2.2% | +66% | +12% | 62 | +0.51 | 9.1% → 9.1% | – | quality +0.24 · analyst α -0.15 |
| ⚪ Hold | -0.14 | **AMD**<br><small>Advanced Micro Devices</small> | 606.80 USD | +2% | -7.4% | +192% | +64% | 65 | -0.15 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.32 |
| ⚪ Hold | -0.19 | **GFS**<br><small>GlobalFoundries</small> | 48.26 USD | +57% | +7.2% | +21% | -11% | 53 | -0.21 | 0.0% → 0.0% | – | analyst α +0.48 · momentum -0.23 |
| ⚪ Hold | -0.24 | **MRVL**<br><small>Marvell Technology</small> | 259.88 USD | +11% | -4.8% | +157% | +58% | 60 | -0.12 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.21 · ⚠️ rich valuation |
| 🔴 Sell | -0.31 | **LRCX**<br><small>Lam Research</small> | 327.26 USD | +14% | -3.7% | +131% | +20% | 61 | +0.03 | 0.0% → 0.0% | – | analyst α -0.27 · momentum +0.10 |
| 🔴 Sell | -0.46 | **TXN**<br><small>Texas Instruments</small> | 282.98 USD | +15% | -2.6% | +46% | +15% | 64 | +0.24 | 0.0% → 0.0% | – | analyst α -0.19 · momentum -0.10 |
| 🔴 Sell | -0.47 | **ASMI**<br><small>ASM.AS</small> | 891.60 EUR | +26% | -0.8% | +44% | +13% | 61 | -0.10 | 0.0% → 0.0% | – | momentum -0.14 · quality -0.06 |
| 🔴 Sell | -0.54 | **Shin-Etsu**<br><small>4063.T</small> | 5,944 JPY | +31% | +1.3% | +38% | -4% | 52 | -0.19 | 0.0% → 0.0% | – | momentum -0.17 · analyst α +0.15 |
| 🔴 Sell | -0.58 | **TER**<br><small>Teradyne</small> | 401.15 USD | +11% | -4.4% | +161% | +21% | 59 | -0.31 | 0.0% → 0.0% | – | analyst α -0.36 · momentum +0.23 |
| 🔴 Sell | -0.67 | **CDNS**<br><small>Cadence Design Systems</small> | 328.03 USD | +24% | -0.7% | -3% | +1% | 62 | +0.31 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.13 |
| 🔴 Sell | -0.74 | **AMKR**<br><small>Amkor Technology</small> | 54.16 USD | +41% | +2.8% | +67% | -5% | 56 | -1.00 | 0.0% → 0.0% | – | quality -0.43 · analyst α +0.23 |
| 🔴🔴 Strong Sell | -0.86 | **QCOM**<br><small>Qualcomm</small> | 187.39 USD | +4% | -5.8% | +5% | +12% | 54 | +0.70 | 0.0% → 0.0% | – | analyst α -0.48 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.90 | **SMIC**<br><small>0981.HK</small> | 60.65 HKD | +56% | +7.9% | -1% | -13% | 37 | -0.98 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.35 |
| 🔴🔴 Strong Sell | -0.95 | **ENTG**<br><small>Entegris</small> | 155.29 USD | +12% | -3.9% | +45% | +18% | 62 | -0.02 | 0.0% → 0.0% | – | analyst α -0.31 · momentum -0.12 |
| 🔴🔴 Strong Sell | -1.06 | **SNPS**<br><small>Synopsys</small> | 420.33 USD | +32% | +1.2% | -9% | -5% | 57 | +0.14 | 0.0% → 0.0% | – | momentum -0.53 · trend -0.18 |
| 🔴🔴 Strong Sell | -1.07 | **INTC**<br><small>Intel</small> | 118.92 USD | -2% | -8.2% | +160% | +48% | 61 | -0.62 | 0.0% → 0.0% | – | analyst α -0.66 · quality -0.24 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.35 | **ARM**<br><small>Arm Holdings</small> | 292.01 USD | -1% | -9.4% | +73% | +36% | 54 | +0.04 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.14 · ⚠️ rich valuation, high σ(e) |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.11"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,184,026 KRW vs 1,787,000 KRW (+78%, 37 analysts); de-biased α +11.8% vs CAPM hurdle 14.4%. Uptrend +27% vs 200-day avg; 12-1 mom +405%; RSI 52. Quality z +0.63 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.22"
    Within rebalance band of target 10.0%: no trade. Analyst target 478,628 KRW vs 270,000 KRW (+77%, 36 analysts); de-biased α +12.5% vs CAPM hurdle 11.4%. Uptrend +20% vs 200-day avg; 12-1 mom +245%; RSI 53. Quality z -0.25 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 4.0 (ch.17-18).

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.07"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,515.54 USD vs 1,072.03 USD (+41%, 46 analysts); de-biased α +2.7% vs CAPM hurdle 14.1%. Uptrend +59% vs 200-day avg; 12-1 mom +486%; RSI 60. Quality z +0.06 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 6.8 (ch.17-18).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.67"
    Within rebalance band of target 9.1%: no trade. Analyst target 42,567 JPY vs 34,090 JPY (+25%, 21 analysts); de-biased α -1.2% vs CAPM hurdle 13.3%. Uptrend +25% vs 200-day avg; 12-1 mom +149%; RSI 55. Quality z +0.33 (ROE 58%). ⚠️ price implies 76% stage-1 growth (reverse DCF).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.54"
    Within rebalance band of target 10.0%: no trade. Analyst target 327.70 USD vs 230.55 USD (+42%, 59 analysts); de-biased α +2.9% vs CAPM hurdle 14.0%. Uptrend +15% vs 200-day avg; 12-1 mom +22%; RSI 60. Quality z +0.48 (ROE 101%).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.40"
    **TRIM 347 sh** → target 8.1% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 86.74 EUR vs 59.55 EUR (+46%, 23 analysts); de-biased α +3.9% vs CAPM hurdle 14.1%. Uptrend +8% vs 200-day avg; 12-1 mom +67%; RSI 55. Quality z -0.04 (ROE 6%).

??? success "AVGO (AVGO) — 🟢 Buy, score +0.31"
    Within rebalance band of target 6.6%: no trade. Analyst target 531.85 USD vs 355.88 USD (+49%, 47 analysts); de-biased α +5.6% vs CAPM hurdle 11.2%. Downtrend -3% vs 200-day avg; 12-1 mom +14%; RSI 47. Quality z +0.27 (ROE 31%).

??? success "TSM (TSM) — 🟢 Buy, score +0.30"
    Within rebalance band of target 7.4%: no trade. Analyst target 552.26 USD vs 456.49 USD (+21%, 20 analysts); de-biased α -1.4% vs CAPM hurdle 10.9%. Uptrend +19% vs 200-day avg; 12-1 mom +53%; RSI 65. Quality z +0.58 (ROE 35%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.28"
    Within rebalance band of target 4.9%: no trade. Analyst target 640.89 USD vs 515.00 USD (+24%, 35 analysts); de-biased α -0.9% vs CAPM hurdle 11.7%. Uptrend +21% vs 200-day avg; 12-1 mom +125%; RSI 64. Quality z +0.03 (ROE 36%).

??? success "Tokyo Electron (8035.T) — 🟢 Buy, score +0.27"
    Within rebalance band of target 4.8%: no trade. No reliable analyst target: α set to 0. Uptrend +24% vs 200-day avg; 12-1 mom +153%; RSI 67. Quality z -0.28 (ROE 29%). ⚠️ price implies 72% stage-1 growth (reverse DCF).

??? note "Disco (6146.T) — ⚪ Hold, score +0.20"
    Hold zone: not owned, no entry. Analyst target 82,580 JPY vs 57,610 JPY (+43%, 20 analysts); de-biased α +4.0% vs CAPM hurdle 11.6%. Downtrend -11% vs 200-day avg; 12-1 mom +47%; RSI 55. Quality z +0.07 (ROE 25%).

??? note "ASX (ASX) — ⚪ Hold, score +0.12"
    Hold zone: not owned, no entry. Analyst target 51.00 USD vs 44.66 USD (+14%, 1 analysts); de-biased α -1.7% vs CAPM hurdle 12.1%. Uptrend +48% vs 200-day avg; 12-1 mom +235%; RSI 63. Quality z -0.68 (ROE 12%). ⚠️ price implies 67% stage-1 growth (reverse DCF).

??? note "ASML (ASML) — ⚪ Hold, score +0.05"
    Hold zone: not owned, no entry. Analyst target 2,123.54 USD vs 1,828.83 USD (+16%, 16 analysts); de-biased α -3.1% vs CAPM hurdle 12.4%. Uptrend +19% vs 200-day avg; 12-1 mom +77%; RSI 62. Quality z +0.42 (ROE 50%).

??? note "KLAC (KLAC) — ⚪ Hold, score -0.01"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 197.39 USD (+18%, 26 analysts); de-biased α -2.2% vs CAPM hurdle 11.2%. Uptrend +12% vs 200-day avg; 12-1 mom +66%; RSI 62. Quality z +0.51 (ROE 87%).

??? note "AMD (AMD) — ⚪ Hold, score -0.14"
    Hold zone: not owned, no entry. Analyst target 618.51 USD vs 606.80 USD (+2%, 50 analysts); de-biased α -7.4% vs CAPM hurdle 15.0%. Uptrend +64% vs 200-day avg; 12-1 mom +192%; RSI 65. Quality z -0.15 (ROE 7%).

??? note "GFS (GFS) — ⚪ Hold, score -0.19"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 48.26 USD (+57%, 22 analysts); de-biased α +7.2% vs CAPM hurdle 12.5%. Downtrend -11% vs 200-day avg; 12-1 mom +21%; RSI 53. Quality z -0.21 (ROE 8%).

??? note "MRVL (MRVL) — ⚪ Hold, score -0.24"
    Hold zone: not owned, no entry. Analyst target 289.11 USD vs 259.88 USD (+11%, 43 analysts); de-biased α -4.8% vs CAPM hurdle 14.2%. Uptrend +58% vs 200-day avg; 12-1 mom +157%; RSI 60. Quality z -0.12 (ROE 19%). ⚠️ price implies 76% stage-1 growth (reverse DCF).

??? failure "LRCX (LRCX) — 🔴 Sell, score -0.31"
    Avoid: not owned. Analyst target 373.77 USD vs 327.26 USD (+14%, 31 analysts); de-biased α -3.7% vs CAPM hurdle 12.7%. Uptrend +20% vs 200-day avg; 12-1 mom +131%; RSI 61. Quality z +0.03 (ROE 65%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.46"
    Avoid: not owned. Analyst target 324.71 USD vs 282.98 USD (+15%, 31 analysts); de-biased α -2.6% vs CAPM hurdle 10.8%. Uptrend +15% vs 200-day avg; 12-1 mom +46%; RSI 64. Quality z +0.24 (ROE 30%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.47"
    Avoid: not owned. Analyst target 1,125.89 EUR vs 891.60 EUR (+26%, 19 analysts); de-biased α -0.8% vs CAPM hurdle 13.2%. Uptrend +13% vs 200-day avg; 12-1 mom +44%; RSI 61. Quality z -0.10 (ROE 19%).

??? failure "Shin-Etsu (4063.T) — 🔴 Sell, score -0.54"
    Avoid: not owned. Analyst target 7,775 JPY vs 5,944 JPY (+31%, 17 analysts); de-biased α +1.3% vs CAPM hurdle 10.8%. Downtrend -4% vs 200-day avg; 12-1 mom +38%; RSI 52. Quality z -0.19 (ROE 10%).

??? failure "TER (TER) — 🔴 Sell, score -0.58"
    Avoid: not owned. Analyst target 446.47 USD vs 401.15 USD (+11%, 15 analysts); de-biased α -4.4% vs CAPM hurdle 12.5%. Uptrend +21% vs 200-day avg; 12-1 mom +161%; RSI 59. Quality z -0.31 (ROE 20%).

??? failure "CDNS (CDNS) — 🔴 Sell, score -0.67"
    Avoid: not owned. Analyst target 405.47 USD vs 328.03 USD (+24%, 26 analysts); de-biased α -0.7% vs CAPM hurdle 10.1%. Uptrend +1% vs 200-day avg; 12-1 mom -3%; RSI 62. Quality z +0.31 (ROE 22%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.74"
    Avoid: not owned. Analyst target 76.40 USD vs 54.16 USD (+41%, 10 analysts); de-biased α +2.8% vs CAPM hurdle 14.1%. Downtrend -5% vs 200-day avg; 12-1 mom +67%; RSI 56. Quality z -1.00 (ROE 9%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.86"
    Avoid: not owned. Analyst target 194.13 USD vs 187.39 USD (+4%, 30 analysts); de-biased α -5.8% vs CAPM hurdle 12.1%. Uptrend +12% vs 200-day avg; 12-1 mom +5%; RSI 54. Quality z +0.70 (ROE 23%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -0.90"
    Avoid: not owned. Analyst target 94.39 HKD vs 60.65 HKD (+56%, 22 analysts); de-biased α +7.9% vs CAPM hurdle 7.4%. Downtrend -13% vs 200-day avg; 12-1 mom -1%; RSI 37. Quality z -0.98 (ROE 3%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.95"
    Avoid: not owned. Analyst target 173.36 USD vs 155.29 USD (+12%, 11 analysts); de-biased α -3.9% vs CAPM hurdle 10.9%. Uptrend +18% vs 200-day avg; 12-1 mom +45%; RSI 62. Quality z -0.02 (ROE 6%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.06"
    Avoid: not owned. Analyst target 553.77 USD vs 420.33 USD (+32%, 25 analysts); de-biased α +1.2% vs CAPM hurdle 10.4%. Downtrend -5% vs 200-day avg; 12-1 mom -9%; RSI 57. Quality z +0.14 (ROE 7%).

??? failure "INTC (INTC) — 🔴🔴 Strong Sell, score -1.07"
    Avoid: not owned. Analyst target 116.37 USD vs 118.92 USD (-2%, 43 analysts); de-biased α -8.2% vs CAPM hurdle 14.1%. Uptrend +48% vs 200-day avg; 12-1 mom +160%; RSI 61. Quality z -0.62 (ROE -0%). ⚠️ price implies 87% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 61% → smaller size.

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.35"
    Avoid: not owned. Analyst target 288.70 USD vs 292.01 USD (-1%, 40 analysts); de-biased α -9.4% vs CAPM hurdle 20.0%. Uptrend +36% vs 200-day avg; 12-1 mom +73%; RSI 54. Quality z +0.04 (ROE 12%). ⚠️ price implies 115% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| NVDA | NVIDIA | 447 | 230.55 USD | $103,056 | 10.2% | Buy |
| MU | Micron Technology | 92 | 1,072.03 USD | $98,626 | 9.7% | Strong Buy |
| 000660.KS | SK hynix | 74 | 1,787,000 KRW | $97,695 | 9.7% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 270,000 KRW | $96,743 | 9.6% | Strong Buy |
| KLAC | KLA Corp | 469 | 197.39 USD | $92,576 | 9.1% | Hold |
| 6857.T | Advantest | 400 | 34,090 JPY | $86,919 | 8.6% | Buy |
| TSM | TSMC | 187 | 456.49 USD | $85,364 | 8.4% | Buy |
| IFX.DE | Infineon Technologies | 1,205 | 59.55 EUR | $81,515 | 8.1% | Buy |
| AVGO | Broadcom | 170 | 355.88 USD | $60,500 | 6.0% | Buy |
| 8035.T | Tokyo Electron | 700 | 11,860 JPY | $52,919 | 5.2% | Buy |
| AMAT | Applied Materials | 91 | 515.00 USD | $46,865 | 4.6% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-09-30 13:45 UTC | TRIM | IFX.DE | -347 | 59.55 | $23,474 |
| 2026-09-30 00:28 UTC | BUY (new) | 8035.T | 700 | 11,900.00 | $52,952 |
| 2026-09-29 15:53 UTC | BUY (new) | TSM | 187 | 457.37 | $85,528 |
| 2026-09-29 15:53 UTC | TRIM | AMAT | -87 | 501.81 | $43,657 |
| 2026-09-29 15:53 UTC | TRIM | AVGO | -112 | 357.74 | $40,067 |
| 2026-09-28 15:29 UTC | BUY (new) | AVGO | 282 | 349.88 | $98,666 |
| 2026-09-28 00:48 UTC | BUY (new) | 005930.KS | 485 | 280,750.00 | $100,255 |
| 2026-09-28 00:48 UTC | BUY (new) | 6857.T | 400 | 34,870.00 | $88,422 |
| 2026-09-28 00:48 UTC | BUY (new) | 000660.KS | 74 | 1,818,500.00 | $99,080 |
| 2026-09-25 14:37 UTC | BUY (new) | KLAC | 469 | 186.53 | $87,480 |
| 2026-09-25 14:37 UTC | BUY (new) | NVDA | 447 | 223.82 | $100,048 |
| 2026-09-25 14:37 UTC | BUY (new) | AMAT | 178 | 479.88 | $85,419 |
| 2026-09-25 14:37 UTC | BUY (new) | MU | 92 | 1,083.05 | $99,641 |
| 2026-09-24 08:59 UTC | BUY (new) | IFX.DE | 1,552 | 56.56 | $99,956 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 4.07%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 16.5%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
