---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-25 04:12 UTC (Tue Nov 24, 11:12 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Tue 23:12) · Tokyo 🟢 open (Wed 13:12) · Korea 🟢 open (Wed 13:12) · Hong Kong 🟢 open (Wed 12:12) · Xetra 🔴 closed (Wed 05:12) · Euronext Amsterdam 🔴 closed (Wed 05:12)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$773,981** | $311,602 (40%) | $462,379 (60%) | -22.60% | -77.25% | 🔴 Risk-off (-20.1%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $773,981), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| BUY (new) | **NVDA**<br><small>NVIDIA</small> | 316 | 155.48 USD | $49,132 | Queued · NYSE/Nasdaq closed | analyst α +0.36 · quality +0.21 |
| ADD | **MU**<br><small>Micron Technology</small> | 58 | 629.79 USD | $36,528 | Queued · NYSE/Nasdaq closed | analyst α +0.85 · momentum +0.53 · ⚠️ cycle-peak P/E |
| TRIM | **AMAT**<br><small>Applied Materials</small> | 70 | 323.64 USD | $22,655 | Queued · NYSE/Nasdaq closed | analyst α +0.19 · momentum +0.10 |
| TRIM | **TSM**<br><small>TSMC</small> | 62 | 349.67 USD | $21,680 | Queued · NYSE/Nasdaq closed | quality +0.28 · analyst α -0.23 |
| TRIM | **MRVL**<br><small>Marvell Technology</small> | 123 | 131.58 USD | $16,184 | Queued · NYSE/Nasdaq closed | analyst α +0.55 · momentum +0.41 · ⚠️ rich valuation |
| TRIM | **TER**<br><small>Teradyne</small> | 58 | 213.30 USD | $12,371 | Queued · NYSE/Nasdaq closed | analyst α +0.41 · trend -0.25 |
| TRIM | **INTC**<br><small>Intel</small> | 178 | 54.90 USD | $9,771 | Queued · NYSE/Nasdaq closed | analyst α +0.48 · momentum +0.30 · ⚠️ rich valuation, high σ(e) |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.53 | **MU**<br><small>Micron Technology</small> | 629.79 USD | +141% | +14.7% | +336% | -19% | 37 | +0.12 | 5.2% → 10.0% | ADD 58 | analyst α +0.85 · momentum +0.53 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.90 | **MRVL**<br><small>Marvell Technology</small> | 131.58 USD | +123% | +10.2% | +202% | -30% | 35 | -0.12 | 10.2% → 8.1% | TRIM 123 | analyst α +0.55 · momentum +0.41 · ⚠️ rich valuation |
| 🟢🟢 Strong Buy | +1.00 | **SK hynix**<br><small>000660.KS</small> | 1,050,000 KRW | – | +0.0% | +120% | -31% | 37 | +0.62 | 4.1% → 4.0% | – | quality +0.33 · momentum +0.20 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +0.96 | **NVDA**<br><small>NVIDIA</small> | 155.48 USD | +111% | +7.1% | +21% | -23% | 40 | +0.47 | 0.0% → 6.4% | BUY 316 | analyst α +0.36 · quality +0.21 |
| 🟢🟢 Strong Buy | +0.78 | **INTC**<br><small>Intel</small> | 54.90 USD | +112% | +7.3% | +162% | -37% | 36 | -0.62 | 4.2% → 3.0% | TRIM 178 | analyst α +0.48 · momentum +0.30 · ⚠️ rich valuation, high σ(e) |
| 🟢 Buy | +0.56 | **AMAT**<br><small>Applied Materials</small> | 323.64 USD | +97% | +4.4% | +74% | -27% | 39 | +0.03 | 6.1% → 3.2% | TRIM 70 | analyst α +0.19 · momentum +0.10 |
| 🟢 Buy | +0.43 | **Advantest**<br><small>6857.T</small> | 23,765 JPY | +80% | -0.6% | +57% | -19% | 36 | +0.33 | 1.9% → 1.9% | – | quality +0.16 · trend +0.03 · ⚠️ rich valuation |
| 🟢 Buy | +0.37 | **TSM**<br><small>TSMC</small> | 349.67 USD | +58% | -5.2% | +56% | -13% | 40 | +0.58 | 5.7% → 2.9% | TRIM 62 | quality +0.28 · analyst α -0.23 |
| 🟢 Buy | +0.31 | **TER**<br><small>Teradyne</small> | 213.30 USD | +109% | +7.1% | +95% | -39% | 36 | -0.31 | 3.4% → 1.8% | TRIM 58 | analyst α +0.41 · trend -0.25 |
| ⚪ Hold | +0.18 | **Infineon**<br><small>IFX.DE</small> | 43.56 EUR | +99% | +4.2% | +51% | -25% | 36 | -0.04 | 1.4% → 1.4% | – | analyst α +0.15 · quality -0.04 |
| ⚪ Hold | +0.17 | **ASX**<br><small>ASE Technology</small> | 29.32 USD | +74% | -0.7% | +192% | -15% | 40 | -0.68 | 3.8% → 3.8% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| ⚪ Hold | +0.14 | **AMD**<br><small>Advanced Micro Devices</small> | 413.24 USD | +50% | -8.4% | +161% | -4% | 39 | -0.15 | 0.0% → 0.0% | – | analyst α -0.31 · momentum +0.26 |
| ⚪ Hold | +0.07 | **Samsung**<br><small>005930.KS</small> | 171,700 KRW | – | +0.0% | +121% | -28% | 34 | -0.26 | 7.6% → 7.6% | – | momentum +0.23 · quality -0.16 · ⚠️ cycle-peak P/E |
| ⚪ Hold | +0.06 | **LRCX**<br><small>Lam Research</small> | 196.18 USD | +91% | +2.6% | +67% | -31% | 39 | +0.02 | 3.4% → 3.4% | – | trend -0.10 · analyst α +0.08 |
| ⚪ Hold | +0.03 | **ASML**<br><small>ASML Holding</small> | 1,335.50 USD | +57% | -5.9% | +65% | -16% | 38 | +0.42 | 0.0% → 0.0% | – | analyst α -0.27 · quality +0.18 |
| ⚪ Hold | -0.10 | **KLAC**<br><small>KLA Corp</small> | 133.71 USD | +75% | -1.1% | +37% | -26% | 40 | +0.51 | 2.6% → 2.6% | – | quality +0.24 · analyst α -0.15 |
| ⚪ Hold | -0.23 | **GFS**<br><small>GlobalFoundries</small> | 36.42 USD | +109% | +7.0% | +33% | -33% | 38 | -0.21 | 0.0% → 0.0% | – | analyst α +0.31 · trend -0.16 |
| 🔴 Sell | -0.29 | **TXN**<br><small>Texas Instruments</small> | 258.58 USD | +26% | -13.0% | +90% | -2% | 39 | +0.24 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.32 |
| 🔴 Sell | -0.37 | **Tokyo Electron**<br><small>8035.T</small> | 7,810 JPY | +96% | +3.8% | +41% | -25% | 36 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · analyst α +0.12 |
| 🔴 Sell | -0.50 | **ARM**<br><small>Arm Holdings</small> | 161.58 USD | +79% | -2.4% | +70% | -31% | 38 | +0.04 | 0.0% → 0.0% | – | analyst α -0.19 · trend -0.12 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.50 | **ASMI**<br><small>ASM.AS</small> | 635.20 EUR | +78% | -1.0% | +51% | -22% | 40 | -0.10 | 0.0% → 0.0% | – | analyst α -0.12 · quality -0.06 |
| 🔴 Sell | -0.60 | **Disco**<br><small>6146.T</small> | 40,640 JPY | +101% | +5.5% | -1% | -37% | 37 | +0.06 | 0.0% → 0.0% | – | momentum -0.35 · analyst α +0.23 |
| 🔴 Sell | -0.66 | **ENTG**<br><small>Entegris</small> | 127.81 USD | +36% | -10.9% | +91% | -9% | 43 | -0.02 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.16 |
| 🔴 Sell | -0.69 | **AVGO**<br><small>Broadcom</small> | 301.23 USD | +76% | -0.7% | -3% | -18% | 41 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.11 |
| 🔴 Sell | -0.74 | **AMKR**<br><small>Amkor Technology</small> | 31.83 USD | +140% | +14.5% | +16% | -43% | 40 | -1.00 | 0.0% → 0.0% | – | analyst α +0.66 · quality -0.43 |
| 🔴🔴 Strong Sell | -0.84 | **SNPS**<br><small>Synopsys</small> | 415.02 USD | +37% | -10.4% | +17% | -6% | 40 | +0.14 | 0.0% → 0.0% | – | analyst α -0.41 · momentum -0.20 |
| 🔴🔴 Strong Sell | -1.04 | **QCOM**<br><small>Qualcomm</small> | 164.97 USD | +18% | -15.2% | +12% | -3% | 47 | +0.70 | 0.0% → 0.0% | – | analyst α -0.85 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.20 | **CDNS**<br><small>Cadence Design Systems</small> | 296.62 USD | +37% | -10.5% | +7% | -10% | 41 | +0.31 | 0.0% → 0.0% | – | analyst α -0.48 · momentum -0.30 |
| 🔴🔴 Strong Sell | -1.23 | **Shin-Etsu**<br><small>4063.T</small> | 5,451 JPY | +42% | -8.8% | +30% | -14% | 41 | -0.20 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.14 |
| 🔴🔴 Strong Sell | -1.51 | **SMIC**<br><small>0981.HK</small> | 47.30 HKD | +103% | +6.8% | -38% | -27% | 44 | -0.99 | 0.0% → 0.0% | – | momentum -0.53 · quality -0.33 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +3.53"
    **ADD 58 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 1,520.02 USD vs 629.79 USD (+141%, 46 analysts); de-biased α +14.7% vs CAPM hurdle 14.0%. Downtrend -19% vs 200-day avg; 12-1 mom +336%; RSI 37. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.90"
    **TRIM 123 sh** → target 8.1% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 293.88 USD vs 131.58 USD (+123%, 43 analysts); de-biased α +10.2% vs CAPM hurdle 14.1%. Downtrend -30% vs 200-day avg; 12-1 mom +202%; RSI 35. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.00"
    Within rebalance band of target 4.0%: no trade. No reliable analyst target: α set to 0. Downtrend -31% vs 200-day avg; 12-1 mom +120%; RSI 37. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "NVDA (NVDA) — 🟢🟢 Strong Buy, score +0.96"
    **BUY (new) 316 sh** → target 6.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 327.70 USD vs 155.48 USD (+111%, 59 analysts); de-biased α +7.1% vs CAPM hurdle 13.9%. Downtrend -23% vs 200-day avg; 12-1 mom +21%; RSI 40. Quality z +0.47 (ROE 101%).

