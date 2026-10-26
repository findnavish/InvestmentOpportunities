---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-26 23:54 UTC (Mon Oct 26, 07:54 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Mon 19:54) · Tokyo 🔴 closed (Tue 08:54) · Korea 🔴 closed (Tue 08:54) · Hong Kong 🔴 closed (Tue 07:54) · Xetra 🔴 closed (Tue 00:54) · Euronext Amsterdam 🔴 closed (Tue 00:54)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$883,175** | $126,836 (14%) | $756,339 (86%) | -11.68% | -12.95% | 🟢 Risk-on (+4.2%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $883,175), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| ADD | **Tokyo Electron**<br><small>8035.T</small> | 200 | 9,139 JPY | $11,603 | Queued · Tokyo closed | analyst α +0.27 · quality -0.18 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.26 | **SK hynix**<br><small>000660.KS</small> | 1,285,000 KRW | +144% | +22.4% | +337% | -13% | 34 | +0.62 | 10.8% → 10.0% | – | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.27 | **MU**<br><small>Micron Technology</small> | 903.70 USD | +68% | +3.4% | +424% | +23% | 42 | +0.12 | 9.4% → 10.0% | – | momentum +0.53 · analyst α +0.23 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.54 | **Samsung**<br><small>005930.KS</small> | 213,500 KRW | +124% | +18.0% | +193% | -9% | 35 | -0.26 | 8.8% → 10.0% | – | analyst α +0.66 · momentum +0.23 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.60 | **Infineon**<br><small>IFX.DE</small> | 50.48 EUR | +72% | +4.4% | +67% | -11% | 37 | -0.04 | 8.3% → 8.9% | – | analyst α +0.41 · trend -0.07 |
| 🟢 Buy | +0.51 | **AMAT**<br><small>Applied Materials</small> | 387.59 USD | +65% | +3.2% | +113% | -12% | 31 | +0.03 | 6.4% → 6.6% | – | analyst α +0.19 · momentum +0.12 |
| 🟢 Buy | +0.50 | **Advantest**<br><small>6857.T</small> | 31,070 JPY | +37% | -4.1% | +84% | +8% | 36 | +0.33 | 4.5% → 5.1% | – | quality +0.16 · trend +0.14 · ⚠️ rich valuation |
| 🟢 Buy | +0.44 | **ASX**<br><small>ASE Technology</small> | 39.92 USD | +28% | -3.0% | +249% | +22% | 44 | -0.68 | 6.0% → 6.2% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.37 | **Tokyo Electron**<br><small>8035.T</small> | 9,139 JPY | +67% | +3.7% | +95% | -9% | 32 | -0.28 | 3.3% → 4.8% | ADD 200 | analyst α +0.27 · quality -0.18 |
| 🟢 Buy | +0.32 | **TSM**<br><small>TSMC</small> | 424.39 USD | +30% | -5.2% | +57% | +7% | 45 | +0.58 | 6.1% → 5.8% | – | quality +0.28 · analyst α -0.15 |
| 🟢 Buy | +0.31 | **NVDA**<br><small>NVIDIA</small> | 215.98 USD | +52% | -0.7% | +24% | +6% | 44 | +0.47 | 4.1% → 4.7% | – | quality +0.21 · momentum -0.17 |
| ⚪ Hold | +0.21 | **KLAC**<br><small>KLA Corp</small> | 149.22 USD | +57% | +1.3% | +63% | -18% | 28 | +0.51 | 4.5% → 4.5% | – | quality +0.24 · trend -0.16 · ⚠️ oversold |
| ⚪ Hold | +0.12 | **ASML**<br><small>ASML Holding</small> | 1,590.18 USD | +32% | -5.2% | +69% | +0% | 38 | +0.42 | 5.4% → 5.4% | – | analyst α -0.19 · quality +0.18 |
| ⚪ Hold | +0.11 | **LRCX**<br><small>Lam Research</small> | 237.37 USD | +58% | +1.3% | +115% | -16% | 29 | +0.02 | 4.4% → 4.4% | – | momentum +0.14 · trend -0.14 · ⚠️ oversold |
| ⚪ Hold | +0.03 | **MRVL**<br><small>Marvell Technology</small> | 233.78 USD | +26% | -7.3% | +217% | +30% | 44 | -0.12 | 0.0% → 0.0% | – | analyst α -0.41 · momentum +0.26 · ⚠️ rich valuation |
| ⚪ Hold | -0.08 | **AVGO**<br><small>Broadcom</small> | 329.28 USD | +61% | +2.6% | +3% | -10% | 40 | +0.26 | 3.7% → 3.7% | – | momentum -0.26 · analyst α +0.15 |
| ⚪ Hold | -0.19 | **TER**<br><small>Teradyne</small> | 308.94 USD | +45% | -2.1% | +175% | -11% | 33 | -0.31 | 0.0% → 0.0% | – | quality -0.21 · momentum +0.20 |
| ⚪ Hold | -0.23 | **Disco**<br><small>6146.T</small> | 48,400 JPY | +69% | +4.4% | +2% | -26% | 32 | +0.06 | 0.0% → 0.0% | – | analyst α +0.36 · momentum -0.30 |
| 🔴 Sell | -0.32 | **GFS**<br><small>GlobalFoundries</small> | 45.00 USD | +69% | +4.0% | +40% | -18% | 43 | -0.21 | 0.0% → 0.0% | – | analyst α +0.31 · trend -0.18 |
| 🔴 Sell | -0.36 | **AMD**<br><small>Advanced Micro Devices</small> | 531.47 USD | +17% | -9.7% | +168% | +32% | 43 | -0.15 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.32 |
| 🔴 Sell | -0.36 | **ASMI**<br><small>ASM.AS</small> | 708.60 EUR | +59% | +1.4% | +55% | -13% | 32 | -0.10 | 0.0% → 0.0% | – | momentum -0.12 · analyst α +0.12 |
| 🔴 Sell | -0.40 | **INTC**<br><small>Intel</small> | 90.51 USD | +29% | -6.5% | +222% | +5% | 38 | -0.62 | 0.0% → 0.0% | – | analyst α -0.31 · momentum +0.30 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.57 | **AMKR**<br><small>Amkor Technology</small> | 36.80 USD | +108% | +13.4% | +69% | -36% | 27 | -1.00 | 0.0% → 0.0% | – | analyst α +0.48 · quality -0.43 · ⚠️ oversold |
| 🔴 Sell | -0.75 | **ENTG**<br><small>Entegris</small> | 140.27 USD | +24% | -7.0% | +68% | +2% | 45 | -0.02 | 0.0% → 0.0% | – | analyst α -0.36 · trend +0.06 |
| 🔴🔴 Strong Sell | -0.79 | **ARM**<br><small>Arm Holdings</small> | 223.35 USD | +29% | -7.8% | +86% | -1% | 38 | +0.04 | 0.0% → 0.0% | – | analyst α -0.48 · momentum +0.07 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -0.95 | **Shin-Etsu**<br><small>4063.T</small> | 5,788 JPY | +34% | -3.9% | +18% | -8% | 41 | -0.20 | 0.0% → 0.0% | – | momentum -0.23 · quality -0.11 |
| 🔴🔴 Strong Sell | -0.96 | **CDNS**<br><small>Cadence Design Systems</small> | 321.35 USD | +26% | -6.1% | -3% | -2% | 48 | +0.31 | 0.0% → 0.0% | – | momentum -0.35 · analyst α -0.23 |
| 🔴🔴 Strong Sell | -1.02 | **TXN**<br><small>Texas Instruments</small> | 298.05 USD | +9% | -10.2% | +66% | +16% | 65 | +0.24 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.16 |
| 🔴🔴 Strong Sell | -1.15 | **QCOM**<br><small>Qualcomm</small> | 179.63 USD | +8% | -10.6% | +21% | +7% | 52 | +0.70 | 0.0% → 0.0% | – | analyst α -0.85 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.23 | **SMIC**<br><small>0981.HK</small> | 45.92 HKD | +109% | +15.3% | -16% | -33% | 18 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.53 · ⚠️ oversold |
| 🔴🔴 Strong Sell | -1.24 | **SNPS**<br><small>Synopsys</small> | 454.33 USD | +25% | -6.4% | -7% | +2% | 51 | +0.14 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.27 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.26"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,285,000 KRW (+144%, 38 analysts); de-biased α +22.4% vs CAPM hurdle 14.3%. Downtrend -13% vs 200-day avg; 12-1 mom +337%; RSI 34. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.27"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 903.70 USD (+68%, 46 analysts); de-biased α +3.4% vs CAPM hurdle 14.0%. Uptrend +23% vs 200-day avg; 12-1 mom +424%; RSI 42. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.54"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 213,500 KRW (+124%, 36 analysts); de-biased α +18.0% vs CAPM hurdle 11.3%. Downtrend -9% vs 200-day avg; 12-1 mom +193%; RSI 35. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.60"
    Within rebalance band of target 8.9%: no trade. Analyst target 86.74 EUR vs 50.48 EUR (+72%, 23 analysts); de-biased α +4.4% vs CAPM hurdle 14.1%. Downtrend -11% vs 200-day avg; 12-1 mom +67%; RSI 37. Quality z -0.04 (ROE 6%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.51"
    Within rebalance band of target 6.6%: no trade. Analyst target 638.94 USD vs 387.59 USD (+65%, 36 analysts); de-biased α +3.2% vs CAPM hurdle 11.6%. Downtrend -12% vs 200-day avg; 12-1 mom +113%; RSI 31. Quality z +0.03 (ROE 36%).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.50"
    Within rebalance band of target 5.1%: no trade. Analyst target 42,686 JPY vs 31,070 JPY (+37%, 21 analysts); de-biased α -4.1% vs CAPM hurdle 13.4%. Uptrend +8% vs 200-day avg; 12-1 mom +84%; RSI 36. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? success "ASX (ASX) — 🟢 Buy, score +0.44"
    Within rebalance band of target 6.2%: no trade. Analyst target 51.00 USD vs 39.92 USD (+28%, 1 analysts); de-biased α -3.0% vs CAPM hurdle 11.9%. Uptrend +22% vs 200-day avg; 12-1 mom +249%; RSI 44. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "Tokyo Electron (8035.T) — 🟢 Buy, score +0.37"
    **ADD 200 sh** → target 4.8% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 15,275 JPY vs 9,139 JPY (+67%, 23 analysts); de-biased α +3.7% vs CAPM hurdle 12.8%. Downtrend -9% vs 200-day avg; 12-1 mom +95%; RSI 32. Quality z -0.28 (ROE 29%).

??? success "TSM (TSM) — 🟢 Buy, score +0.32"
    Within rebalance band of target 5.8%: no trade. Analyst target 552.26 USD vs 424.39 USD (+30%, 20 analysts); de-biased α -5.2% vs CAPM hurdle 10.8%. Uptrend +7% vs 200-day avg; 12-1 mom +57%; RSI 45. Quality z +0.58 (ROE 35%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.31"
    Within rebalance band of target 4.7%: no trade. Analyst target 327.70 USD vs 215.98 USD (+52%, 59 analysts); de-biased α -0.7% vs CAPM hurdle 13.9%. Uptrend +6% vs 200-day avg; 12-1 mom +24%; RSI 44. Quality z +0.47 (ROE 101%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.21"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 149.22 USD (+57%, 26 analysts); de-biased α +1.3% vs CAPM hurdle 11.1%. Downtrend -18% vs 200-day avg; 12-1 mom +63%; RSI 28. Quality z +0.51 (ROE 87%). ⚠️ oversold.

??? note "ASML (ASML) — ⚪ Hold, score +0.12"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,590.18 USD (+32%, 16 analysts); de-biased α -5.2% vs CAPM hurdle 12.3%. Uptrend +0% vs 200-day avg; 12-1 mom +69%; RSI 38. Quality z +0.42 (ROE 50%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.11"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 237.37 USD (+58%, 31 analysts); de-biased α +1.3% vs CAPM hurdle 12.6%. Downtrend -16% vs 200-day avg; 12-1 mom +115%; RSI 29. Quality z +0.02 (ROE 65%). ⚠️ oversold.

??? note "MRVL (MRVL) — ⚪ Hold, score +0.03"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 233.78 USD (+26%, 43 analysts); de-biased α -7.3% vs CAPM hurdle 14.1%. Uptrend +30% vs 200-day avg; 12-1 mom +217%; RSI 44. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "AVGO (AVGO) — ⚪ Hold, score -0.08"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 329.28 USD (+61%, 47 analysts); de-biased α +2.6% vs CAPM hurdle 11.2%. Downtrend -10% vs 200-day avg; 12-1 mom +3%; RSI 40. Quality z +0.26 (ROE 31%).

??? note "TER (TER) — ⚪ Hold, score -0.19"
    Hold zone: not owned, no entry. Analyst target 446.47 USD vs 308.94 USD (+45%, 15 analysts); de-biased α -2.1% vs CAPM hurdle 12.3%. Downtrend -11% vs 200-day avg; 12-1 mom +175%; RSI 33. Quality z -0.31 (ROE 20%).

??? note "Disco (6146.T) — ⚪ Hold, score -0.23"
    Hold zone: not owned, no entry. Analyst target 81,730 JPY vs 48,400 JPY (+69%, 20 analysts); de-biased α +4.4% vs CAPM hurdle 11.5%. Downtrend -26% vs 200-day avg; 12-1 mom +2%; RSI 32. Quality z +0.06 (ROE 25%).

??? failure "GFS (GFS) — 🔴 Sell, score -0.32"
    Avoid: not owned. Analyst target 76.00 USD vs 45.00 USD (+69%, 22 analysts); de-biased α +4.0% vs CAPM hurdle 12.4%. Downtrend -18% vs 200-day avg; 12-1 mom +40%; RSI 43. Quality z -0.21 (ROE 8%).

??? failure "AMD (AMD) — 🔴 Sell, score -0.36"
    Avoid: not owned. Analyst target 619.51 USD vs 531.47 USD (+17%, 50 analysts); de-biased α -9.7% vs CAPM hurdle 14.9%. Uptrend +32% vs 200-day avg; 12-1 mom +168%; RSI 43. Quality z -0.15 (ROE 7%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.36"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 708.60 EUR (+59%, 19 analysts); de-biased α +1.4% vs CAPM hurdle 13.2%. Downtrend -13% vs 200-day avg; 12-1 mom +55%; RSI 32. Quality z -0.10 (ROE 19%).

??? failure "INTC (INTC) — 🔴 Sell, score -0.40"
    Avoid: not owned. Analyst target 116.37 USD vs 90.51 USD (+29%, 43 analysts); de-biased α -6.5% vs CAPM hurdle 14.0%. Uptrend +5% vs 200-day avg; 12-1 mom +222%; RSI 38. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.57"
    Avoid: not owned. Analyst target 76.40 USD vs 36.80 USD (+108%, 10 analysts); de-biased α +13.4% vs CAPM hurdle 14.0%. Downtrend -36% vs 200-day avg; 12-1 mom +69%; RSI 27. Quality z -1.00 (ROE 9%). ⚠️ oversold.

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.75"
    Avoid: not owned. Analyst target 173.36 USD vs 140.27 USD (+24%, 11 analysts); de-biased α -7.0% vs CAPM hurdle 11.0%. Uptrend +2% vs 200-day avg; 12-1 mom +68%; RSI 45. Quality z -0.02 (ROE 6%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -0.79"
    Avoid: not owned. Analyst target 288.70 USD vs 223.35 USD (+29%, 40 analysts); de-biased α -7.8% vs CAPM hurdle 19.6%. Downtrend -1% vs 200-day avg; 12-1 mom +86%; RSI 38. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -0.95"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,788 JPY (+34%, 17 analysts); de-biased α -3.9% vs CAPM hurdle 10.8%. Downtrend -8% vs 200-day avg; 12-1 mom +18%; RSI 41. Quality z -0.20 (ROE 10%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -0.96"
    Avoid: not owned. Analyst target 405.47 USD vs 321.35 USD (+26%, 26 analysts); de-biased α -6.1% vs CAPM hurdle 10.0%. Downtrend -2% vs 200-day avg; 12-1 mom -3%; RSI 48. Quality z +0.31 (ROE 22%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -1.02"
    Avoid: not owned. Analyst target 324.71 USD vs 298.05 USD (+9%, 31 analysts); de-biased α -10.2% vs CAPM hurdle 10.8%. Uptrend +16% vs 200-day avg; 12-1 mom +66%; RSI 65. Quality z +0.24 (ROE 30%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.15"
    Avoid: not owned. Analyst target 194.13 USD vs 179.63 USD (+8%, 30 analysts); de-biased α -10.6% vs CAPM hurdle 11.9%. Uptrend +7% vs 200-day avg; 12-1 mom +21%; RSI 52. Quality z +0.70 (ROE 23%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.23"
    Avoid: not owned. Analyst target 95.99 HKD vs 45.92 HKD (+109%, 21 analysts); de-biased α +15.3% vs CAPM hurdle 7.3%. Downtrend -33% vs 200-day avg; 12-1 mom -16%; RSI 18. Quality z -0.99 (ROE 3%). ⚠️ oversold.

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.24"
    Avoid: not owned. Analyst target 569.78 USD vs 454.33 USD (+25%, 26 analysts); de-biased α -6.4% vs CAPM hurdle 10.3%. Uptrend +2% vs 200-day avg; 12-1 mom -7%; RSI 51. Quality z +0.14 (ROE 7%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 98 | 1,285,000 KRW | $95,043 | 10.8% | Strong Buy |
| MU | Micron Technology | 92 | 903.70 USD | $83,140 | 9.4% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 213,500 KRW | $78,150 | 8.8% | Strong Buy |
| IFX.DE | Infineon Technologies | 1,301 | 50.48 EUR | $73,404 | 8.3% | Buy |
| AMAT | Applied Materials | 145 | 387.59 USD | $56,201 | 6.4% | Buy |
| TSM | TSMC | 127 | 424.39 USD | $53,897 | 6.1% | Buy |
| ASX | ASE Technology | 1,320 | 39.92 USD | $52,688 | 6.0% | Buy |
| ASML | ASML Holding | 30 | 1,590.18 USD | $47,705 | 5.4% | Hold |
| KLAC | KLA Corp | 268 | 149.22 USD | $39,991 | 4.5% | Hold |
| 6857.T | Advantest | 200 | 31,070 JPY | $39,446 | 4.5% | Buy |
| LRCX | Lam Research | 162 | 237.37 USD | $38,454 | 4.4% | Hold |
| NVDA | NVIDIA | 168 | 215.98 USD | $36,285 | 4.1% | Buy |
| AVGO | Broadcom | 100 | 329.28 USD | $32,928 | 3.7% | Hold |
| 8035.T | Tokyo Electron | 500 | 9,139 JPY | $29,007 | 3.3% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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
| 2026-10-15 15:02 UTC | ADD | ASX | 339 | 41.52 | $14,077 |
| 2026-10-15 15:02 UTC | TRIM | KLAC | -93 | 172.43 | $16,036 |
| 2026-10-15 04:41 UTC | BUY (new) | 6857.T | 100 | 34,860.00 | $22,075 |
| 2026-10-15 04:41 UTC | ADD | 000660.KS | 24 | 1,270,000.00 | $22,625 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 40.7%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
