---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-24 10:56 UTC (Tue Nov 24, 05:56 AM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Tue 05:56) · Tokyo 🔴 closed (Tue 19:56) · Korea 🔴 closed (Tue 19:56) · Hong Kong 🔴 closed (Tue 18:56) · Xetra 🟢 open (Tue 11:56) · Euronext Amsterdam 🟢 open (Tue 11:56)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$817,208** | $311,602 (38%) | $505,606 (62%) | -18.28% | -75.20% | 🔴 Risk-off (-12.9%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $817,208), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| BUY (new) | **NVDA**<br><small>NVIDIA</small> | 318 | 165.18 USD | $52,529 | Queued · NYSE/Nasdaq closed | analyst α +0.36 · quality +0.21 |
| ADD | **MU**<br><small>Micron Technology</small> | 51 | 707.69 USD | $36,092 | Queued · NYSE/Nasdaq closed | analyst α +0.55 · momentum +0.53 · ⚠️ cycle-peak P/E |
| TRIM | **TSM**<br><small>TSMC</small> | 78 | 363.34 USD | $28,341 | Queued · NYSE/Nasdaq closed | quality +0.28 · analyst α -0.23 |
| TRIM | **INTC**<br><small>Intel</small> | 438 | 59.67 USD | $26,135 | Queued · NYSE/Nasdaq closed | momentum +0.30 · analyst α +0.27 · ⚠️ rich valuation, high σ(e) |
| TRIM | **AMAT**<br><small>Applied Materials</small> | 68 | 347.20 USD | $23,610 | Queued · NYSE/Nasdaq closed | analyst α +0.19 · momentum +0.10 |
| TRIM | **MRVL**<br><small>Marvell Technology</small> | 160 | 144.88 USD | $23,181 | Queued · NYSE/Nasdaq closed | analyst α +0.48 · momentum +0.41 · ⚠️ rich valuation |
| TRIM | **ASX**<br><small>ASE Technology</small> | 537 | 31.90 USD | $17,130 | Queued · NYSE/Nasdaq closed | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| ADD | **Samsung**<br><small>005930.KS</small> | 115 | 191,400 KRW | $16,386 | Queued · Korea closed | analyst α +0.85 · momentum +0.23 · ⚠️ cycle-peak P/E |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.02 | **MU**<br><small>Micron Technology</small> | 707.69 USD | +115% | +10.6% | +336% | -9% | 42 | +0.12 | 5.5% → 10.0% | ADD 51 | analyst α +0.55 · momentum +0.53 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.15 | **Samsung**<br><small>005930.KS</small> | 191,400 KRW | +149% | +20.0% | +112% | -20% | 42 | -0.26 | 8.0% → 10.0% | ADD 115 | analyst α +0.85 · momentum +0.23 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.82 | **MRVL**<br><small>Marvell Technology</small> | 144.88 USD | +103% | +7.6% | +202% | -23% | 39 | -0.12 | 10.7% → 7.8% | TRIM 160 | analyst α +0.48 · momentum +0.41 · ⚠️ rich valuation |
| 🟢🟢 Strong Buy | +1.04 | **SK hynix**<br><small>000660.KS</small> | 1,172,000 KRW | – | +0.0% | +107% | -23% | 43 | +0.62 | 4.4% → 4.1% | – | quality +0.33 · momentum +0.20 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +0.97 | **NVDA**<br><small>NVIDIA</small> | 165.18 USD | +98% | +6.5% | +21% | -19% | 43 | +0.47 | 0.0% → 6.4% | BUY 318 | analyst α +0.36 · quality +0.21 |
| 🟢 Buy | +0.58 | **AMAT**<br><small>Applied Materials</small> | 347.20 USD | +84% | +3.6% | +74% | -22% | 43 | +0.03 | 6.2% → 3.3% | TRIM 68 | analyst α +0.19 · momentum +0.10 |
| 🟢 Buy | +0.30 | **INTC**<br><small>Intel</small> | 59.67 USD | +95% | +5.6% | +162% | -32% | 40 | -0.62 | 4.3% → 1.1% | TRIM 438 | momentum +0.30 · analyst α +0.27 · ⚠️ rich valuation, high σ(e) |
| 🟢 Buy | +0.30 | **ASX**<br><small>ASE Technology</small> | 31.90 USD | +60% | -1.2% | +192% | -7% | 43 | -0.68 | 3.9% → 1.8% | TRIM 537 | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.27 | **TSM**<br><small>TSMC</small> | 363.34 USD | +52% | -4.1% | +56% | -10% | 43 | +0.58 | 5.6% → 2.1% | TRIM 78 | quality +0.28 · analyst α -0.23 |
| ⚪ Hold | +0.23 | **Advantest**<br><small>6857.T</small> | 27,275 JPY | +57% | -3.8% | +63% | -7% | 42 | +0.33 | 2.1% → 2.1% | – | analyst α -0.19 · quality +0.16 · ⚠️ rich valuation |
| ⚪ Hold | +0.06 | **Infineon**<br><small>IFX.DE</small> | 46.85 EUR | +85% | +3.3% | +51% | -19% | 41 | -0.04 | 1.4% → 1.4% | – | analyst α +0.12 · quality -0.04 |
| ⚪ Hold | -0.00 | **ASML**<br><small>ASML Holding</small> | 1,383.37 USD | +52% | -4.7% | +65% | -13% | 41 | +0.42 | 0.0% → 0.0% | – | analyst α -0.27 · quality +0.18 |
| ⚪ Hold | -0.02 | **LRCX**<br><small>Lam Research</small> | 209.82 USD | +79% | +2.0% | +67% | -26% | 42 | +0.02 | 3.5% → 3.5% | – | trend -0.14 · analyst α +0.08 |
| ⚪ Hold | -0.02 | **KLAC**<br><small>KLA Corp</small> | 145.92 USD | +60% | -2.3% | +37% | -20% | 46 | +0.51 | 2.7% → 2.7% | – | quality +0.24 · analyst α -0.12 |
| ⚪ Hold | -0.14 | **TER**<br><small>Teradyne</small> | 233.56 USD | +91% | +5.1% | +95% | -33% | 40 | -0.31 | 3.5% → 3.5% | – | trend -0.25 · analyst α +0.23 |
| ⚪ Hold | -0.16 | **AMD**<br><small>Advanced Micro Devices</small> | 454.07 USD | +36% | -9.2% | +161% | +5% | 43 | -0.15 | 0.0% → 0.0% | – | analyst α -0.48 · momentum +0.26 |
| ⚪ Hold | -0.24 | **GFS**<br><small>GlobalFoundries</small> | 38.97 USD | +95% | +6.1% | +33% | -29% | 43 | -0.21 | 0.0% → 0.0% | – | analyst α +0.31 · trend -0.16 |
| 🔴 Sell | -0.38 | **ASMI**<br><small>ASM.AS</small> | 670.20 EUR | +68% | -0.8% | +51% | -17% | 44 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · momentum -0.05 |
| 🔴 Sell | -0.38 | **ARM**<br><small>Arm Holdings</small> | 176.64 USD | +63% | -3.7% | +70% | -25% | 42 | +0.04 | 0.0% → 0.0% | – | analyst α -0.15 · trend -0.10 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.42 | **Tokyo Electron**<br><small>8035.T</small> | 8,916 JPY | +71% | +0.3% | +46% | -14% | 45 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · momentum -0.07 |
| 🔴 Sell | -0.56 | **ENTG**<br><small>Entegris</small> | 142.05 USD | +22% | -11.8% | +91% | +1% | 49 | -0.02 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.21 |
| 🔴 Sell | -0.64 | **AVGO**<br><small>Broadcom</small> | 313.54 USD | +69% | +0.1% | -3% | -14% | 44 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.11 |
| 🔴🔴 Strong Sell | -0.77 | **AMKR**<br><small>Amkor Technology</small> | 34.79 USD | +120% | +11.9% | +16% | -38% | 44 | -1.00 | 0.0% → 0.0% | – | analyst α +0.66 · quality -0.43 |
| 🔴🔴 Strong Sell | -0.77 | **QCOM**<br><small>Qualcomm</small> | 165.37 USD | +17% | -12.8% | +12% | -3% | 47 | +0.70 | 0.0% → 0.0% | – | analyst α -0.66 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.78 | **TXN**<br><small>Texas Instruments</small> | 291.19 USD | +12% | -14.0% | +89% | +10% | 50 | +0.24 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -0.81 | **Disco**<br><small>6146.T</small> | 44,660 JPY | +83% | +3.4% | +7% | -31% | 43 | +0.06 | 0.0% → 0.0% | – | momentum -0.35 · trend -0.18 |
| 🔴🔴 Strong Sell | -0.93 | **SNPS**<br><small>Synopsys</small> | 427.20 USD | +33% | -8.9% | +17% | -3% | 44 | +0.14 | 0.0% → 0.0% | – | analyst α -0.41 · momentum -0.20 |
| 🔴🔴 Strong Sell | -1.04 | **CDNS**<br><small>Cadence Design Systems</small> | 304.26 USD | +33% | -8.8% | +7% | -7% | 44 | +0.31 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.30 |
| 🔴🔴 Strong Sell | -1.29 | **Shin-Etsu**<br><small>4063.T</small> | 5,464 JPY | +42% | -6.4% | +30% | -14% | 42 | -0.20 | 0.0% → 0.0% | – | analyst α -0.31 · momentum -0.14 |
| 🔴🔴 Strong Sell | -1.39 | **SMIC**<br><small>0981.HK</small> | 49.00 HKD | +96% | +7.5% | -38% | -25% | 48 | -0.99 | 0.0% → 0.0% | – | momentum -0.53 · analyst α +0.41 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +3.02"
    **ADD 51 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 1,520.02 USD vs 707.69 USD (+115%, 46 analysts); de-biased α +10.6% vs CAPM hurdle 14.0%. Downtrend -9% vs 200-day avg; 12-1 mom +336%; RSI 42. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.15"
    **ADD 115 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 477,517 KRW vs 191,400 KRW (+149%, 36 analysts); de-biased α +20.0% vs CAPM hurdle 11.3%. Downtrend -20% vs 200-day avg; 12-1 mom +112%; RSI 42. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.82"
    **TRIM 160 sh** → target 7.8% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 293.88 USD vs 144.88 USD (+103%, 43 analysts); de-biased α +7.6% vs CAPM hurdle 14.1%. Downtrend -23% vs 200-day avg; 12-1 mom +202%; RSI 39. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.04"
    Within rebalance band of target 4.1%: no trade. No reliable analyst target: α set to 0. Downtrend -23% vs 200-day avg; 12-1 mom +107%; RSI 43. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "NVDA (NVDA) — 🟢🟢 Strong Buy, score +0.97"
    **BUY (new) 318 sh** → target 6.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 327.70 USD vs 165.18 USD (+98%, 59 analysts); de-biased α +6.5% vs CAPM hurdle 13.9%. Downtrend -19% vs 200-day avg; 12-1 mom +21%; RSI 43. Quality z +0.47 (ROE 101%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.58"
    **TRIM 68 sh** → target 3.3% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 347.20 USD (+84%, 36 analysts); de-biased α +3.6% vs CAPM hurdle 11.6%. Downtrend -22% vs 200-day avg; 12-1 mom +74%; RSI 43. Quality z +0.03 (ROE 36%).

??? success "INTC (INTC) — 🟢 Buy, score +0.30"
    **TRIM 438 sh** → target 1.1% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 116.37 USD vs 59.67 USD (+95%, 43 analysts); de-biased α +5.6% vs CAPM hurdle 14.0%. Downtrend -32% vs 200-day avg; 12-1 mom +162%; RSI 40. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "ASX (ASX) — 🟢 Buy, score +0.30"
    **TRIM 537 sh** → target 1.8% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 51.00 USD vs 31.90 USD (+60%, 1 analysts); de-biased α -1.2% vs CAPM hurdle 11.9%. Downtrend -7% vs 200-day avg; 12-1 mom +192%; RSI 43. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "TSM (TSM) — 🟢 Buy, score +0.27"
    **TRIM 78 sh** → target 2.1% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 552.26 USD vs 363.34 USD (+52%, 20 analysts); de-biased α -4.1% vs CAPM hurdle 10.8%. Downtrend -10% vs 200-day avg; 12-1 mom +56%; RSI 43. Quality z +0.58 (ROE 35%).

??? note "Advantest (6857.T) — ⚪ Hold, score +0.23"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 27,275 JPY (+57%, 21 analysts); de-biased α -3.8% vs CAPM hurdle 13.4%. Downtrend -7% vs 200-day avg; 12-1 mom +63%; RSI 42. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "Infineon (IFX.DE) — ⚪ Hold, score +0.06"
    Hold zone: keep any existing position, no new money. Analyst target 86.74 EUR vs 46.85 EUR (+85%, 23 analysts); de-biased α +3.3% vs CAPM hurdle 14.1%. Downtrend -19% vs 200-day avg; 12-1 mom +51%; RSI 41. Quality z -0.04 (ROE 6%).

??? note "ASML (ASML) — ⚪ Hold, score -0.00"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,383.37 USD (+52%, 16 analysts); de-biased α -4.7% vs CAPM hurdle 12.3%. Downtrend -13% vs 200-day avg; 12-1 mom +65%; RSI 41. Quality z +0.42 (ROE 50%).

??? note "LRCX (LRCX) — ⚪ Hold, score -0.02"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 209.82 USD (+79%, 31 analysts); de-biased α +2.0% vs CAPM hurdle 12.6%. Downtrend -26% vs 200-day avg; 12-1 mom +67%; RSI 42. Quality z +0.02 (ROE 65%).

??? note "KLAC (KLAC) — ⚪ Hold, score -0.02"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 145.92 USD (+60%, 26 analysts); de-biased α -2.3% vs CAPM hurdle 11.1%. Downtrend -20% vs 200-day avg; 12-1 mom +37%; RSI 46. Quality z +0.51 (ROE 87%).

??? note "TER (TER) — ⚪ Hold, score -0.14"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 233.56 USD (+91%, 15 analysts); de-biased α +5.1% vs CAPM hurdle 12.3%. Downtrend -33% vs 200-day avg; 12-1 mom +95%; RSI 40. Quality z -0.31 (ROE 20%).

??? note "AMD (AMD) — ⚪ Hold, score -0.16"
    Hold zone: not owned, no entry. Analyst target 619.51 USD vs 454.07 USD (+36%, 50 analysts); de-biased α -9.2% vs CAPM hurdle 14.9%. Uptrend +5% vs 200-day avg; 12-1 mom +161%; RSI 43. Quality z -0.15 (ROE 7%).

??? note "GFS (GFS) — ⚪ Hold, score -0.24"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 38.97 USD (+95%, 22 analysts); de-biased α +6.1% vs CAPM hurdle 12.4%. Downtrend -29% vs 200-day avg; 12-1 mom +33%; RSI 43. Quality z -0.21 (ROE 8%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.38"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 670.20 EUR (+68%, 19 analysts); de-biased α -0.8% vs CAPM hurdle 13.2%. Downtrend -17% vs 200-day avg; 12-1 mom +51%; RSI 44. Quality z -0.10 (ROE 19%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.38"
    Avoid: not owned. Analyst target 288.70 USD vs 176.64 USD (+63%, 40 analysts); de-biased α -3.7% vs CAPM hurdle 19.6%. Downtrend -25% vs 200-day avg; 12-1 mom +70%; RSI 42. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "Tokyo Electron (8035.T) — 🔴 Sell, score -0.42"
    Avoid: not owned. Analyst target 15,275 JPY vs 8,916 JPY (+71%, 23 analysts); de-biased α +0.3% vs CAPM hurdle 12.8%. Downtrend -14% vs 200-day avg; 12-1 mom +46%; RSI 45. Quality z -0.28 (ROE 29%).

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.56"
    Avoid: not owned. Analyst target 173.36 USD vs 142.05 USD (+22%, 11 analysts); de-biased α -11.8% vs CAPM hurdle 11.0%. Uptrend +1% vs 200-day avg; 12-1 mom +91%; RSI 49. Quality z -0.02 (ROE 6%).

??? failure "AVGO (AVGO) — 🔴 Sell, score -0.64"
    Avoid: not owned. Analyst target 531.31 USD vs 313.54 USD (+69%, 47 analysts); de-biased α +0.1% vs CAPM hurdle 11.2%. Downtrend -14% vs 200-day avg; 12-1 mom -3%; RSI 44. Quality z +0.26 (ROE 31%).

??? failure "AMKR (AMKR) — 🔴🔴 Strong Sell, score -0.77"
    Avoid: not owned. Analyst target 76.40 USD vs 34.79 USD (+120%, 10 analysts); de-biased α +11.9% vs CAPM hurdle 14.0%. Downtrend -38% vs 200-day avg; 12-1 mom +16%; RSI 44. Quality z -1.00 (ROE 9%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.77"
    Avoid: not owned. Analyst target 194.13 USD vs 165.37 USD (+17%, 30 analysts); de-biased α -12.8% vs CAPM hurdle 11.9%. Downtrend -3% vs 200-day avg; 12-1 mom +12%; RSI 47. Quality z +0.70 (ROE 23%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -0.78"
    Avoid: not owned. Analyst target 324.71 USD vs 291.19 USD (+12%, 31 analysts); de-biased α -14.0% vs CAPM hurdle 10.8%. Uptrend +10% vs 200-day avg; 12-1 mom +89%; RSI 50. Quality z +0.24 (ROE 30%).

??? failure "Disco (6146.T) — 🔴🔴 Strong Sell, score -0.81"
    Avoid: not owned. Analyst target 81,730 JPY vs 44,660 JPY (+83%, 20 analysts); de-biased α +3.4% vs CAPM hurdle 11.5%. Downtrend -31% vs 200-day avg; 12-1 mom +7%; RSI 43. Quality z +0.06 (ROE 25%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.93"
    Avoid: not owned. Analyst target 569.78 USD vs 427.20 USD (+33%, 26 analysts); de-biased α -8.9% vs CAPM hurdle 10.3%. Downtrend -3% vs 200-day avg; 12-1 mom +17%; RSI 44. Quality z +0.14 (ROE 7%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.04"
    Avoid: not owned. Analyst target 405.47 USD vs 304.26 USD (+33%, 26 analysts); de-biased α -8.8% vs CAPM hurdle 10.0%. Downtrend -7% vs 200-day avg; 12-1 mom +7%; RSI 44. Quality z +0.31 (ROE 22%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.29"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,464 JPY (+42%, 17 analysts); de-biased α -6.4% vs CAPM hurdle 10.8%. Downtrend -14% vs 200-day avg; 12-1 mom +30%; RSI 42. Quality z -0.20 (ROE 10%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.39"
    Avoid: not owned. Analyst target 95.99 HKD vs 49.00 HKD (+96%, 21 analysts); de-biased α +7.5% vs CAPM hurdle 7.3%. Downtrend -25% vs 200-day avg; 12-1 mom -38%; RSI 48. Quality z -0.99 (ROE 3%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MRVL | Marvell Technology | 601 | 144.88 USD | $87,073 | 10.7% | Strong Buy |
| 005930.KS | Samsung Electronics | 458 | 191,400 KRW | $65,258 | 8.0% | Strong Buy |
| AMAT | Applied Materials | 146 | 347.20 USD | $50,691 | 6.2% | Buy |
| TSM | TSMC | 127 | 363.34 USD | $46,144 | 5.6% | Buy |
| MU | Micron Technology | 64 | 707.69 USD | $45,292 | 5.5% | Strong Buy |
| 000660.KS | SK hynix | 41 | 1,172,000 KRW | $35,771 | 4.4% | Strong Buy |
| INTC | Intel | 595 | 59.67 USD | $35,504 | 4.3% | Buy |
| ASX | ASE Technology | 1,010 | 31.90 USD | $32,219 | 3.9% | Buy |
| TER | Teradyne | 123 | 233.56 USD | $28,728 | 3.5% | Hold |
| LRCX | Lam Research | 136 | 209.82 USD | $28,536 | 3.5% | Hold |
| KLAC | KLA Corp | 150 | 145.92 USD | $21,888 | 2.7% | Hold |
| 6857.T | Advantest | 100 | 27,275 JPY | $17,122 | 2.1% | Hold |
| IFX.DE | Infineon Technologies | 222 | 46.85 EUR | $11,381 | 1.4% | Hold |

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

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 58.5%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
