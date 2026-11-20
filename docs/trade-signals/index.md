---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-20 11:54 UTC (Fri Nov 20, 06:54 AM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Fri 06:54) · Tokyo 🔴 closed (Fri 20:54) · Korea 🔴 closed (Fri 20:54) · Hong Kong 🔴 closed (Fri 19:54) · Xetra 🟢 open (Fri 12:54) · Euronext Amsterdam 🟢 open (Fri 12:54)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$795,006** | $343,041 (43%) | $451,965 (57%) | -20.50% | -75.60% | 🔴 Risk-off (-14.2%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $795,006), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| ADD | **NVDA**<br><small>NVIDIA</small> | 249 | 146.00 USD | $36,354 | Queued · NYSE/Nasdaq closed | analyst α +0.85 · quality +0.21 · ⚠️ oversold |
| TRIM | **TSM**<br><small>TSMC</small> | 46 | 352.09 USD | $16,196 | Queued · NYSE/Nasdaq closed | quality +0.28 · analyst α -0.15 |
| ADD | **MRVL**<br><small>Marvell Technology</small> | 103 | 138.36 USD | $14,251 | Queued · NYSE/Nasdaq closed | analyst α +0.48 · momentum +0.41 · ⚠️ rich valuation |
| TRIM | **SK hynix**<br><small>000660.KS</small> | 11 | 1,101,000 KRW | $9,042 | Queued · Korea closed | quality +0.33 · momentum +0.20 · ⚠️ cycle-peak P/E, high σ(e) |
| TRIM | **AMAT**<br><small>Applied Materials</small> | 24 | 338.85 USD | $8,132 | Queued · NYSE/Nasdaq closed | analyst α +0.19 · momentum +0.07 |
| ADD | **Infineon**<br><small>IFX.DE</small> | 144 | 46.65 EUR | $7,364 | Executed (paper) | analyst α +0.15 · momentum +0.05 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.11 | **MU**<br><small>Micron Technology</small> | 690.12 USD | +120% | +11.5% | +280% | -11% | 36 | +0.12 | 10.1% → 10.0% | – | analyst α +0.55 · momentum +0.53 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.82 | **NVDA**<br><small>NVIDIA</small> | 146.00 USD | +124% | +12.6% | +14% | -28% | 20 | +0.47 | 4.9% → 9.5% | ADD 249 | analyst α +0.85 · quality +0.21 · ⚠️ oversold |
| 🟢🟢 Strong Buy | +1.81 | **MRVL**<br><small>Marvell Technology</small> | 138.36 USD | +112% | +9.5% | +175% | -27% | 32 | -0.12 | 4.3% → 6.1% | ADD 103 | analyst α +0.48 · momentum +0.41 · ⚠️ rich valuation |
| 🟢🟢 Strong Buy | +0.98 | **SK hynix**<br><small>000660.KS</small> | 1,101,000 KRW | – | +0.0% | +102% | -28% | 37 | +0.62 | 4.2% → 3.1% | TRIM 11 | quality +0.33 · momentum +0.20 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +0.84 | **Advantest**<br><small>6857.T</small> | 24,255 JPY | +76% | +0.6% | +63% | -18% | 33 | +0.33 | 1.9% → 2.9% | – | quality +0.16 · momentum +0.10 · ⚠️ rich valuation |
| 🟢 Buy | +0.57 | **AMAT**<br><small>Applied Materials</small> | 338.85 USD | +89% | +4.2% | +61% | -24% | 37 | +0.03 | 3.6% → 2.5% | TRIM 24 | analyst α +0.19 · momentum +0.07 |
| 🟢 Buy | +0.57 | **INTC**<br><small>Intel</small> | 55.68 USD | +109% | +8.7% | +143% | -36% | 31 | -0.62 | 1.6% → 1.7% | – | analyst α +0.41 · momentum +0.30 · ⚠️ rich valuation, high σ(e) |
| 🟢 Buy | +0.56 | **TSM**<br><small>TSMC</small> | 352.09 USD | +57% | -3.4% | +57% | -12% | 34 | +0.58 | 5.6% → 3.6% | TRIM 46 | quality +0.28 · analyst α -0.15 |
| 🟢 Buy | +0.46 | **Infineon**<br><small>IFX.DE</small> | 46.65 EUR | +86% | +3.0% | +59% | -19% | 38 | -0.04 | 2.4% → 2.4% | ADD 144 | analyst α +0.15 · momentum +0.05 |
| ⚪ Hold | +0.18 | **ASX**<br><small>ASE Technology</small> | 30.48 USD | +67% | -0.5% | +171% | -11% | 36 | -0.68 | 3.1% → 3.1% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| ⚪ Hold | +0.07 | **TER**<br><small>Teradyne</small> | 227.40 USD | +96% | +6.0% | +84% | -35% | 33 | -0.31 | 1.0% → 1.0% | – | analyst α +0.27 · quality -0.21 |
| ⚪ Hold | +0.01 | **Samsung**<br><small>005930.KS</small> | 182,600 KRW | – | +0.0% | +119% | -23% | 35 | -0.26 | 7.9% → 7.9% | – | momentum +0.23 · quality -0.16 · ⚠️ cycle-peak P/E |
| ⚪ Hold | +0.01 | **LRCX**<br><small>Lam Research</small> | 203.64 USD | +84% | +2.9% | +55% | -28% | 36 | +0.02 | 1.5% → 1.5% | – | analyst α +0.12 · trend -0.12 |
| ⚪ Hold | -0.11 | **KLAC**<br><small>KLA Corp</small> | 141.38 USD | +65% | -1.4% | +27% | -22% | 40 | +0.51 | 4.8% → 4.8% | – | quality +0.24 · momentum -0.14 |
| ⚪ Hold | -0.18 | **AMD**<br><small>Advanced Micro Devices</small> | 489.17 USD | +27% | -12.1% | +127% | +14% | 45 | -0.15 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.32 |
| 🔴 Sell | -0.25 | **Tokyo Electron**<br><small>8035.T</small> | 8,347 JPY | +83% | +2.7% | +55% | -20% | 37 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · analyst α +0.08 |
| 🔴 Sell | -0.25 | **ASMI**<br><small>ASM.AS</small> | 648.60 EUR | +74% | +0.2% | +52% | -20% | 39 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · momentum -0.05 |
| 🔴 Sell | -0.26 | **ASML**<br><small>ASML Holding</small> | 1,355.88 USD | +55% | -4.4% | +51% | -15% | 34 | +0.42 | 0.0% → 0.0% | – | analyst α -0.27 · quality +0.18 |
| 🔴 Sell | -0.28 | **Disco**<br><small>6146.T</small> | 41,390 JPY | +97% | +6.6% | +7% | -36% | 35 | +0.06 | 0.0% → 0.0% | – | analyst α +0.31 · momentum -0.26 |
| 🔴 Sell | -0.39 | **GFS**<br><small>GlobalFoundries</small> | 38.96 USD | +95% | +5.6% | +32% | -29% | 39 | -0.21 | 0.0% → 0.0% | – | analyst α +0.23 · trend -0.16 |
| 🔴 Sell | -0.44 | **ENTG**<br><small>Entegris</small> | 138.02 USD | +26% | -11.4% | +74% | -1% | 45 | -0.02 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.21 |
| 🔴 Sell | -0.64 | **ARM**<br><small>Arm Holdings</small> | 177.29 USD | +63% | -4.3% | +53% | -24% | 38 | +0.04 | 0.0% → 0.0% | – | analyst α -0.19 · trend -0.06 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.64 | **AMKR**<br><small>Amkor Technology</small> | 34.14 USD | +124% | +12.5% | +25% | -39% | 40 | -1.00 | 0.0% → 0.0% | – | analyst α +0.66 · quality -0.43 |
| 🔴🔴 Strong Sell | -0.85 | **TXN**<br><small>Texas Instruments</small> | 285.75 USD | +14% | -13.9% | +84% | +8% | 46 | +0.24 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.25 |
| 🔴🔴 Strong Sell | -0.94 | **QCOM**<br><small>Qualcomm</small> | 161.95 USD | +20% | -12.6% | +6% | -5% | 42 | +0.70 | 0.0% → 0.0% | – | analyst α -0.66 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.96 | **SNPS**<br><small>Synopsys</small> | 431.03 USD | +32% | -9.6% | +9% | -2% | 40 | +0.14 | 0.0% → 0.0% | – | analyst α -0.41 · momentum -0.23 |
| 🔴🔴 Strong Sell | -0.98 | **AVGO**<br><small>Broadcom</small> | 346.55 USD | +53% | -4.4% | -8% | -6% | 53 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.23 |
| 🔴🔴 Strong Sell | -1.14 | **CDNS**<br><small>Cadence Design Systems</small> | 304.79 USD | +33% | -9.3% | +1% | -7% | 40 | +0.31 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.35 |
| 🔴🔴 Strong Sell | -1.26 | **Shin-Etsu**<br><small>4063.T</small> | 5,273 JPY | +47% | -5.6% | +32% | -17% | 32 | -0.20 | 0.0% → 0.0% | – | analyst α -0.31 · momentum -0.12 |
| 🔴🔴 Strong Sell | -1.43 | **SMIC**<br><small>0981.HK</small> | 49.12 HKD | +95% | +6.9% | -36% | -25% | 48 | -0.99 | 0.0% → 0.0% | – | momentum -0.53 · analyst α +0.36 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +3.11"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 690.12 USD (+120%, 46 analysts); de-biased α +11.5% vs CAPM hurdle 14.0%. Downtrend -11% vs 200-day avg; 12-1 mom +280%; RSI 36. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "NVDA (NVDA) — 🟢🟢 Strong Buy, score +1.82"
    **ADD 249 sh** → target 9.5% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 327.70 USD vs 146.00 USD (+124%, 59 analysts); de-biased α +12.6% vs CAPM hurdle 13.9%. Downtrend -28% vs 200-day avg; 12-1 mom +14%; RSI 20. Quality z +0.47 (ROE 101%). ⚠️ oversold.

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.81"
    **ADD 103 sh** → target 6.1% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 293.88 USD vs 138.36 USD (+112%, 43 analysts); de-biased α +9.5% vs CAPM hurdle 14.1%. Downtrend -27% vs 200-day avg; 12-1 mom +175%; RSI 32. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +0.98"
    **TRIM 11 sh** → target 3.1% of NAV (sized ∝ score ÷ σ(e), cap 10%). No reliable analyst target: α set to 0. Downtrend -28% vs 200-day avg; 12-1 mom +102%; RSI 37. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "Advantest (6857.T) — 🟢🟢 Strong Buy, score +0.84"
    Within rebalance band of target 2.9%: no trade. Analyst target 42,686 JPY vs 24,255 JPY (+76%, 21 analysts); de-biased α +0.6% vs CAPM hurdle 13.4%. Downtrend -18% vs 200-day avg; 12-1 mom +63%; RSI 33. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.57"
    **TRIM 24 sh** → target 2.5% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 338.85 USD (+89%, 36 analysts); de-biased α +4.2% vs CAPM hurdle 11.6%. Downtrend -24% vs 200-day avg; 12-1 mom +61%; RSI 37. Quality z +0.03 (ROE 36%).

