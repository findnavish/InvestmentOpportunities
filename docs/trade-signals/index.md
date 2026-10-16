---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-16 12:26 UTC (Fri Oct 16, 08:26 AM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Fri 08:26) · Tokyo 🔴 closed (Fri 21:26) · Korea 🔴 closed (Fri 21:26) · Hong Kong 🔴 closed (Fri 20:26) · Xetra 🟢 open (Fri 14:26) · Euronext Amsterdam 🟢 open (Fri 14:26)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$918,008** | $96,078 (10%) | $821,930 (90%) | -8.20% | -8.98% | 🟢 Risk-on (+10.4%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $918,008), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **TSM**<br><small>TSMC</small> | 49 | 422.55 USD | $20,705 | Queued · NYSE/Nasdaq closed | quality +0.28 · momentum -0.12 |
| TRIM | **Infineon**<br><small>IFX.DE</small> | 293 | 52.84 EUR | $17,423 | Executed (paper) | analyst α +0.41 · trend -0.14 |
| TRIM | **AMAT**<br><small>Applied Materials</small> | 33 | 430.28 USD | $14,199 | Queued · NYSE/Nasdaq closed | analyst α +0.19 · momentum +0.07 |
| ADD | **ASX**<br><small>ASE Technology</small> | 329 | 41.88 USD | $13,780 | Queued · NYSE/Nasdaq closed | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.25 | **SK hynix**<br><small>000660.KS</small> | 1,284,000 KRW | +145% | +24.8% | +421% | -12% | 27 | +0.62 | 10.3% → 10.0% | – | analyst α +0.85 · momentum +0.53 · ⚠️ oversold, cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.14 | **MU**<br><small>Micron Technology</small> | 931.40 USD | +63% | +4.5% | +410% | +30% | 39 | +0.12 | 9.3% → 10.0% | – | momentum +0.41 · analyst α +0.36 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.48 | **Samsung**<br><small>005930.KS</small> | 217,500 KRW | +120% | +19.4% | +211% | -6% | 33 | -0.26 | 8.6% → 10.0% | – | analyst α +0.66 · momentum +0.30 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.61 | **Infineon**<br><small>IFX.DE</small> | 52.84 EUR | +64% | +4.9% | +69% | -7% | 38 | -0.04 | 8.4% → 8.4% | TRIM 293 | analyst α +0.41 · trend -0.14 |
| 🟢 Buy | +0.55 | **ASX**<br><small>ASE Technology</small> | 41.88 USD | +22% | -2.6% | +239% | +31% | 44 | -0.68 | 5.7% → 7.2% | ADD 329 | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.53 | **NVDA**<br><small>NVIDIA</small> | 217.24 USD | +51% | +1.5% | +22% | +7% | 40 | +0.47 | 8.8% → 7.4% | – | quality +0.21 · momentum -0.17 |
| 🟢 Buy | +0.51 | **KLAC**<br><small>KLA Corp</small> | 174.44 USD | +34% | -2.0% | +56% | -4% | 36 | +0.51 | 5.3% → 6.5% | – | quality +0.24 · trend -0.06 |
| 🟢 Buy | +0.49 | **AMAT**<br><small>Applied Materials</small> | 430.28 USD | +48% | +1.5% | +84% | -2% | 33 | +0.03 | 7.3% → 5.7% | TRIM 33 | analyst α +0.19 · momentum +0.07 |
| 🟢 Buy | +0.39 | **Advantest**<br><small>6857.T</small> | 34,480 JPY | +24% | -5.2% | +116% | +22% | 44 | +0.33 | 2.4% → 3.7% | – | analyst α -0.27 · quality +0.16 · ⚠️ rich valuation |
| 🟢 Buy | +0.38 | **TSM**<br><small>TSMC</small> | 422.55 USD | +31% | -2.6% | +43% | +7% | 38 | +0.58 | 8.6% → 6.3% | TRIM 49 | quality +0.28 · momentum -0.12 |
| ⚪ Hold | +0.16 | **LRCX**<br><small>Lam Research</small> | 277.33 USD | +35% | -2.1% | +87% | -2% | 34 | +0.02 | 0.0% → 0.0% | – | momentum +0.10 · trend -0.03 |
| ⚪ Hold | +0.14 | **Tokyo Electron**<br><small>8035.T</small> | 10,570 JPY | +45% | +0.4% | +101% | +7% | 43 | -0.28 | 4.4% → 4.4% | – | quality -0.18 · momentum +0.12 |
| ⚪ Hold | +0.08 | **ASML**<br><small>ASML Holding</small> | 1,658.58 USD | +26% | -4.2% | +62% | +5% | 39 | +0.42 | 5.4% → 5.4% | – | analyst α -0.19 · quality +0.18 |
| ⚪ Hold | +0.07 | **MRVL**<br><small>Marvell Technology</small> | 241.38 USD | +22% | -5.9% | +171% | +37% | 43 | -0.12 | 0.0% → 0.0% | – | analyst α -0.36 · trend +0.25 · ⚠️ rich valuation |
| ⚪ Hold | +0.03 | **AVGO**<br><small>Broadcom</small> | 344.27 USD | +54% | +3.2% | -1% | -6% | 41 | +0.26 | 5.0% → 5.0% | – | analyst α +0.31 · momentum -0.30 |
| ⚪ Hold | -0.21 | **ASMI**<br><small>ASM.AS</small> | 765.60 EUR | +47% | +0.8% | +45% | -5% | 34 | -0.10 | 0.0% → 0.0% | – | analyst α +0.12 · trend -0.09 |
| 🔴 Sell | -0.29 | **TER**<br><small>Teradyne</small> | 343.30 USD | +30% | -3.3% | +151% | -0% | 37 | -0.31 | 0.0% → 0.0% | – | quality -0.21 · momentum +0.20 |
| 🔴 Sell | -0.33 | **INTC**<br><small>Intel</small> | 95.31 USD | +22% | -5.8% | +193% | +13% | 36 | -0.62 | 0.0% → 0.0% | – | analyst α -0.31 · momentum +0.26 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.35 | **GFS**<br><small>GlobalFoundries</small> | 48.77 USD | +56% | +3.1% | +31% | -11% | 53 | -0.21 | 0.0% → 0.0% | – | analyst α +0.27 · trend -0.16 |
| 🔴 Sell | -0.41 | **Disco**<br><small>6146.T</small> | 53,760 JPY | +52% | +2.5% | +14% | -18% | 41 | +0.06 | 0.0% → 0.0% | – | momentum -0.26 · analyst α +0.23 |
| 🔴 Sell | -0.44 | **AMKR**<br><small>Amkor Technology</small> | 44.05 USD | +73% | +7.2% | +56% | -23% | 33 | -1.00 | 0.0% → 0.0% | – | analyst α +0.48 · quality -0.43 |
| 🔴 Sell | -0.54 | **TXN**<br><small>Texas Instruments</small> | 279.13 USD | +16% | -5.9% | +51% | +10% | 50 | +0.24 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.12 |
| 🔴 Sell | -0.68 | **QCOM**<br><small>Qualcomm</small> | 178.36 USD | +9% | -8.1% | +18% | +6% | 49 | +0.70 | 0.0% → 0.0% | – | analyst α -0.55 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.95 | **CDNS**<br><small>Cadence Design Systems</small> | 324.36 USD | +25% | -4.0% | -13% | -1% | 47 | +0.31 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.15 |
| 🔴🔴 Strong Sell | -0.97 | **AMD**<br><small>Advanced Micro Devices</small> | 562.13 USD | +10% | -9.0% | +128% | +43% | 44 | -0.15 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -0.99 | **Shin-Etsu**<br><small>4063.T</small> | 6,002 JPY | +29% | -2.7% | +20% | -4% | 49 | -0.20 | 0.0% → 0.0% | – | momentum -0.20 · quality -0.11 |
| 🔴🔴 Strong Sell | -1.04 | **SNPS**<br><small>Synopsys</small> | 468.02 USD | +22% | -4.9% | -13% | +5% | 55 | +0.14 | 0.0% → 0.0% | – | momentum -0.35 · analyst α -0.23 |
| 🔴🔴 Strong Sell | -1.09 | **ENTG**<br><small>Entegris</small> | 146.94 USD | +18% | -6.0% | +43% | +8% | 44 | -0.02 | 0.0% → 0.0% | – | analyst α -0.48 · momentum -0.10 |
| 🔴🔴 Strong Sell | -1.20 | **ARM**<br><small>Arm Holdings</small> | 244.59 USD | +18% | -8.2% | +55% | +9% | 39 | +0.04 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.10 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.33 | **SMIC**<br><small>0981.HK</small> | 52.40 HKD | +83% | +11.2% | -29% | -24% | 25 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.53 · ⚠️ oversold |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.25"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,284,000 KRW (+145%, 38 analysts); de-biased α +24.8% vs CAPM hurdle 14.3%. Downtrend -12% vs 200-day avg; 12-1 mom +421%; RSI 27. Quality z +0.62 (ROE 44%). ⚠️ oversold; cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.14"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 931.40 USD (+63%, 46 analysts); de-biased α +4.5% vs CAPM hurdle 14.0%. Uptrend +30% vs 200-day avg; 12-1 mom +410%; RSI 39. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.48"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 217,500 KRW (+120%, 36 analysts); de-biased α +19.4% vs CAPM hurdle 11.3%. Downtrend -6% vs 200-day avg; 12-1 mom +211%; RSI 33. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.61"
    **TRIM 293 sh** → target 8.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 86.74 EUR vs 52.84 EUR (+64%, 23 analysts); de-biased α +4.9% vs CAPM hurdle 14.1%. Downtrend -7% vs 200-day avg; 12-1 mom +69%; RSI 38. Quality z -0.04 (ROE 6%).

