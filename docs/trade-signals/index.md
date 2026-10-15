---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-15 22:20 UTC (Thu Oct 15, 06:20 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Thu 18:20) · Tokyo 🔴 closed (Fri 07:20) · Korea 🔴 closed (Fri 07:20) · Hong Kong 🔴 closed (Fri 06:20) · Xetra 🔴 closed (Fri 00:20) · Euronext Amsterdam 🔴 closed (Fri 00:20)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$908,206** | $78,663 (9%) | $829,542 (91%) | -9.18% | -8.98% | 🟢 Risk-on (+10.4%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $908,206), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **NVDA**<br><small>NVIDIA</small> | 79 | 217.24 USD | $17,162 | Queued · NYSE/Nasdaq closed | quality +0.21 · momentum -0.20 |
| TRIM | **AMAT**<br><small>Applied Materials</small> | 27 | 430.28 USD | $11,618 | Queued · NYSE/Nasdaq closed | analyst α +0.23 · momentum +0.07 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +2.60 | **MU**<br><small>Micron Technology</small> | 931.40 USD | +63% | +5.2% | +396% | +30% | 39 | +0.12 | 9.4% → 10.0% | – | analyst α +0.41 · momentum +0.41 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.05 | **Samsung**<br><small>005930.KS</small> | 206,500 KRW | +131% | +23.0% | +211% | -11% | 27 | -0.26 | 8.2% → 10.0% | – | analyst α +0.85 · momentum +0.30 · ⚠️ oversold, cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.87 | **SK hynix**<br><small>000660.KS</small> | 1,251,000 KRW | – | +0.0% | +421% | -14% | 25 | +0.62 | 10.1% → 10.0% | – | momentum +0.53 · quality +0.33 · ⚠️ oversold, cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +0.90 | **Infineon**<br><small>IFX.DE</small> | 52.34 EUR | +66% | +5.9% | +67% | -7% | 36 | -0.04 | 10.3% → 9.8% | – | analyst α +0.48 · trend -0.12 |
| 🟢 Buy | +0.65 | **AMAT**<br><small>Applied Materials</small> | 430.28 USD | +48% | +2.2% | +91% | -2% | 33 | +0.03 | 7.4% → 6.1% | TRIM 27 | analyst α +0.23 · momentum +0.07 |
| 🟢 Buy | +0.64 | **KLAC**<br><small>KLA Corp</small> | 174.44 USD | +34% | -1.3% | +64% | -3% | 36 | +0.51 | 5.4% → 6.5% | – | quality +0.24 · trend -0.06 |
| 🟢 Buy | +0.64 | **NVDA**<br><small>NVIDIA</small> | 217.24 USD | +51% | +2.1% | +19% | +7% | 40 | +0.47 | 8.9% → 7.0% | TRIM 79 | quality +0.21 · momentum -0.20 |
| 🟢 Buy | +0.57 | **TSM**<br><small>TSMC</small> | 422.55 USD | +31% | -2.0% | +43% | +8% | 38 | +0.58 | 8.7% → 7.6% | – | quality +0.28 · momentum -0.10 |
| 🟢 Buy | +0.47 | **ASX**<br><small>ASE Technology</small> | 41.88 USD | +22% | -2.2% | +239% | +31% | 44 | -0.68 | 5.7% → 4.8% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.45 | **Advantest**<br><small>6857.T</small> | 34,350 JPY | +24% | -4.4% | +116% | +22% | 44 | +0.33 | 2.4% → 3.3% | – | analyst α -0.27 · quality +0.16 · ⚠️ rich valuation |
| ⚪ Hold | +0.24 | **Tokyo Electron**<br><small>8035.T</small> | 10,340 JPY | +48% | +1.9% | +101% | +4% | 40 | -0.28 | 4.3% → 4.3% | – | quality -0.18 · analyst α +0.15 |
| ⚪ Hold | +0.19 | **AVGO**<br><small>Broadcom</small> | 344.27 USD | +54% | +3.8% | -1% | -6% | 41 | +0.26 | 5.1% → 5.1% | – | analyst α +0.36 · momentum -0.30 |
| ⚪ Hold | +0.18 | **LRCX**<br><small>Lam Research</small> | 277.33 USD | +35% | -1.4% | +95% | -1% | 34 | +0.02 | 0.0% → 0.0% | – | momentum +0.10 · trend -0.03 |
| ⚪ Hold | +0.08 | **MRVL**<br><small>Marvell Technology</small> | 241.38 USD | +22% | -5.2% | +167% | +38% | 43 | -0.12 | 0.0% → 0.0% | – | analyst α -0.36 · trend +0.25 · ⚠️ rich valuation |
| ⚪ Hold | +0.08 | **ASML**<br><small>ASML Holding</small> | 1,658.58 USD | +26% | -3.5% | +64% | +6% | 39 | +0.42 | 5.5% → 5.5% | – | analyst α -0.19 · quality +0.18 |
| ⚪ Hold | -0.24 | **GFS**<br><small>GlobalFoundries</small> | 48.77 USD | +56% | +3.8% | +23% | -11% | 53 | -0.21 | 0.0% → 0.0% | – | analyst α +0.31 · momentum -0.14 |
| 🔴 Sell | -0.32 | **AMKR**<br><small>Amkor Technology</small> | 44.05 USD | +73% | +7.9% | +56% | -23% | 33 | -1.00 | 0.0% → 0.0% | – | analyst α +0.55 · quality -0.43 |
| 🔴 Sell | -0.33 | **TER**<br><small>Teradyne</small> | 343.30 USD | +30% | -2.6% | +150% | -0% | 37 | -0.31 | 0.0% → 0.0% | – | quality -0.21 · momentum +0.20 |
| 🔴 Sell | -0.36 | **ASMI**<br><small>ASM.AS</small> | 761.60 EUR | +48% | +1.7% | +42% | -6% | 34 | -0.10 | 0.0% → 0.0% | – | momentum -0.12 · analyst α +0.12 |
| 🔴 Sell | -0.38 | **Disco**<br><small>6146.T</small> | 53,270 JPY | +53% | +3.6% | +14% | -19% | 39 | +0.06 | 0.0% → 0.0% | – | analyst α +0.27 · momentum -0.26 |
| 🔴 Sell | -0.38 | **INTC**<br><small>Intel</small> | 95.31 USD | +22% | -5.1% | +184% | +13% | 36 | -0.62 | 0.0% → 0.0% | – | analyst α -0.31 · momentum +0.26 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.57 | **TXN**<br><small>Texas Instruments</small> | 279.13 USD | +16% | -5.3% | +54% | +11% | 50 | +0.24 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.12 |
| 🔴🔴 Strong Sell | -0.75 | **QCOM**<br><small>Qualcomm</small> | 178.36 USD | +9% | -7.4% | +17% | +6% | 49 | +0.70 | 0.0% → 0.0% | – | analyst α -0.55 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.94 | **CDNS**<br><small>Cadence Design Systems</small> | 324.36 USD | +25% | -3.4% | -14% | -1% | 47 | +0.31 | 0.0% → 0.0% | – | momentum -0.35 · analyst α -0.15 |
| 🔴🔴 Strong Sell | -0.99 | **Shin-Etsu**<br><small>4063.T</small> | 5,992 JPY | +30% | -2.0% | +20% | -4% | 49 | -0.20 | 0.0% → 0.0% | – | momentum -0.17 · quality -0.11 |
| 🔴🔴 Strong Sell | -1.12 | **AMD**<br><small>Advanced Micro Devices</small> | 562.13 USD | +10% | -8.3% | +135% | +43% | 45 | -0.15 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -1.20 | **ENTG**<br><small>Entegris</small> | 146.94 USD | +18% | -5.3% | +44% | +9% | 44 | -0.02 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.09 |
| 🔴🔴 Strong Sell | -1.28 | **SMIC**<br><small>0981.HK</small> | 52.15 HKD | +84% | +12.1% | -33% | -24% | 24 | -0.99 | 0.0% → 0.0% | – | analyst α +0.66 · momentum -0.53 · ⚠️ oversold |
| 🔴🔴 Strong Sell | -1.33 | **SNPS**<br><small>Synopsys</small> | 468.02 USD | +22% | -4.3% | -15% | +5% | 55 | +0.14 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.23 |
| 🔴🔴 Strong Sell | -1.43 | **ARM**<br><small>Arm Holdings</small> | 244.59 USD | +18% | -7.5% | +45% | +10% | 39 | +0.04 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.10 · ⚠️ rich valuation, high σ(e) |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.60"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 931.40 USD (+63%, 46 analysts); de-biased α +5.2% vs CAPM hurdle 14.0%. Uptrend +30% vs 200-day avg; 12-1 mom +396%; RSI 39. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.05"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 206,500 KRW (+131%, 36 analysts); de-biased α +23.0% vs CAPM hurdle 11.3%. Downtrend -11% vs 200-day avg; 12-1 mom +211%; RSI 27. Quality z -0.26 (ROE 11%). ⚠️ oversold; cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.87"
    Within rebalance band of target 10.0%: no trade. No reliable analyst target: α set to 0. Downtrend -14% vs 200-day avg; 12-1 mom +421%; RSI 25. Quality z +0.62 (ROE 44%). ⚠️ oversold; cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "Infineon (IFX.DE) — 🟢🟢 Strong Buy, score +0.90"
    Within rebalance band of target 9.8%: no trade. Analyst target 86.74 EUR vs 52.34 EUR (+66%, 23 analysts); de-biased α +5.9% vs CAPM hurdle 14.1%. Downtrend -7% vs 200-day avg; 12-1 mom +67%; RSI 36. Quality z -0.04 (ROE 6%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.65"
    **TRIM 27 sh** → target 6.1% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 430.28 USD (+48%, 36 analysts); de-biased α +2.2% vs CAPM hurdle 11.6%. Downtrend -2% vs 200-day avg; 12-1 mom +91%; RSI 33. Quality z +0.03 (ROE 36%).

??? success "KLAC (KLAC) — 🟢 Buy, score +0.64"
    Within rebalance band of target 6.5%: no trade. Analyst target 233.77 USD vs 174.44 USD (+34%, 26 analysts); de-biased α -1.3% vs CAPM hurdle 11.1%. Downtrend -3% vs 200-day avg; 12-1 mom +64%; RSI 36. Quality z +0.51 (ROE 87%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.64"
    **TRIM 79 sh** → target 7.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 327.70 USD vs 217.24 USD (+51%, 59 analysts); de-biased α +2.1% vs CAPM hurdle 13.9%. Uptrend +7% vs 200-day avg; 12-1 mom +19%; RSI 40. Quality z +0.47 (ROE 101%).

??? success "TSM (TSM) — 🟢 Buy, score +0.57"
    Within rebalance band of target 7.6%: no trade. Analyst target 552.26 USD vs 422.55 USD (+31%, 20 analysts); de-biased α -2.0% vs CAPM hurdle 10.8%. Uptrend +8% vs 200-day avg; 12-1 mom +43%; RSI 38. Quality z +0.58 (ROE 35%).

??? success "ASX (ASX) — 🟢 Buy, score +0.47"
    Within rebalance band of target 4.8%: no trade. Analyst target 51.00 USD vs 41.88 USD (+22%, 1 analysts); de-biased α -2.2% vs CAPM hurdle 11.9%. Uptrend +31% vs 200-day avg; 12-1 mom +239%; RSI 44. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.45"
    Within rebalance band of target 3.3%: no trade. Analyst target 42,686 JPY vs 34,350 JPY (+24%, 21 analysts); de-biased α -4.4% vs CAPM hurdle 13.4%. Uptrend +22% vs 200-day avg; 12-1 mom +116%; RSI 44. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.24"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 10,340 JPY (+48%, 23 analysts); de-biased α +1.9% vs CAPM hurdle 12.8%. Uptrend +4% vs 200-day avg; 12-1 mom +101%; RSI 40. Quality z -0.28 (ROE 29%).

??? note "AVGO (AVGO) — ⚪ Hold, score +0.19"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 344.27 USD (+54%, 47 analysts); de-biased α +3.8% vs CAPM hurdle 11.2%. Downtrend -6% vs 200-day avg; 12-1 mom -1%; RSI 41. Quality z +0.26 (ROE 31%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.18"
    Hold zone: not owned, no entry. Analyst target 375.06 USD vs 277.33 USD (+35%, 31 analysts); de-biased α -1.4% vs CAPM hurdle 12.6%. Downtrend -1% vs 200-day avg; 12-1 mom +95%; RSI 34. Quality z +0.02 (ROE 65%).

??? note "MRVL (MRVL) — ⚪ Hold, score +0.08"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 241.38 USD (+22%, 43 analysts); de-biased α -5.2% vs CAPM hurdle 14.1%. Uptrend +38% vs 200-day avg; 12-1 mom +167%; RSI 43. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "ASML (ASML) — ⚪ Hold, score +0.08"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,658.58 USD (+26%, 16 analysts); de-biased α -3.5% vs CAPM hurdle 12.3%. Uptrend +6% vs 200-day avg; 12-1 mom +64%; RSI 39. Quality z +0.42 (ROE 50%).

??? note "GFS (GFS) — ⚪ Hold, score -0.24"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 48.77 USD (+56%, 22 analysts); de-biased α +3.8% vs CAPM hurdle 12.4%. Downtrend -11% vs 200-day avg; 12-1 mom +23%; RSI 53. Quality z -0.21 (ROE 8%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.32"
    Avoid: not owned. Analyst target 76.40 USD vs 44.05 USD (+73%, 10 analysts); de-biased α +7.9% vs CAPM hurdle 14.0%. Downtrend -23% vs 200-day avg; 12-1 mom +56%; RSI 33. Quality z -1.00 (ROE 9%).

??? failure "TER (TER) — 🔴 Sell, score -0.33"
    Avoid: not owned. Analyst target 446.47 USD vs 343.30 USD (+30%, 15 analysts); de-biased α -2.6% vs CAPM hurdle 12.3%. Downtrend -0% vs 200-day avg; 12-1 mom +150%; RSI 37. Quality z -0.31 (ROE 20%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.36"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 761.60 EUR (+48%, 19 analysts); de-biased α +1.7% vs CAPM hurdle 13.2%. Downtrend -6% vs 200-day avg; 12-1 mom +42%; RSI 34. Quality z -0.10 (ROE 19%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.38"
    Avoid: not owned. Analyst target 81,730 JPY vs 53,270 JPY (+53%, 20 analysts); de-biased α +3.6% vs CAPM hurdle 11.5%. Downtrend -19% vs 200-day avg; 12-1 mom +14%; RSI 39. Quality z +0.06 (ROE 25%).

??? failure "INTC (INTC) — 🔴 Sell, score -0.38"
    Avoid: not owned. Analyst target 116.37 USD vs 95.31 USD (+22%, 43 analysts); de-biased α -5.1% vs CAPM hurdle 14.0%. Uptrend +13% vs 200-day avg; 12-1 mom +184%; RSI 36. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "TXN (TXN) — 🔴 Sell, score -0.57"
    Avoid: not owned. Analyst target 324.71 USD vs 279.13 USD (+16%, 31 analysts); de-biased α -5.3% vs CAPM hurdle 10.8%. Uptrend +11% vs 200-day avg; 12-1 mom +54%; RSI 50. Quality z +0.24 (ROE 30%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.75"
    Avoid: not owned. Analyst target 194.13 USD vs 178.36 USD (+9%, 30 analysts); de-biased α -7.4% vs CAPM hurdle 11.9%. Uptrend +6% vs 200-day avg; 12-1 mom +17%; RSI 49. Quality z +0.70 (ROE 23%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -0.94"
    Avoid: not owned. Analyst target 405.47 USD vs 324.36 USD (+25%, 26 analysts); de-biased α -3.4% vs CAPM hurdle 10.0%. Downtrend -1% vs 200-day avg; 12-1 mom -14%; RSI 47. Quality z +0.31 (ROE 22%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -0.99"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,992 JPY (+30%, 17 analysts); de-biased α -2.0% vs CAPM hurdle 10.8%. Downtrend -4% vs 200-day avg; 12-1 mom +20%; RSI 49. Quality z -0.20 (ROE 10%).

??? failure "AMD (AMD) — 🔴🔴 Strong Sell, score -1.12"
    Avoid: not owned. Analyst target 619.51 USD vs 562.13 USD (+10%, 50 analysts); de-biased α -8.3% vs CAPM hurdle 14.9%. Uptrend +43% vs 200-day avg; 12-1 mom +135%; RSI 45. Quality z -0.15 (ROE 7%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -1.20"
    Avoid: not owned. Analyst target 173.36 USD vs 146.94 USD (+18%, 11 analysts); de-biased α -5.3% vs CAPM hurdle 11.0%. Uptrend +9% vs 200-day avg; 12-1 mom +44%; RSI 44. Quality z -0.02 (ROE 6%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.28"
    Avoid: not owned. Analyst target 95.99 HKD vs 52.15 HKD (+84%, 21 analysts); de-biased α +12.1% vs CAPM hurdle 7.3%. Downtrend -24% vs 200-day avg; 12-1 mom -33%; RSI 24. Quality z -0.99 (ROE 3%). ⚠️ oversold.

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.33"
    Avoid: not owned. Analyst target 569.78 USD vs 468.02 USD (+22%, 26 analysts); de-biased α -4.3% vs CAPM hurdle 10.3%. Uptrend +5% vs 200-day avg; 12-1 mom -15%; RSI 55. Quality z +0.14 (ROE 7%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.43"
    Avoid: not owned. Analyst target 288.70 USD vs 244.59 USD (+18%, 40 analysts); de-biased α -7.5% vs CAPM hurdle 19.6%. Uptrend +10% vs 200-day avg; 12-1 mom +45%; RSI 39. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| IFX.DE | Infineon Technologies | 1,594 | 52.34 EUR | $93,584 | 10.3% | Strong Buy |
| 000660.KS | SK hynix | 98 | 1,251,000 KRW | $91,406 | 10.1% | Strong Buy |
| MU | Micron Technology | 92 | 931.40 USD | $85,689 | 9.4% | Strong Buy |
| NVDA | NVIDIA | 371 | 217.24 USD | $80,596 | 8.9% | Buy |
| TSM | TSMC | 187 | 422.55 USD | $79,017 | 8.7% | Buy |
| 005930.KS | Samsung Electronics | 485 | 206,500 KRW | $74,672 | 8.2% | Strong Buy |
| AMAT | Applied Materials | 156 | 430.28 USD | $67,124 | 7.4% | Buy |
| ASX | ASE Technology | 1,239 | 41.88 USD | $51,896 | 5.7% | Buy |
| ASML | ASML Holding | 30 | 1,658.58 USD | $49,757 | 5.5% | Hold |
| KLAC | KLA Corp | 279 | 174.44 USD | $48,669 | 5.4% | Buy |
| AVGO | Broadcom | 134 | 344.27 USD | $46,132 | 5.1% | Hold |
| 8035.T | Tokyo Electron | 600 | 10,340 JPY | $39,263 | 4.3% | Hold |
| 6857.T | Advantest | 100 | 34,350 JPY | $21,739 | 2.4% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-10-15 15:02 UTC | ADD | ASX | 339 | 41.52 | $14,077 |
| 2026-10-15 15:02 UTC | TRIM | KLAC | -93 | 172.43 | $16,036 |
| 2026-10-15 04:41 UTC | BUY (new) | 6857.T | 100 | 34,860.00 | $22,075 |
| 2026-10-15 04:41 UTC | ADD | 000660.KS | 24 | 1,270,000.00 | $22,625 |
| 2026-10-14 00:21 UTC | SELL (exit) | 6857.T | -200 | 40,990.00 | $51,779 |
| 2026-10-13 16:00 UTC | BUY (new) | ASML | 30 | 1,699.05 | $50,972 |
| 2026-10-13 16:00 UTC | TRIM | AMAT | -45 | 464.47 | $20,901 |
| 2026-10-13 16:00 UTC | TRIM | ASX | -609 | 47.11 | $28,690 |
| 2026-10-13 07:43 UTC | ADD | IFX.DE | 620 | 54.55 | $37,861 |
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

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 28.5%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