??? success "INTC (INTC) — 🟢🟢 Strong Buy, score +0.78"
    **TRIM 178 sh** → target 3.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 116.37 USD vs 54.90 USD (+112%, 43 analysts); de-biased α +7.3% vs CAPM hurdle 14.0%. Downtrend -37% vs 200-day avg; 12-1 mom +162%; RSI 36. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "AMAT (AMAT) — 🟢 Buy, score +0.56"
    **TRIM 70 sh** → target 3.2% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 323.64 USD (+97%, 36 analysts); de-biased α +4.4% vs CAPM hurdle 11.6%. Downtrend -27% vs 200-day avg; 12-1 mom +74%; RSI 39. Quality z +0.03 (ROE 36%).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.43"
    Within rebalance band of target 1.9%: no trade. Analyst target 42,686 JPY vs 23,765 JPY (+80%, 21 analysts); de-biased α -0.6% vs CAPM hurdle 13.4%. Downtrend -19% vs 200-day avg; 12-1 mom +57%; RSI 36. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? success "TSM (TSM) — 🟢 Buy, score +0.37"
    **TRIM 62 sh** → target 2.9% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 552.26 USD vs 349.67 USD (+58%, 20 analysts); de-biased α -5.2% vs CAPM hurdle 10.8%. Downtrend -13% vs 200-day avg; 12-1 mom +56%; RSI 40. Quality z +0.58 (ROE 35%).