??? success "ASX (ASX) — 🟢 Buy, score +0.55"
    **ADD 329 sh** → target 7.2% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 51.00 USD vs 41.88 USD (+22%, 1 analysts); de-biased α -2.6% vs CAPM hurdle 11.9%. Uptrend +31% vs 200-day avg; 12-1 mom +239%; RSI 44. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.53"
    Within rebalance band of target 7.4%: no trade. Analyst target 327.70 USD vs 217.24 USD (+51%, 59 analysts); de-biased α +1.5% vs CAPM hurdle 13.9%. Uptrend +7% vs 200-day avg; 12-1 mom +22%; RSI 40. Quality z +0.47 (ROE 101%).

??? success "KLAC (KLAC) — 🟢 Buy, score +0.51"
    Within rebalance band of target 6.5%: no trade. Analyst target 233.77 USD vs 174.44 USD (+34%, 26 analysts); de-biased α -2.0% vs CAPM hurdle 11.1%. Downtrend -4% vs 200-day avg; 12-1 mom +56%; RSI 36. Quality z +0.51 (ROE 87%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.49"
    **TRIM 33 sh** → target 5.7% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 430.28 USD (+48%, 36 analysts); de-biased α +1.5% vs CAPM hurdle 11.6%. Downtrend -2% vs 200-day avg; 12-1 mom +84%; RSI 33. Quality z +0.03 (ROE 36%).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.39"
    Within rebalance band of target 3.7%: no trade. Analyst target 42,686 JPY vs 34,480 JPY (+24%, 21 analysts); de-biased α -5.2% vs CAPM hurdle 13.4%. Uptrend +22% vs 200-day avg; 12-1 mom +116%; RSI 44. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? success "TSM (TSM) — 🟢 Buy, score +0.38"
    **TRIM 49 sh** → target 6.3% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 552.26 USD vs 422.55 USD (+31%, 20 analysts); de-biased α -2.6% vs CAPM hurdle 10.8%. Uptrend +7% vs 200-day avg; 12-1 mom +43%; RSI 38. Quality z +0.58 (ROE 35%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.16"
    Hold zone: not owned, no entry. Analyst target 375.06 USD vs 277.33 USD (+35%, 31 analysts); de-biased α -2.1% vs CAPM hurdle 12.6%. Downtrend -2% vs 200-day avg; 12-1 mom +87%; RSI 34. Quality z +0.02 (ROE 65%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.14"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 10,570 JPY (+45%, 23 analysts); de-biased α +0.4% vs CAPM hurdle 12.8%. Uptrend +7% vs 200-day avg; 12-1 mom +101%; RSI 43. Quality z -0.28 (ROE 29%).

??? note "ASML (ASML) — ⚪ Hold, score +0.08"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,658.58 USD (+26%, 16 analysts); de-biased α -4.2% vs CAPM hurdle 12.3%. Uptrend +5% vs 200-day avg; 12-1 mom +62%; RSI 39. Quality z +0.42 (ROE 50%).

??? note "MRVL (MRVL) — ⚪ Hold, score +0.07"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 241.38 USD (+22%, 43 analysts); de-biased α -5.9% vs CAPM hurdle 14.1%. Uptrend +37% vs 200-day avg; 12-1 mom +171%; RSI 43. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "AVGO (AVGO) — ⚪ Hold, score +0.03"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 344.27 USD (+54%, 47 analysts); de-biased α +3.2% vs CAPM hurdle 11.2%. Downtrend -6% vs 200-day avg; 12-1 mom -1%; RSI 41. Quality z +0.26 (ROE 31%).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.21"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 765.60 EUR (+47%, 19 analysts); de-biased α +0.8% vs CAPM hurdle 13.2%. Downtrend -5% vs 200-day avg; 12-1 mom +45%; RSI 34. Quality z -0.10 (ROE 19%).

??? failure "TER (TER) — 🔴 Sell, score -0.29"
    Avoid: not owned. Analyst target 446.47 USD vs 343.30 USD (+30%, 15 analysts); de-biased α -3.3% vs CAPM hurdle 12.3%. Downtrend -0% vs 200-day avg; 12-1 mom +151%; RSI 37. Quality z -0.31 (ROE 20%).

??? failure "INTC (INTC) — 🔴 Sell, score -0.33"
    Avoid: not owned. Analyst target 116.37 USD vs 95.31 USD (+22%, 43 analysts); de-biased α -5.8% vs CAPM hurdle 14.0%. Uptrend +13% vs 200-day avg; 12-1 mom +193%; RSI 36. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "GFS (GFS) — 🔴 Sell, score -0.35"
    Avoid: not owned. Analyst target 76.00 USD vs 48.77 USD (+56%, 22 analysts); de-biased α +3.1% vs CAPM hurdle 12.4%. Downtrend -11% vs 200-day avg; 12-1 mom +31%; RSI 53. Quality z -0.21 (ROE 8%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.41"
    Avoid: not owned. Analyst target 81,730 JPY vs 53,760 JPY (+52%, 20 analysts); de-biased α +2.5% vs CAPM hurdle 11.5%. Downtrend -18% vs 200-day avg; 12-1 mom +14%; RSI 41. Quality z +0.06 (ROE 25%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.44"
    Avoid: not owned. Analyst target 76.40 USD vs 44.05 USD (+73%, 10 analysts); de-biased α +7.2% vs CAPM hurdle 14.0%. Downtrend -23% vs 200-day avg; 12-1 mom +56%; RSI 33. Quality z -1.00 (ROE 9%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.54"
    Avoid: not owned. Analyst target 324.71 USD vs 279.13 USD (+16%, 31 analysts); de-biased α -5.9% vs CAPM hurdle 10.8%. Uptrend +10% vs 200-day avg; 12-1 mom +51%; RSI 50. Quality z +0.24 (ROE 30%).

??? failure "QCOM (QCOM) — 🔴 Sell, score -0.68"
    Avoid: not owned. Analyst target 194.13 USD vs 178.36 USD (+9%, 30 analysts); de-biased α -8.1% vs CAPM hurdle 11.9%. Uptrend +6% vs 200-day avg; 12-1 mom +18%; RSI 49. Quality z +0.70 (ROE 23%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -0.95"
    Avoid: not owned. Analyst target 405.47 USD vs 324.36 USD (+25%, 26 analysts); de-biased α -4.0% vs CAPM hurdle 10.0%. Downtrend -1% vs 200-day avg; 12-1 mom -13%; RSI 47. Quality z +0.31 (ROE 22%).

??? failure "AMD (AMD) — 🔴🔴 Strong Sell, score -0.97"
    Avoid: not owned. Analyst target 619.51 USD vs 562.13 USD (+10%, 50 analysts); de-biased α -9.0% vs CAPM hurdle 14.9%. Uptrend +43% vs 200-day avg; 12-1 mom +128%; RSI 44. Quality z -0.15 (ROE 7%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -0.99"
    Avoid: not owned. Analyst target 7,763 JPY vs 6,002 JPY (+29%, 17 analysts); de-biased α -2.7% vs CAPM hurdle 10.8%. Downtrend -4% vs 200-day avg; 12-1 mom +20%; RSI 49. Quality z -0.20 (ROE 10%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.04"
    Avoid: not owned. Analyst target 569.78 USD vs 468.02 USD (+22%, 26 analysts); de-biased α -4.9% vs CAPM hurdle 10.3%. Uptrend +5% vs 200-day avg; 12-1 mom -13%; RSI 55. Quality z +0.14 (ROE 7%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -1.09"
    Avoid: not owned. Analyst target 173.36 USD vs 146.94 USD (+18%, 11 analysts); de-biased α -6.0% vs CAPM hurdle 11.0%. Uptrend +8% vs 200-day avg; 12-1 mom +43%; RSI 44. Quality z -0.02 (ROE 6%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.20"
    Avoid: not owned. Analyst target 288.70 USD vs 244.59 USD (+18%, 40 analysts); de-biased α -8.2% vs CAPM hurdle 19.6%. Uptrend +9% vs 200-day avg; 12-1 mom +55%; RSI 39. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.33"
    Avoid: not owned. Analyst target 95.99 HKD vs 52.40 HKD (+83%, 21 analysts); de-biased α +11.2% vs CAPM hurdle 7.3%. Downtrend -24% vs 200-day avg; 12-1 mom -29%; RSI 25. Quality z -0.99 (ROE 3%). ⚠️ oversold.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 98 | 1,284,000 KRW | $94,492 | 10.3% | Strong Buy |
| MU | Micron Technology | 92 | 931.40 USD | $85,689 | 9.3% | Strong Buy |
| NVDA | NVIDIA | 371 | 217.24 USD | $80,596 | 8.8% | Buy |
| 005930.KS | Samsung Electronics | 485 | 217,500 KRW | $79,214 | 8.6% | Strong Buy |
| TSM | TSMC | 187 | 422.55 USD | $79,017 | 8.6% | Buy |
| IFX.DE | Infineon Technologies | 1,301 | 52.84 EUR | $77,363 | 8.4% | Buy |
| AMAT | Applied Materials | 156 | 430.28 USD | $67,124 | 7.3% | Buy |
| ASX | ASE Technology | 1,239 | 41.88 USD | $51,896 | 5.7% | Buy |
| ASML | ASML Holding | 30 | 1,658.58 USD | $49,757 | 5.4% | Hold |
| KLAC | KLA Corp | 279 | 174.44 USD | $48,669 | 5.3% | Buy |
| AVGO | Broadcom | 134 | 344.27 USD | $46,132 | 5.0% | Hold |
| 8035.T | Tokyo Electron | 600 | 10,570 JPY | $40,152 | 4.4% | Hold |
| 6857.T | Advantest | 100 | 34,480 JPY | $21,830 | 2.4% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-10-16 12:26 UTC | TRIM | IFX.DE | -293 | 52.84 | $17,423 |
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

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 31.2%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
