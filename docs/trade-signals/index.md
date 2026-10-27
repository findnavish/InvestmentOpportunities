---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-27 05:07 UTC (Tue Oct 27, 01:07 AM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Tue 01:07) · Tokyo 🟢 open (Tue 14:07) · Korea 🟢 open (Tue 14:07) · Hong Kong 🟢 open (Tue 13:07) · Xetra 🔴 closed (Tue 06:07) · Euronext Amsterdam 🔴 closed (Tue 06:07)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$895,206** | $126,836 (14%) | $768,370 (86%) | -10.48% | -12.95% | 🟢 Risk-on (+4.2%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $895,206), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| ADD | **AMAT**<br><small>Applied Materials</small> | 46 | 387.59 USD | $17,829 | Queued · NYSE/Nasdaq closed | analyst α +0.27 · momentum +0.14 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.29 | **SK hynix**<br><small>000660.KS</small> | 1,346,000 KRW | +133% | +20.0% | +337% | -9% | 39 | +0.62 | 11.1% → 10.0% | – | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.37 | **MU**<br><small>Micron Technology</small> | 903.70 USD | +68% | +3.8% | +424% | +23% | 42 | +0.12 | 9.3% → 10.0% | – | momentum +0.53 · analyst α +0.31 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.53 | **Samsung**<br><small>005930.KS</small> | 221,500 KRW | +116% | +16.4% | +193% | -6% | 41 | -0.26 | 9.1% → 10.0% | – | analyst α +0.66 · momentum +0.23 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.68 | **AMAT**<br><small>Applied Materials</small> | 387.59 USD | +65% | +3.6% | +113% | -12% | 31 | +0.03 | 6.3% → 8.3% | ADD 46 | analyst α +0.27 · momentum +0.14 |
| 🟢 Buy | +0.66 | **Infineon**<br><small>IFX.DE</small> | 50.48 EUR | +72% | +4.8% | +67% | -11% | 37 | -0.04 | 8.2% → 9.3% | – | analyst α +0.41 · trend -0.07 |
| 🟢 Buy | +0.42 | **ASX**<br><small>ASE Technology</small> | 39.92 USD | +28% | -2.8% | +241% | +22% | 44 | -0.68 | 5.9% → 5.6% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.38 | **TSM**<br><small>TSMC</small> | 424.39 USD | +30% | -4.8% | +55% | +7% | 45 | +0.58 | 6.0% → 6.6% | – | quality +0.28 · analyst α -0.12 |
| 🟢 Buy | +0.30 | **NVDA**<br><small>NVIDIA</small> | 215.98 USD | +52% | -0.3% | +23% | +6% | 44 | +0.47 | 4.1% → 4.3% | – | quality +0.21 · momentum -0.17 |
| ⚪ Hold | +0.24 | **ASML**<br><small>ASML Holding</small> | 1,590.18 USD | +32% | -4.8% | +73% | +0% | 38 | +0.42 | 5.3% → 5.3% | – | quality +0.18 · analyst α -0.15 |
| ⚪ Hold | +0.20 | **KLAC**<br><small>KLA Corp</small> | 149.22 USD | +57% | +1.7% | +61% | -18% | 28 | +0.51 | 4.5% → 4.5% | – | quality +0.24 · trend -0.16 · ⚠️ oversold |
| ⚪ Hold | +0.19 | **Tokyo Electron**<br><small>8035.T</small> | 9,390 JPY | +63% | +2.9% | +95% | -6% | 36 | -0.28 | 3.3% → 3.3% | – | analyst α +0.19 · quality -0.18 |
| ⚪ Hold | +0.11 | **MRVL**<br><small>Marvell Technology</small> | 233.78 USD | +26% | -6.9% | +217% | +30% | 44 | -0.12 | 0.0% → 0.0% | – | analyst α -0.41 · momentum +0.30 · ⚠️ rich valuation |
| ⚪ Hold | +0.05 | **LRCX**<br><small>Lam Research</small> | 237.37 USD | +58% | +1.6% | +108% | -16% | 29 | +0.02 | 4.3% → 4.3% | – | trend -0.14 · momentum +0.12 · ⚠️ oversold |
| ⚪ Hold | +0.05 | **Advantest**<br><small>6857.T</small> | 33,980 JPY | +26% | -6.7% | +91% | +18% | 47 | +0.33 | 4.8% → 4.8% | – | analyst α -0.36 · quality +0.16 · ⚠️ rich valuation |
| ⚪ Hold | -0.19 | **AVGO**<br><small>Broadcom</small> | 329.28 USD | +61% | +2.9% | -1% | -10% | 40 | +0.26 | 3.7% → 3.7% | – | momentum -0.30 · analyst α +0.15 |
| ⚪ Hold | -0.20 | **GFS**<br><small>GlobalFoundries</small> | 45.00 USD | +69% | +4.4% | +40% | -18% | 43 | -0.21 | 0.0% → 0.0% | – | analyst α +0.36 · trend -0.18 |
| ⚪ Hold | -0.24 | **TER**<br><small>Teradyne</small> | 308.94 USD | +45% | -1.7% | +179% | -11% | 33 | -0.31 | 0.0% → 0.0% | – | quality -0.21 · momentum +0.20 |
| 🔴 Sell | -0.34 | **AMD**<br><small>Advanced Micro Devices</small> | 531.47 USD | +17% | -9.4% | +140% | +31% | 43 | -0.15 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.32 |
| 🔴 Sell | -0.38 | **ASMI**<br><small>ASM.AS</small> | 708.60 EUR | +59% | +1.8% | +55% | -13% | 32 | -0.10 | 0.0% → 0.0% | – | momentum -0.12 · analyst α +0.12 |
| 🔴 Sell | -0.38 | **INTC**<br><small>Intel</small> | 90.51 USD | +29% | -6.2% | +203% | +5% | 38 | -0.62 | 0.0% → 0.0% | – | analyst α -0.27 · momentum +0.26 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.42 | **Disco**<br><small>6146.T</small> | 50,150 JPY | +63% | +3.3% | +2% | -23% | 38 | +0.06 | 0.0% → 0.0% | – | momentum -0.26 · analyst α +0.23 |
| 🔴 Sell | -0.68 | **AMKR**<br><small>Amkor Technology</small> | 36.80 USD | +108% | +13.8% | +63% | -36% | 27 | -1.00 | 0.0% → 0.0% | – | analyst α +0.48 · quality -0.43 · ⚠️ oversold |
| 🔴 Sell | -0.69 | **ENTG**<br><small>Entegris</small> | 140.27 USD | +24% | -6.6% | +65% | +2% | 45 | -0.02 | 0.0% → 0.0% | – | analyst α -0.31 · trend +0.04 |
| 🔴🔴 Strong Sell | -0.84 | **CDNS**<br><small>Cadence Design Systems</small> | 321.35 USD | +26% | -5.7% | -5% | -2% | 48 | +0.31 | 0.0% → 0.0% | – | momentum -0.35 · analyst α -0.19 |
| 🔴🔴 Strong Sell | -0.84 | **TXN**<br><small>Texas Instruments</small> | 298.05 USD | +9% | -9.8% | +69% | +16% | 64 | +0.24 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.14 |
| 🔴🔴 Strong Sell | -0.91 | **Shin-Etsu**<br><small>4063.T</small> | 5,876 JPY | +32% | -4.0% | +18% | -7% | 46 | -0.20 | 0.0% → 0.0% | – | momentum -0.20 · quality -0.11 |
| 🔴🔴 Strong Sell | -0.94 | **ARM**<br><small>Arm Holdings</small> | 223.35 USD | +29% | -7.4% | +66% | -2% | 38 | +0.04 | 0.0% → 0.0% | – | analyst α -0.48 · quality +0.03 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.08 | **SNPS**<br><small>Synopsys</small> | 454.33 USD | +25% | -6.0% | -7% | +2% | 51 | +0.14 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.23 |
| 🔴🔴 Strong Sell | -1.17 | **QCOM**<br><small>Qualcomm</small> | 179.63 USD | +8% | -10.3% | +13% | +7% | 52 | +0.70 | 0.0% → 0.0% | – | analyst α -0.85 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.18 | **SMIC**<br><small>0981.HK</small> | 46.48 HKD | +107% | +15.0% | -14% | -32% | 21 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.53 · ⚠️ oversold |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.29"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,346,000 KRW (+133%, 38 analysts); de-biased α +20.0% vs CAPM hurdle 14.3%. Downtrend -9% vs 200-day avg; 12-1 mom +337%; RSI 39. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.37"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 903.70 USD (+68%, 46 analysts); de-biased α +3.8% vs CAPM hurdle 14.0%. Uptrend +23% vs 200-day avg; 12-1 mom +424%; RSI 42. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.53"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 221,500 KRW (+116%, 36 analysts); de-biased α +16.4% vs CAPM hurdle 11.3%. Downtrend -6% vs 200-day avg; 12-1 mom +193%; RSI 41. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.68"
    **ADD 46 sh** → target 8.3% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 387.59 USD (+65%, 36 analysts); de-biased α +3.6% vs CAPM hurdle 11.6%. Downtrend -12% vs 200-day avg; 12-1 mom +113%; RSI 31. Quality z +0.03 (ROE 36%).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.66"
    Within rebalance band of target 9.3%: no trade. Analyst target 86.74 EUR vs 50.48 EUR (+72%, 23 analysts); de-biased α +4.8% vs CAPM hurdle 14.1%. Downtrend -11% vs 200-day avg; 12-1 mom +67%; RSI 37. Quality z -0.04 (ROE 6%).

