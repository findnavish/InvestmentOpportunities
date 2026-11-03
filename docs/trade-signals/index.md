---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-03 15:09 UTC (Tue Nov 03, 10:09 AM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🟢 open (Tue 10:09) · Tokyo 🔴 closed (Wed 00:09) · Korea 🔴 closed (Wed 00:09) · Hong Kong 🔴 closed (Tue 23:09) · Xetra 🟢 open (Tue 16:09) · Euronext Amsterdam 🟢 open (Tue 16:09)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$889,404** | $360,906 (41%) | $528,499 (59%) | -11.06% | -17.28% | 🔴 Risk-off (-2.0%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $889,404), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **NVDA**<br><small>NVIDIA</small> | 141 | 208.26 USD | $29,365 | Executed (paper) | quality +0.21 · momentum -0.20 |
| ADD | **MRVL**<br><small>Marvell Technology</small> | 50 | 172.03 USD | $8,601 | Executed (paper) | analyst α +0.27 · momentum +0.26 · ⚠️ oversold, rich valuation |
| ADD | **INTC**<br><small>Intel</small> | 106 | 62.03 USD | $6,576 | Executed (paper) | analyst α +0.41 · momentum +0.30 · ⚠️ oversold, rich valuation, high σ(e) |
| ADD | **AMAT**<br><small>Applied Materials</small> | 15 | 385.21 USD | $5,778 | Executed (paper) | analyst α +0.23 · momentum +0.14 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.15 | **SK hynix**<br><small>000660.KS</small> | 1,397,000 KRW | +125% | +16.7% | +282% | -7% | 45 | +0.62 | 9.4% → 8.9% | – | analyst α +0.66 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.42 | **MU**<br><small>Micron Technology</small> | 861.12 USD | +77% | +4.7% | +376% | +15% | 41 | +0.12 | 6.2% → 7.1% | – | momentum +0.53 · analyst α +0.31 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.46 | **Samsung**<br><small>005930.KS</small> | 220,000 KRW | +117% | +15.6% | +187% | -6% | 43 | -0.26 | 5.9% → 6.1% | – | analyst α +0.55 · momentum +0.23 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.04 | **MRVL**<br><small>Marvell Technology</small> | 172.03 USD | +71% | +3.2% | +190% | -7% | 29 | -0.12 | 3.2% → 3.2% | ADD 50 | analyst α +0.27 · momentum +0.26 · ⚠️ oversold, rich valuation |
| 🟢 Buy | +0.67 | **AMAT**<br><small>Applied Materials</small> | 385.21 USD | +66% | +2.7% | +134% | -13% | 37 | +0.03 | 2.7% → 2.7% | ADD 15 | analyst α +0.23 · momentum +0.14 |
| 🟢 Buy | +0.61 | **INTC**<br><small>Intel</small> | 62.03 USD | +88% | +7.4% | +191% | -29% | 25 | -0.62 | 1.6% → 1.6% | ADD 106 | analyst α +0.41 · momentum +0.30 · ⚠️ oversold, rich valuation, high σ(e) |
| 🟢 Buy | +0.29 | **NVDA**<br><small>NVIDIA</small> | 208.26 USD | +57% | -0.1% | +18% | +2% | 41 | +0.47 | 1.4% → 1.4% | TRIM 141 | quality +0.21 · momentum -0.20 |
| 🟢 Buy | +0.29 | **ASX**<br><small>ASE Technology</small> | 39.39 USD | +29% | -3.2% | +200% | +18% | 44 | -0.68 | 1.4% → 1.3% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| ⚪ Hold | +0.22 | **Infineon**<br><small>IFX.DE</small> | 52.55 EUR | +65% | +1.9% | +87% | -8% | 45 | -0.04 | 1.5% → 1.5% | – | analyst α +0.12 · momentum +0.05 |
| ⚪ Hold | +0.20 | **TSM**<br><small>TSMC</small> | 405.57 USD | +36% | -4.4% | +63% | +2% | 40 | +0.58 | 5.8% → 5.8% | – | quality +0.28 · analyst α -0.15 |
| ⚪ Hold | +0.12 | **LRCX**<br><small>Lam Research</small> | 232.57 USD | +61% | +1.3% | +121% | -18% | 34 | +0.02 | 4.2% → 4.2% | – | trend -0.12 · momentum +0.10 |
| ⚪ Hold | +0.10 | **Advantest**<br><small>6857.T</small> | 35,860 JPY | +19% | -9.5% | +121% | +23% | 52 | +0.33 | 5.1% → 5.1% | – | analyst α -0.55 · trend +0.32 · ⚠️ rich valuation |
| ⚪ Hold | -0.01 | **TER**<br><small>Teradyne</small> | 271.84 USD | +64% | +2.1% | +145% | -22% | 31 | -0.31 | 1.1% → 1.1% | – | quality -0.21 · analyst α +0.19 |
| ⚪ Hold | -0.05 | **KLAC**<br><small>KLA Corp</small> | 155.73 USD | +50% | -1.1% | +72% | -14% | 40 | +0.51 | 4.7% → 4.7% | – | quality +0.24 · trend -0.10 |
| ⚪ Hold | -0.11 | **ASML**<br><small>ASML Holding</small> | 1,565.56 USD | +34% | -5.4% | +76% | -2% | 41 | +0.42 | 5.3% → 5.3% | – | analyst α -0.27 · quality +0.18 |
| ⚪ Hold | -0.12 | **GFS**<br><small>GlobalFoundries</small> | 43.29 USD | +76% | +4.9% | +37% | -21% | 42 | -0.21 | 0.0% → 0.0% | – | analyst α +0.36 · momentum -0.14 |
| ⚪ Hold | -0.23 | **Tokyo Electron**<br><small>8035.T</small> | 10,105 JPY | +51% | -1.1% | +96% | -2% | 46 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · momentum +0.07 |
| ⚪ Hold | -0.24 | **AMD**<br><small>Advanced Micro Devices</small> | 489.89 USD | +26% | -8.1% | +147% | +19% | 40 | -0.15 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.21 |
| 🔴 Sell | -0.43 | **ASMI**<br><small>ASM.AS</small> | 728.00 EUR | +55% | -0.4% | +75% | -10% | 41 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · trend -0.06 |
| 🔴 Sell | -0.47 | **Disco**<br><small>6146.T</small> | 50,380 JPY | +62% | +1.9% | +13% | -23% | 41 | +0.06 | 0.0% → 0.0% | – | momentum -0.23 · trend -0.18 |
| 🔴 Sell | -0.65 | **ARM**<br><small>Arm Holdings</small> | 203.47 USD | +42% | -5.4% | +78% | -11% | 36 | +0.04 | 0.0% → 0.0% | – | analyst α -0.23 · trend -0.07 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.66 | **AVGO**<br><small>Broadcom</small> | 333.69 USD | +59% | +1.2% | -1% | -9% | 46 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.11 |
| 🔴 Sell | -0.67 | **AMKR**<br><small>Amkor Technology</small> | 38.49 USD | +98% | +10.3% | +70% | -33% | 38 | -1.00 | 0.0% → 0.0% | – | analyst α +0.48 · quality -0.43 |
| 🔴🔴 Strong Sell | -0.75 | **SMIC**<br><small>0981.HK</small> | 42.62 HKD | +125% | +18.5% | -19% | -37% | 23 | -0.99 | 0.0% → 0.0% | – | analyst α +0.85 · momentum -0.53 · ⚠️ oversold |
| 🔴🔴 Strong Sell | -0.83 | **QCOM**<br><small>Qualcomm</small> | 161.74 USD | +20% | -8.4% | +2% | -4% | 37 | +0.70 | 0.0% → 0.0% | – | analyst α -0.48 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.97 | **SNPS**<br><small>Synopsys</small> | 455.71 USD | +25% | -7.3% | +8% | +3% | 49 | +0.14 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.26 |
| 🔴🔴 Strong Sell | -0.99 | **CDNS**<br><small>Cadence Design Systems</small> | 314.86 USD | +29% | -6.3% | +4% | -4% | 43 | +0.31 | 0.0% → 0.0% | – | analyst α -0.31 · momentum -0.30 |
| 🔴🔴 Strong Sell | -1.09 | **TXN**<br><small>Texas Instruments</small> | 309.53 USD | +5% | -12.0% | +86% | +20% | 66 | +0.24 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.25 |
| 🔴🔴 Strong Sell | -1.10 | **Shin-Etsu**<br><small>4063.T</small> | 5,906 JPY | +31% | -5.4% | +25% | -7% | 47 | -0.20 | 0.0% → 0.0% | – | analyst α -0.19 · momentum -0.17 |
| 🔴🔴 Strong Sell | -1.23 | **ENTG**<br><small>Entegris</small> | 157.87 USD | +10% | -11.2% | +83% | +14% | 55 | -0.02 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.14 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.15"
    Within rebalance band of target 8.9%: no trade. Analyst target 3,141,025 KRW vs 1,397,000 KRW (+125%, 38 analysts); de-biased α +16.7% vs CAPM hurdle 14.3%. Downtrend -7% vs 200-day avg; 12-1 mom +282%; RSI 45. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.42"
    Within rebalance band of target 7.1%: no trade. Analyst target 1,520.02 USD vs 861.12 USD (+77%, 46 analysts); de-biased α +4.7% vs CAPM hurdle 14.0%. Uptrend +15% vs 200-day avg; 12-1 mom +376%; RSI 41. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.46"
    Within rebalance band of target 6.1%: no trade. Analyst target 477,517 KRW vs 220,000 KRW (+117%, 36 analysts); de-biased α +15.6% vs CAPM hurdle 11.3%. Downtrend -6% vs 200-day avg; 12-1 mom +187%; RSI 43. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.04"
    **ADD 50 sh** → target 3.2% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 293.88 USD vs 172.03 USD (+71%, 43 analysts); de-biased α +3.2% vs CAPM hurdle 14.1%. Downtrend -7% vs 200-day avg; 12-1 mom +190%; RSI 29. Quality z -0.12 (ROE 19%). ⚠️ oversold; price implies 78% stage-1 growth (reverse DCF).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.67"
    **ADD 15 sh** → target 2.7% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 385.21 USD (+66%, 36 analysts); de-biased α +2.7% vs CAPM hurdle 11.6%. Downtrend -13% vs 200-day avg; 12-1 mom +134%; RSI 37. Quality z +0.03 (ROE 36%).

??? success "INTC (INTC) — 🟢 Buy, score +0.61"
    **ADD 106 sh** → target 1.6% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 116.37 USD vs 62.03 USD (+88%, 43 analysts); de-biased α +7.4% vs CAPM hurdle 14.0%. Downtrend -29% vs 200-day avg; 12-1 mom +191%; RSI 25. Quality z -0.62 (ROE -0%). ⚠️ oversold; price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "NVDA (NVDA) — 🟢 Buy, score +0.29"
    **TRIM 141 sh** → target 1.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 327.70 USD vs 208.26 USD (+57%, 59 analysts); de-biased α -0.1% vs CAPM hurdle 13.9%. Uptrend +2% vs 200-day avg; 12-1 mom +18%; RSI 41. Quality z +0.47 (ROE 101%).

??? success "ASX (ASX) — 🟢 Buy, score +0.29"
    Within rebalance band of target 1.3%: no trade. Analyst target 51.00 USD vs 39.39 USD (+29%, 1 analysts); de-biased α -3.2% vs CAPM hurdle 11.9%. Uptrend +18% vs 200-day avg; 12-1 mom +200%; RSI 44. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? note "Infineon (IFX.DE) — ⚪ Hold, score +0.22"
    Hold zone: keep any existing position, no new money. Analyst target 86.74 EUR vs 52.55 EUR (+65%, 23 analysts); de-biased α +1.9% vs CAPM hurdle 14.1%. Downtrend -8% vs 200-day avg; 12-1 mom +87%; RSI 45. Quality z -0.04 (ROE 6%).

??? note "TSM (TSM) — ⚪ Hold, score +0.20"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 405.57 USD (+36%, 20 analysts); de-biased α -4.4% vs CAPM hurdle 10.8%. Uptrend +2% vs 200-day avg; 12-1 mom +63%; RSI 40. Quality z +0.58 (ROE 35%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.12"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 232.57 USD (+61%, 31 analysts); de-biased α +1.3% vs CAPM hurdle 12.6%. Downtrend -18% vs 200-day avg; 12-1 mom +121%; RSI 34. Quality z +0.02 (ROE 65%).

??? note "Advantest (6857.T) — ⚪ Hold, score +0.10"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 35,860 JPY (+19%, 21 analysts); de-biased α -9.5% vs CAPM hurdle 13.4%. Uptrend +23% vs 200-day avg; 12-1 mom +121%; RSI 52. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "TER (TER) — ⚪ Hold, score -0.01"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 271.84 USD (+64%, 15 analysts); de-biased α +2.1% vs CAPM hurdle 12.3%. Downtrend -22% vs 200-day avg; 12-1 mom +145%; RSI 31. Quality z -0.31 (ROE 20%).

??? note "KLAC (KLAC) — ⚪ Hold, score -0.05"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 155.73 USD (+50%, 26 analysts); de-biased α -1.1% vs CAPM hurdle 11.1%. Downtrend -14% vs 200-day avg; 12-1 mom +72%; RSI 40. Quality z +0.51 (ROE 87%).

??? note "ASML (ASML) — ⚪ Hold, score -0.11"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,565.56 USD (+34%, 16 analysts); de-biased α -5.4% vs CAPM hurdle 12.3%. Downtrend -2% vs 200-day avg; 12-1 mom +76%; RSI 41. Quality z +0.42 (ROE 50%).

??? note "GFS (GFS) — ⚪ Hold, score -0.12"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 43.29 USD (+76%, 22 analysts); de-biased α +4.9% vs CAPM hurdle 12.4%. Downtrend -21% vs 200-day avg; 12-1 mom +37%; RSI 42. Quality z -0.21 (ROE 8%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score -0.23"
    Hold zone: not owned, no entry. Analyst target 15,275 JPY vs 10,105 JPY (+51%, 23 analysts); de-biased α -1.1% vs CAPM hurdle 12.8%. Downtrend -2% vs 200-day avg; 12-1 mom +96%; RSI 46. Quality z -0.28 (ROE 29%).

??? note "AMD (AMD) — ⚪ Hold, score -0.24"
    Hold zone: not owned, no entry. Analyst target 619.51 USD vs 489.89 USD (+26%, 50 analysts); de-biased α -8.1% vs CAPM hurdle 14.9%. Uptrend +19% vs 200-day avg; 12-1 mom +147%; RSI 40. Quality z -0.15 (ROE 7%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.43"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 728.00 EUR (+55%, 19 analysts); de-biased α -0.4% vs CAPM hurdle 13.2%. Downtrend -10% vs 200-day avg; 12-1 mom +75%; RSI 41. Quality z -0.10 (ROE 19%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.47"
    Avoid: not owned. Analyst target 81,730 JPY vs 50,380 JPY (+62%, 20 analysts); de-biased α +1.9% vs CAPM hurdle 11.5%. Downtrend -23% vs 200-day avg; 12-1 mom +13%; RSI 41. Quality z +0.06 (ROE 25%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.65"
    Avoid: not owned. Analyst target 288.70 USD vs 203.47 USD (+42%, 40 analysts); de-biased α -5.4% vs CAPM hurdle 19.6%. Downtrend -11% vs 200-day avg; 12-1 mom +78%; RSI 36. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "AVGO (AVGO) — 🔴 Sell, score -0.66"
    Avoid: not owned. Analyst target 531.31 USD vs 333.69 USD (+59%, 47 analysts); de-biased α +1.2% vs CAPM hurdle 11.2%. Downtrend -9% vs 200-day avg; 12-1 mom -1%; RSI 46. Quality z +0.26 (ROE 31%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.67"
    Avoid: not owned. Analyst target 76.40 USD vs 38.49 USD (+98%, 10 analysts); de-biased α +10.3% vs CAPM hurdle 14.0%. Downtrend -33% vs 200-day avg; 12-1 mom +70%; RSI 38. Quality z -1.00 (ROE 9%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -0.75"
    Avoid: not owned. Analyst target 95.99 HKD vs 42.62 HKD (+125%, 21 analysts); de-biased α +18.5% vs CAPM hurdle 7.3%. Downtrend -37% vs 200-day avg; 12-1 mom -19%; RSI 23. Quality z -0.99 (ROE 3%). ⚠️ oversold.

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.83"
    Avoid: not owned. Analyst target 194.13 USD vs 161.74 USD (+20%, 30 analysts); de-biased α -8.4% vs CAPM hurdle 11.9%. Downtrend -4% vs 200-day avg; 12-1 mom +2%; RSI 37. Quality z +0.70 (ROE 23%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.97"
    Avoid: not owned. Analyst target 569.78 USD vs 455.71 USD (+25%, 26 analysts); de-biased α -7.3% vs CAPM hurdle 10.3%. Uptrend +3% vs 200-day avg; 12-1 mom +8%; RSI 49. Quality z +0.14 (ROE 7%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -0.99"
    Avoid: not owned. Analyst target 405.47 USD vs 314.86 USD (+29%, 26 analysts); de-biased α -6.3% vs CAPM hurdle 10.0%. Downtrend -4% vs 200-day avg; 12-1 mom +4%; RSI 43. Quality z +0.31 (ROE 22%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -1.09"
    Avoid: not owned. Analyst target 324.71 USD vs 309.53 USD (+5%, 31 analysts); de-biased α -12.0% vs CAPM hurdle 10.8%. Uptrend +20% vs 200-day avg; 12-1 mom +86%; RSI 66. Quality z +0.24 (ROE 30%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.10"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,906 JPY (+31%, 17 analysts); de-biased α -5.4% vs CAPM hurdle 10.8%. Downtrend -7% vs 200-day avg; 12-1 mom +25%; RSI 47. Quality z -0.20 (ROE 10%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -1.23"
    Avoid: not owned. Analyst target 173.36 USD vs 157.87 USD (+10%, 11 analysts); de-biased α -11.2% vs CAPM hurdle 11.0%. Uptrend +14% vs 200-day avg; 12-1 mom +83%; RSI 55. Quality z -0.02 (ROE 6%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 80 | 1,397,000 KRW | $83,218 | 9.4% | Strong Buy |
| MU | Micron Technology | 64 | 861.12 USD | $55,112 | 6.2% | Strong Buy |
| 005930.KS | Samsung Electronics | 322 | 220,000 KRW | $52,748 | 5.9% | Strong Buy |
| TSM | TSMC | 127 | 405.57 USD | $51,507 | 5.8% | Hold |
| ASML | ASML Holding | 30 | 1,565.56 USD | $46,967 | 5.3% | Hold |
| 6857.T | Advantest | 200 | 35,860 JPY | $45,262 | 5.1% | Hold |
| KLAC | KLA Corp | 268 | 155.73 USD | $41,736 | 4.7% | Hold |
| LRCX | Lam Research | 162 | 232.57 USD | $37,676 | 4.2% | Hold |
| MRVL | Marvell Technology | 164 | 172.03 USD | $28,213 | 3.2% | Strong Buy |
| AMAT | Applied Materials | 62 | 385.21 USD | $23,883 | 2.7% | Buy |
| INTC | Intel | 236 | 62.03 USD | $14,640 | 1.6% | Buy |
| IFX.DE | Infineon Technologies | 225 | 52.55 EUR | $13,236 | 1.5% | Hold |
| NVDA | NVIDIA | 60 | 208.26 USD | $12,496 | 1.4% | Buy |
| ASX | ASE Technology | 312 | 39.39 USD | $12,290 | 1.4% | Buy |
| TER | Teradyne | 35 | 271.84 USD | $9,514 | 1.1% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-11-03 15:09 UTC | ADD | INTC | 106 | 62.03 | $6,576 |
| 2026-11-03 15:09 UTC | ADD | MRVL | 50 | 172.03 | $8,602 |
| 2026-11-03 15:09 UTC | ADD | AMAT | 15 | 385.21 | $5,778 |
| 2026-11-03 15:09 UTC | TRIM | NVDA | -141 | 208.26 | $29,365 |
| 2026-11-02 15:55 UTC | BUY (new) | TER | 35 | 270.99 | $9,485 |
| 2026-11-02 15:55 UTC | ADD | MRVL | 35 | 184.11 | $6,444 |
| 2026-11-02 15:55 UTC | TRIM | IFX.DE | -1,076 | 52.66 | $63,473 |
| 2026-11-02 06:06 UTC | TRIM | 000660.KS | -18 | 1,490,500.00 | $20,008 |
| 2026-11-02 06:06 UTC | TRIM | 005930.KS | -163 | 231,750.00 | $28,171 |
| 2026-11-02 06:06 UTC | SELL (exit) | 8035.T | -500 | 10,115.00 | $32,062 |
| 2026-10-30 19:24 UTC | TRIM | MU | -28 | 866.70 | $24,267 |
| 2026-10-30 19:24 UTC | TRIM | AMAT | -65 | 385.15 | $25,035 |
| 2026-10-30 19:24 UTC | TRIM | MRVL | -139 | 193.20 | $26,855 |
| 2026-10-30 19:24 UTC | TRIM | INTC | -391 | 63.40 | $24,787 |
| 2026-10-30 19:24 UTC | TRIM | ASX | -1,008 | 38.89 | $39,201 |
| 2026-10-30 14:10 UTC | BUY (new) | INTC | 521 | 65.38 | $34,063 |
| 2026-10-30 14:10 UTC | TRIM | AMAT | -33 | 399.62 | $13,187 |
| 2026-10-29 14:21 UTC | BUY (new) | MRVL | 218 | 219.82 | $47,921 |
| 2026-10-29 14:21 UTC | TRIM | NVDA | -84 | 213.56 | $17,939 |
| 2026-10-29 14:21 UTC | SELL (exit) | AVGO | -100 | 342.58 | $34,258 |
| 2026-10-28 16:04 UTC | ADD | NVDA | 117 | 217.19 | $25,411 |
| 2026-10-26 19:22 UTC | TRIM | AMAT | -57 | 391.16 | $22,296 |
| 2026-10-26 19:22 UTC | TRIM | NVDA | -58 | 216.65 | $12,566 |
| 2026-10-26 19:22 UTC | TRIM | ASX | -395 | 40.15 | $15,859 |
| 2026-10-26 06:15 UTC | ADD | 6857.T | 100 | 31,220.00 | $19,871 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 43.9%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
