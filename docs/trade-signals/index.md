---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-09-30 23:51 UTC (Wed Sep 30, 07:51 PM ET) · refreshes hourly · weekly model inputs as of 2026-09-25
**Markets:** NYSE/Nasdaq 🔴 closed (Wed 19:51) · Tokyo 🔴 closed (Thu 08:51) · Korea 🔴 closed (Thu 08:51) · Hong Kong 🔴 closed (Thu 07:51) · Xetra 🔴 closed (Thu 01:51) · Euronext Amsterdam 🔴 closed (Thu 01:51)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$1,006,969** | $126,732 (13%) | $880,238 (87%) | +0.70% | +0.46% | 🟢 Risk-on (+25.7%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $1,006,969), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| ADD | **AMAT**<br><small>Applied Materials</small> | 39 | 511.67 USD | $19,955 | Queued · NYSE/Nasdaq closed | momentum +0.07 · trend +0.07 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.14 | **SK hynix**<br><small>000660.KS</small> | 1,787,000 KRW | +78% | +11.8% | +407% | +27% | 52 | +0.63 | 9.7% → 10.0% | – | analyst α +0.66 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.22 | **Samsung**<br><small>005930.KS</small> | 270,000 KRW | +77% | +12.4% | +244% | +20% | 53 | -0.25 | 9.6% → 10.0% | – | analyst α +0.85 · momentum +0.35 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.01 | **MU**<br><small>Micron Technology</small> | 1,067.49 USD | +42% | +2.8% | +486% | +59% | 60 | +0.06 | 9.8% → 10.0% | – | momentum +0.53 · trend +0.21 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.73 | **Advantest**<br><small>6857.T</small> | 34,090 JPY | +25% | -1.3% | +150% | +25% | 55 | +0.33 | 8.6% → 8.9% | – | quality +0.16 · momentum +0.14 · ⚠️ rich valuation |
| 🟢 Buy | +0.50 | **Infineon**<br><small>IFX.DE</small> | 59.28 EUR | +46% | +4.0% | +67% | +7% | 54 | -0.04 | 8.0% → 9.1% | – | analyst α +0.36 · trend -0.09 |
| 🟢 Buy | +0.46 | **NVDA**<br><small>NVIDIA</small> | 228.29 USD | +44% | +3.2% | +22% | +14% | 58 | +0.48 | 8.4% → 8.4% | – | analyst α +0.23 · quality +0.21 |
| 🟢 Buy | +0.42 | **AMAT**<br><small>Applied Materials</small> | 511.67 USD | +25% | -0.7% | +125% | +21% | 63 | +0.03 | 4.6% → 6.6% | ADD 39 | momentum +0.07 · trend +0.07 |
| 🟢 Buy | +0.33 | **TSM**<br><small>TSMC</small> | 456.28 USD | +21% | -1.5% | +53% | +19% | 65 | +0.58 | 8.5% → 7.3% | – | quality +0.28 · analyst α -0.08 |
| 🟢 Buy | +0.30 | **Tokyo Electron**<br><small>8035.T</small> | 11,860 JPY | – | +0.0% | +149% | +23% | 67 | -0.28 | 5.2% → 4.7% | – | quality -0.18 · momentum +0.12 · ⚠️ rich valuation |
| ⚪ Hold | +0.24 | **AVGO**<br><small>Broadcom</small> | 351.29 USD | +51% | +6.0% | +14% | -4% | 44 | +0.27 | 5.9% → 5.9% | – | analyst α +0.41 · momentum -0.26 |
| ⚪ Hold | +0.12 | **ASX**<br><small>ASE Technology</small> | 44.49 USD | +15% | -1.7% | +235% | +47% | 62 | -0.68 | 0.0% → 0.0% | – | momentum +0.30 · quality -0.28 · ⚠️ rich valuation |
| ⚪ Hold | +0.02 | **ASML**<br><small>ASML Holding</small> | 1,811.25 USD | +17% | -2.9% | +77% | +18% | 60 | +0.42 | 0.0% → 0.0% | – | analyst α -0.23 · quality +0.18 |
| ⚪ Hold | -0.01 | **Disco**<br><small>6146.T</small> | 57,610 JPY | +43% | +4.0% | +35% | -11% | 55 | +0.07 | 0.0% → 0.0% | – | analyst α +0.31 · trend -0.21 |
| ⚪ Hold | -0.01 | **KLAC**<br><small>KLA Corp</small> | 195.03 USD | +20% | -1.9% | +66% | +10% | 59 | +0.51 | 9.1% → 9.1% | – | quality +0.24 · analyst α -0.15 |
| ⚪ Hold | -0.15 | **AMD**<br><small>Advanced Micro Devices</small> | 611.74 USD | +1% | -7.7% | +192% | +65% | 66 | -0.15 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.32 |
| ⚪ Hold | -0.16 | **MRVL**<br><small>Marvell Technology</small> | 264.21 USD | +9% | -5.4% | +157% | +60% | 62 | -0.12 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.25 · ⚠️ rich valuation |
| 🔴 Sell | -0.27 | **GFS**<br><small>GlobalFoundries</small> | 47.91 USD | +59% | +7.4% | +21% | -11% | 51 | -0.21 | 0.0% → 0.0% | – | analyst α +0.48 · trend -0.25 |
| 🔴 Sell | -0.37 | **LRCX**<br><small>Lam Research</small> | 328.61 USD | +14% | -3.9% | +131% | +20% | 61 | +0.03 | 0.0% → 0.0% | – | analyst α -0.31 · momentum +0.10 |
| 🔴 Sell | -0.42 | **TXN**<br><small>Texas Instruments</small> | 280.03 USD | +16% | -2.4% | +46% | +14% | 61 | +0.24 | 0.0% → 0.0% | – | analyst α -0.19 · quality +0.10 |
| 🔴 Sell | -0.43 | **ASMI**<br><small>ASM.AS</small> | 889.80 EUR | +27% | -0.8% | +44% | +13% | 61 | -0.10 | 0.0% → 0.0% | – | momentum -0.12 · quality -0.06 |
| 🔴 Sell | -0.50 | **Shin-Etsu**<br><small>4063.T</small> | 5,944 JPY | +31% | +1.2% | +35% | -4% | 52 | -0.19 | 0.0% → 0.0% | – | analyst α +0.15 · momentum -0.14 |
| 🔴 Sell | -0.59 | **TER**<br><small>Teradyne</small> | 400.91 USD | +11% | -4.5% | +161% | +21% | 58 | -0.31 | 0.0% → 0.0% | – | analyst α -0.36 · momentum +0.23 |
| 🔴 Sell | -0.71 | **AMKR**<br><small>Amkor Technology</small> | 52.37 USD | +46% | +3.9% | +67% | -8% | 51 | -1.00 | 0.0% → 0.0% | – | quality -0.43 · analyst α +0.27 |
| 🔴🔴 Strong Sell | -0.82 | **CDNS**<br><small>Cadence Design Systems</small> | 330.18 USD | +23% | -1.0% | -3% | +1% | 63 | +0.31 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.13 |
| 🔴🔴 Strong Sell | -0.82 | **ENTG**<br><small>Entegris</small> | 154.14 USD | +12% | -3.8% | +45% | +17% | 61 | -0.02 | 0.0% → 0.0% | – | analyst α -0.27 · momentum -0.10 |
| 🔴🔴 Strong Sell | -0.87 | **QCOM**<br><small>Qualcomm</small> | 184.06 USD | +5% | -5.4% | +5% | +10% | 52 | +0.70 | 0.0% → 0.0% | – | analyst α -0.48 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.91 | **SMIC**<br><small>0981.HK</small> | 60.65 HKD | +56% | +7.8% | -1% | -13% | 37 | -0.98 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.35 |
| 🔴🔴 Strong Sell | -1.01 | **SNPS**<br><small>Synopsys</small> | 435.07 USD | +27% | -0.0% | -9% | -2% | 62 | +0.14 | 0.0% → 0.0% | – | momentum -0.53 · trend -0.12 |
| 🔴🔴 Strong Sell | -1.08 | **INTC**<br><small>Intel</small> | 120.16 USD | -3% | -8.5% | +160% | +50% | 62 | -0.62 | 0.0% → 0.0% | – | analyst α -0.66 · quality -0.24 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.37 | **ARM**<br><small>Arm Holdings</small> | 289.76 USD | -0% | -9.3% | +73% | +35% | 53 | +0.04 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.14 · ⚠️ rich valuation, high σ(e) |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.14"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,184,026 KRW vs 1,787,000 KRW (+78%, 37 analysts); de-biased α +11.8% vs CAPM hurdle 14.4%. Uptrend +27% vs 200-day avg; 12-1 mom +407%; RSI 52. Quality z +0.63 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.22"
    Within rebalance band of target 10.0%: no trade. Analyst target 478,628 KRW vs 270,000 KRW (+77%, 36 analysts); de-biased α +12.4% vs CAPM hurdle 11.4%. Uptrend +20% vs 200-day avg; 12-1 mom +244%; RSI 53. Quality z -0.25 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 4.0 (ch.17-18).

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.01"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,515.54 USD vs 1,067.49 USD (+42%, 46 analysts); de-biased α +2.8% vs CAPM hurdle 14.1%. Uptrend +59% vs 200-day avg; 12-1 mom +486%; RSI 60. Quality z +0.06 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 6.8 (ch.17-18).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.73"
    Within rebalance band of target 8.9%: no trade. Analyst target 42,567 JPY vs 34,090 JPY (+25%, 21 analysts); de-biased α -1.3% vs CAPM hurdle 13.3%. Uptrend +25% vs 200-day avg; 12-1 mom +150%; RSI 55. Quality z +0.33 (ROE 58%). ⚠️ price implies 76% stage-1 growth (reverse DCF).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.50"
    Within rebalance band of target 9.1%: no trade. Analyst target 86.74 EUR vs 59.28 EUR (+46%, 23 analysts); de-biased α +4.0% vs CAPM hurdle 14.1%. Uptrend +7% vs 200-day avg; 12-1 mom +67%; RSI 54. Quality z -0.04 (ROE 6%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.46"
    Within rebalance band of target 8.4%: no trade. Analyst target 327.70 USD vs 228.29 USD (+44%, 59 analysts); de-biased α +3.2% vs CAPM hurdle 14.0%. Uptrend +14% vs 200-day avg; 12-1 mom +22%; RSI 58. Quality z +0.48 (ROE 101%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.42"
    **ADD 39 sh** → target 6.6% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 640.89 USD vs 511.67 USD (+25%, 35 analysts); de-biased α -0.7% vs CAPM hurdle 11.7%. Uptrend +21% vs 200-day avg; 12-1 mom +125%; RSI 63. Quality z +0.03 (ROE 36%).

??? success "TSM (TSM) — 🟢 Buy, score +0.33"
    Within rebalance band of target 7.3%: no trade. Analyst target 552.26 USD vs 456.28 USD (+21%, 20 analysts); de-biased α -1.5% vs CAPM hurdle 10.9%. Uptrend +19% vs 200-day avg; 12-1 mom +53%; RSI 65. Quality z +0.58 (ROE 35%).

??? success "Tokyo Electron (8035.T) — 🟢 Buy, score +0.30"
    Within rebalance band of target 4.7%: no trade. No reliable analyst target: α set to 0. Uptrend +23% vs 200-day avg; 12-1 mom +149%; RSI 67. Quality z -0.28 (ROE 29%). ⚠️ price implies 72% stage-1 growth (reverse DCF).

??? note "AVGO (AVGO) — ⚪ Hold, score +0.24"
    Hold zone: keep any existing position, no new money. Analyst target 531.85 USD vs 351.29 USD (+51%, 47 analysts); de-biased α +6.0% vs CAPM hurdle 11.2%. Downtrend -4% vs 200-day avg; 12-1 mom +14%; RSI 44. Quality z +0.27 (ROE 31%).

??? note "ASX (ASX) — ⚪ Hold, score +0.12"
    Hold zone: not owned, no entry. Analyst target 51.00 USD vs 44.49 USD (+15%, 1 analysts); de-biased α -1.7% vs CAPM hurdle 12.1%. Uptrend +47% vs 200-day avg; 12-1 mom +235%; RSI 62. Quality z -0.68 (ROE 12%). ⚠️ price implies 67% stage-1 growth (reverse DCF).

??? note "ASML (ASML) — ⚪ Hold, score +0.02"
    Hold zone: not owned, no entry. Analyst target 2,123.54 USD vs 1,811.25 USD (+17%, 16 analysts); de-biased α -2.9% vs CAPM hurdle 12.4%. Uptrend +18% vs 200-day avg; 12-1 mom +77%; RSI 60. Quality z +0.42 (ROE 50%).

??? note "Disco (6146.T) — ⚪ Hold, score -0.01"
    Hold zone: not owned, no entry. Analyst target 82,580 JPY vs 57,610 JPY (+43%, 20 analysts); de-biased α +4.0% vs CAPM hurdle 11.6%. Downtrend -11% vs 200-day avg; 12-1 mom +35%; RSI 55. Quality z +0.07 (ROE 25%).

??? note "KLAC (KLAC) — ⚪ Hold, score -0.01"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 195.03 USD (+20%, 26 analysts); de-biased α -1.9% vs CAPM hurdle 11.2%. Uptrend +10% vs 200-day avg; 12-1 mom +66%; RSI 59. Quality z +0.51 (ROE 87%).

??? note "AMD (AMD) — ⚪ Hold, score -0.15"
    Hold zone: not owned, no entry. Analyst target 618.51 USD vs 611.74 USD (+1%, 50 analysts); de-biased α -7.7% vs CAPM hurdle 15.0%. Uptrend +65% vs 200-day avg; 12-1 mom +192%; RSI 66. Quality z -0.15 (ROE 7%).

??? note "MRVL (MRVL) — ⚪ Hold, score -0.16"
    Hold zone: not owned, no entry. Analyst target 289.11 USD vs 264.21 USD (+9%, 43 analysts); de-biased α -5.4% vs CAPM hurdle 14.2%. Uptrend +60% vs 200-day avg; 12-1 mom +157%; RSI 62. Quality z -0.12 (ROE 19%). ⚠️ price implies 76% stage-1 growth (reverse DCF).

??? failure "GFS (GFS) — 🔴 Sell, score -0.27"
    Avoid: not owned. Analyst target 76.00 USD vs 47.91 USD (+59%, 22 analysts); de-biased α +7.4% vs CAPM hurdle 12.5%. Downtrend -11% vs 200-day avg; 12-1 mom +21%; RSI 51. Quality z -0.21 (ROE 8%).

??? failure "LRCX (LRCX) — 🔴 Sell, score -0.37"
    Avoid: not owned. Analyst target 373.77 USD vs 328.61 USD (+14%, 31 analysts); de-biased α -3.9% vs CAPM hurdle 12.7%. Uptrend +20% vs 200-day avg; 12-1 mom +131%; RSI 61. Quality z +0.03 (ROE 65%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.42"
    Avoid: not owned. Analyst target 324.71 USD vs 280.03 USD (+16%, 31 analysts); de-biased α -2.4% vs CAPM hurdle 10.8%. Uptrend +14% vs 200-day avg; 12-1 mom +46%; RSI 61. Quality z +0.24 (ROE 30%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.43"
    Avoid: not owned. Analyst target 1,125.89 EUR vs 889.80 EUR (+27%, 19 analysts); de-biased α -0.8% vs CAPM hurdle 13.2%. Uptrend +13% vs 200-day avg; 12-1 mom +44%; RSI 61. Quality z -0.10 (ROE 19%).

??? failure "Shin-Etsu (4063.T) — 🔴 Sell, score -0.50"
    Avoid: not owned. Analyst target 7,775 JPY vs 5,944 JPY (+31%, 17 analysts); de-biased α +1.2% vs CAPM hurdle 10.8%. Downtrend -4% vs 200-day avg; 12-1 mom +35%; RSI 52. Quality z -0.19 (ROE 10%).

??? failure "TER (TER) — 🔴 Sell, score -0.59"
    Avoid: not owned. Analyst target 446.47 USD vs 400.91 USD (+11%, 15 analysts); de-biased α -4.5% vs CAPM hurdle 12.5%. Uptrend +21% vs 200-day avg; 12-1 mom +161%; RSI 58. Quality z -0.31 (ROE 20%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.71"
    Avoid: not owned. Analyst target 76.40 USD vs 52.37 USD (+46%, 10 analysts); de-biased α +3.9% vs CAPM hurdle 14.1%. Downtrend -8% vs 200-day avg; 12-1 mom +67%; RSI 51. Quality z -1.00 (ROE 9%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -0.82"
    Avoid: not owned. Analyst target 405.47 USD vs 330.18 USD (+23%, 26 analysts); de-biased α -1.0% vs CAPM hurdle 10.1%. Uptrend +1% vs 200-day avg; 12-1 mom -3%; RSI 63. Quality z +0.31 (ROE 22%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.82"
    Avoid: not owned. Analyst target 173.36 USD vs 154.14 USD (+12%, 11 analysts); de-biased α -3.8% vs CAPM hurdle 10.9%. Uptrend +17% vs 200-day avg; 12-1 mom +45%; RSI 61. Quality z -0.02 (ROE 6%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.87"
    Avoid: not owned. Analyst target 194.13 USD vs 184.06 USD (+5%, 30 analysts); de-biased α -5.4% vs CAPM hurdle 12.1%. Uptrend +10% vs 200-day avg; 12-1 mom +5%; RSI 52. Quality z +0.70 (ROE 23%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -0.91"
    Avoid: not owned. Analyst target 94.39 HKD vs 60.65 HKD (+56%, 22 analysts); de-biased α +7.8% vs CAPM hurdle 7.4%. Downtrend -13% vs 200-day avg; 12-1 mom -1%; RSI 37. Quality z -0.98 (ROE 3%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.01"
    Avoid: not owned. Analyst target 553.77 USD vs 435.07 USD (+27%, 25 analysts); de-biased α -0.0% vs CAPM hurdle 10.4%. Downtrend -2% vs 200-day avg; 12-1 mom -9%; RSI 62. Quality z +0.14 (ROE 7%).

??? failure "INTC (INTC) — 🔴🔴 Strong Sell, score -1.08"
    Avoid: not owned. Analyst target 116.37 USD vs 120.16 USD (-3%, 43 analysts); de-biased α -8.5% vs CAPM hurdle 14.1%. Uptrend +50% vs 200-day avg; 12-1 mom +160%; RSI 62. Quality z -0.62 (ROE -0%). ⚠️ price implies 87% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 61% → smaller size.

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.37"
    Avoid: not owned. Analyst target 288.70 USD vs 289.76 USD (-0%, 40 analysts); de-biased α -9.3% vs CAPM hurdle 20.0%. Uptrend +35% vs 200-day avg; 12-1 mom +73%; RSI 53. Quality z +0.04 (ROE 12%). ⚠️ price implies 115% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 92 | 1,067.49 USD | $98,209 | 9.8% | Strong Buy |
| 000660.KS | SK hynix | 74 | 1,787,000 KRW | $97,465 | 9.7% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 270,000 KRW | $96,515 | 9.6% | Strong Buy |
| KLAC | KLA Corp | 469 | 195.03 USD | $91,469 | 9.1% | Hold |
| 6857.T | Advantest | 400 | 34,090 JPY | $86,601 | 8.6% | Buy |
| TSM | TSMC | 187 | 456.28 USD | $85,324 | 8.5% | Buy |
| NVDA | NVIDIA | 371 | 228.29 USD | $84,696 | 8.4% | Buy |
| IFX.DE | Infineon Technologies | 1,205 | 59.28 EUR | $80,952 | 8.0% | Buy |
| AVGO | Broadcom | 170 | 351.29 USD | $59,719 | 5.9% | Hold |
| 8035.T | Tokyo Electron | 700 | 11,860 JPY | $52,725 | 5.2% | Buy |
| AMAT | Applied Materials | 91 | 511.67 USD | $46,562 | 4.6% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-09-30 19:21 UTC | TRIM | NVDA | -76 | 230.81 | $17,541 |
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

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 4.07%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 16.9%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
