---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-12 17:56 UTC (Mon Oct 12, 01:56 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🟢 open (Mon 13:56) · Tokyo 🔴 closed (Tue 02:56) · Korea 🔴 closed (Tue 02:56) · Hong Kong 🔴 closed (Tue 01:56) · Xetra 🔴 closed (Mon 19:56) · Euronext Amsterdam 🔴 closed (Mon 19:56)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$999,708** | $108,999 (11%) | $890,708 (89%) | -0.03% | -3.69% | 🟢 Risk-on (+17.6%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $999,708), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| SELL (exit) | **Advantest**<br><small>6857.T</small> | 200 | 41,560 JPY | $52,388 | Queued · Tokyo closed | analyst α -0.85 · trend +0.18 · ⚠️ rich valuation |
| ADD | **KLAC**<br><small>KLA Corp</small> | 153 | 190.68 USD | $29,174 | Executed (paper) | quality +0.24 · trend -0.09 |
| ADD | **AMAT**<br><small>Applied Materials</small> | 41 | 497.22 USD | $20,386 | Executed (paper) | analyst α +0.12 · momentum +0.10 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.33 | **SK hynix**<br><small>000660.KS</small> | 1,613,000 KRW | +95% | +15.4% | +395% | +12% | 40 | +0.62 | 8.9% → 10.0% | – | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.34 | **MU**<br><small>Micron Technology</small> | 991.44 USD | +53% | +5.1% | +408% | +41% | 45 | +0.12 | 9.1% → 10.0% | – | momentum +0.53 · analyst α +0.36 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.60 | **Samsung**<br><small>005930.KS</small> | 251,250 KRW | +90% | +15.1% | +223% | +9% | 42 | -0.26 | 9.1% → 10.0% | – | analyst α +0.66 · momentum +0.30 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.62 | **AMAT**<br><small>Applied Materials</small> | 497.22 USD | +29% | -0.5% | +108% | +14% | 51 | +0.03 | 10.0% → 10.0% | ADD 41 | analyst α +0.12 · momentum +0.10 |
| 🟢 Buy | +0.56 | **TSM**<br><small>TSMC</small> | 446.65 USD | +24% | -1.4% | +46% | +14% | 49 | +0.58 | 8.4% → 10.0% | – | quality +0.28 · momentum -0.12 |
| 🟢 Buy | +0.43 | **NVDA**<br><small>NVIDIA</small> | 226.46 USD | +45% | +3.0% | +14% | +12% | 50 | +0.47 | 8.4% → 8.8% | – | analyst α +0.23 · momentum -0.23 |
| 🟢 Buy | +0.41 | **ASX**<br><small>ASE Technology</small> | 47.03 USD | +8% | -2.7% | +240% | +50% | 64 | -0.68 | 7.1% → 7.7% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.38 | **KLAC**<br><small>KLA Corp</small> | 190.68 USD | +23% | -1.8% | +72% | +6% | 49 | +0.51 | 7.1% → 7.1% | ADD 153 | quality +0.24 · trend -0.09 |
| 🟢 Buy | +0.34 | **Infineon**<br><small>IFX.DE</small> | 57.32 EUR | +51% | +4.7% | +81% | +2% | 46 | -0.04 | 6.2% → 6.9% | – | analyst α +0.27 · trend -0.12 |
| ⚪ Hold | +0.24 | **ASML**<br><small>ASML Holding</small> | 1,758.96 USD | +19% | -2.9% | +74% | +13% | 50 | +0.42 | 0.0% → 0.0% | – | quality +0.18 · analyst α -0.12 |
| ⚪ Hold | +0.06 | **LRCX**<br><small>Lam Research</small> | 310.80 USD | +21% | -2.7% | +112% | +11% | 47 | +0.02 | 0.0% → 0.0% | – | momentum +0.12 · analyst α -0.05 |
| ⚪ Hold | +0.03 | **Tokyo Electron**<br><small>8035.T</small> | 12,430 JPY | +23% | -2.0% | +107% | +26% | 62 | -0.28 | 4.7% → 4.7% | – | quality -0.18 · trend +0.14 |
| ⚪ Hold | -0.05 | **AVGO**<br><small>Broadcom</small> | 355.80 USD | +49% | +5.0% | +6% | -3% | 47 | +0.26 | 4.8% → 4.8% | – | analyst α +0.31 · momentum -0.30 |
| ⚪ Hold | -0.08 | **MRVL**<br><small>Marvell Technology</small> | 266.36 USD | +10% | -5.7% | +161% | +54% | 56 | -0.12 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.32 · ⚠️ rich valuation |
| ⚪ Hold | -0.15 | **GFS**<br><small>GlobalFoundries</small> | 48.59 USD | +56% | +6.3% | +33% | -11% | 52 | -0.21 | 0.0% → 0.0% | – | analyst α +0.41 · trend -0.21 |
| ⚪ Hold | -0.22 | **TXN**<br><small>Texas Instruments</small> | 281.55 USD | +15% | -3.2% | +54% | +12% | 53 | +0.24 | 0.0% → 0.0% | – | analyst α -0.15 · quality +0.10 |
| ⚪ Hold | -0.23 | **ASMI**<br><small>ASM.AS</small> | 878.20 EUR | +29% | -0.9% | +52% | +9% | 52 | -0.10 | 0.0% → 0.0% | – | analyst α +0.08 · momentum -0.07 |
| 🔴 Sell | -0.30 | **Disco**<br><small>6146.T</small> | 61,250 JPY | +33% | +0.9% | +16% | -6% | 58 | +0.06 | 0.0% → 0.0% | – | momentum -0.20 · analyst α +0.19 |
| 🔴 Sell | -0.38 | **TER**<br><small>Teradyne</small> | 385.24 USD | +16% | -3.8% | +162% | +13% | 47 | -0.31 | 0.0% → 0.0% | – | analyst α -0.23 · momentum +0.23 |
| 🔴 Sell | -0.44 | **AMKR**<br><small>Amkor Technology</small> | 48.06 USD | +59% | +6.6% | +70% | -16% | 41 | -1.00 | 0.0% → 0.0% | – | analyst α +0.48 · quality -0.43 |
| 🔴 Sell | -0.47 | **INTC**<br><small>Intel</small> | 101.03 USD | +15% | -4.5% | +172% | +21% | 40 | -0.62 | 0.0% → 0.0% | – | analyst α -0.36 · momentum +0.26 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.52 | **QCOM**<br><small>Qualcomm</small> | 173.57 USD | +12% | -4.3% | +12% | +3% | 43 | +0.70 | 0.0% → 0.0% | – | quality +0.43 · analyst α -0.31 |
| 🔴 Sell | -0.56 | **Shin-Etsu**<br><small>4063.T</small> | 6,110 JPY | +27% | -0.3% | +21% | -2% | 55 | -0.20 | 0.0% → 0.0% | – | momentum -0.17 · analyst α +0.15 |
| 🔴 Sell | -0.73 | **Advantest**<br><small>6857.T</small> | 41,560 JPY | +3% | -7.4% | +134% | +48% | 71 | +0.33 | 5.2% → 0.0% | SELL 200 | analyst α -0.85 · trend +0.18 · ⚠️ rich valuation |
| 🔴🔴 Strong Sell | -0.77 | **AMD**<br><small>Advanced Micro Devices</small> | 590.45 USD | +5% | -7.2% | +122% | +52% | 52 | -0.15 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.25 |
| 🔴🔴 Strong Sell | -0.92 | **ENTG**<br><small>Entegris</small> | 160.03 USD | +8% | -5.4% | +49% | +19% | 58 | -0.02 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.10 |
| 🔴🔴 Strong Sell | -1.00 | **CDNS**<br><small>Cadence Design Systems</small> | 351.98 USD | +15% | -3.5% | -17% | +8% | 65 | +0.31 | 0.0% → 0.0% | – | momentum -0.35 · analyst α -0.19 |
| 🔴🔴 Strong Sell | -1.00 | **ARM**<br><small>Arm Holdings</small> | 255.65 USD | +13% | -6.4% | +55% | +16% | 41 | +0.04 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.09 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.18 | **SNPS**<br><small>Synopsys</small> | 503.19 USD | +13% | -4.0% | -18% | +13% | 71 | +0.14 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.27 |
| 🔴🔴 Strong Sell | -1.33 | **SMIC**<br><small>0981.HK</small> | 56.20 HKD | +71% | +11.1% | -20% | -19% | 31 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.53 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.33"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,613,000 KRW (+95%, 38 analysts); de-biased α +15.4% vs CAPM hurdle 14.3%. Uptrend +12% vs 200-day avg; 12-1 mom +395%; RSI 40. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.34"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 991.44 USD (+53%, 46 analysts); de-biased α +5.1% vs CAPM hurdle 14.0%. Uptrend +41% vs 200-day avg; 12-1 mom +408%; RSI 45. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.60"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 251,250 KRW (+90%, 36 analysts); de-biased α +15.1% vs CAPM hurdle 11.3%. Uptrend +9% vs 200-day avg; 12-1 mom +223%; RSI 42. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.62"
    **ADD 41 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 497.22 USD (+29%, 36 analysts); de-biased α -0.5% vs CAPM hurdle 11.6%. Uptrend +14% vs 200-day avg; 12-1 mom +108%; RSI 51. Quality z +0.03 (ROE 36%).

??? success "TSM (TSM) — 🟢 Buy, score +0.56"
    Within rebalance band of target 10.0%: no trade. Analyst target 552.26 USD vs 446.65 USD (+24%, 20 analysts); de-biased α -1.4% vs CAPM hurdle 10.8%. Uptrend +14% vs 200-day avg; 12-1 mom +46%; RSI 49. Quality z +0.58 (ROE 35%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.43"
    Within rebalance band of target 8.8%: no trade. Analyst target 327.70 USD vs 226.46 USD (+45%, 59 analysts); de-biased α +3.0% vs CAPM hurdle 13.9%. Uptrend +12% vs 200-day avg; 12-1 mom +14%; RSI 50. Quality z +0.47 (ROE 101%).

??? success "ASX (ASX) — 🟢 Buy, score +0.41"
    Within rebalance band of target 7.7%: no trade. Analyst target 51.00 USD vs 47.03 USD (+8%, 1 analysts); de-biased α -2.7% vs CAPM hurdle 11.9%. Uptrend +50% vs 200-day avg; 12-1 mom +240%; RSI 64. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "KLAC (KLAC) — 🟢 Buy, score +0.38"
    **ADD 153 sh** → target 7.1% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 233.77 USD vs 190.68 USD (+23%, 26 analysts); de-biased α -1.8% vs CAPM hurdle 11.1%. Uptrend +6% vs 200-day avg; 12-1 mom +72%; RSI 49. Quality z +0.51 (ROE 87%).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.34"
    Within rebalance band of target 6.9%: no trade. Analyst target 86.74 EUR vs 57.32 EUR (+51%, 23 analysts); de-biased α +4.7% vs CAPM hurdle 14.1%. Uptrend +2% vs 200-day avg; 12-1 mom +81%; RSI 46. Quality z -0.04 (ROE 6%).

??? note "ASML (ASML) — ⚪ Hold, score +0.24"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,758.96 USD (+19%, 16 analysts); de-biased α -2.9% vs CAPM hurdle 12.3%. Uptrend +13% vs 200-day avg; 12-1 mom +74%; RSI 50. Quality z +0.42 (ROE 50%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.06"
    Hold zone: not owned, no entry. Analyst target 375.06 USD vs 310.80 USD (+21%, 31 analysts); de-biased α -2.7% vs CAPM hurdle 12.6%. Uptrend +11% vs 200-day avg; 12-1 mom +112%; RSI 47. Quality z +0.02 (ROE 65%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.03"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 12,430 JPY (+23%, 23 analysts); de-biased α -2.0% vs CAPM hurdle 12.8%. Uptrend +26% vs 200-day avg; 12-1 mom +107%; RSI 62. Quality z -0.28 (ROE 29%).

??? note "AVGO (AVGO) — ⚪ Hold, score -0.05"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 355.80 USD (+49%, 47 analysts); de-biased α +5.0% vs CAPM hurdle 11.2%. Downtrend -3% vs 200-day avg; 12-1 mom +6%; RSI 47. Quality z +0.26 (ROE 31%).

??? note "MRVL (MRVL) — ⚪ Hold, score -0.08"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 266.36 USD (+10%, 43 analysts); de-biased α -5.7% vs CAPM hurdle 14.1%. Uptrend +54% vs 200-day avg; 12-1 mom +161%; RSI 56. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "GFS (GFS) — ⚪ Hold, score -0.15"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 48.59 USD (+56%, 22 analysts); de-biased α +6.3% vs CAPM hurdle 12.4%. Downtrend -11% vs 200-day avg; 12-1 mom +33%; RSI 52. Quality z -0.21 (ROE 8%).

??? note "TXN (TXN) — ⚪ Hold, score -0.22"
    Hold zone: not owned, no entry. Analyst target 324.71 USD vs 281.55 USD (+15%, 31 analysts); de-biased α -3.2% vs CAPM hurdle 10.8%. Uptrend +12% vs 200-day avg; 12-1 mom +54%; RSI 53. Quality z +0.24 (ROE 30%).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.23"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 878.20 EUR (+29%, 19 analysts); de-biased α -0.9% vs CAPM hurdle 13.2%. Uptrend +9% vs 200-day avg; 12-1 mom +52%; RSI 52. Quality z -0.10 (ROE 19%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.30"
    Avoid: not owned. Analyst target 81,730 JPY vs 61,250 JPY (+33%, 20 analysts); de-biased α +0.9% vs CAPM hurdle 11.5%. Downtrend -6% vs 200-day avg; 12-1 mom +16%; RSI 58. Quality z +0.06 (ROE 25%).

??? failure "TER (TER) — 🔴 Sell, score -0.38"
    Avoid: not owned. Analyst target 446.47 USD vs 385.24 USD (+16%, 15 analysts); de-biased α -3.8% vs CAPM hurdle 12.3%. Uptrend +13% vs 200-day avg; 12-1 mom +162%; RSI 47. Quality z -0.31 (ROE 20%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.44"
    Avoid: not owned. Analyst target 76.40 USD vs 48.06 USD (+59%, 10 analysts); de-biased α +6.6% vs CAPM hurdle 14.0%. Downtrend -16% vs 200-day avg; 12-1 mom +70%; RSI 41. Quality z -1.00 (ROE 9%).

??? failure "INTC (INTC) — 🔴 Sell, score -0.47"
    Avoid: not owned. Analyst target 116.37 USD vs 101.03 USD (+15%, 43 analysts); de-biased α -4.5% vs CAPM hurdle 14.0%. Uptrend +21% vs 200-day avg; 12-1 mom +172%; RSI 40. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "QCOM (QCOM) — 🔴 Sell, score -0.52"
    Avoid: not owned. Analyst target 194.13 USD vs 173.57 USD (+12%, 30 analysts); de-biased α -4.3% vs CAPM hurdle 11.9%. Uptrend +3% vs 200-day avg; 12-1 mom +12%; RSI 43. Quality z +0.70 (ROE 23%).

??? failure "Shin-Etsu (4063.T) — 🔴 Sell, score -0.56"
    Avoid: not owned. Analyst target 7,763 JPY vs 6,110 JPY (+27%, 17 analysts); de-biased α -0.3% vs CAPM hurdle 10.8%. Downtrend -2% vs 200-day avg; 12-1 mom +21%; RSI 55. Quality z -0.20 (ROE 10%).

??? failure "Advantest (6857.T) — 🔴 Sell, score -0.73"
    **SELL (exit) 200 sh** → target 0.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 42,686 JPY vs 41,560 JPY (+3%, 21 analysts); de-biased α -7.4% vs CAPM hurdle 13.4%. Uptrend +48% vs 200-day avg; 12-1 mom +134%; RSI 71. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? failure "AMD (AMD) — 🔴🔴 Strong Sell, score -0.77"
    Avoid: not owned. Analyst target 619.51 USD vs 590.45 USD (+5%, 50 analysts); de-biased α -7.2% vs CAPM hurdle 14.9%. Uptrend +52% vs 200-day avg; 12-1 mom +122%; RSI 52. Quality z -0.15 (ROE 7%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.92"
    Avoid: not owned. Analyst target 173.36 USD vs 160.03 USD (+8%, 11 analysts); de-biased α -5.4% vs CAPM hurdle 11.0%. Uptrend +19% vs 200-day avg; 12-1 mom +49%; RSI 58. Quality z -0.02 (ROE 6%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.00"
    Avoid: not owned. Analyst target 405.47 USD vs 351.98 USD (+15%, 26 analysts); de-biased α -3.5% vs CAPM hurdle 10.0%. Uptrend +8% vs 200-day avg; 12-1 mom -17%; RSI 65. Quality z +0.31 (ROE 22%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.00"
    Avoid: not owned. Analyst target 288.70 USD vs 255.65 USD (+13%, 40 analysts); de-biased α -6.4% vs CAPM hurdle 19.6%. Uptrend +16% vs 200-day avg; 12-1 mom +55%; RSI 41. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.18"
    Avoid: not owned. Analyst target 569.78 USD vs 503.19 USD (+13%, 26 analysts); de-biased α -4.0% vs CAPM hurdle 10.3%. Uptrend +13% vs 200-day avg; 12-1 mom -18%; RSI 71. Quality z +0.14 (ROE 7%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.33"
    Avoid: not owned. Analyst target 95.99 HKD vs 56.20 HKD (+71%, 21 analysts); de-biased α +11.1% vs CAPM hurdle 7.3%. Downtrend -19% vs 200-day avg; 12-1 mom -20%; RSI 31. Quality z -0.99 (ROE 3%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| AMAT | Applied Materials | 201 | 497.22 USD | $99,941 | 10.0% | Buy |
| 005930.KS | Samsung Electronics | 485 | 251,250 KRW | $91,301 | 9.1% | Strong Buy |
| MU | Micron Technology | 92 | 991.44 USD | $91,212 | 9.1% | Strong Buy |
| 000660.KS | SK hynix | 74 | 1,613,000 KRW | $89,432 | 8.9% | Strong Buy |
| NVDA | NVIDIA | 371 | 226.46 USD | $84,017 | 8.4% | Buy |
| TSM | TSMC | 187 | 446.65 USD | $83,524 | 8.4% | Buy |
| ASX | ASE Technology | 1,509 | 47.03 USD | $70,968 | 7.1% | Buy |
| KLAC | KLA Corp | 372 | 190.68 USD | $70,933 | 7.1% | Buy |
| IFX.DE | Infineon Technologies | 974 | 57.32 EUR | $62,310 | 6.2% | Buy |
| 6857.T | Advantest | 200 | 41,560 JPY | $52,388 | 5.2% | Sell |
| AVGO | Broadcom | 134 | 355.80 USD | $47,678 | 4.8% | Hold |
| 8035.T | Tokyo Electron | 600 | 12,430 JPY | $47,005 | 4.7% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-10-12 17:56 UTC | ADD | KLAC | 153 | 190.68 | $29,174 |
| 2026-10-12 17:56 UTC | ADD | AMAT | 41 | 497.22 | $20,386 |
| 2026-10-09 16:14 UTC | TRIM | KLAC | -47 | 196.81 | $9,250 |
| 2026-10-09 09:06 UTC | TRIM | IFX.DE | -437 | 59.90 | $29,382 |
| 2026-10-08 16:29 UTC | ADD | AMAT | 32 | 522.02 | $16,705 |
| 2026-10-08 08:59 UTC | ADD | IFX.DE | 479 | 59.28 | $31,780 |
| 2026-10-07 16:29 UTC | TRIM | KLAC | -184 | 195.46 | $35,964 |
| 2026-10-06 17:12 UTC | ADD | KLAC | 189 | 198.10 | $37,441 |
| 2026-10-06 17:12 UTC | TRIM | AVGO | -36 | 377.64 | $13,595 |
| 2026-10-06 10:19 UTC | ADD | IFX.DE | 316 | 63.45 | $22,554 |
| 2026-10-05 16:01 UTC | TRIM | KLAC | -208 | 203.82 | $42,395 |
| 2026-10-02 18:25 UTC | ADD | AMAT | 37 | 538.40 | $19,921 |
| 2026-10-02 12:37 UTC | TRIM | IFX.DE | -589 | 62.56 | $41,458 |
| 2026-10-02 05:39 UTC | TRIM | 6857.T | -100 | 38,710.00 | $24,524 |
| 2026-10-01 19:32 UTC | BUY (new) | ASX | 1,509 | 44.67 | $67,415 |
| 2026-10-01 05:56 UTC | TRIM | 6857.T | -100 | 37,090.00 | $23,417 |
| 2026-10-01 05:56 UTC | TRIM | 8035.T | -100 | 12,505.00 | $7,895 |
| 2026-09-30 19:21 UTC | TRIM | NVDA | -76 | 230.81 | $17,541 |
| 2026-09-30 13:45 UTC | TRIM | IFX.DE | -347 | 59.55 | $23,474 |
| 2026-09-30 00:28 UTC | BUY (new) | 8035.T | 700 | 11,900.00 | $52,952 |
| 2026-09-29 15:53 UTC | BUY (new) | TSM | 187 | 457.37 | $85,528 |
| 2026-09-29 15:53 UTC | TRIM | AMAT | -87 | 501.81 | $43,657 |
| 2026-09-29 15:53 UTC | TRIM | AVGO | -112 | 357.74 | $40,067 |
| 2026-09-28 15:29 UTC | BUY (new) | AVGO | 282 | 349.88 | $98,666 |
| 2026-09-28 00:48 UTC | BUY (new) | 005930.KS | 485 | 280,750.00 | $100,255 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 19.1%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