??? success "ASX (ASX) — 🟢 Buy, score +0.42"
    Within rebalance band of target 5.6%: no trade. Analyst target 51.00 USD vs 39.92 USD (+28%, 1 analysts); de-biased α -2.8% vs CAPM hurdle 11.9%. Uptrend +22% vs 200-day avg; 12-1 mom +241%; RSI 44. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "TSM (TSM) — 🟢 Buy, score +0.38"
    Within rebalance band of target 6.6%: no trade. Analyst target 552.26 USD vs 424.39 USD (+30%, 20 analysts); de-biased α -4.8% vs CAPM hurdle 10.8%. Uptrend +7% vs 200-day avg; 12-1 mom +55%; RSI 45. Quality z +0.58 (ROE 35%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.30"
    Within rebalance band of target 4.3%: no trade. Analyst target 327.70 USD vs 215.98 USD (+52%, 59 analysts); de-biased α -0.3% vs CAPM hurdle 13.9%. Uptrend +6% vs 200-day avg; 12-1 mom +23%; RSI 44. Quality z +0.47 (ROE 101%).

??? note "ASML (ASML) — ⚪ Hold, score +0.24"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,590.18 USD (+32%, 16 analysts); de-biased α -4.8% vs CAPM hurdle 12.3%. Uptrend +0% vs 200-day avg; 12-1 mom +73%; RSI 38. Quality z +0.42 (ROE 50%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.20"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 149.22 USD (+57%, 26 analysts); de-biased α +1.7% vs CAPM hurdle 11.1%. Downtrend -18% vs 200-day avg; 12-1 mom +61%; RSI 28. Quality z +0.51 (ROE 87%). ⚠️ oversold.

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.19"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 9,390 JPY (+63%, 23 analysts); de-biased α +2.9% vs CAPM hurdle 12.8%. Downtrend -6% vs 200-day avg; 12-1 mom +95%; RSI 36. Quality z -0.28 (ROE 29%).

??? note "MRVL (MRVL) — ⚪ Hold, score +0.11"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 233.78 USD (+26%, 43 analysts); de-biased α -6.9% vs CAPM hurdle 14.1%. Uptrend +30% vs 200-day avg; 12-1 mom +217%; RSI 44. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.05"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 237.37 USD (+58%, 31 analysts); de-biased α +1.6% vs CAPM hurdle 12.6%. Downtrend -16% vs 200-day avg; 12-1 mom +108%; RSI 29. Quality z +0.02 (ROE 65%). ⚠️ oversold.

??? note "Advantest (6857.T) — ⚪ Hold, score +0.05"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 33,980 JPY (+26%, 21 analysts); de-biased α -6.7% vs CAPM hurdle 13.4%. Uptrend +18% vs 200-day avg; 12-1 mom +91%; RSI 47. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "AVGO (AVGO) — ⚪ Hold, score -0.19"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 329.28 USD (+61%, 47 analysts); de-biased α +2.9% vs CAPM hurdle 11.2%. Downtrend -10% vs 200-day avg; 12-1 mom -1%; RSI 40. Quality z +0.26 (ROE 31%).

??? note "GFS (GFS) — ⚪ Hold, score -0.20"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 45.00 USD (+69%, 22 analysts); de-biased α +4.4% vs CAPM hurdle 12.4%. Downtrend -18% vs 200-day avg; 12-1 mom +40%; RSI 43. Quality z -0.21 (ROE 8%).

??? note "TER (TER) — ⚪ Hold, score -0.24"
    Hold zone: not owned, no entry. Analyst target 446.47 USD vs 308.94 USD (+45%, 15 analysts); de-biased α -1.7% vs CAPM hurdle 12.3%. Downtrend -11% vs 200-day avg; 12-1 mom +179%; RSI 33. Quality z -0.31 (ROE 20%).

??? failure "AMD (AMD) — 🔴 Sell, score -0.34"
    Avoid: not owned. Analyst target 619.51 USD vs 531.47 USD (+17%, 50 analysts); de-biased α -9.4% vs CAPM hurdle 14.9%. Uptrend +31% vs 200-day avg; 12-1 mom +140%; RSI 43. Quality z -0.15 (ROE 7%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.38"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 708.60 EUR (+59%, 19 analysts); de-biased α +1.8% vs CAPM hurdle 13.2%. Downtrend -13% vs 200-day avg; 12-1 mom +55%; RSI 32. Quality z -0.10 (ROE 19%).

??? failure "INTC (INTC) — 🔴 Sell, score -0.38"
    Avoid: not owned. Analyst target 116.37 USD vs 90.51 USD (+29%, 43 analysts); de-biased α -6.2% vs CAPM hurdle 14.0%. Uptrend +5% vs 200-day avg; 12-1 mom +203%; RSI 38. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "Disco (6146.T) — 🔴 Sell, score -0.42"
    Avoid: not owned. Analyst target 81,730 JPY vs 50,150 JPY (+63%, 20 analysts); de-biased α +3.3% vs CAPM hurdle 11.5%. Downtrend -23% vs 200-day avg; 12-1 mom +2%; RSI 38. Quality z +0.06 (ROE 25%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.68"
    Avoid: not owned. Analyst target 76.40 USD vs 36.80 USD (+108%, 10 analysts); de-biased α +13.8% vs CAPM hurdle 14.0%. Downtrend -36% vs 200-day avg; 12-1 mom +63%; RSI 27. Quality z -1.00 (ROE 9%). ⚠️ oversold.

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.69"
    Avoid: not owned. Analyst target 173.36 USD vs 140.27 USD (+24%, 11 analysts); de-biased α -6.6% vs CAPM hurdle 11.0%. Uptrend +2% vs 200-day avg; 12-1 mom +65%; RSI 45. Quality z -0.02 (ROE 6%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -0.84"
    Avoid: not owned. Analyst target 405.47 USD vs 321.35 USD (+26%, 26 analysts); de-biased α -5.7% vs CAPM hurdle 10.0%. Downtrend -2% vs 200-day avg; 12-1 mom -5%; RSI 48. Quality z +0.31 (ROE 22%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -0.84"
    Avoid: not owned. Analyst target 324.71 USD vs 298.05 USD (+9%, 31 analysts); de-biased α -9.8% vs CAPM hurdle 10.8%. Uptrend +16% vs 200-day avg; 12-1 mom +69%; RSI 64. Quality z +0.24 (ROE 30%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -0.91"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,876 JPY (+32%, 17 analysts); de-biased α -4.0% vs CAPM hurdle 10.8%. Downtrend -7% vs 200-day avg; 12-1 mom +18%; RSI 46. Quality z -0.20 (ROE 10%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -0.94"
    Avoid: not owned. Analyst target 288.70 USD vs 223.35 USD (+29%, 40 analysts); de-biased α -7.4% vs CAPM hurdle 19.6%. Downtrend -2% vs 200-day avg; 12-1 mom +66%; RSI 38. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.08"
    Avoid: not owned. Analyst target 569.78 USD vs 454.33 USD (+25%, 26 analysts); de-biased α -6.0% vs CAPM hurdle 10.3%. Uptrend +2% vs 200-day avg; 12-1 mom -7%; RSI 51. Quality z +0.14 (ROE 7%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.17"
    Avoid: not owned. Analyst target 194.13 USD vs 179.63 USD (+8%, 30 analysts); de-biased α -10.3% vs CAPM hurdle 11.9%. Uptrend +7% vs 200-day avg; 12-1 mom +13%; RSI 52. Quality z +0.70 (ROE 23%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.18"
    Avoid: not owned. Analyst target 95.99 HKD vs 46.48 HKD (+107%, 21 analysts); de-biased α +15.0% vs CAPM hurdle 7.3%. Downtrend -32% vs 200-day avg; 12-1 mom -14%; RSI 21. Quality z -0.99 (ROE 3%). ⚠️ oversold.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 98 | 1,346,000 KRW | $99,652 | 11.1% | Strong Buy |
| MU | Micron Technology | 92 | 903.70 USD | $83,140 | 9.3% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 221,500 KRW | $81,158 | 9.1% | Strong Buy |
| IFX.DE | Infineon Technologies | 1,301 | 50.48 EUR | $73,363 | 8.2% | Buy |
| AMAT | Applied Materials | 145 | 387.59 USD | $56,201 | 6.3% | Buy |
| TSM | TSMC | 127 | 424.39 USD | $53,897 | 6.0% | Buy |
| ASX | ASE Technology | 1,320 | 39.92 USD | $52,688 | 5.9% | Buy |
| ASML | ASML Holding | 30 | 1,590.18 USD | $47,705 | 5.3% | Hold |
| 6857.T | Advantest | 200 | 33,980 JPY | $43,119 | 4.8% | Hold |
| KLAC | KLA Corp | 268 | 149.22 USD | $39,991 | 4.5% | Hold |
| LRCX | Lam Research | 162 | 237.37 USD | $38,454 | 4.3% | Hold |
| NVDA | NVIDIA | 168 | 215.98 USD | $36,285 | 4.1% | Buy |
| AVGO | Broadcom | 100 | 329.28 USD | $32,928 | 3.7% | Hold |
| 8035.T | Tokyo Electron | 500 | 9,390 JPY | $29,789 | 3.3% | Hold |

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

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 39.2%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