??? success "INTC (INTC) — 🟢 Buy, score +0.57"
    Within rebalance band of target 1.7%: no trade. Analyst target 116.37 USD vs 55.68 USD (+109%, 43 analysts); de-biased α +8.7% vs CAPM hurdle 14.0%. Downtrend -36% vs 200-day avg; 12-1 mom +143%; RSI 31. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "TSM (TSM) — 🟢 Buy, score +0.56"
    **TRIM 46 sh** → target 3.6% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 552.26 USD vs 352.09 USD (+57%, 20 analysts); de-biased α -3.4% vs CAPM hurdle 10.8%. Downtrend -12% vs 200-day avg; 12-1 mom +57%; RSI 34. Quality z +0.58 (ROE 35%).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.46"
    **ADD 144 sh** → target 2.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 86.74 EUR vs 46.65 EUR (+86%, 23 analysts); de-biased α +3.0% vs CAPM hurdle 14.1%. Downtrend -19% vs 200-day avg; 12-1 mom +59%; RSI 38. Quality z -0.04 (ROE 6%).

??? note "ASX (ASX) — ⚪ Hold, score +0.18"
    Hold zone: keep any existing position, no new money. Analyst target 51.00 USD vs 30.48 USD (+67%, 1 analysts); de-biased α -0.5% vs CAPM hurdle 11.9%. Downtrend -11% vs 200-day avg; 12-1 mom +171%; RSI 36. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? note "TER (TER) — ⚪ Hold, score +0.07"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 227.40 USD (+96%, 15 analysts); de-biased α +6.0% vs CAPM hurdle 12.3%. Downtrend -35% vs 200-day avg; 12-1 mom +84%; RSI 33. Quality z -0.31 (ROE 20%).

