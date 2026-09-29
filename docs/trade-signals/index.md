---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-09-29 01:58 UTC (Mon Sep 28, 09:58 PM ET) · refreshes hourly · weekly model inputs as of 2026-09-25
**Markets:** NYSE/Nasdaq 🔴 closed (Mon 21:58) · Tokyo 🟢 open (Tue 10:58) · Korea 🟢 open (Tue 10:58) · Hong Kong 🟢 open (Tue 09:58) · Xetra 🔴 closed (Tue 03:58) · Euronext Amsterdam 🔴 closed (Tue 03:58)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$993,316** | $140,605 (14%) | $852,711 (86%) | -0.67% | -0.83% | 🟢 Risk-on (+24.8%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $993,316), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| – | No trades this hour | | | | | All positions are within their rebalance bands. |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.40 | **SK hynix**<br><small>000660.KS</small> | 1,775,000 KRW | +79% | +11.5% | +465% | +27% | 51 | +0.63 | 9.7% → 10.0% | – | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.09 | **MU**<br><small>Micron Technology</small> | 1,053.89 USD | +44% | +2.7% | +497% | +58% | 58 | +0.06 | 9.8% → 10.0% | – | momentum +0.53 · trend +0.25 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.85 | **Samsung**<br><small>005930.KS</small> | 274,500 KRW | +74% | +11.1% | +267% | +23% | 55 | -0.25 | 9.9% → 10.0% | – | analyst α +0.66 · momentum +0.35 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.72 | **Advantest**<br><small>6857.T</small> | 33,390 JPY | +27% | -1.2% | +161% | +23% | 52 | +0.33 | 8.5% → 10.0% | – | quality +0.16 · momentum +0.12 · ⚠️ rich valuation |
| 🟢 Buy | +0.40 | **Infineon**<br><small>IFX.DE</small> | 56.68 EUR | +53% | +5.1% | +74% | +3% | 48 | -0.04 | 10.1% → 10.0% | – | analyst α +0.36 · trend -0.09 |
| 🟢 Buy | +0.34 | **AMAT**<br><small>Applied Materials</small> | 486.71 USD | +32% | +0.3% | +143% | +15% | 56 | +0.03 | 8.7% → 10.0% | – | analyst α +0.08 · momentum +0.07 |
| 🟢 Buy | +0.31 | **NVDA**<br><small>NVIDIA</small> | 228.88 USD | +43% | +2.6% | +28% | +15% | 59 | +0.48 | 10.3% → 10.0% | – | momentum -0.23 · quality +0.21 |
| 🟢 Buy | +0.30 | **AVGO**<br><small>Broadcom</small> | 349.57 USD | +52% | +5.6% | +11% | -5% | 42 | +0.27 | 9.9% → 10.0% | – | analyst α +0.41 · momentum -0.26 |
| ⚪ Hold | +0.18 | **Tokyo Electron**<br><small>8035.T</small> | 11,455 JPY | – | +0.0% | +186% | +21% | 63 | -0.28 | 0.0% → 0.0% | – | momentum +0.20 · quality -0.18 · ⚠️ rich valuation |
| ⚪ Hold | +0.16 | **ASX**<br><small>ASE Technology</small> | 43.78 USD | +16% | -1.7% | +243% | +46% | 62 | -0.68 | 0.0% → 0.0% | – | momentum +0.30 · quality -0.28 · ⚠️ rich valuation |
| ⚪ Hold | +0.15 | **ASML**<br><small>ASML Holding</small> | 1,771.41 USD | +20% | -2.8% | +84% | +16% | 57 | +0.42 | 0.0% → 0.0% | – | analyst α -0.19 · quality +0.18 |
| ⚪ Hold | +0.14 | **KLAC**<br><small>KLA Corp</small> | 189.37 USD | +23% | -1.6% | +74% | +8% | 55 | +0.51 | 8.9% → 8.9% | – | quality +0.24 · analyst α -0.08 |
| ⚪ Hold | +0.14 | **TSM**<br><small>TSMC</small> | 452.88 USD | +22% | -1.8% | +56% | +19% | 63 | +0.58 | 0.0% → 0.0% | – | quality +0.28 · analyst α -0.15 |
| ⚪ Hold | -0.01 | **MRVL**<br><small>Marvell Technology</small> | 251.89 USD | +15% | -4.6% | +189% | +54% | 57 | -0.12 | 0.0% → 0.0% | – | analyst α -0.36 · momentum +0.23 · ⚠️ rich valuation |
| ⚪ Hold | -0.07 | **GFS**<br><small>GlobalFoundries</small> | 47.78 USD | +59% | +6.9% | +41% | -11% | 51 | -0.21 | 0.0% → 0.0% | – | analyst α +0.48 · trend -0.21 |
| ⚪ Hold | -0.14 | **AMD**<br><small>Advanced Micro Devices</small> | 607.86 USD | +2% | -8.1% | +196% | +66% | 66 | -0.15 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.32 |
| ⚪ Hold | -0.18 | **Disco**<br><small>6146.T</small> | 55,460 JPY | +49% | +4.8% | +47% | -14% | 49 | +0.07 | 0.0% → 0.0% | – | trend -0.32 · analyst α +0.31 |
| ⚪ Hold | -0.24 | **ASMI**<br><small>ASM.AS</small> | 847.80 EUR | +33% | +0.2% | +60% | +8% | 54 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · trend -0.06 |
| 🔴 Sell | -0.32 | **LRCX**<br><small>Lam Research</small> | 314.51 USD | +19% | -3.1% | +150% | +16% | 56 | +0.03 | 0.0% → 0.0% | – | analyst α -0.27 · momentum +0.10 |
| 🔴 Sell | -0.57 | **TXN**<br><small>Texas Instruments</small> | 278.51 USD | +17% | -2.8% | +50% | +14% | 60 | +0.24 | 0.0% → 0.0% | – | analyst α -0.23 · momentum -0.12 |
| 🔴 Sell | -0.60 | **AMKR**<br><small>Amkor Technology</small> | 53.18 USD | +44% | +2.8% | +78% | -7% | 54 | -1.00 | 0.0% → 0.0% | – | quality -0.43 · analyst α +0.27 |
| 🔴 Sell | -0.64 | **SMIC**<br><small>0981.HK</small> | 61.05 HKD | +55% | +7.0% | +2% | -12% | 38 | -0.98 | 0.0% → 0.0% | – | analyst α +0.55 · quality -0.33 |
| 🔴 Sell | -0.67 | **Shin-Etsu**<br><small>4063.T</small> | 5,730 JPY | +36% | +1.9% | +38% | -7% | 40 | -0.19 | 0.0% → 0.0% | – | momentum -0.20 · trend -0.18 |
| 🔴 Sell | -0.72 | **CDNS**<br><small>Cadence Design Systems</small> | 326.70 USD | +24% | -1.3% | -1% | +0% | 62 | +0.31 | 0.0% → 0.0% | – | momentum -0.35 · quality +0.13 |
| 🔴🔴 Strong Sell | -0.76 | **TER**<br><small>Teradyne</small> | 401.25 USD | +11% | -5.0% | +180% | +21% | 59 | -0.31 | 0.0% → 0.0% | – | analyst α -0.41 · quality -0.21 |
| 🔴🔴 Strong Sell | -0.83 | **ENTG**<br><small>Entegris</small> | 150.69 USD | +15% | -3.7% | +59% | +15% | 58 | -0.02 | 0.0% → 0.0% | – | analyst α -0.31 · momentum -0.07 |
| 🔴🔴 Strong Sell | -0.94 | **SNPS**<br><small>Synopsys</small> | 417.59 USD | +33% | +0.8% | -5% | -6% | 56 | +0.14 | 0.0% → 0.0% | – | momentum -0.53 · trend -0.14 |
| 🔴🔴 Strong Sell | -1.01 | **QCOM**<br><small>Qualcomm</small> | 187.41 USD | +4% | -6.4% | -1% | +12% | 54 | +0.70 | 0.0% → 0.0% | – | analyst α -0.48 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.19 | **INTC**<br><small>Intel</small> | 116.13 USD | +0% | -8.2% | +171% | +46% | 59 | -0.62 | 0.0% → 0.0% | – | analyst α -0.66 · quality -0.24 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.31 | **ARM**<br><small>Arm Holdings</small> | 283.26 USD | +2% | -9.3% | +81% | +33% | 52 | +0.04 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.14 · ⚠️ rich valuation, high σ(e) |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.40"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,184,026 KRW vs 1,775,000 KRW (+79%, 37 analysts); de-biased α +11.5% vs CAPM hurdle 14.4%. Uptrend +27% vs 200-day avg; 12-1 mom +465%; RSI 51. Quality z +0.63 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.09"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,515.54 USD vs 1,053.89 USD (+44%, 46 analysts); de-biased α +2.7% vs CAPM hurdle 14.1%. Uptrend +58% vs 200-day avg; 12-1 mom +497%; RSI 58. Quality z +0.06 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 6.8 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.85"
    Within rebalance band of target 10.0%: no trade. Analyst target 478,628 KRW vs 274,500 KRW (+74%, 36 analysts); de-biased α +11.1% vs CAPM hurdle 11.4%. Uptrend +23% vs 200-day avg; 12-1 mom +267%; RSI 55. Quality z -0.25 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 4.0 (ch.17-18).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.72"
    Within rebalance band of target 10.0%: no trade. Analyst target 42,567 JPY vs 33,390 JPY (+27%, 21 analysts); de-biased α -1.2% vs CAPM hurdle 13.3%. Uptrend +23% vs 200-day avg; 12-1 mom +161%; RSI 52. Quality z +0.33 (ROE 58%). ⚠️ price implies 76% stage-1 growth (reverse DCF).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.40"
    Within rebalance band of target 10.0%: no trade. Analyst target 86.74 EUR vs 56.68 EUR (+53%, 23 analysts); de-biased α +5.1% vs CAPM hurdle 14.1%. Uptrend +3% vs 200-day avg; 12-1 mom +74%; RSI 48. Quality z -0.04 (ROE 6%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.34"
    Within rebalance band of target 10.0%: no trade. Analyst target 640.89 USD vs 486.71 USD (+32%, 35 analysts); de-biased α +0.3% vs CAPM hurdle 11.7%. Uptrend +15% vs 200-day avg; 12-1 mom +143%; RSI 56. Quality z +0.03 (ROE 36%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.31"
    Within rebalance band of target 10.0%: no trade. Analyst target 327.70 USD vs 228.88 USD (+43%, 59 analysts); de-biased α +2.6% vs CAPM hurdle 14.0%. Uptrend +15% vs 200-day avg; 12-1 mom +28%; RSI 59. Quality z +0.48 (ROE 101%).

??? success "AVGO (AVGO) — 🟢 Buy, score +0.30"
    Within rebalance band of target 10.0%: no trade. Analyst target 531.85 USD vs 349.57 USD (+52%, 47 analysts); de-biased α +5.6% vs CAPM hurdle 11.2%. Downtrend -5% vs 200-day avg; 12-1 mom +11%; RSI 42. Quality z +0.27 (ROE 31%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.18"
    Hold zone: not owned, no entry. No reliable analyst target: α set to 0. Uptrend +21% vs 200-day avg; 12-1 mom +186%; RSI 63. Quality z -0.28 (ROE 29%). ⚠️ price implies 72% stage-1 growth (reverse DCF).

??? note "ASX (ASX) — ⚪ Hold, score +0.16"
    Hold zone: not owned, no entry. Analyst target 51.00 USD vs 43.78 USD (+16%, 1 analysts); de-biased α -1.7% vs CAPM hurdle 12.1%. Uptrend +46% vs 200-day avg; 12-1 mom +243%; RSI 62. Quality z -0.68 (ROE 12%). ⚠️ price implies 67% stage-1 growth (reverse DCF).

??? note "ASML (ASML) — ⚪ Hold, score +0.15"
    Hold zone: not owned, no entry. Analyst target 2,123.54 USD vs 1,771.41 USD (+20%, 16 analysts); de-biased α -2.8% vs CAPM hurdle 12.4%. Uptrend +16% vs 200-day avg; 12-1 mom +84%; RSI 57. Quality z +0.42 (ROE 50%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.14"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 189.37 USD (+23%, 26 analysts); de-biased α -1.6% vs CAPM hurdle 11.2%. Uptrend +8% vs 200-day avg; 12-1 mom +74%; RSI 55. Quality z +0.51 (ROE 87%).

??? note "TSM (TSM) — ⚪ Hold, score +0.14"
    Hold zone: not owned, no entry. Analyst target 552.26 USD vs 452.88 USD (+22%, 20 analysts); de-biased α -1.8% vs CAPM hurdle 10.9%. Uptrend +19% vs 200-day avg; 12-1 mom +56%; RSI 63. Quality z +0.58 (ROE 35%).

??? note "MRVL (MRVL) — ⚪ Hold, score -0.01"
    Hold zone: not owned, no entry. Analyst target 289.11 USD vs 251.89 USD (+15%, 43 analysts); de-biased α -4.6% vs CAPM hurdle 14.2%. Uptrend +54% vs 200-day avg; 12-1 mom +189%; RSI 57. Quality z -0.12 (ROE 19%). ⚠️ price implies 76% stage-1 growth (reverse DCF).

??? note "GFS (GFS) — ⚪ Hold, score -0.07"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 47.78 USD (+59%, 22 analysts); de-biased α +6.9% vs CAPM hurdle 12.5%. Downtrend -11% vs 200-day avg; 12-1 mom +41%; RSI 51. Quality z -0.21 (ROE 8%).

??? note "AMD (AMD) — ⚪ Hold, score -0.14"
    Hold zone: not owned, no entry. Analyst target 618.51 USD vs 607.86 USD (+2%, 50 analysts); de-biased α -8.1% vs CAPM hurdle 15.0%. Uptrend +66% vs 200-day avg; 12-1 mom +196%; RSI 66. Quality z -0.15 (ROE 7%).

??? note "Disco (6146.T) — ⚪ Hold, score -0.18"
    Hold zone: not owned, no entry. Analyst target 82,580 JPY vs 55,460 JPY (+49%, 20 analysts); de-biased α +4.8% vs CAPM hurdle 11.6%. Downtrend -14% vs 200-day avg; 12-1 mom +47%; RSI 49. Quality z +0.07 (ROE 25%).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.24"
    Hold zone: not owned, no entry. Analyst target 1,125.89 EUR vs 847.80 EUR (+33%, 19 analysts); de-biased α +0.2% vs CAPM hurdle 13.2%. Uptrend +8% vs 200-day avg; 12-1 mom +60%; RSI 54. Quality z -0.10 (ROE 19%).

??? failure "LRCX (LRCX) — 🔴 Sell, score -0.32"
    Avoid: not owned. Analyst target 373.77 USD vs 314.51 USD (+19%, 31 analysts); de-biased α -3.1% vs CAPM hurdle 12.7%. Uptrend +16% vs 200-day avg; 12-1 mom +150%; RSI 56. Quality z +0.03 (ROE 65%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.57"
    Avoid: not owned. Analyst target 324.71 USD vs 278.51 USD (+17%, 31 analysts); de-biased α -2.8% vs CAPM hurdle 10.8%. Uptrend +14% vs 200-day avg; 12-1 mom +50%; RSI 60. Quality z +0.24 (ROE 30%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.60"
    Avoid: not owned. Analyst target 76.40 USD vs 53.18 USD (+44%, 10 analysts); de-biased α +2.8% vs CAPM hurdle 14.1%. Downtrend -7% vs 200-day avg; 12-1 mom +78%; RSI 54. Quality z -1.00 (ROE 9%).

??? failure "SMIC (0981.HK) — 🔴 Sell, score -0.64"
    Avoid: not owned. Analyst target 94.39 HKD vs 61.05 HKD (+55%, 22 analysts); de-biased α +7.0% vs CAPM hurdle 7.4%. Downtrend -12% vs 200-day avg; 12-1 mom +2%; RSI 38. Quality z -0.98 (ROE 3%).

??? failure "Shin-Etsu (4063.T) — 🔴 Sell, score -0.67"
    Avoid: not owned. Analyst target 7,775 JPY vs 5,730 JPY (+36%, 17 analysts); de-biased α +1.9% vs CAPM hurdle 10.8%. Downtrend -7% vs 200-day avg; 12-1 mom +38%; RSI 40. Quality z -0.19 (ROE 10%).

??? failure "CDNS (CDNS) — 🔴 Sell, score -0.72"
    Avoid: not owned. Analyst target 405.47 USD vs 326.70 USD (+24%, 26 analysts); de-biased α -1.3% vs CAPM hurdle 10.1%. Uptrend +0% vs 200-day avg; 12-1 mom -1%; RSI 62. Quality z +0.31 (ROE 22%).

??? failure "TER (TER) — 🔴🔴 Strong Sell, score -0.76"
    Avoid: not owned. Analyst target 446.47 USD vs 401.25 USD (+11%, 15 analysts); de-biased α -5.0% vs CAPM hurdle 12.5%. Uptrend +21% vs 200-day avg; 12-1 mom +180%; RSI 59. Quality z -0.31 (ROE 20%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.83"
    Avoid: not owned. Analyst target 173.36 USD vs 150.69 USD (+15%, 11 analysts); de-biased α -3.7% vs CAPM hurdle 10.9%. Uptrend +15% vs 200-day avg; 12-1 mom +59%; RSI 58. Quality z -0.02 (ROE 6%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.94"
    Avoid: not owned. Analyst target 553.77 USD vs 417.59 USD (+33%, 25 analysts); de-biased α +0.8% vs CAPM hurdle 10.4%. Downtrend -6% vs 200-day avg; 12-1 mom -5%; RSI 56. Quality z +0.14 (ROE 7%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.01"
    Avoid: not owned. Analyst target 194.13 USD vs 187.41 USD (+4%, 30 analysts); de-biased α -6.4% vs CAPM hurdle 12.1%. Uptrend +12% vs 200-day avg; 12-1 mom -1%; RSI 54. Quality z +0.70 (ROE 23%).

??? failure "INTC (INTC) — 🔴🔴 Strong Sell, score -1.19"
    Avoid: not owned. Analyst target 116.37 USD vs 116.13 USD (+0%, 43 analysts); de-biased α -8.2% vs CAPM hurdle 14.1%. Uptrend +46% vs 200-day avg; 12-1 mom +171%; RSI 59. Quality z -0.62 (ROE -0%). ⚠️ price implies 87% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 61% → smaller size.

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.31"
    Avoid: not owned. Analyst target 288.70 USD vs 283.26 USD (+2%, 40 analysts); de-biased α -9.3% vs CAPM hurdle 20.0%. Uptrend +33% vs 200-day avg; 12-1 mom +81%; RSI 52. Quality z +0.04 (ROE 12%). ⚠️ price implies 115% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| NVDA | NVIDIA | 447 | 228.88 USD | $102,309 | 10.3% | Buy |
| IFX.DE | Infineon Technologies | 1,552 | 56.68 EUR | $100,008 | 10.1% | Buy |
| AVGO | Broadcom | 282 | 349.57 USD | $98,579 | 9.9% | Buy |
| 005930.KS | Samsung Electronics | 485 | 274,500 KRW | $97,965 | 9.9% | Strong Buy |
| MU | Micron Technology | 92 | 1,053.89 USD | $96,958 | 9.8% | Strong Buy |
| 000660.KS | SK hynix | 74 | 1,775,000 KRW | $96,653 | 9.7% | Strong Buy |
| KLAC | KLA Corp | 469 | 189.37 USD | $88,815 | 8.9% | Hold |
| AMAT | Applied Materials | 178 | 486.71 USD | $86,634 | 8.7% | Buy |
| 6857.T | Advantest | 400 | 33,390 JPY | $84,789 | 8.5% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 4.07%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 19.1%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