??? success "TER (TER) — 🟢 Buy, score +0.31"
    **TRIM 58 sh** → target 1.8% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 446.47 USD vs 213.30 USD (+109%, 15 analysts); de-biased α +7.1% vs CAPM hurdle 12.3%. Downtrend -39% vs 200-day avg; 12-1 mom +95%; RSI 36. Quality z -0.31 (ROE 20%).

??? note "Infineon (IFX.DE) — ⚪ Hold, score +0.18"
    Hold zone: keep any existing position, no new money. Analyst target 86.74 EUR vs 43.56 EUR (+99%, 23 analysts); de-biased α +4.2% vs CAPM hurdle 14.1%. Downtrend -25% vs 200-day avg; 12-1 mom +51%; RSI 36. Quality z -0.04 (ROE 6%).

??? note "ASX (ASX) — ⚪ Hold, score +0.17"
    Hold zone: keep any existing position, no new money. Analyst target 51.00 USD vs 29.32 USD (+74%, 1 analysts); de-biased α -0.7% vs CAPM hurdle 11.9%. Downtrend -15% vs 200-day avg; 12-1 mom +192%; RSI 40. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? note "AMD (AMD) — ⚪ Hold, score +0.14"
    Hold zone: not owned, no entry. Analyst target 619.51 USD vs 413.24 USD (+50%, 50 analysts); de-biased α -8.4% vs CAPM hurdle 14.9%. Downtrend -4% vs 200-day avg; 12-1 mom +161%; RSI 39. Quality z -0.15 (ROE 7%).