??? note "Samsung (005930.KS) — ⚪ Hold, score +0.01"
    Hold zone: keep any existing position, no new money. No reliable analyst target: α set to 0. Downtrend -23% vs 200-day avg; 12-1 mom +119%; RSI 35. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.01"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 203.64 USD (+84%, 31 analysts); de-biased α +2.9% vs CAPM hurdle 12.6%. Downtrend -28% vs 200-day avg; 12-1 mom +55%; RSI 36. Quality z +0.02 (ROE 65%).

??? note "KLAC (KLAC) — ⚪ Hold, score -0.11"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 141.38 USD (+65%, 26 analysts); de-biased α -1.4% vs CAPM hurdle 11.1%. Downtrend -22% vs 200-day avg; 12-1 mom +27%; RSI 40. Quality z +0.51 (ROE 87%).

??? note "AMD (AMD) — ⚪ Hold, score -0.18"
    Hold zone: not owned, no entry. Analyst target 619.51 USD vs 489.17 USD (+27%, 50 analysts); de-biased α -12.1% vs CAPM hurdle 14.9%. Uptrend +14% vs 200-day avg; 12-1 mom +127%; RSI 45. Quality z -0.15 (ROE 7%).

??? failure "Tokyo Electron (8035.T) — 🔴 Sell, score -0.25"
    Avoid: not owned. Analyst target 15,275 JPY vs 8,347 JPY (+83%, 23 analysts); de-biased α +2.7% vs CAPM hurdle 12.8%. Downtrend -20% vs 200-day avg; 12-1 mom +55%; RSI 37. Quality z -0.28 (ROE 29%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.25"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 648.60 EUR (+74%, 19 analysts); de-biased α +0.2% vs CAPM hurdle 13.2%. Downtrend -20% vs 200-day avg; 12-1 mom +52%; RSI 39. Quality z -0.10 (ROE 19%).

??? failure "ASML (ASML) — 🔴 Sell, score -0.26"
    Avoid: not owned. Analyst target 2,096.77 USD vs 1,355.88 USD (+55%, 16 analysts); de-biased α -4.4% vs CAPM hurdle 12.3%. Downtrend -15% vs 200-day avg; 12-1 mom +51%; RSI 34. Quality z +0.42 (ROE 50%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.28"
    Avoid: not owned. Analyst target 81,730 JPY vs 41,390 JPY (+97%, 20 analysts); de-biased α +6.6% vs CAPM hurdle 11.5%. Downtrend -36% vs 200-day avg; 12-1 mom +7%; RSI 35. Quality z +0.06 (ROE 25%).

??? failure "GFS (GFS) — 🔴 Sell, score -0.39"
    Avoid: not owned. Analyst target 76.00 USD vs 38.96 USD (+95%, 22 analysts); de-biased α +5.6% vs CAPM hurdle 12.4%. Downtrend -29% vs 200-day avg; 12-1 mom +32%; RSI 39. Quality z -0.21 (ROE 8%).

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.44"
    Avoid: not owned. Analyst target 173.36 USD vs 138.02 USD (+26%, 11 analysts); de-biased α -11.4% vs CAPM hurdle 11.0%. Downtrend -1% vs 200-day avg; 12-1 mom +74%; RSI 45. Quality z -0.02 (ROE 6%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.64"
    Avoid: not owned. Analyst target 288.70 USD vs 177.29 USD (+63%, 40 analysts); de-biased α -4.3% vs CAPM hurdle 19.6%. Downtrend -24% vs 200-day avg; 12-1 mom +53%; RSI 38. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.64"
    Avoid: not owned. Analyst target 76.40 USD vs 34.14 USD (+124%, 10 analysts); de-biased α +12.5% vs CAPM hurdle 14.0%. Downtrend -39% vs 200-day avg; 12-1 mom +25%; RSI 40. Quality z -1.00 (ROE 9%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -0.85"
    Avoid: not owned. Analyst target 324.71 USD vs 285.75 USD (+14%, 31 analysts); de-biased α -13.9% vs CAPM hurdle 10.8%. Uptrend +8% vs 200-day avg; 12-1 mom +84%; RSI 46. Quality z +0.24 (ROE 30%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.94"
    Avoid: not owned. Analyst target 194.13 USD vs 161.95 USD (+20%, 30 analysts); de-biased α -12.6% vs CAPM hurdle 11.9%. Downtrend -5% vs 200-day avg; 12-1 mom +6%; RSI 42. Quality z +0.70 (ROE 23%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.96"
    Avoid: not owned. Analyst target 569.78 USD vs 431.03 USD (+32%, 26 analysts); de-biased α -9.6% vs CAPM hurdle 10.3%. Downtrend -2% vs 200-day avg; 12-1 mom +9%; RSI 40. Quality z +0.14 (ROE 7%).

??? failure "AVGO (AVGO) — 🔴🔴 Strong Sell, score -0.98"
    Avoid: not owned. Analyst target 531.31 USD vs 346.55 USD (+53%, 47 analysts); de-biased α -4.4% vs CAPM hurdle 11.2%. Downtrend -6% vs 200-day avg; 12-1 mom -8%; RSI 53. Quality z +0.26 (ROE 31%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.14"
    Avoid: not owned. Analyst target 405.47 USD vs 304.79 USD (+33%, 26 analysts); de-biased α -9.3% vs CAPM hurdle 10.0%. Downtrend -7% vs 200-day avg; 12-1 mom +1%; RSI 40. Quality z +0.31 (ROE 22%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.26"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,273 JPY (+47%, 17 analysts); de-biased α -5.6% vs CAPM hurdle 10.8%. Downtrend -17% vs 200-day avg; 12-1 mom +32%; RSI 32. Quality z -0.20 (ROE 10%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.43"
    Avoid: not owned. Analyst target 95.99 HKD vs 49.12 HKD (+95%, 21 analysts); de-biased α +6.9% vs CAPM hurdle 7.3%. Downtrend -25% vs 200-day avg; 12-1 mom -36%; RSI 48. Quality z -0.99 (ROE 3%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 116 | 690.12 USD | $80,054 | 10.1% | Strong Buy |
| 005930.KS | Samsung Electronics | 458 | 182,600 KRW | $62,440 | 7.9% | Hold |
| TSM | TSMC | 127 | 352.09 USD | $44,715 | 5.6% | Buy |
| NVDA | NVIDIA | 268 | 146.00 USD | $39,128 | 4.9% | Strong Buy |
| KLAC | KLA Corp | 268 | 141.38 USD | $37,890 | 4.8% | Hold |
| MRVL | Marvell Technology | 248 | 138.36 USD | $34,313 | 4.3% | Strong Buy |
| 000660.KS | SK hynix | 41 | 1,101,000 KRW | $33,703 | 4.2% | Strong Buy |
| AMAT | Applied Materials | 84 | 338.85 USD | $28,463 | 3.6% | Buy |
| ASX | ASE Technology | 805 | 30.48 USD | $24,536 | 3.1% | Hold |
| IFX.DE | Infineon Technologies | 369 | 46.65 EUR | $18,871 | 2.4% | Buy |
| 6857.T | Advantest | 100 | 24,255 JPY | $15,275 | 1.9% | Strong Buy |
| INTC | Intel | 230 | 55.68 USD | $12,806 | 1.6% | Buy |
| LRCX | Lam Research | 58 | 203.64 USD | $11,811 | 1.5% | Hold |
| TER | Teradyne | 35 | 227.40 USD | $7,959 | 1.0% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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
| 2026-11-10 17:51 UTC | ADD | ASX | 552 | 34.76 | $19,188 |
| 2026-11-10 17:51 UTC | TRIM | INTC | -140 | 57.20 | $8,008 |
| 2026-11-09 17:30 UTC | ADD | NVDA | 119 | 177.94 | $21,175 |
| 2026-11-09 17:30 UTC | ADD | INTC | 112 | 58.31 | $6,531 |
| 2026-11-09 17:30 UTC | TRIM | AMAT | -18 | 370.39 | $6,667 |
| 2026-11-06 17:58 UTC | ADD | AMAT | 20 | 333.00 | $6,660 |
| 2026-11-06 17:58 UTC | SELL (exit) | ASML | -30 | 1,418.92 | $42,568 |
| 2026-11-06 17:58 UTC | TRIM | INTC | -184 | 55.91 | $10,287 |
| 2026-11-06 02:27 UTC | ADD | 005930.KS | 240 | 191,400.00 | $33,864 |
| 2026-11-06 02:27 UTC | TRIM | 000660.KS | -30 | 1,169,000.00 | $25,854 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 60.4%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
