---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-24 00:51 UTC (Mon Nov 23, 07:51 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Mon 19:51) · Tokyo 🟢 open (Tue 09:51) · Korea 🟢 open (Tue 09:51) · Hong Kong 🔴 closed (Tue 08:51) · Xetra 🔴 closed (Tue 01:51) · Euronext Amsterdam 🔴 closed (Tue 01:51)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$817,185** | $311,602 (38%) | $505,583 (62%) | -18.28% | -75.20% | 🔴 Risk-off (-12.9%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $817,185), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| BUY (new) | **NVDA**<br><small>NVIDIA</small> | 340 | 165.18 USD | $56,163 | Queued · NYSE/Nasdaq closed | analyst α +0.41 · quality +0.21 |
| ADD | **MU**<br><small>Micron Technology</small> | 51 | 707.69 USD | $36,092 | Queued · NYSE/Nasdaq closed | analyst α +0.66 · momentum +0.53 · ⚠️ cycle-peak P/E |
| TRIM | **TSM**<br><small>TSMC</small> | 77 | 363.34 USD | $27,977 | Queued · NYSE/Nasdaq closed | quality +0.28 · analyst α -0.23 |
| TRIM | **INTC**<br><small>Intel</small> | 375 | 59.67 USD | $22,376 | Queued · NYSE/Nasdaq closed | analyst α +0.31 · momentum +0.30 · ⚠️ rich valuation, high σ(e) |
| TRIM | **MRVL**<br><small>Marvell Technology</small> | 154 | 144.88 USD | $22,312 | Queued · NYSE/Nasdaq closed | analyst α +0.48 · momentum +0.41 · ⚠️ rich valuation |
| TRIM | **AMAT**<br><small>Applied Materials</small> | 52 | 347.20 USD | $18,054 | Queued · NYSE/Nasdaq closed | analyst α +0.23 · momentum +0.10 |
| TRIM | **ASX**<br><small>ASE Technology</small> | 384 | 31.90 USD | $12,250 | Queued · NYSE/Nasdaq closed | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.51 | **MU**<br><small>Micron Technology</small> | 707.69 USD | +115% | +11.5% | +336% | -9% | 42 | +0.12 | 5.5% → 10.0% | ADD 51 | analyst α +0.66 · momentum +0.53 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.91 | **MRVL**<br><small>Marvell Technology</small> | 144.88 USD | +103% | +8.5% | +199% | -23% | 39 | -0.12 | 10.7% → 7.9% | TRIM 154 | analyst α +0.48 · momentum +0.41 · ⚠️ rich valuation |
| 🟢🟢 Strong Buy | +1.19 | **SK hynix**<br><small>000660.KS</small> | 1,181,000 KRW | – | +0.0% | +107% | -23% | 44 | +0.62 | 4.4% → 4.6% | – | quality +0.33 · momentum +0.20 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +1.07 | **NVDA**<br><small>NVIDIA</small> | 165.18 USD | +98% | +7.4% | +17% | -19% | 43 | +0.47 | 0.0% → 6.9% | BUY 340 | analyst α +0.41 · quality +0.21 |
| 🟢 Buy | +0.73 | **AMAT**<br><small>Applied Materials</small> | 347.20 USD | +84% | +4.4% | +72% | -22% | 43 | +0.03 | 6.2% → 4.0% | TRIM 52 | analyst α +0.23 · momentum +0.10 |
| 🟢 Buy | +0.44 | **INTC**<br><small>Intel</small> | 59.67 USD | +95% | +6.5% | +159% | -32% | 40 | -0.62 | 4.3% → 1.6% | TRIM 375 | analyst α +0.31 · momentum +0.30 · ⚠️ rich valuation, high σ(e) |
| 🟢 Buy | +0.41 | **ASX**<br><small>ASE Technology</small> | 31.90 USD | +60% | -0.8% | +184% | -7% | 43 | -0.68 | 3.9% → 2.4% | TRIM 384 | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.31 | **Advantest**<br><small>6857.T</small> | 27,225 JPY | +57% | -2.9% | +63% | -8% | 42 | +0.33 | 2.1% → 1.4% | – | analyst α -0.19 · quality +0.16 · ⚠️ rich valuation |
| 🟢 Buy | +0.29 | **TSM**<br><small>TSMC</small> | 363.34 USD | +52% | -3.3% | +52% | -10% | 43 | +0.58 | 5.6% → 2.2% | TRIM 77 | quality +0.28 · analyst α -0.23 |
| ⚪ Hold | +0.22 | **LRCX**<br><small>Lam Research</small> | 209.82 USD | +79% | +2.9% | +66% | -26% | 42 | +0.02 | 3.5% → 3.5% | – | analyst α +0.15 · trend -0.14 |
| ⚪ Hold | +0.10 | **Infineon**<br><small>IFX.DE</small> | 48.53 EUR | +79% | +2.6% | +49% | -16% | 45 | -0.04 | 1.4% → 1.4% | – | analyst α +0.12 · quality -0.04 |
| ⚪ Hold | +0.06 | **Samsung**<br><small>005930.KS</small> | 189,900 KRW | – | +0.0% | +112% | -20% | 41 | -0.26 | 7.9% → 7.9% | – | momentum +0.23 · quality -0.16 · ⚠️ cycle-peak P/E |
| ⚪ Hold | +0.01 | **KLAC**<br><small>KLA Corp</small> | 145.92 USD | +60% | -1.4% | +33% | -20% | 46 | +0.51 | 2.7% → 2.7% | – | quality +0.24 · momentum -0.12 |
| ⚪ Hold | -0.04 | **ASML**<br><small>ASML Holding</small> | 1,383.37 USD | +52% | -3.8% | +61% | -13% | 41 | +0.42 | 0.0% → 0.0% | – | analyst α -0.27 · quality +0.18 |
| ⚪ Hold | -0.04 | **TER**<br><small>Teradyne</small> | 233.56 USD | +91% | +6.0% | +98% | -33% | 40 | -0.31 | 3.5% → 3.5% | – | analyst α +0.27 · trend -0.25 |
| ⚪ Hold | -0.10 | **AMKR**<br><small>Amkor Technology</small> | 34.79 USD | +120% | +12.8% | +31% | -38% | 44 | -1.00 | 0.0% → 0.0% | – | analyst α +0.85 · quality -0.43 |
| ⚪ Hold | -0.13 | **GFS**<br><small>GlobalFoundries</small> | 38.97 USD | +95% | +7.0% | +38% | -29% | 43 | -0.21 | 0.0% → 0.0% | – | analyst α +0.36 · trend -0.18 |
| ⚪ Hold | -0.17 | **AMD**<br><small>Advanced Micro Devices</small> | 454.07 USD | +36% | -8.3% | +151% | +5% | 43 | -0.15 | 0.0% → 0.0% | – | analyst α -0.48 · momentum +0.26 |
| 🔴 Sell | -0.39 | **Tokyo Electron**<br><small>8035.T</small> | 9,132 JPY | +67% | +0.1% | +46% | -12% | 47 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · momentum -0.07 |
| 🔴 Sell | -0.54 | **AVGO**<br><small>Broadcom</small> | 313.54 USD | +69% | +1.0% | -7% | -15% | 44 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.11 |
| 🔴 Sell | -0.56 | **ASMI**<br><small>ASM.AS</small> | 695.40 EUR | +62% | -1.4% | +47% | -14% | 47 | -0.10 | 0.0% → 0.0% | – | analyst α -0.12 · quality -0.06 |
| 🔴 Sell | -0.58 | **ARM**<br><small>Arm Holdings</small> | 176.64 USD | +63% | -2.8% | +59% | -25% | 42 | +0.04 | 0.0% → 0.0% | – | analyst α -0.15 · trend -0.10 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.58 | **Disco**<br><small>6146.T</small> | 45,960 JPY | +78% | +3.0% | +7% | -29% | 46 | +0.06 | 0.0% → 0.0% | – | momentum -0.30 · analyst α +0.19 |
| 🔴 Sell | -0.60 | **ENTG**<br><small>Entegris</small> | 142.05 USD | +22% | -10.9% | +96% | +1% | 49 | -0.02 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.21 |
| 🔴 Sell | -0.73 | **QCOM**<br><small>Qualcomm</small> | 165.37 USD | +17% | -11.9% | +13% | -3% | 47 | +0.70 | 0.0% → 0.0% | – | analyst α -0.66 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.84 | **TXN**<br><small>Texas Instruments</small> | 291.19 USD | +12% | -13.1% | +89% | +10% | 50 | +0.24 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -1.12 | **SMIC**<br><small>0981.HK</small> | 48.74 HKD | +97% | +8.7% | -38% | -25% | 47 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.53 |
| 🔴🔴 Strong Sell | -1.16 | **SNPS**<br><small>Synopsys</small> | 427.20 USD | +33% | -8.0% | +12% | -3% | 44 | +0.14 | 0.0% → 0.0% | – | analyst α -0.41 · momentum -0.26 |
| 🔴🔴 Strong Sell | -1.20 | **CDNS**<br><small>Cadence Design Systems</small> | 304.26 USD | +33% | -7.9% | +5% | -7% | 44 | +0.31 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.35 |
| 🔴🔴 Strong Sell | -1.49 | **Shin-Etsu**<br><small>4063.T</small> | 5,430 JPY | +43% | -5.3% | +30% | -14% | 40 | -0.20 | 0.0% → 0.0% | – | analyst α -0.31 · momentum -0.17 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +3.51"
    **ADD 51 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 1,520.02 USD vs 707.69 USD (+115%, 46 analysts); de-biased α +11.5% vs CAPM hurdle 14.0%. Downtrend -9% vs 200-day avg; 12-1 mom +336%; RSI 42. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.91"
    **TRIM 154 sh** → target 7.9% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 293.88 USD vs 144.88 USD (+103%, 43 analysts); de-biased α +8.5% vs CAPM hurdle 14.1%. Downtrend -23% vs 200-day avg; 12-1 mom +199%; RSI 39. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.19"
    Within rebalance band of target 4.6%: no trade. No reliable analyst target: α set to 0. Downtrend -23% vs 200-day avg; 12-1 mom +107%; RSI 44. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "NVDA (NVDA) — 🟢🟢 Strong Buy, score +1.07"
    **BUY (new) 340 sh** → target 6.9% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 327.70 USD vs 165.18 USD (+98%, 59 analysts); de-biased α +7.4% vs CAPM hurdle 13.9%. Downtrend -19% vs 200-day avg; 12-1 mom +17%; RSI 43. Quality z +0.47 (ROE 101%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.73"
    **TRIM 52 sh** → target 4.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 347.20 USD (+84%, 36 analysts); de-biased α +4.4% vs CAPM hurdle 11.6%. Downtrend -22% vs 200-day avg; 12-1 mom +72%; RSI 43. Quality z +0.03 (ROE 36%).

??? success "INTC (INTC) — 🟢 Buy, score +0.44"
    **TRIM 375 sh** → target 1.6% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 116.37 USD vs 59.67 USD (+95%, 43 analysts); de-biased α +6.5% vs CAPM hurdle 14.0%. Downtrend -32% vs 200-day avg; 12-1 mom +159%; RSI 40. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "ASX (ASX) — 🟢 Buy, score +0.41"
    **TRIM 384 sh** → target 2.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 51.00 USD vs 31.90 USD (+60%, 1 analysts); de-biased α -0.8% vs CAPM hurdle 11.9%. Downtrend -7% vs 200-day avg; 12-1 mom +184%; RSI 43. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.31"
    Within rebalance band of target 1.4%: no trade. Analyst target 42,686 JPY vs 27,225 JPY (+57%, 21 analysts); de-biased α -2.9% vs CAPM hurdle 13.4%. Downtrend -8% vs 200-day avg; 12-1 mom +63%; RSI 42. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? success "TSM (TSM) — 🟢 Buy, score +0.29"
    **TRIM 77 sh** → target 2.2% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 552.26 USD vs 363.34 USD (+52%, 20 analysts); de-biased α -3.3% vs CAPM hurdle 10.8%. Downtrend -10% vs 200-day avg; 12-1 mom +52%; RSI 43. Quality z +0.58 (ROE 35%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.22"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 209.82 USD (+79%, 31 analysts); de-biased α +2.9% vs CAPM hurdle 12.6%. Downtrend -26% vs 200-day avg; 12-1 mom +66%; RSI 42. Quality z +0.02 (ROE 65%).

??? note "Infineon (IFX.DE) — ⚪ Hold, score +0.10"
    Hold zone: keep any existing position, no new money. Analyst target 86.74 EUR vs 48.53 EUR (+79%, 23 analysts); de-biased α +2.6% vs CAPM hurdle 14.1%. Downtrend -16% vs 200-day avg; 12-1 mom +49%; RSI 45. Quality z -0.04 (ROE 6%).

??? note "Samsung (005930.KS) — ⚪ Hold, score +0.06"
    Hold zone: keep any existing position, no new money. No reliable analyst target: α set to 0. Downtrend -20% vs 200-day avg; 12-1 mom +112%; RSI 41. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.01"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 145.92 USD (+60%, 26 analysts); de-biased α -1.4% vs CAPM hurdle 11.1%. Downtrend -20% vs 200-day avg; 12-1 mom +33%; RSI 46. Quality z +0.51 (ROE 87%).

??? note "ASML (ASML) — ⚪ Hold, score -0.04"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,383.37 USD (+52%, 16 analysts); de-biased α -3.8% vs CAPM hurdle 12.3%. Downtrend -13% vs 200-day avg; 12-1 mom +61%; RSI 41. Quality z +0.42 (ROE 50%).

??? note "TER (TER) — ⚪ Hold, score -0.04"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 233.56 USD (+91%, 15 analysts); de-biased α +6.0% vs CAPM hurdle 12.3%. Downtrend -33% vs 200-day avg; 12-1 mom +98%; RSI 40. Quality z -0.31 (ROE 20%).

??? note "AMKR (AMKR) — ⚪ Hold, score -0.10"
    Hold zone: not owned, no entry. Analyst target 76.40 USD vs 34.79 USD (+120%, 10 analysts); de-biased α +12.8% vs CAPM hurdle 14.0%. Downtrend -38% vs 200-day avg; 12-1 mom +31%; RSI 44. Quality z -1.00 (ROE 9%).

??? note "GFS (GFS) — ⚪ Hold, score -0.13"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 38.97 USD (+95%, 22 analysts); de-biased α +7.0% vs CAPM hurdle 12.4%. Downtrend -29% vs 200-day avg; 12-1 mom +38%; RSI 43. Quality z -0.21 (ROE 8%).

??? note "AMD (AMD) — ⚪ Hold, score -0.17"
    Hold zone: not owned, no entry. Analyst target 619.51 USD vs 454.07 USD (+36%, 50 analysts); de-biased α -8.3% vs CAPM hurdle 14.9%. Uptrend +5% vs 200-day avg; 12-1 mom +151%; RSI 43. Quality z -0.15 (ROE 7%).

??? failure "Tokyo Electron (8035.T) — 🔴 Sell, score -0.39"
    Avoid: not owned. Analyst target 15,275 JPY vs 9,132 JPY (+67%, 23 analysts); de-biased α +0.1% vs CAPM hurdle 12.8%. Downtrend -12% vs 200-day avg; 12-1 mom +46%; RSI 47. Quality z -0.28 (ROE 29%).

??? failure "AVGO (AVGO) — 🔴 Sell, score -0.54"
    Avoid: not owned. Analyst target 531.31 USD vs 313.54 USD (+69%, 47 analysts); de-biased α +1.0% vs CAPM hurdle 11.2%. Downtrend -15% vs 200-day avg; 12-1 mom -7%; RSI 44. Quality z +0.26 (ROE 31%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.56"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 695.40 EUR (+62%, 19 analysts); de-biased α -1.4% vs CAPM hurdle 13.2%. Downtrend -14% vs 200-day avg; 12-1 mom +47%; RSI 47. Quality z -0.10 (ROE 19%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.58"
    Avoid: not owned. Analyst target 288.70 USD vs 176.64 USD (+63%, 40 analysts); de-biased α -2.8% vs CAPM hurdle 19.6%. Downtrend -25% vs 200-day avg; 12-1 mom +59%; RSI 42. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "Disco (6146.T) — 🔴 Sell, score -0.58"
    Avoid: not owned. Analyst target 81,730 JPY vs 45,960 JPY (+78%, 20 analysts); de-biased α +3.0% vs CAPM hurdle 11.5%. Downtrend -29% vs 200-day avg; 12-1 mom +7%; RSI 46. Quality z +0.06 (ROE 25%).

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.60"
    Avoid: not owned. Analyst target 173.36 USD vs 142.05 USD (+22%, 11 analysts); de-biased α -10.9% vs CAPM hurdle 11.0%. Uptrend +1% vs 200-day avg; 12-1 mom +96%; RSI 49. Quality z -0.02 (ROE 6%).

??? failure "QCOM (QCOM) — 🔴 Sell, score -0.73"
    Avoid: not owned. Analyst target 194.13 USD vs 165.37 USD (+17%, 30 analysts); de-biased α -11.9% vs CAPM hurdle 11.9%. Downtrend -3% vs 200-day avg; 12-1 mom +13%; RSI 47. Quality z +0.70 (ROE 23%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -0.84"
    Avoid: not owned. Analyst target 324.71 USD vs 291.19 USD (+12%, 31 analysts); de-biased α -13.1% vs CAPM hurdle 10.8%. Uptrend +10% vs 200-day avg; 12-1 mom +89%; RSI 50. Quality z +0.24 (ROE 30%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.12"
    Avoid: not owned. Analyst target 95.99 HKD vs 48.74 HKD (+97%, 21 analysts); de-biased α +8.7% vs CAPM hurdle 7.3%. Downtrend -25% vs 200-day avg; 12-1 mom -38%; RSI 47. Quality z -0.99 (ROE 3%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.16"
    Avoid: not owned. Analyst target 569.78 USD vs 427.20 USD (+33%, 26 analysts); de-biased α -8.0% vs CAPM hurdle 10.3%. Downtrend -3% vs 200-day avg; 12-1 mom +12%; RSI 44. Quality z +0.14 (ROE 7%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.20"
    Avoid: not owned. Analyst target 405.47 USD vs 304.26 USD (+33%, 26 analysts); de-biased α -7.9% vs CAPM hurdle 10.0%. Downtrend -7% vs 200-day avg; 12-1 mom +5%; RSI 44. Quality z +0.31 (ROE 22%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.49"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,430 JPY (+43%, 17 analysts); de-biased α -5.3% vs CAPM hurdle 10.8%. Downtrend -14% vs 200-day avg; 12-1 mom +30%; RSI 40. Quality z -0.20 (ROE 10%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MRVL | Marvell Technology | 601 | 144.88 USD | $87,073 | 10.7% | Strong Buy |
| 005930.KS | Samsung Electronics | 458 | 189,900 KRW | $64,647 | 7.9% | Hold |
| AMAT | Applied Materials | 146 | 347.20 USD | $50,691 | 6.2% | Buy |
| TSM | TSMC | 127 | 363.34 USD | $46,144 | 5.6% | Buy |
| MU | Micron Technology | 64 | 707.69 USD | $45,292 | 5.5% | Strong Buy |
| 000660.KS | SK hynix | 41 | 1,181,000 KRW | $35,991 | 4.4% | Strong Buy |
| INTC | Intel | 595 | 59.67 USD | $35,504 | 4.3% | Buy |
| ASX | ASE Technology | 1,010 | 31.90 USD | $32,219 | 3.9% | Buy |
| TER | Teradyne | 123 | 233.56 USD | $28,728 | 3.5% | Hold |
| LRCX | Lam Research | 136 | 209.82 USD | $28,536 | 3.5% | Hold |
| KLAC | KLA Corp | 150 | 145.92 USD | $21,888 | 2.7% | Hold |
| 6857.T | Advantest | 100 | 27,225 JPY | $17,119 | 2.1% | Buy |
| IFX.DE | Infineon Technologies | 222 | 48.53 EUR | $11,753 | 1.4% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-11-23 12:44 UTC | TRIM | IFX.DE | -147 | 47.12 | $7,589 |
| 2026-11-20 20:22 UTC | ADD | INTC | 365 | 52.70 | $19,236 |
| 2026-11-20 20:22 UTC | ADD | MRVL | 353 | 123.14 | $43,470 |
| 2026-11-20 20:22 UTC | ADD | ASX | 205 | 26.54 | $5,441 |
| 2026-11-20 20:22 UTC | ADD | TER | 88 | 204.82 | $18,024 |
| 2026-11-20 20:22 UTC | ADD | LRCX | 78 | 183.03 | $14,277 |
| 2026-11-20 20:22 UTC | ADD | AMAT | 62 | 303.82 | $18,837 |
| 2026-11-20 20:22 UTC | TRIM | MU | -52 | 596.09 | $30,997 |
| 2026-11-20 20:22 UTC | TRIM | KLAC | -118 | 126.94 | $14,979 |
| 2026-11-20 20:22 UTC | SELL (exit) | NVDA | -268 | 128.30 | $34,384 |
| 2026-11-20 11:54 UTC | ADD | IFX.DE | 144 | 46.65 | $7,364 |
| 2026-11-17 03:55 UTC | TRIM | 000660.KS | -47 | 1,144,000.00 | $40,195 |
| 2026-11-16 20:30 UTC | ADD | ASX | 231 | 32.86 | $7,591 |
| 2026-11-16 20:30 UTC | ADD | INTC | 78 | 55.61 | $4,338 |
| 2026-11-16 20:30 UTC | TRIM | NVDA | -69 | 155.52 | $10,731 |
| 2026-11-13 16:26 UTC | ADD | NVDA | 79 | 159.94 | $12,635 |
| 2026-11-13 16:26 UTC | ADD | AMAT | 23 | 357.03 | $8,212 |
| 2026-11-13 16:26 UTC | TRIM | ASX | -290 | 34.86 | $10,109 |
| 2026-11-13 00:26 UTC | TRIM | 005930.KS | -104 | 214,000.00 | $16,663 |
| 2026-11-12 18:57 UTC | ADD | NVDA | 79 | 164.84 | $13,022 |
| 2026-11-12 18:57 UTC | ADD | AMAT | 20 | 386.98 | $7,740 |
| 2026-11-11 15:13 UTC | TRIM | AMAT | -32 | 387.02 | $12,385 |
| 2026-11-11 15:13 UTC | TRIM | MRVL | -76 | 165.15 | $12,551 |
| 2026-11-11 15:13 UTC | TRIM | INTC | -83 | 61.66 | $5,118 |
| 2026-11-11 06:23 UTC | ADD | 000660.KS | 38 | 1,277,000.00 | $36,371 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 55.0%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