??? note "Samsung (005930.KS) — ⚪ Hold, score +0.07"
    Hold zone: keep any existing position, no new money. No reliable analyst target: α set to 0. Downtrend -28% vs 200-day avg; 12-1 mom +121%; RSI 34. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.06"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 196.18 USD (+91%, 31 analysts); de-biased α +2.6% vs CAPM hurdle 12.6%. Downtrend -31% vs 200-day avg; 12-1 mom +67%; RSI 39. Quality z +0.02 (ROE 65%).

??? note "ASML (ASML) — ⚪ Hold, score +0.03"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,335.50 USD (+57%, 16 analysts); de-biased α -5.9% vs CAPM hurdle 12.3%. Downtrend -16% vs 200-day avg; 12-1 mom +65%; RSI 38. Quality z +0.42 (ROE 50%).

??? note "KLAC (KLAC) — ⚪ Hold, score -0.10"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 133.71 USD (+75%, 26 analysts); de-biased α -1.1% vs CAPM hurdle 11.1%. Downtrend -26% vs 200-day avg; 12-1 mom +37%; RSI 40. Quality z +0.51 (ROE 87%).

??? note "GFS (GFS) — ⚪ Hold, score -0.23"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 36.42 USD (+109%, 22 analysts); de-biased α +7.0% vs CAPM hurdle 12.4%. Downtrend -33% vs 200-day avg; 12-1 mom +33%; RSI 38. Quality z -0.21 (ROE 8%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.29"
    Avoid: not owned. Analyst target 324.71 USD vs 258.58 USD (+26%, 31 analysts); de-biased α -13.0% vs CAPM hurdle 10.8%. Downtrend -2% vs 200-day avg; 12-1 mom +90%; RSI 39. Quality z +0.24 (ROE 30%).

??? failure "Tokyo Electron (8035.T) — 🔴 Sell, score -0.37"
    Avoid: not owned. Analyst target 15,275 JPY vs 7,810 JPY (+96%, 23 analysts); de-biased α +3.8% vs CAPM hurdle 12.8%. Downtrend -25% vs 200-day avg; 12-1 mom +41%; RSI 36. Quality z -0.28 (ROE 29%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.50"
    Avoid: not owned. Analyst target 288.70 USD vs 161.58 USD (+79%, 40 analysts); de-biased α -2.4% vs CAPM hurdle 19.6%. Downtrend -31% vs 200-day avg; 12-1 mom +70%; RSI 38. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.50"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 635.20 EUR (+78%, 19 analysts); de-biased α -1.0% vs CAPM hurdle 13.2%. Downtrend -22% vs 200-day avg; 12-1 mom +51%; RSI 40. Quality z -0.10 (ROE 19%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.60"
    Avoid: not owned. Analyst target 81,730 JPY vs 40,640 JPY (+101%, 20 analysts); de-biased α +5.5% vs CAPM hurdle 11.5%. Downtrend -37% vs 200-day avg; 12-1 mom -1%; RSI 37. Quality z +0.06 (ROE 25%).

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.66"
    Avoid: not owned. Analyst target 173.36 USD vs 127.81 USD (+36%, 11 analysts); de-biased α -10.9% vs CAPM hurdle 11.0%. Downtrend -9% vs 200-day avg; 12-1 mom +91%; RSI 43. Quality z -0.02 (ROE 6%).

??? failure "AVGO (AVGO) — 🔴 Sell, score -0.69"
    Avoid: not owned. Analyst target 531.31 USD vs 301.23 USD (+76%, 47 analysts); de-biased α -0.7% vs CAPM hurdle 11.2%. Downtrend -18% vs 200-day avg; 12-1 mom -3%; RSI 41. Quality z +0.26 (ROE 31%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.74"
    Avoid: not owned. Analyst target 76.40 USD vs 31.83 USD (+140%, 10 analysts); de-biased α +14.5% vs CAPM hurdle 14.0%. Downtrend -43% vs 200-day avg; 12-1 mom +16%; RSI 40. Quality z -1.00 (ROE 9%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.84"
    Avoid: not owned. Analyst target 569.78 USD vs 415.02 USD (+37%, 26 analysts); de-biased α -10.4% vs CAPM hurdle 10.3%. Downtrend -6% vs 200-day avg; 12-1 mom +17%; RSI 40. Quality z +0.14 (ROE 7%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.04"
    Avoid: not owned. Analyst target 194.13 USD vs 164.97 USD (+18%, 30 analysts); de-biased α -15.2% vs CAPM hurdle 11.9%. Downtrend -3% vs 200-day avg; 12-1 mom +12%; RSI 47. Quality z +0.70 (ROE 23%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.20"
    Avoid: not owned. Analyst target 405.47 USD vs 296.62 USD (+37%, 26 analysts); de-biased α -10.5% vs CAPM hurdle 10.0%. Downtrend -10% vs 200-day avg; 12-1 mom +7%; RSI 41. Quality z +0.31 (ROE 22%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.23"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,451 JPY (+42%, 17 analysts); de-biased α -8.8% vs CAPM hurdle 10.8%. Downtrend -14% vs 200-day avg; 12-1 mom +30%; RSI 41. Quality z -0.20 (ROE 10%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.51"
    Avoid: not owned. Analyst target 95.99 HKD vs 47.30 HKD (+103%, 21 analysts); de-biased α +6.8% vs CAPM hurdle 7.3%. Downtrend -27% vs 200-day avg; 12-1 mom -38%; RSI 44. Quality z -0.99 (ROE 3%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MRVL | Marvell Technology | 601 | 131.58 USD | $79,080 | 10.2% | Strong Buy |
| 005930.KS | Samsung Electronics | 458 | 171,700 KRW | $58,538 | 7.6% | Hold |
| AMAT | Applied Materials | 146 | 323.64 USD | $47,251 | 6.1% | Buy |
| TSM | TSMC | 127 | 349.67 USD | $44,408 | 5.7% | Buy |
| MU | Micron Technology | 64 | 629.79 USD | $40,307 | 5.2% | Strong Buy |
| INTC | Intel | 595 | 54.90 USD | $32,663 | 4.2% | Strong Buy |
| 000660.KS | SK hynix | 41 | 1,050,000 KRW | $32,046 | 4.1% | Strong Buy |
| ASX | ASE Technology | 1,010 | 29.32 USD | $29,608 | 3.8% | Hold |
| LRCX | Lam Research | 136 | 196.18 USD | $26,680 | 3.4% | Hold |
| TER | Teradyne | 123 | 213.30 USD | $26,236 | 3.4% | Buy |
| KLAC | KLA Corp | 150 | 133.71 USD | $20,057 | 2.6% | Hold |
| 6857.T | Advantest | 100 | 23,765 JPY | $14,917 | 1.9% | Buy |
| IFX.DE | Infineon Technologies | 222 | 43.56 EUR | $10,588 | 1.4% | Hold |

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

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 68.6%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
