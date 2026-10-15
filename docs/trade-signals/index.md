---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-15 15:02 UTC (Thu Oct 15, 11:02 AM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🟢 open (Thu 11:02) · Tokyo 🔴 closed (Fri 00:02) · Korea 🔴 closed (Fri 00:02) · Hong Kong 🔴 closed (Thu 23:02) · Xetra 🟢 open (Thu 17:02) · Euronext Amsterdam 🟢 open (Thu 17:02)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$900,513** | $78,663 (9%) | $821,850 (91%) | -9.95% | -10.52% | 🟢 Risk-on (+8.5%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $900,513), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **KLAC**<br><small>KLA Corp</small> | 93 | 172.43 USD | $16,036 | Executed (paper) | quality +0.24 · trend -0.07 |
| ADD | **ASX**<br><small>ASE Technology</small> | 339 | 41.53 USD | $14,077 | Executed (paper) | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +2.60 | **MU**<br><small>Micron Technology</small> | 908.28 USD | +67% | +5.8% | +396% | +27% | 36 | +0.12 | 9.3% → 10.0% | – | analyst α +0.41 · momentum +0.41 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.10 | **Samsung**<br><small>005930.KS</small> | 206,500 KRW | +131% | +22.6% | +227% | -11% | 27 | -0.26 | 8.3% → 10.0% | – | analyst α +0.85 · momentum +0.30 · ⚠️ oversold, cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.87 | **SK hynix**<br><small>000660.KS</small> | 1,251,000 KRW | – | +0.0% | +452% | -14% | 25 | +0.62 | 10.1% → 10.0% | – | momentum +0.53 · quality +0.33 · ⚠️ oversold, cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +0.90 | **Infineon**<br><small>IFX.DE</small> | 51.85 EUR | +67% | +5.9% | +67% | -8% | 36 | -0.04 | 10.3% → 9.9% | – | analyst α +0.48 · trend -0.12 |
| 🟢 Buy | +0.70 | **NVDA**<br><small>NVIDIA</small> | 216.39 USD | +51% | +1.8% | +19% | +7% | 40 | +0.47 | 8.9% → 7.8% | – | quality +0.21 · momentum -0.20 |
| 🟢 Buy | +0.69 | **AMAT**<br><small>Applied Materials</small> | 426.57 USD | +50% | +2.1% | +91% | -3% | 32 | +0.03 | 7.4% → 6.4% | – | analyst α +0.23 · momentum +0.07 |
| 🟢 Buy | +0.57 | **TSM**<br><small>TSMC</small> | 416.83 USD | +32% | -2.0% | +43% | +6% | 36 | +0.58 | 8.7% → 7.6% | – | quality +0.28 · momentum -0.10 |
| 🟢 Buy | +0.55 | **ASX**<br><small>ASE Technology</small> | 41.53 USD | +23% | -2.3% | +239% | +30% | 43 | -0.68 | 5.7% → 5.7% | ADD 339 | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.53 | **KLAC**<br><small>KLA Corp</small> | 172.43 USD | +36% | -1.4% | +64% | -4% | 35 | +0.51 | 5.3% → 5.3% | TRIM 93 | quality +0.24 · trend -0.07 |
| ⚪ Hold | +0.25 | **Tokyo Electron**<br><small>8035.T</small> | 10,340 JPY | +48% | +1.4% | +102% | +5% | 40 | -0.28 | 4.4% → 4.4% | – | quality -0.18 · momentum +0.12 |
| ⚪ Hold | +0.23 | **Advantest**<br><small>6857.T</small> | 34,350 JPY | +24% | -4.8% | +132% | +22% | 44 | +0.33 | 2.4% → 2.4% | – | analyst α -0.36 · quality +0.16 · ⚠️ rich valuation |
| ⚪ Hold | +0.23 | **LRCX**<br><small>Lam Research</small> | 271.59 USD | +38% | -1.1% | +95% | -3% | 33 | +0.02 | 0.0% → 0.0% | – | momentum +0.10 · analyst α +0.05 |
| ⚪ Hold | +0.20 | **MRVL**<br><small>Marvell Technology</small> | 234.90 USD | +25% | -4.8% | +167% | +34% | 40 | -0.12 | 0.0% → 0.0% | – | analyst α -0.31 · trend +0.25 · ⚠️ rich valuation |
| ⚪ Hold | +0.14 | **ASML**<br><small>ASML Holding</small> | 1,632.20 USD | +28% | -3.4% | +64% | +4% | 37 | +0.42 | 5.4% → 5.4% | – | quality +0.18 · analyst α -0.15 |
| ⚪ Hold | +0.07 | **AVGO**<br><small>Broadcom</small> | 340.35 USD | +56% | +3.9% | -1% | -7% | 40 | +0.26 | 5.1% → 5.1% | – | analyst α +0.31 · momentum -0.30 |
| ⚪ Hold | -0.18 | **GFS**<br><small>GlobalFoundries</small> | 47.40 USD | +60% | +4.5% | +23% | -13% | 48 | -0.21 | 0.0% → 0.0% | – | analyst α +0.36 · trend -0.16 |
| 🔴 Sell | -0.27 | **ASMI**<br><small>ASM.AS</small> | 753.40 EUR | +50% | +1.7% | +42% | -7% | 33 | -0.10 | 0.0% → 0.0% | – | analyst α +0.15 · momentum -0.12 |
| 🔴 Sell | -0.28 | **INTC**<br><small>Intel</small> | 92.82 USD | +25% | -4.7% | +184% | +10% | 34 | -0.62 | 0.0% → 0.0% | – | analyst α -0.27 · momentum +0.26 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.33 | **TER**<br><small>Teradyne</small> | 340.80 USD | +31% | -2.8% | +150% | -1% | 36 | -0.31 | 0.0% → 0.0% | – | quality -0.21 · momentum +0.20 |
| 🔴 Sell | -0.38 | **Disco**<br><small>6146.T</small> | 53,270 JPY | +53% | +3.1% | +16% | -18% | 39 | +0.06 | 0.0% → 0.0% | – | analyst α +0.27 · momentum -0.26 |
| 🔴 Sell | -0.49 | **AMKR**<br><small>Amkor Technology</small> | 42.92 USD | +78% | +8.6% | +56% | -25% | 32 | -1.00 | 0.0% → 0.0% | – | analyst α +0.55 · quality -0.43 |
| 🔴 Sell | -0.72 | **TXN**<br><small>Texas Instruments</small> | 277.77 USD | +17% | -5.6% | +54% | +10% | 49 | +0.24 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.12 |
| 🔴🔴 Strong Sell | -1.01 | **ENTG**<br><small>Entegris</small> | 145.52 USD | +19% | -5.5% | +44% | +7% | 43 | -0.02 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.10 |
| 🔴🔴 Strong Sell | -1.03 | **CDNS**<br><small>Cadence Design Systems</small> | 320.94 USD | +26% | -3.5% | -14% | -2% | 45 | +0.31 | 0.0% → 0.0% | – | momentum -0.35 · analyst α -0.19 |
| 🔴🔴 Strong Sell | -1.04 | **Shin-Etsu**<br><small>4063.T</small> | 5,992 JPY | +30% | -2.4% | +20% | -4% | 49 | -0.20 | 0.0% → 0.0% | – | momentum -0.17 · quality -0.11 |
| 🔴🔴 Strong Sell | -1.04 | **QCOM**<br><small>Qualcomm</small> | 175.64 USD | +11% | -7.4% | +17% | +5% | 46 | +0.70 | 0.0% → 0.0% | – | analyst α -0.66 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.10 | **SMIC**<br><small>0981.HK</small> | 52.15 HKD | +84% | +11.6% | -33% | -24% | 24 | -0.99 | 0.0% → 0.0% | – | analyst α +0.66 · momentum -0.53 · ⚠️ oversold |
| 🔴🔴 Strong Sell | -1.12 | **AMD**<br><small>Advanced Micro Devices</small> | 543.91 USD | +14% | -7.8% | +135% | +39% | 41 | -0.15 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -1.28 | **ARM**<br><small>Arm Holdings</small> | 236.26 USD | +22% | -6.9% | +45% | +6% | 35 | +0.04 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.06 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.36 | **SNPS**<br><small>Synopsys</small> | 461.77 USD | +23% | -4.3% | -15% | +4% | 52 | +0.14 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.23 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.60"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 908.28 USD (+67%, 46 analysts); de-biased α +5.8% vs CAPM hurdle 14.0%. Uptrend +27% vs 200-day avg; 12-1 mom +396%; RSI 36. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.10"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 206,500 KRW (+131%, 36 analysts); de-biased α +22.6% vs CAPM hurdle 11.3%. Downtrend -11% vs 200-day avg; 12-1 mom +227%; RSI 27. Quality z -0.26 (ROE 11%). ⚠️ oversold; cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.87"
    Within rebalance band of target 10.0%: no trade. No reliable analyst target: α set to 0. Downtrend -14% vs 200-day avg; 12-1 mom +452%; RSI 25. Quality z +0.62 (ROE 44%). ⚠️ oversold; cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "Infineon (IFX.DE) — 🟢🟢 Strong Buy, score +0.90"
    Within rebalance band of target 9.9%: no trade. Analyst target 86.74 EUR vs 51.85 EUR (+67%, 23 analysts); de-biased α +5.9% vs CAPM hurdle 14.1%. Downtrend -8% vs 200-day avg; 12-1 mom +67%; RSI 36. Quality z -0.04 (ROE 6%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.70"
    Within rebalance band of target 7.8%: no trade. Analyst target 327.70 USD vs 216.39 USD (+51%, 59 analysts); de-biased α +1.8% vs CAPM hurdle 13.9%. Uptrend +7% vs 200-day avg; 12-1 mom +19%; RSI 40. Quality z +0.47 (ROE 101%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.69"
    Within rebalance band of target 6.4%: no trade. Analyst target 638.94 USD vs 426.57 USD (+50%, 36 analysts); de-biased α +2.1% vs CAPM hurdle 11.6%. Downtrend -3% vs 200-day avg; 12-1 mom +91%; RSI 32. Quality z +0.03 (ROE 36%).

??? success "TSM (TSM) — 🟢 Buy, score +0.57"
    Within rebalance band of target 7.6%: no trade. Analyst target 552.26 USD vs 416.83 USD (+32%, 20 analysts); de-biased α -2.0% vs CAPM hurdle 10.8%. Uptrend +6% vs 200-day avg; 12-1 mom +43%; RSI 36. Quality z +0.58 (ROE 35%).

??? success "ASX (ASX) — 🟢 Buy, score +0.55"
    **ADD 339 sh** → target 5.7% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 51.00 USD vs 41.53 USD (+23%, 1 analysts); de-biased α -2.3% vs CAPM hurdle 11.9%. Uptrend +30% vs 200-day avg; 12-1 mom +239%; RSI 43. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "KLAC (KLAC) — 🟢 Buy, score +0.53"
    **TRIM 93 sh** → target 5.3% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 233.77 USD vs 172.43 USD (+36%, 26 analysts); de-biased α -1.4% vs CAPM hurdle 11.1%. Downtrend -4% vs 200-day avg; 12-1 mom +64%; RSI 35. Quality z +0.51 (ROE 87%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.25"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 10,340 JPY (+48%, 23 analysts); de-biased α +1.4% vs CAPM hurdle 12.8%. Uptrend +5% vs 200-day avg; 12-1 mom +102%; RSI 40. Quality z -0.28 (ROE 29%).

??? note "Advantest (6857.T) — ⚪ Hold, score +0.23"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 34,350 JPY (+24%, 21 analysts); de-biased α -4.8% vs CAPM hurdle 13.4%. Uptrend +22% vs 200-day avg; 12-1 mom +132%; RSI 44. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.23"
    Hold zone: not owned, no entry. Analyst target 375.06 USD vs 271.59 USD (+38%, 31 analysts); de-biased α -1.1% vs CAPM hurdle 12.6%. Downtrend -3% vs 200-day avg; 12-1 mom +95%; RSI 33. Quality z +0.02 (ROE 65%).

??? note "MRVL (MRVL) — ⚪ Hold, score +0.20"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 234.90 USD (+25%, 43 analysts); de-biased α -4.8% vs CAPM hurdle 14.1%. Uptrend +34% vs 200-day avg; 12-1 mom +167%; RSI 40. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "ASML (ASML) — ⚪ Hold, score +0.14"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,632.20 USD (+28%, 16 analysts); de-biased α -3.4% vs CAPM hurdle 12.3%. Uptrend +4% vs 200-day avg; 12-1 mom +64%; RSI 37. Quality z +0.42 (ROE 50%).

??? note "AVGO (AVGO) — ⚪ Hold, score +0.07"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 340.35 USD (+56%, 47 analysts); de-biased α +3.9% vs CAPM hurdle 11.2%. Downtrend -7% vs 200-day avg; 12-1 mom -1%; RSI 40. Quality z +0.26 (ROE 31%).

??? note "GFS (GFS) — ⚪ Hold, score -0.18"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 47.40 USD (+60%, 22 analysts); de-biased α +4.5% vs CAPM hurdle 12.4%. Downtrend -13% vs 200-day avg; 12-1 mom +23%; RSI 48. Quality z -0.21 (ROE 8%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.27"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 753.40 EUR (+50%, 19 analysts); de-biased α +1.7% vs CAPM hurdle 13.2%. Downtrend -7% vs 200-day avg; 12-1 mom +42%; RSI 33. Quality z -0.10 (ROE 19%).

??? failure "INTC (INTC) — 🔴 Sell, score -0.28"
    Avoid: not owned. Analyst target 116.37 USD vs 92.82 USD (+25%, 43 analysts); de-biased α -4.7% vs CAPM hurdle 14.0%. Uptrend +10% vs 200-day avg; 12-1 mom +184%; RSI 34. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "TER (TER) — 🔴 Sell, score -0.33"
    Avoid: not owned. Analyst target 446.47 USD vs 340.80 USD (+31%, 15 analysts); de-biased α -2.8% vs CAPM hurdle 12.3%. Downtrend -1% vs 200-day avg; 12-1 mom +150%; RSI 36. Quality z -0.31 (ROE 20%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.38"
    Avoid: not owned. Analyst target 81,730 JPY vs 53,270 JPY (+53%, 20 analysts); de-biased α +3.1% vs CAPM hurdle 11.5%. Downtrend -18% vs 200-day avg; 12-1 mom +16%; RSI 39. Quality z +0.06 (ROE 25%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.49"
    Avoid: not owned. Analyst target 76.40 USD vs 42.92 USD (+78%, 10 analysts); de-biased α +8.6% vs CAPM hurdle 14.0%. Downtrend -25% vs 200-day avg; 12-1 mom +56%; RSI 32. Quality z -1.00 (ROE 9%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.72"
    Avoid: not owned. Analyst target 324.71 USD vs 277.77 USD (+17%, 31 analysts); de-biased α -5.6% vs CAPM hurdle 10.8%. Uptrend +10% vs 200-day avg; 12-1 mom +54%; RSI 49. Quality z +0.24 (ROE 30%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -1.01"
    Avoid: not owned. Analyst target 173.36 USD vs 145.52 USD (+19%, 11 analysts); de-biased α -5.5% vs CAPM hurdle 11.0%. Uptrend +7% vs 200-day avg; 12-1 mom +44%; RSI 43. Quality z -0.02 (ROE 6%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.03"
    Avoid: not owned. Analyst target 405.47 USD vs 320.94 USD (+26%, 26 analysts); de-biased α -3.5% vs CAPM hurdle 10.0%. Downtrend -2% vs 200-day avg; 12-1 mom -14%; RSI 45. Quality z +0.31 (ROE 22%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.04"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,992 JPY (+30%, 17 analysts); de-biased α -2.4% vs CAPM hurdle 10.8%. Downtrend -4% vs 200-day avg; 12-1 mom +20%; RSI 49. Quality z -0.20 (ROE 10%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.04"
    Avoid: not owned. Analyst target 194.13 USD vs 175.64 USD (+11%, 30 analysts); de-biased α -7.4% vs CAPM hurdle 11.9%. Uptrend +5% vs 200-day avg; 12-1 mom +17%; RSI 46. Quality z +0.70 (ROE 23%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.10"
    Avoid: not owned. Analyst target 95.99 HKD vs 52.15 HKD (+84%, 21 analysts); de-biased α +11.6% vs CAPM hurdle 7.3%. Downtrend -24% vs 200-day avg; 12-1 mom -33%; RSI 24. Quality z -0.99 (ROE 3%). ⚠️ oversold.

??? failure "AMD (AMD) — 🔴🔴 Strong Sell, score -1.12"
    Avoid: not owned. Analyst target 619.51 USD vs 543.91 USD (+14%, 50 analysts); de-biased α -7.8% vs CAPM hurdle 14.9%. Uptrend +39% vs 200-day avg; 12-1 mom +135%; RSI 41. Quality z -0.15 (ROE 7%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.28"
    Avoid: not owned. Analyst target 288.70 USD vs 236.26 USD (+22%, 40 analysts); de-biased α -6.9% vs CAPM hurdle 19.6%. Uptrend +6% vs 200-day avg; 12-1 mom +45%; RSI 35. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.36"
    Avoid: not owned. Analyst target 569.78 USD vs 461.77 USD (+23%, 26 analysts); de-biased α -4.3% vs CAPM hurdle 10.3%. Uptrend +4% vs 200-day avg; 12-1 mom -15%; RSI 52. Quality z +0.14 (ROE 7%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| IFX.DE | Infineon Technologies | 1,594 | 51.85 EUR | $92,583 | 10.3% | Strong Buy |
| 000660.KS | SK hynix | 98 | 1,251,000 KRW | $91,274 | 10.1% | Strong Buy |
| MU | Micron Technology | 92 | 908.28 USD | $83,562 | 9.3% | Strong Buy |
| NVDA | NVIDIA | 371 | 216.39 USD | $80,281 | 8.9% | Buy |
| TSM | TSMC | 187 | 416.83 USD | $77,946 | 8.7% | Buy |
| 005930.KS | Samsung Electronics | 485 | 206,500 KRW | $74,564 | 8.3% | Strong Buy |
| AMAT | Applied Materials | 156 | 426.57 USD | $66,545 | 7.4% | Buy |
| ASX | ASE Technology | 1,239 | 41.53 USD | $51,449 | 5.7% | Buy |
| ASML | ASML Holding | 30 | 1,632.20 USD | $48,966 | 5.4% | Hold |
| KLAC | KLA Corp | 279 | 172.43 USD | $48,108 | 5.3% | Buy |
| AVGO | Broadcom | 134 | 340.35 USD | $45,607 | 5.1% | Hold |
| 8035.T | Tokyo Electron | 600 | 10,340 JPY | $39,239 | 4.4% | Hold |
| 6857.T | Advantest | 100 | 34,350 JPY | $21,726 | 2.4% | Hold |

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

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 30.2%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
