---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-10 17:51 UTC (Tue Nov 10, 12:51 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🟢 open (Tue 12:51) · Tokyo 🔴 closed (Wed 02:51) · Korea 🔴 closed (Wed 02:51) · Hong Kong 🔴 closed (Wed 01:51) · Xetra 🔴 closed (Tue 18:51) · Euronext Amsterdam 🔴 closed (Tue 18:51)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$834,319** | $332,664 (40%) | $501,654 (60%) | -16.57% | -74.55% | 🔴 Risk-off (-9.9%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $834,319), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| ADD | **ASX**<br><small>ASE Technology</small> | 552 | 34.76 USD | $19,188 | Executed (paper) | momentum +0.41 · quality -0.28 · ⚠️ rich valuation |
| TRIM | **INTC**<br><small>Intel</small> | 140 | 57.20 USD | $8,008 | Executed (paper) | analyst α +0.41 · momentum +0.26 · ⚠️ oversold, rich valuation, high σ(e) |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +2.90 | **MU**<br><small>Micron Technology</small> | 703.85 USD | +116% | +12.1% | +316% | -7% | 34 | +0.12 | 9.8% → 10.0% | – | analyst α +0.55 · momentum +0.53 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.20 | **Samsung**<br><small>005930.KS</small> | 199,600 KRW | +139% | +18.7% | +156% | -15% | 38 | -0.26 | 10.0% → 10.0% | – | analyst α +0.85 · momentum +0.23 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.34 | **SK hynix**<br><small>000660.KS</small> | 1,220,000 KRW | – | +0.0% | +188% | -19% | 39 | +0.62 | 5.4% → 5.0% | – | quality +0.33 · momentum +0.30 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +1.23 | **MRVL**<br><small>Marvell Technology</small> | 150.68 USD | +95% | +6.8% | +193% | -19% | 31 | -0.12 | 5.9% → 4.9% | – | momentum +0.35 · analyst α +0.31 · ⚠️ rich valuation |
| 🟢 Buy | +0.69 | **NVDA**<br><small>NVIDIA</small> | 167.02 USD | +96% | +7.2% | +21% | -18% | 23 | +0.47 | 3.6% → 4.2% | – | analyst α +0.36 · momentum -0.23 · ⚠️ oversold |
| 🟢 Buy | +0.63 | **AMAT**<br><small>Applied Materials</small> | 367.61 USD | +74% | +2.2% | +117% | -17% | 41 | +0.03 | 3.2% → 3.3% | – | analyst α +0.15 · momentum +0.14 |
| 🟢 Buy | +0.62 | **ASX**<br><small>ASE Technology</small> | 34.76 USD | +47% | -2.2% | +215% | +3% | 41 | -0.68 | 3.6% → 3.6% | ADD 552 | momentum +0.41 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.61 | **Advantest**<br><small>6857.T</small> | 29,505 JPY | +45% | -5.5% | +140% | +1% | 39 | +0.33 | 2.2% → 2.5% | – | analyst α -0.23 · momentum +0.17 · ⚠️ rich valuation |
| 🟢 Buy | +0.45 | **INTC**<br><small>Intel</small> | 57.20 USD | +103% | +9.0% | +166% | -34% | 28 | -0.62 | 1.6% → 1.6% | TRIM 140 | analyst α +0.41 · momentum +0.26 · ⚠️ oversold, rich valuation, high σ(e) |
| ⚪ Hold | +0.18 | **TSM**<br><small>TSMC</small> | 388.80 USD | +42% | -5.4% | +57% | -3% | 41 | +0.58 | 5.9% → 5.9% | – | quality +0.28 · analyst α -0.19 |
| ⚪ Hold | +0.12 | **Infineon**<br><small>IFX.DE</small> | 49.30 EUR | +76% | +2.2% | +70% | -14% | 43 | -0.04 | 1.5% → 1.5% | – | analyst α +0.12 · quality -0.04 |
| ⚪ Hold | +0.05 | **Tokyo Electron**<br><small>8035.T</small> | 8,978 JPY | +70% | +1.2% | +105% | -13% | 40 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · momentum +0.10 |
| ⚪ Hold | +0.04 | **LRCX**<br><small>Lam Research</small> | 220.84 USD | +70% | +1.0% | +95% | -22% | 39 | +0.02 | 1.5% → 1.5% | – | trend -0.10 · momentum +0.07 |
| ⚪ Hold | +0.03 | **KLAC**<br><small>KLA Corp</small> | 150.99 USD | +55% | -2.4% | +60% | -17% | 44 | +0.51 | 4.9% → 4.9% | – | quality +0.24 · analyst α -0.12 |
| ⚪ Hold | -0.02 | **ASML**<br><small>ASML Holding</small> | 1,495.10 USD | +40% | -6.3% | +73% | -6% | 42 | +0.42 | 0.0% → 0.0% | – | analyst α -0.27 · quality +0.18 |
| ⚪ Hold | -0.16 | **TER**<br><small>Teradyne</small> | 242.74 USD | +84% | +4.5% | +111% | -31% | 34 | -0.31 | 1.0% → 1.0% | – | analyst α +0.23 · trend -0.21 |
| 🔴 Sell | -0.25 | **ASMI**<br><small>ASM.AS</small> | 679.80 EUR | +66% | -0.1% | +72% | -16% | 39 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · trend -0.02 |
| 🔴 Sell | -0.29 | **GFS**<br><small>GlobalFoundries</small> | 40.33 USD | +88% | +5.7% | +42% | -27% | 41 | -0.21 | 0.0% → 0.0% | – | analyst α +0.27 · trend -0.14 |
| 🔴 Sell | -0.32 | **AMD**<br><small>Advanced Micro Devices</small> | 505.39 USD | +23% | -11.5% | +154% | +21% | 47 | -0.15 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.32 |
| 🔴 Sell | -0.49 | **Disco**<br><small>6146.T</small> | 45,540 JPY | +79% | +3.8% | +15% | -30% | 39 | +0.06 | 0.0% → 0.0% | – | momentum -0.26 · analyst α +0.19 |
| 🔴 Sell | -0.55 | **AMKR**<br><small>Amkor Technology</small> | 34.29 USD | +123% | +14.0% | +39% | -39% | 37 | -1.00 | 0.0% → 0.0% | – | analyst α +0.66 · quality -0.43 |
| 🔴 Sell | -0.56 | **ENTG**<br><small>Entegris</small> | 135.50 USD | +28% | -9.1% | +85% | -2% | 44 | -0.02 | 0.0% → 0.0% | – | analyst α -0.36 · trend +0.10 |
| 🔴 Sell | -0.72 | **ARM**<br><small>Arm Holdings</small> | 176.70 USD | +63% | -2.5% | +68% | -24% | 34 | +0.04 | 0.0% → 0.0% | – | analyst α -0.15 · trend -0.12 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -0.76 | **AVGO**<br><small>Broadcom</small> | 325.58 USD | +63% | -0.2% | +2% | -11% | 47 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.11 |
| 🔴🔴 Strong Sell | -0.79 | **SNPS**<br><small>Synopsys</small> | 452.36 USD | +26% | -9.5% | +28% | +2% | 48 | +0.14 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.18 |
| 🔴🔴 Strong Sell | -1.07 | **QCOM**<br><small>Qualcomm</small> | 169.95 USD | +14% | -12.3% | +4% | +1% | 48 | +0.70 | 0.0% → 0.0% | – | analyst α -0.66 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.15 | **TXN**<br><small>Texas Instruments</small> | 297.18 USD | +9% | -13.3% | +78% | +14% | 54 | +0.24 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.25 |
| 🔴🔴 Strong Sell | -1.26 | **CDNS**<br><small>Cadence Design Systems</small> | 327.60 USD | +24% | -10.0% | +7% | -0% | 50 | +0.31 | 0.0% → 0.0% | – | analyst α -0.48 · momentum -0.30 |
| 🔴🔴 Strong Sell | -1.30 | **SMIC**<br><small>0981.HK</small> | 47.24 HKD | +103% | +10.6% | -23% | -29% | 42 | -0.99 | 0.0% → 0.0% | – | momentum -0.53 · analyst α +0.48 |
| 🔴🔴 Strong Sell | -1.40 | **Shin-Etsu**<br><small>4063.T</small> | 5,666 JPY | +37% | -6.4% | +26% | -10% | 44 | -0.20 | 0.0% → 0.0% | – | analyst α -0.31 · momentum -0.20 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.90"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 703.85 USD (+116%, 46 analysts); de-biased α +12.1% vs CAPM hurdle 14.0%. Downtrend -7% vs 200-day avg; 12-1 mom +316%; RSI 34. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.20"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 199,600 KRW (+139%, 36 analysts); de-biased α +18.7% vs CAPM hurdle 11.3%. Downtrend -15% vs 200-day avg; 12-1 mom +156%; RSI 38. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.34"
    Within rebalance band of target 5.0%: no trade. No reliable analyst target: α set to 0. Downtrend -19% vs 200-day avg; 12-1 mom +188%; RSI 39. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.23"
    Within rebalance band of target 4.9%: no trade. Analyst target 293.88 USD vs 150.68 USD (+95%, 43 analysts); de-biased α +6.8% vs CAPM hurdle 14.1%. Downtrend -19% vs 200-day avg; 12-1 mom +193%; RSI 31. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.69"
    Within rebalance band of target 4.2%: no trade. Analyst target 327.70 USD vs 167.02 USD (+96%, 59 analysts); de-biased α +7.2% vs CAPM hurdle 13.9%. Downtrend -18% vs 200-day avg; 12-1 mom +21%; RSI 23. Quality z +0.47 (ROE 101%). ⚠️ oversold.

??? success "AMAT (AMAT) — 🟢 Buy, score +0.63"
    Within rebalance band of target 3.3%: no trade. Analyst target 638.94 USD vs 367.61 USD (+74%, 36 analysts); de-biased α +2.2% vs CAPM hurdle 11.6%. Downtrend -17% vs 200-day avg; 12-1 mom +117%; RSI 41. Quality z +0.03 (ROE 36%).

??? success "ASX (ASX) — 🟢 Buy, score +0.62"
    **ADD 552 sh** → target 3.6% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 51.00 USD vs 34.76 USD (+47%, 1 analysts); de-biased α -2.2% vs CAPM hurdle 11.9%. Uptrend +3% vs 200-day avg; 12-1 mom +215%; RSI 41. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.61"
    Within rebalance band of target 2.5%: no trade. Analyst target 42,686 JPY vs 29,505 JPY (+45%, 21 analysts); de-biased α -5.5% vs CAPM hurdle 13.4%. Uptrend +1% vs 200-day avg; 12-1 mom +140%; RSI 39. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? success "INTC (INTC) — 🟢 Buy, score +0.45"
    **TRIM 140 sh** → target 1.6% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 116.37 USD vs 57.20 USD (+103%, 43 analysts); de-biased α +9.0% vs CAPM hurdle 14.0%. Downtrend -34% vs 200-day avg; 12-1 mom +166%; RSI 28. Quality z -0.62 (ROE -0%). ⚠️ oversold; price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? note "TSM (TSM) — ⚪ Hold, score +0.18"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 388.80 USD (+42%, 20 analysts); de-biased α -5.4% vs CAPM hurdle 10.8%. Downtrend -3% vs 200-day avg; 12-1 mom +57%; RSI 41. Quality z +0.58 (ROE 35%).

??? note "Infineon (IFX.DE) — ⚪ Hold, score +0.12"
    Hold zone: keep any existing position, no new money. Analyst target 86.74 EUR vs 49.30 EUR (+76%, 23 analysts); de-biased α +2.2% vs CAPM hurdle 14.1%. Downtrend -14% vs 200-day avg; 12-1 mom +70%; RSI 43. Quality z -0.04 (ROE 6%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.05"
    Hold zone: not owned, no entry. Analyst target 15,275 JPY vs 8,978 JPY (+70%, 23 analysts); de-biased α +1.2% vs CAPM hurdle 12.8%. Downtrend -13% vs 200-day avg; 12-1 mom +105%; RSI 40. Quality z -0.28 (ROE 29%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.04"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 220.84 USD (+70%, 31 analysts); de-biased α +1.0% vs CAPM hurdle 12.6%. Downtrend -22% vs 200-day avg; 12-1 mom +95%; RSI 39. Quality z +0.02 (ROE 65%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.03"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 150.99 USD (+55%, 26 analysts); de-biased α -2.4% vs CAPM hurdle 11.1%. Downtrend -17% vs 200-day avg; 12-1 mom +60%; RSI 44. Quality z +0.51 (ROE 87%).

??? note "ASML (ASML) — ⚪ Hold, score -0.02"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,495.10 USD (+40%, 16 analysts); de-biased α -6.3% vs CAPM hurdle 12.3%. Downtrend -6% vs 200-day avg; 12-1 mom +73%; RSI 42. Quality z +0.42 (ROE 50%).

??? note "TER (TER) — ⚪ Hold, score -0.16"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 242.74 USD (+84%, 15 analysts); de-biased α +4.5% vs CAPM hurdle 12.3%. Downtrend -31% vs 200-day avg; 12-1 mom +111%; RSI 34. Quality z -0.31 (ROE 20%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.25"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 679.80 EUR (+66%, 19 analysts); de-biased α -0.1% vs CAPM hurdle 13.2%. Downtrend -16% vs 200-day avg; 12-1 mom +72%; RSI 39. Quality z -0.10 (ROE 19%).

??? failure "GFS (GFS) — 🔴 Sell, score -0.29"
    Avoid: not owned. Analyst target 76.00 USD vs 40.33 USD (+88%, 22 analysts); de-biased α +5.7% vs CAPM hurdle 12.4%. Downtrend -27% vs 200-day avg; 12-1 mom +42%; RSI 41. Quality z -0.21 (ROE 8%).

??? failure "AMD (AMD) — 🔴 Sell, score -0.32"
    Avoid: not owned. Analyst target 619.51 USD vs 505.39 USD (+23%, 50 analysts); de-biased α -11.5% vs CAPM hurdle 14.9%. Uptrend +21% vs 200-day avg; 12-1 mom +154%; RSI 47. Quality z -0.15 (ROE 7%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.49"
    Avoid: not owned. Analyst target 81,730 JPY vs 45,540 JPY (+79%, 20 analysts); de-biased α +3.8% vs CAPM hurdle 11.5%. Downtrend -30% vs 200-day avg; 12-1 mom +15%; RSI 39. Quality z +0.06 (ROE 25%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.55"
    Avoid: not owned. Analyst target 76.40 USD vs 34.29 USD (+123%, 10 analysts); de-biased α +14.0% vs CAPM hurdle 14.0%. Downtrend -39% vs 200-day avg; 12-1 mom +39%; RSI 37. Quality z -1.00 (ROE 9%).

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.56"
    Avoid: not owned. Analyst target 173.36 USD vs 135.50 USD (+28%, 11 analysts); de-biased α -9.1% vs CAPM hurdle 11.0%. Downtrend -2% vs 200-day avg; 12-1 mom +85%; RSI 44. Quality z -0.02 (ROE 6%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.72"
    Avoid: not owned. Analyst target 288.70 USD vs 176.70 USD (+63%, 40 analysts); de-biased α -2.5% vs CAPM hurdle 19.6%. Downtrend -24% vs 200-day avg; 12-1 mom +68%; RSI 34. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "AVGO (AVGO) — 🔴🔴 Strong Sell, score -0.76"
    Avoid: not owned. Analyst target 531.31 USD vs 325.58 USD (+63%, 47 analysts); de-biased α -0.2% vs CAPM hurdle 11.2%. Downtrend -11% vs 200-day avg; 12-1 mom +2%; RSI 47. Quality z +0.26 (ROE 31%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.79"
    Avoid: not owned. Analyst target 569.78 USD vs 452.36 USD (+26%, 26 analysts); de-biased α -9.5% vs CAPM hurdle 10.3%. Uptrend +2% vs 200-day avg; 12-1 mom +28%; RSI 48. Quality z +0.14 (ROE 7%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.07"
    Avoid: not owned. Analyst target 194.13 USD vs 169.95 USD (+14%, 30 analysts); de-biased α -12.3% vs CAPM hurdle 11.9%. Uptrend +1% vs 200-day avg; 12-1 mom +4%; RSI 48. Quality z +0.70 (ROE 23%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -1.15"
    Avoid: not owned. Analyst target 324.71 USD vs 297.18 USD (+9%, 31 analysts); de-biased α -13.3% vs CAPM hurdle 10.8%. Uptrend +14% vs 200-day avg; 12-1 mom +78%; RSI 54. Quality z +0.24 (ROE 30%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.26"
    Avoid: not owned. Analyst target 405.47 USD vs 327.60 USD (+24%, 26 analysts); de-biased α -10.0% vs CAPM hurdle 10.0%. Downtrend -0% vs 200-day avg; 12-1 mom +7%; RSI 50. Quality z +0.31 (ROE 22%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.30"
    Avoid: not owned. Analyst target 95.99 HKD vs 47.24 HKD (+103%, 21 analysts); de-biased α +10.6% vs CAPM hurdle 7.3%. Downtrend -29% vs 200-day avg; 12-1 mom -23%; RSI 42. Quality z -0.99 (ROE 3%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.40"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,666 JPY (+37%, 17 analysts); de-biased α -6.4% vs CAPM hurdle 10.8%. Downtrend -10% vs 200-day avg; 12-1 mom +26%; RSI 44. Quality z -0.20 (ROE 10%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 005930.KS | Samsung Electronics | 562 | 199,600 KRW | $83,480 | 10.0% | Strong Buy |
| MU | Micron Technology | 116 | 703.85 USD | $81,647 | 9.8% | Strong Buy |
| TSM | TSMC | 127 | 388.80 USD | $49,378 | 5.9% | Hold |
| MRVL | Marvell Technology | 324 | 150.68 USD | $48,820 | 5.9% | Strong Buy |
| 000660.KS | SK hynix | 50 | 1,220,000 KRW | $45,396 | 5.4% | Strong Buy |
| KLAC | KLA Corp | 268 | 150.99 USD | $40,465 | 4.9% | Hold |
| ASX | ASE Technology | 864 | 34.76 USD | $30,033 | 3.6% | Buy |
| NVDA | NVIDIA | 179 | 167.02 USD | $29,897 | 3.6% | Buy |
| AMAT | Applied Materials | 73 | 367.61 USD | $26,836 | 3.2% | Buy |
| 6857.T | Advantest | 100 | 29,505 JPY | $18,581 | 2.2% | Buy |
| INTC | Intel | 235 | 57.20 USD | $13,442 | 1.6% | Buy |
| LRCX | Lam Research | 58 | 220.84 USD | $12,809 | 1.5% | Hold |
| IFX.DE | Infineon Technologies | 225 | 49.30 EUR | $12,374 | 1.5% | Hold |
| TER | Teradyne | 35 | 242.74 USD | $8,496 | 1.0% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-11-10 17:51 UTC | ADD | ASX | 552 | 34.76 | $19,188 |
| 2026-11-10 17:51 UTC | TRIM | INTC | -140 | 57.20 | $8,008 |
| 2026-11-09 17:30 UTC | ADD | NVDA | 119 | 177.94 | $21,175 |
| 2026-11-09 17:30 UTC | ADD | INTC | 112 | 58.31 | $6,531 |
| 2026-11-09 17:30 UTC | TRIM | AMAT | -18 | 370.39 | $6,667 |
| 2026-11-06 17:58 UTC | ADD | AMAT | 20 | 333.00 | $6,660 |
| 2026-11-06 17:58 UTC | SELL (exit) | ASML | -30 | 1,418.92 | $42,568 |
| 2026-11-06 17:58 UTC | TRIM | INTC | -184 | 55.91 | $10,287 |
| 2026-11-06 02:27 UTC | ADD | 005930.KS | 240 | 191,400.00 | $33,864 |
| 2026-11-06 02:27 UTC | TRIM | 000660.KS | -30 | 1,169,000.00 | $25,854 |
| 2026-11-06 02:27 UTC | TRIM | 6857.T | -100 | 27,610.00 | $17,487 |
| 2026-11-05 15:28 UTC | ADD | INTC | 309 | 52.94 | $16,359 |
| 2026-11-05 15:28 UTC | ADD | MRVL | 160 | 140.70 | $22,512 |
| 2026-11-05 15:28 UTC | ADD | MU | 52 | 693.52 | $36,063 |
| 2026-11-05 15:28 UTC | ADD | AMAT | 21 | 332.95 | $6,992 |
| 2026-11-05 15:28 UTC | TRIM | LRCX | -104 | 195.72 | $20,355 |
| 2026-11-04 17:18 UTC | TRIM | AMAT | -12 | 366.64 | $4,400 |
| 2026-11-04 17:18 UTC | TRIM | INTC | -98 | 57.47 | $5,632 |
| 2026-11-03 15:09 UTC | ADD | INTC | 106 | 62.03 | $6,576 |
| 2026-11-03 15:09 UTC | ADD | MRVL | 50 | 172.03 | $8,602 |
| 2026-11-03 15:09 UTC | ADD | AMAT | 15 | 385.21 | $5,778 |
| 2026-11-03 15:09 UTC | TRIM | NVDA | -141 | 208.26 | $29,365 |
| 2026-11-02 15:55 UTC | BUY (new) | TER | 35 | 270.99 | $9,485 |
| 2026-11-02 15:55 UTC | ADD | MRVL | 35 | 184.11 | $6,444 |
| 2026-11-02 15:55 UTC | TRIM | IFX.DE | -1,076 | 52.66 | $63,473 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 53.6%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
