---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-13 00:41 UTC (Mon Oct 12, 08:41 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Mon 20:41) · Tokyo 🟢 open (Tue 09:41) · Korea 🟢 open (Tue 09:41) · Hong Kong 🔴 closed (Tue 08:41) · Xetra 🔴 closed (Tue 02:41) · Euronext Amsterdam 🔴 closed (Tue 02:41)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$984,267** | $108,999 (11%) | $875,267 (89%) | -1.57% | -3.66% | 🟢 Risk-on (+17.7%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $984,267), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **KLAC**<br><small>KLA Corp</small> | 67 | 190.12 USD | $12,738 | Queued · NYSE/Nasdaq closed | quality +0.24 · trend -0.06 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.25 | **SK hynix**<br><small>000660.KS</small> | 1,506,000 KRW | +109% | +18.5% | +395% | +5% | 34 | +0.62 | 8.5% → 10.0% | – | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.37 | **MU**<br><small>Micron Technology</small> | 988.97 USD | +54% | +4.8% | +408% | +40% | 45 | +0.12 | 9.2% → 10.0% | – | momentum +0.53 · analyst α +0.36 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.49 | **Samsung**<br><small>005930.KS</small> | 237,500 KRW | +101% | +17.4% | +223% | +4% | 37 | -0.26 | 8.8% → 10.0% | – | analyst α +0.66 · momentum +0.30 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.63 | **AMAT**<br><small>Applied Materials</small> | 497.53 USD | +28% | -0.8% | +108% | +14% | 51 | +0.03 | 10.2% → 9.2% | – | analyst α +0.12 · momentum +0.10 |
| 🟢 Buy | +0.50 | **TSM**<br><small>TSMC</small> | 444.58 USD | +24% | -1.6% | +46% | +14% | 48 | +0.58 | 8.4% → 10.0% | – | quality +0.28 · momentum -0.12 |
| 🟢 Buy | +0.46 | **NVDA**<br><small>NVIDIA</small> | 226.42 USD | +45% | +2.6% | +14% | +12% | 50 | +0.47 | 8.5% → 7.9% | – | analyst α +0.23 · momentum -0.23 |
| 🟢 Buy | +0.41 | **ASX**<br><small>ASE Technology</small> | 47.56 USD | +7% | -3.0% | +240% | +51% | 65 | -0.68 | 7.3% → 6.6% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.37 | **KLAC**<br><small>KLA Corp</small> | 190.12 USD | +23% | -2.1% | +72% | +6% | 49 | +0.51 | 7.2% → 5.9% | TRIM 67 | quality +0.24 · trend -0.06 |
| 🟢 Buy | +0.35 | **Infineon**<br><small>IFX.DE</small> | 57.32 EUR | +51% | +4.3% | +81% | +2% | 46 | -0.04 | 6.3% → 5.9% | – | analyst α +0.27 · trend -0.12 |
| ⚪ Hold | +0.20 | **Tokyo Electron**<br><small>8035.T</small> | 11,890 JPY | +28% | -0.9% | +107% | +21% | 55 | -0.28 | 4.6% → 4.6% | – | quality -0.18 · trend +0.12 |
| ⚪ Hold | +0.19 | **ASML**<br><small>ASML Holding</small> | 1,750.03 USD | +20% | -3.1% | +74% | +12% | 49 | +0.42 | 0.0% → 0.0% | – | quality +0.18 · analyst α -0.12 |
| ⚪ Hold | +0.09 | **LRCX**<br><small>Lam Research</small> | 309.64 USD | +21% | -2.9% | +112% | +11% | 47 | +0.02 | 0.0% → 0.0% | – | momentum +0.12 · analyst α -0.05 |
| ⚪ Hold | -0.05 | **AVGO**<br><small>Broadcom</small> | 354.77 USD | +50% | +4.7% | +6% | -3% | 47 | +0.26 | 4.8% → 4.8% | – | analyst α +0.31 · momentum -0.30 |
| ⚪ Hold | -0.08 | **MRVL**<br><small>Marvell Technology</small> | 265.91 USD | +11% | -6.0% | +161% | +54% | 55 | -0.12 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.32 · ⚠️ rich valuation |
| ⚪ Hold | -0.11 | **Advantest**<br><small>6857.T</small> | 39,690 JPY | +8% | -6.5% | +134% | +42% | 62 | +0.33 | 5.1% → 5.1% | – | analyst α -0.55 · trend +0.18 · ⚠️ rich valuation |
| ⚪ Hold | -0.15 | **GFS**<br><small>GlobalFoundries</small> | 48.35 USD | +57% | +6.1% | +33% | -11% | 51 | -0.21 | 0.0% → 0.0% | – | analyst α +0.41 · trend -0.21 |
| ⚪ Hold | -0.25 | **ASMI**<br><small>ASM.AS</small> | 878.20 EUR | +29% | -1.2% | +52% | +9% | 52 | -0.10 | 0.0% → 0.0% | – | momentum -0.07 · quality -0.06 |
| ⚪ Hold | -0.25 | **TXN**<br><small>Texas Instruments</small> | 281.97 USD | +15% | -3.6% | +54% | +13% | 54 | +0.24 | 0.0% → 0.0% | – | analyst α -0.19 · quality +0.10 |
| 🔴 Sell | -0.30 | **Disco**<br><small>6146.T</small> | 59,160 JPY | +38% | +1.7% | +16% | -9% | 52 | +0.06 | 0.0% → 0.0% | – | momentum -0.20 · analyst α +0.19 |
| 🔴 Sell | -0.41 | **TER**<br><small>Teradyne</small> | 383.82 USD | +16% | -4.1% | +162% | +12% | 47 | -0.31 | 0.0% → 0.0% | – | analyst α -0.23 · momentum +0.23 |
| 🔴 Sell | -0.44 | **INTC**<br><small>Intel</small> | 101.33 USD | +15% | -4.9% | +172% | +22% | 40 | -0.62 | 0.0% → 0.0% | – | analyst α -0.36 · momentum +0.26 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.44 | **AMKR**<br><small>Amkor Technology</small> | 48.13 USD | +59% | +6.2% | +70% | -16% | 41 | -1.00 | 0.0% → 0.0% | – | analyst α +0.48 · quality -0.43 |
| 🔴 Sell | -0.50 | **QCOM**<br><small>Qualcomm</small> | 174.45 USD | +11% | -4.8% | +12% | +4% | 44 | +0.70 | 0.0% → 0.0% | – | quality +0.43 · analyst α -0.31 |
| 🔴 Sell | -0.57 | **Shin-Etsu**<br><small>4063.T</small> | 6,077 JPY | +28% | -0.5% | +21% | -3% | 54 | -0.20 | 0.0% → 0.0% | – | momentum -0.17 · analyst α +0.15 |
| 🔴🔴 Strong Sell | -0.88 | **CDNS**<br><small>Cadence Design Systems</small> | 348.45 USD | +16% | -3.5% | -17% | +7% | 63 | +0.31 | 0.0% → 0.0% | – | momentum -0.35 · analyst α -0.15 |
| 🔴🔴 Strong Sell | -0.93 | **ENTG**<br><small>Entegris</small> | 160.01 USD | +8% | -5.7% | +49% | +19% | 58 | -0.02 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.10 |
| 🔴🔴 Strong Sell | -1.19 | **AMD**<br><small>Advanced Micro Devices</small> | 594.14 USD | +4% | -7.8% | +122% | +53% | 53 | -0.15 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.25 |
| 🔴🔴 Strong Sell | -1.20 | **SNPS**<br><small>Synopsys</small> | 502.51 USD | +13% | -4.4% | -18% | +13% | 71 | +0.14 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.27 |
| 🔴🔴 Strong Sell | -1.24 | **ARM**<br><small>Arm Holdings</small> | 255.05 USD | +13% | -6.7% | +55% | +15% | 41 | +0.04 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.09 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.34 | **SMIC**<br><small>0981.HK</small> | 56.20 HKD | +71% | +10.8% | -20% | -19% | 31 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.53 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.25"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,506,000 KRW (+109%, 38 analysts); de-biased α +18.5% vs CAPM hurdle 14.3%. Uptrend +5% vs 200-day avg; 12-1 mom +395%; RSI 34. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.37"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 988.97 USD (+54%, 46 analysts); de-biased α +4.8% vs CAPM hurdle 14.0%. Uptrend +40% vs 200-day avg; 12-1 mom +408%; RSI 45. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.49"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 237,500 KRW (+101%, 36 analysts); de-biased α +17.4% vs CAPM hurdle 11.3%. Uptrend +4% vs 200-day avg; 12-1 mom +223%; RSI 37. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.63"
    Within rebalance band of target 9.2%: no trade. Analyst target 638.94 USD vs 497.53 USD (+28%, 36 analysts); de-biased α -0.8% vs CAPM hurdle 11.6%. Uptrend +14% vs 200-day avg; 12-1 mom +108%; RSI 51. Quality z +0.03 (ROE 36%).

