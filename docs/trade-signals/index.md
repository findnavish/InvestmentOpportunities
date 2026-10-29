---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-29 20:19 UTC (Thu Oct 29, 04:19 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Thu 16:19) · Tokyo 🔴 closed (Fri 05:19) · Korea 🔴 closed (Fri 05:19) · Hong Kong 🔴 closed (Fri 04:19) · Xetra 🔴 closed (Thu 21:19) · Euronext Amsterdam 🔴 closed (Thu 21:19)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$947,513** | $105,638 (11%) | $841,874 (89%) | -5.25% | -9.14% | 🟢 Risk-on (+8.1%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $947,513), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **TSM**<br><small>TSMC</small> | 26 | 431.62 USD | $11,222 | Queued · NYSE/Nasdaq closed | quality +0.28 · momentum -0.12 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.04 | **SK hynix**<br><small>000660.KS</small> | 1,537,000 KRW | +104% | +14.6% | +265% | +3% | 53 | +0.62 | 11.9% → 10.0% | – | analyst α +0.55 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.64 | **MU**<br><small>Micron Technology</small> | 934.26 USD | +63% | +4.3% | +380% | +26% | 47 | +0.12 | 9.1% → 10.0% | – | momentum +0.53 · analyst α +0.36 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.55 | **Samsung**<br><small>005930.KS</small> | 232,000 KRW | +106% | +15.9% | +178% | -2% | 47 | -0.26 | 8.9% → 10.0% | – | analyst α +0.66 · momentum +0.20 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.64 | **MRVL**<br><small>Marvell Technology</small> | 218.20 USD | +35% | -2.7% | +199% | +20% | 40 | -0.12 | 5.0% → 6.0% | – | momentum +0.30 · trend +0.14 · ⚠️ rich valuation |
| 🟢 Buy | +0.62 | **Infineon**<br><small>IFX.DE</small> | 54.29 EUR | +60% | +3.7% | +74% | -5% | 48 | -0.04 | 8.3% → 9.1% | – | analyst α +0.31 · trend -0.06 |
| 🟢 Buy | +0.55 | **AMAT**<br><small>Applied Materials</small> | 421.70 USD | +52% | +2.2% | +126% | -5% | 44 | +0.03 | 6.5% → 6.9% | – | analyst α +0.15 · momentum +0.14 |
| 🟢 Buy | +0.38 | **ASX**<br><small>ASE Technology</small> | 44.58 USD | +14% | -3.5% | +236% | +35% | 56 | -0.68 | 6.2% → 5.2% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.38 | **NVDA**<br><small>NVIDIA</small> | 213.72 USD | +53% | +2.0% | +14% | +5% | 42 | +0.47 | 4.5% → 5.6% | – | quality +0.21 · momentum -0.20 |
| 🟢 Buy | +0.26 | **TSM**<br><small>TSMC</small> | 431.62 USD | +28% | -3.4% | +53% | +8% | 48 | +0.58 | 5.8% → 4.6% | TRIM 26 | quality +0.28 · momentum -0.12 |
| ⚪ Hold | +0.21 | **Tokyo Electron**<br><small>8035.T</small> | 9,990 JPY | +53% | +2.4% | +104% | -1% | 44 | -0.28 | 3.3% → 3.3% | – | analyst α +0.19 · quality -0.18 |
| ⚪ Hold | +0.15 | **ASML**<br><small>ASML Holding</small> | 1,675.70 USD | +25% | -4.6% | +73% | +5% | 49 | +0.42 | 5.3% → 5.3% | – | analyst α -0.19 · quality +0.18 |
| ⚪ Hold | +0.07 | **KLAC**<br><small>KLA Corp</small> | 167.92 USD | +39% | -0.8% | +63% | -8% | 46 | +0.51 | 4.7% → 4.7% | – | quality +0.24 · trend -0.12 |
| ⚪ Hold | +0.06 | **LRCX**<br><small>Lam Research</small> | 254.39 USD | +47% | +0.9% | +112% | -10% | 39 | +0.02 | 4.3% → 4.3% | – | trend -0.14 · momentum +0.12 |
| ⚪ Hold | +0.06 | **Advantest**<br><small>6857.T</small> | 37,070 JPY | +15% | -7.4% | +96% | +28% | 56 | +0.33 | 5.0% → 5.0% | – | analyst α -0.41 · trend +0.21 · ⚠️ rich valuation |
| ⚪ Hold | -0.10 | **GFS**<br><small>GlobalFoundries</small> | 45.85 USD | +66% | +5.5% | +39% | -17% | 46 | -0.21 | 0.0% → 0.0% | – | analyst α +0.41 · trend -0.18 |
| ⚪ Hold | -0.12 | **TER**<br><small>Teradyne</small> | 296.40 USD | +51% | +1.7% | +178% | -15% | 33 | -0.31 | 0.0% → 0.0% | – | momentum +0.23 · quality -0.21 |
| 🔴 Sell | -0.28 | **Disco**<br><small>6146.T</small> | 52,170 JPY | +57% | +3.6% | +8% | -20% | 44 | +0.06 | 0.0% → 0.0% | – | analyst α +0.27 · momentum -0.23 |
| 🔴 Sell | -0.35 | **INTC**<br><small>Intel</small> | 92.08 USD | +26% | -4.8% | +190% | +6% | 41 | -0.62 | 0.0% → 0.0% | – | momentum +0.26 · quality -0.24 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.39 | **AVGO**<br><small>Broadcom</small> | 345.05 USD | +54% | +3.0% | -5% | -6% | 49 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · analyst α +0.23 |
| 🔴 Sell | -0.43 | **ASMI**<br><small>ASM.AS</small> | 796.20 EUR | +42% | -0.7% | +58% | -2% | 50 | -0.10 | 0.0% → 0.0% | – | momentum -0.10 · quality -0.06 |
| 🔴 Sell | -0.58 | **AMKR**<br><small>Amkor Technology</small> | 41.19 USD | +85% | +10.1% | +64% | -28% | 41 | -1.00 | 0.0% → 0.0% | – | analyst α +0.48 · quality -0.43 |
| 🔴 Sell | -0.68 | **TXN**<br><small>Texas Instruments</small> | 312.92 USD | +4% | -9.2% | +72% | +21% | 72 | +0.24 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.16 |
| 🔴🔴 Strong Sell | -0.76 | **ARM**<br><small>Arm Holdings</small> | 228.79 USD | +26% | -6.2% | +67% | +0% | 42 | +0.04 | 0.0% → 0.0% | – | analyst α -0.31 · momentum -0.03 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -0.77 | **SMIC**<br><small>0981.HK</small> | 44.96 HKD | +114% | +18.7% | -15% | -34% | 24 | -0.99 | 0.0% → 0.0% | – | analyst α +0.85 · momentum -0.53 · ⚠️ oversold |
| 🔴🔴 Strong Sell | -0.92 | **ENTG**<br><small>Entegris</small> | 159.87 USD | +8% | -8.5% | +69% | +16% | 57 | -0.02 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.12 |
| 🔴🔴 Strong Sell | -0.95 | **QCOM**<br><small>Qualcomm</small> | 185.34 USD | +5% | -9.2% | +4% | +10% | 57 | +0.70 | 0.0% → 0.0% | – | analyst α -0.66 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.97 | **CDNS**<br><small>Cadence Design Systems</small> | 342.76 USD | +18% | -5.8% | -3% | +5% | 58 | +0.31 | 0.0% → 0.0% | – | momentum -0.30 · analyst α -0.27 |
| 🔴🔴 Strong Sell | -0.98 | **Shin-Etsu**<br><small>4063.T</small> | 5,982 JPY | +30% | -2.7% | +21% | -5% | 51 | -0.20 | 0.0% → 0.0% | – | momentum -0.17 · quality -0.11 |
| 🔴🔴 Strong Sell | -1.07 | **AMD**<br><small>Advanced Micro Devices</small> | 566.46 USD | +9% | -9.3% | +137% | +38% | 51 | -0.15 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -1.23 | **SNPS**<br><small>Synopsys</small> | 490.28 USD | +16% | -6.4% | -5% | +11% | 61 | +0.14 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.35 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.04"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,537,000 KRW (+104%, 38 analysts); de-biased α +14.6% vs CAPM hurdle 14.3%. Uptrend +3% vs 200-day avg; 12-1 mom +265%; RSI 53. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.64"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 934.26 USD (+63%, 46 analysts); de-biased α +4.3% vs CAPM hurdle 14.0%. Uptrend +26% vs 200-day avg; 12-1 mom +380%; RSI 47. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.55"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 232,000 KRW (+106%, 36 analysts); de-biased α +15.9% vs CAPM hurdle 11.3%. Downtrend -2% vs 200-day avg; 12-1 mom +178%; RSI 47. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "MRVL (MRVL) — 🟢 Buy, score +0.64"
    Within rebalance band of target 6.0%: no trade. Analyst target 293.88 USD vs 218.20 USD (+35%, 43 analysts); de-biased α -2.7% vs CAPM hurdle 14.1%. Uptrend +20% vs 200-day avg; 12-1 mom +199%; RSI 40. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.62"
    Within rebalance band of target 9.1%: no trade. Analyst target 86.74 EUR vs 54.29 EUR (+60%, 23 analysts); de-biased α +3.7% vs CAPM hurdle 14.1%. Downtrend -5% vs 200-day avg; 12-1 mom +74%; RSI 48. Quality z -0.04 (ROE 6%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.55"
    Within rebalance band of target 6.9%: no trade. Analyst target 638.94 USD vs 421.70 USD (+52%, 36 analysts); de-biased α +2.2% vs CAPM hurdle 11.6%. Downtrend -5% vs 200-day avg; 12-1 mom +126%; RSI 44. Quality z +0.03 (ROE 36%).

??? success "ASX (ASX) — 🟢 Buy, score +0.38"
    Within rebalance band of target 5.2%: no trade. Analyst target 51.00 USD vs 44.58 USD (+14%, 1 analysts); de-biased α -3.5% vs CAPM hurdle 11.9%. Uptrend +35% vs 200-day avg; 12-1 mom +236%; RSI 56. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.38"
    Within rebalance band of target 5.6%: no trade. Analyst target 327.70 USD vs 213.72 USD (+53%, 59 analysts); de-biased α +2.0% vs CAPM hurdle 13.9%. Uptrend +5% vs 200-day avg; 12-1 mom +14%; RSI 42. Quality z +0.47 (ROE 101%).

??? success "TSM (TSM) — 🟢 Buy, score +0.26"
    **TRIM 26 sh** → target 4.6% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 552.26 USD vs 431.62 USD (+28%, 20 analysts); de-biased α -3.4% vs CAPM hurdle 10.8%. Uptrend +8% vs 200-day avg; 12-1 mom +53%; RSI 48. Quality z +0.58 (ROE 35%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.21"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 9,990 JPY (+53%, 23 analysts); de-biased α +2.4% vs CAPM hurdle 12.8%. Downtrend -1% vs 200-day avg; 12-1 mom +104%; RSI 44. Quality z -0.28 (ROE 29%).

??? note "ASML (ASML) — ⚪ Hold, score +0.15"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,675.70 USD (+25%, 16 analysts); de-biased α -4.6% vs CAPM hurdle 12.3%. Uptrend +5% vs 200-day avg; 12-1 mom +73%; RSI 49. Quality z +0.42 (ROE 50%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.07"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 167.92 USD (+39%, 26 analysts); de-biased α -0.8% vs CAPM hurdle 11.1%. Downtrend -8% vs 200-day avg; 12-1 mom +63%; RSI 46. Quality z +0.51 (ROE 87%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.06"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 254.39 USD (+47%, 31 analysts); de-biased α +0.9% vs CAPM hurdle 12.6%. Downtrend -10% vs 200-day avg; 12-1 mom +112%; RSI 39. Quality z +0.02 (ROE 65%).

??? note "Advantest (6857.T) — ⚪ Hold, score +0.06"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 37,070 JPY (+15%, 21 analysts); de-biased α -7.4% vs CAPM hurdle 13.4%. Uptrend +28% vs 200-day avg; 12-1 mom +96%; RSI 56. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "GFS (GFS) — ⚪ Hold, score -0.10"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 45.85 USD (+66%, 22 analysts); de-biased α +5.5% vs CAPM hurdle 12.4%. Downtrend -17% vs 200-day avg; 12-1 mom +39%; RSI 46. Quality z -0.21 (ROE 8%).

??? note "TER (TER) — ⚪ Hold, score -0.12"
    Hold zone: not owned, no entry. Analyst target 446.47 USD vs 296.40 USD (+51%, 15 analysts); de-biased α +1.7% vs CAPM hurdle 12.3%. Downtrend -15% vs 200-day avg; 12-1 mom +178%; RSI 33. Quality z -0.31 (ROE 20%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.28"
    Avoid: not owned. Analyst target 81,730 JPY vs 52,170 JPY (+57%, 20 analysts); de-biased α +3.6% vs CAPM hurdle 11.5%. Downtrend -20% vs 200-day avg; 12-1 mom +8%; RSI 44. Quality z +0.06 (ROE 25%).

??? failure "INTC (INTC) — 🔴 Sell, score -0.35"
    Avoid: not owned. Analyst target 116.37 USD vs 92.08 USD (+26%, 43 analysts); de-biased α -4.8% vs CAPM hurdle 14.0%. Uptrend +6% vs 200-day avg; 12-1 mom +190%; RSI 41. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "AVGO (AVGO) — 🔴 Sell, score -0.39"
    Avoid: not owned. Analyst target 531.31 USD vs 345.05 USD (+54%, 47 analysts); de-biased α +3.0% vs CAPM hurdle 11.2%. Downtrend -6% vs 200-day avg; 12-1 mom -5%; RSI 49. Quality z +0.26 (ROE 31%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.43"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 796.20 EUR (+42%, 19 analysts); de-biased α -0.7% vs CAPM hurdle 13.2%. Downtrend -2% vs 200-day avg; 12-1 mom +58%; RSI 50. Quality z -0.10 (ROE 19%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.58"
    Avoid: not owned. Analyst target 76.40 USD vs 41.19 USD (+85%, 10 analysts); de-biased α +10.1% vs CAPM hurdle 14.0%. Downtrend -28% vs 200-day avg; 12-1 mom +64%; RSI 41. Quality z -1.00 (ROE 9%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.68"
    Avoid: not owned. Analyst target 324.71 USD vs 312.92 USD (+4%, 31 analysts); de-biased α -9.2% vs CAPM hurdle 10.8%. Uptrend +21% vs 200-day avg; 12-1 mom +72%; RSI 72. Quality z +0.24 (ROE 30%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -0.76"
    Avoid: not owned. Analyst target 288.70 USD vs 228.79 USD (+26%, 40 analysts); de-biased α -6.2% vs CAPM hurdle 19.6%. Uptrend +0% vs 200-day avg; 12-1 mom +67%; RSI 42. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -0.77"
    Avoid: not owned. Analyst target 95.99 HKD vs 44.96 HKD (+114%, 21 analysts); de-biased α +18.7% vs CAPM hurdle 7.3%. Downtrend -34% vs 200-day avg; 12-1 mom -15%; RSI 24. Quality z -0.99 (ROE 3%). ⚠️ oversold.

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.92"
    Avoid: not owned. Analyst target 173.36 USD vs 159.87 USD (+8%, 11 analysts); de-biased α -8.5% vs CAPM hurdle 11.0%. Uptrend +16% vs 200-day avg; 12-1 mom +69%; RSI 57. Quality z -0.02 (ROE 6%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.95"
    Avoid: not owned. Analyst target 194.13 USD vs 185.34 USD (+5%, 30 analysts); de-biased α -9.2% vs CAPM hurdle 11.9%. Uptrend +10% vs 200-day avg; 12-1 mom +4%; RSI 57. Quality z +0.70 (ROE 23%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -0.97"
    Avoid: not owned. Analyst target 405.47 USD vs 342.76 USD (+18%, 26 analysts); de-biased α -5.8% vs CAPM hurdle 10.0%. Uptrend +5% vs 200-day avg; 12-1 mom -3%; RSI 58. Quality z +0.31 (ROE 22%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -0.98"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,982 JPY (+30%, 17 analysts); de-biased α -2.7% vs CAPM hurdle 10.8%. Downtrend -5% vs 200-day avg; 12-1 mom +21%; RSI 51. Quality z -0.20 (ROE 10%).

??? failure "AMD (AMD) — 🔴🔴 Strong Sell, score -1.07"
    Avoid: not owned. Analyst target 619.51 USD vs 566.46 USD (+9%, 50 analysts); de-biased α -9.3% vs CAPM hurdle 14.9%. Uptrend +38% vs 200-day avg; 12-1 mom +137%; RSI 51. Quality z -0.15 (ROE 7%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.23"
    Avoid: not owned. Analyst target 569.78 USD vs 490.28 USD (+16%, 26 analysts); de-biased α -6.4% vs CAPM hurdle 10.3%. Uptrend +11% vs 200-day avg; 12-1 mom -5%; RSI 61. Quality z +0.14 (ROE 7%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 98 | 1,537,000 KRW | $112,457 | 11.9% | Strong Buy |
| MU | Micron Technology | 92 | 934.26 USD | $85,952 | 9.1% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 232,000 KRW | $84,007 | 8.9% | Strong Buy |
| IFX.DE | Infineon Technologies | 1,301 | 54.29 EUR | $78,944 | 8.3% | Buy |
| AMAT | Applied Materials | 145 | 421.70 USD | $61,147 | 6.5% | Buy |
| ASX | ASE Technology | 1,320 | 44.58 USD | $58,846 | 6.2% | Buy |
| TSM | TSMC | 127 | 431.62 USD | $54,816 | 5.8% | Buy |
| ASML | ASML Holding | 30 | 1,675.70 USD | $50,271 | 5.3% | Hold |
| MRVL | Marvell Technology | 218 | 218.20 USD | $47,568 | 5.0% | Buy |
| 6857.T | Advantest | 200 | 37,070 JPY | $47,019 | 5.0% | Hold |
| KLAC | KLA Corp | 268 | 167.92 USD | $45,003 | 4.7% | Hold |
| NVDA | NVIDIA | 201 | 213.72 USD | $42,958 | 4.5% | Buy |
| LRCX | Lam Research | 162 | 254.39 USD | $41,211 | 4.3% | Hold |
| 8035.T | Tokyo Electron | 500 | 9,990 JPY | $31,678 | 3.3% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-10-29 14:21 UTC | BUY (new) | MRVL | 218 | 219.82 | $47,921 |
| 2026-10-29 14:21 UTC | TRIM | NVDA | -84 | 213.56 | $17,939 |
| 2026-10-29 14:21 UTC | SELL (exit) | AVGO | -100 | 342.58 | $34,258 |
| 2026-10-28 16:04 UTC | ADD | NVDA | 117 | 217.19 | $25,411 |
| 2026-10-26 19:22 UTC | TRIM | AMAT | -57 | 391.16 | $22,296 |
| 2026-10-26 19:22 UTC | TRIM | NVDA | -58 | 216.65 | $12,566 |
| 2026-10-26 19:22 UTC | TRIM | ASX | -395 | 40.15 | $15,859 |
| 2026-10-26 06:15 UTC | ADD | 6857.T | 100 | 31,220.00 | $19,871 |
| 2026-10-23 19:14 UTC | ADD | KLAC | 57 | 145.31 | $8,282 |
| 2026-10-23 15:05 UTC | ADD | ASX | 383 | 38.70 | $14,822 |
| 2026-10-23 15:05 UTC | TRIM | NVDA | -68 | 212.70 | $14,464 |
| 2026-10-22 15:18 UTC | ADD | LRCX | 57 | 234.49 | $13,366 |
| 2026-10-22 15:18 UTC | ADD | AMAT | 46 | 380.67 | $17,511 |
| 2026-10-22 15:18 UTC | TRIM | TSM | -27 | 414.23 | $11,184 |
| 2026-10-21 19:21 UTC | ADD | TSM | 37 | 430.88 | $15,943 |
| 2026-10-21 15:16 UTC | TRIM | KLAC | -68 | 164.22 | $11,167 |
| 2026-10-20 17:08 UTC | BUY (new) | LRCX | 105 | 263.68 | $27,686 |
| 2026-10-20 17:08 UTC | TRIM | AVGO | -34 | 334.29 | $11,366 |
| 2026-10-20 17:08 UTC | TRIM | NVDA | -77 | 216.83 | $16,696 |
| 2026-10-19 15:37 UTC | TRIM | TSM | -25 | 426.75 | $10,669 |
| 2026-10-19 15:37 UTC | TRIM | ASX | -465 | 41.40 | $19,251 |
| 2026-10-19 01:19 UTC | TRIM | 8035.T | -100 | 10,325.00 | $6,537 |
| 2026-10-16 17:25 UTC | ADD | ASX | 558 | 39.86 | $22,242 |
| 2026-10-16 17:25 UTC | TRIM | TSM | -45 | 412.93 | $18,582 |
| 2026-10-16 12:26 UTC | TRIM | IFX.DE | -293 | 52.84 | $17,423 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 31.5%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