??? success "TSM (TSM) — 🟢 Buy, score +0.50"
    Within rebalance band of target 10.0%: no trade. Analyst target 552.26 USD vs 444.58 USD (+24%, 20 analysts); de-biased α -1.6% vs CAPM hurdle 10.8%. Uptrend +14% vs 200-day avg; 12-1 mom +46%; RSI 48. Quality z +0.58 (ROE 35%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.46"
    Within rebalance band of target 7.9%: no trade. Analyst target 327.70 USD vs 226.42 USD (+45%, 59 analysts); de-biased α +2.6% vs CAPM hurdle 13.9%. Uptrend +12% vs 200-day avg; 12-1 mom +14%; RSI 50. Quality z +0.47 (ROE 101%).

??? success "ASX (ASX) — 🟢 Buy, score +0.41"
    Within rebalance band of target 6.6%: no trade. Analyst target 51.00 USD vs 47.56 USD (+7%, 1 analysts); de-biased α -3.0% vs CAPM hurdle 11.9%. Uptrend +51% vs 200-day avg; 12-1 mom +240%; RSI 65. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "KLAC (KLAC) — 🟢 Buy, score +0.37"
    **TRIM 67 sh** → target 5.9% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 233.77 USD vs 190.12 USD (+23%, 26 analysts); de-biased α -2.1% vs CAPM hurdle 11.1%. Uptrend +6% vs 200-day avg; 12-1 mom +72%; RSI 49. Quality z +0.51 (ROE 87%).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.35"
    Within rebalance band of target 5.9%: no trade. Analyst target 86.74 EUR vs 57.32 EUR (+51%, 23 analysts); de-biased α +4.3% vs CAPM hurdle 14.1%. Uptrend +2% vs 200-day avg; 12-1 mom +81%; RSI 46. Quality z -0.04 (ROE 6%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.20"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 11,890 JPY (+28%, 23 analysts); de-biased α -0.9% vs CAPM hurdle 12.8%. Uptrend +21% vs 200-day avg; 12-1 mom +107%; RSI 55. Quality z -0.28 (ROE 29%).

??? note "ASML (ASML) — ⚪ Hold, score +0.19"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,750.03 USD (+20%, 16 analysts); de-biased α -3.1% vs CAPM hurdle 12.3%. Uptrend +12% vs 200-day avg; 12-1 mom +74%; RSI 49. Quality z +0.42 (ROE 50%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.09"
    Hold zone: not owned, no entry. Analyst target 375.06 USD vs 309.64 USD (+21%, 31 analysts); de-biased α -2.9% vs CAPM hurdle 12.6%. Uptrend +11% vs 200-day avg; 12-1 mom +112%; RSI 47. Quality z +0.02 (ROE 65%).

??? note "AVGO (AVGO) — ⚪ Hold, score -0.05"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 354.77 USD (+50%, 47 analysts); de-biased α +4.7% vs CAPM hurdle 11.2%. Downtrend -3% vs 200-day avg; 12-1 mom +6%; RSI 47. Quality z +0.26 (ROE 31%).

??? note "MRVL (MRVL) — ⚪ Hold, score -0.08"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 265.91 USD (+11%, 43 analysts); de-biased α -6.0% vs CAPM hurdle 14.1%. Uptrend +54% vs 200-day avg; 12-1 mom +161%; RSI 55. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "Advantest (6857.T) — ⚪ Hold, score -0.11"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 39,690 JPY (+8%, 21 analysts); de-biased α -6.5% vs CAPM hurdle 13.4%. Uptrend +42% vs 200-day avg; 12-1 mom +134%; RSI 62. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "GFS (GFS) — ⚪ Hold, score -0.15"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 48.35 USD (+57%, 22 analysts); de-biased α +6.1% vs CAPM hurdle 12.4%. Downtrend -11% vs 200-day avg; 12-1 mom +33%; RSI 51. Quality z -0.21 (ROE 8%).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.25"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 878.20 EUR (+29%, 19 analysts); de-biased α -1.2% vs CAPM hurdle 13.2%. Uptrend +9% vs 200-day avg; 12-1 mom +52%; RSI 52. Quality z -0.10 (ROE 19%).

??? note "TXN (TXN) — ⚪ Hold, score -0.25"
    Hold zone: not owned, no entry. Analyst target 324.71 USD vs 281.97 USD (+15%, 31 analysts); de-biased α -3.6% vs CAPM hurdle 10.8%. Uptrend +13% vs 200-day avg; 12-1 mom +54%; RSI 54. Quality z +0.24 (ROE 30%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.30"
    Avoid: not owned. Analyst target 81,730 JPY vs 59,160 JPY (+38%, 20 analysts); de-biased α +1.7% vs CAPM hurdle 11.5%. Downtrend -9% vs 200-day avg; 12-1 mom +16%; RSI 52. Quality z +0.06 (ROE 25%).

??? failure "TER (TER) — 🔴 Sell, score -0.41"
    Avoid: not owned. Analyst target 446.47 USD vs 383.82 USD (+16%, 15 analysts); de-biased α -4.1% vs CAPM hurdle 12.3%. Uptrend +12% vs 200-day avg; 12-1 mom +162%; RSI 47. Quality z -0.31 (ROE 20%).

??? failure "INTC (INTC) — 🔴 Sell, score -0.44"
    Avoid: not owned. Analyst target 116.37 USD vs 101.33 USD (+15%, 43 analysts); de-biased α -4.9% vs CAPM hurdle 14.0%. Uptrend +22% vs 200-day avg; 12-1 mom +172%; RSI 40. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.44"
    Avoid: not owned. Analyst target 76.40 USD vs 48.13 USD (+59%, 10 analysts); de-biased α +6.2% vs CAPM hurdle 14.0%. Downtrend -16% vs 200-day avg; 12-1 mom +70%; RSI 41. Quality z -1.00 (ROE 9%).

??? failure "QCOM (QCOM) — 🔴 Sell, score -0.50"
    Avoid: not owned. Analyst target 194.13 USD vs 174.45 USD (+11%, 30 analysts); de-biased α -4.8% vs CAPM hurdle 11.9%. Uptrend +4% vs 200-day avg; 12-1 mom +12%; RSI 44. Quality z +0.70 (ROE 23%).

??? failure "Shin-Etsu (4063.T) — 🔴 Sell, score -0.57"
    Avoid: not owned. Analyst target 7,763 JPY vs 6,077 JPY (+28%, 17 analysts); de-biased α -0.5% vs CAPM hurdle 10.8%. Downtrend -3% vs 200-day avg; 12-1 mom +21%; RSI 54. Quality z -0.20 (ROE 10%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -0.88"
    Avoid: not owned. Analyst target 405.47 USD vs 348.45 USD (+16%, 26 analysts); de-biased α -3.5% vs CAPM hurdle 10.0%. Uptrend +7% vs 200-day avg; 12-1 mom -17%; RSI 63. Quality z +0.31 (ROE 22%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.93"
    Avoid: not owned. Analyst target 173.36 USD vs 160.01 USD (+8%, 11 analysts); de-biased α -5.7% vs CAPM hurdle 11.0%. Uptrend +19% vs 200-day avg; 12-1 mom +49%; RSI 58. Quality z -0.02 (ROE 6%).

??? failure "AMD (AMD) — 🔴🔴 Strong Sell, score -1.19"
    Avoid: not owned. Analyst target 619.51 USD vs 594.14 USD (+4%, 50 analysts); de-biased α -7.8% vs CAPM hurdle 14.9%. Uptrend +53% vs 200-day avg; 12-1 mom +122%; RSI 53. Quality z -0.15 (ROE 7%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.20"
    Avoid: not owned. Analyst target 569.78 USD vs 502.51 USD (+13%, 26 analysts); de-biased α -4.4% vs CAPM hurdle 10.3%. Uptrend +13% vs 200-day avg; 12-1 mom -18%; RSI 71. Quality z +0.14 (ROE 7%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.24"
    Avoid: not owned. Analyst target 288.70 USD vs 255.05 USD (+13%, 40 analysts); de-biased α -6.7% vs CAPM hurdle 19.6%. Uptrend +15% vs 200-day avg; 12-1 mom +55%; RSI 41. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.34"
    Avoid: not owned. Analyst target 95.99 HKD vs 56.20 HKD (+71%, 21 analysts); de-biased α +10.8% vs CAPM hurdle 7.3%. Downtrend -19% vs 200-day avg; 12-1 mom -20%; RSI 31. Quality z -0.99 (ROE 3%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| AMAT | Applied Materials | 201 | 497.53 USD | $100,004 | 10.2% | Buy |
| MU | Micron Technology | 92 | 988.97 USD | $90,985 | 9.2% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 237,500 KRW | $86,245 | 8.8% | Strong Buy |
| NVDA | NVIDIA | 371 | 226.42 USD | $84,002 | 8.5% | Buy |
| 000660.KS | SK hynix | 74 | 1,506,000 KRW | $83,442 | 8.5% | Strong Buy |
| TSM | TSMC | 187 | 444.58 USD | $83,136 | 8.4% | Buy |
| ASX | ASE Technology | 1,509 | 47.56 USD | $71,760 | 7.3% | Buy |
| KLAC | KLA Corp | 372 | 190.12 USD | $70,725 | 7.2% | Buy |
| IFX.DE | Infineon Technologies | 974 | 57.32 EUR | $62,296 | 6.3% | Buy |
| 6857.T | Advantest | 200 | 39,690 JPY | $50,104 | 5.1% | Hold |
| AVGO | Broadcom | 134 | 354.77 USD | $47,539 | 4.8% | Hold |
| 8035.T | Tokyo Electron | 600 | 11,890 JPY | $45,029 | 4.6% | Hold |

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

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 20.5%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
