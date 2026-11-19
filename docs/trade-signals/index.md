---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-19 21:36 UTC (Thu Nov 19, 04:36 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Thu 16:36) · Tokyo 🔴 closed (Fri 06:36) · Korea 🔴 closed (Fri 06:36) · Hong Kong 🔴 closed (Fri 05:36) · Xetra 🔴 closed (Thu 22:36) · Euronext Amsterdam 🔴 closed (Thu 22:36)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$803,638** | $350,409 (44%) | $453,229 (56%) | -19.64% | -75.60% | 🔴 Risk-off (-14.2%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $803,638), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| ADD | **NVDA**<br><small>NVIDIA</small> | 207 | 146.00 USD | $30,222 | Queued · NYSE/Nasdaq closed | analyst α +0.66 · quality +0.21 · ⚠️ oversold |
| TRIM | **TSM**<br><small>TSMC</small> | 60 | 352.09 USD | $21,125 | Queued · NYSE/Nasdaq closed | quality +0.28 · analyst α -0.12 |
| ADD | **MRVL**<br><small>Marvell Technology</small> | 145 | 138.36 USD | $20,062 | Queued · NYSE/Nasdaq closed | analyst α +0.41 · momentum +0.41 · ⚠️ rich valuation |
| TRIM | **ASX**<br><small>ASE Technology</small> | 308 | 30.48 USD | $9,388 | Queued · NYSE/Nasdaq closed | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| TRIM | **AMAT**<br><small>Applied Materials</small> | 17 | 338.85 USD | $5,760 | Queued · NYSE/Nasdaq closed | analyst α +0.19 · momentum +0.07 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +2.73 | **MU**<br><small>Micron Technology</small> | 690.12 USD | +120% | +11.5% | +300% | -11% | 36 | +0.12 | 10.0% → 10.0% | – | momentum +0.53 · analyst α +0.48 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.13 | **Samsung**<br><small>005930.KS</small> | 193,900 KRW | +146% | +18.8% | +134% | -18% | 39 | -0.26 | 8.3% → 10.0% | – | analyst α +0.85 · momentum +0.23 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.53 | **MRVL**<br><small>Marvell Technology</small> | 138.36 USD | +112% | +9.6% | +212% | -27% | 32 | -0.12 | 4.3% → 6.8% | ADD 145 | analyst α +0.41 · momentum +0.41 · ⚠️ rich valuation |
| 🟢🟢 Strong Buy | +1.26 | **NVDA**<br><small>NVIDIA</small> | 146.00 USD | +124% | +12.6% | +23% | -28% | 20 | +0.47 | 4.9% → 8.6% | ADD 207 | analyst α +0.66 · quality +0.21 · ⚠️ oversold |
| 🟢🟢 Strong Buy | +1.23 | **SK hynix**<br><small>000660.KS</small> | 1,164,000 KRW | – | +0.0% | +124% | -24% | 40 | +0.62 | 4.5% → 5.0% | – | quality +0.33 · momentum +0.20 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢 Buy | +0.48 | **AMAT**<br><small>Applied Materials</small> | 338.85 USD | +89% | +4.3% | +83% | -24% | 37 | +0.03 | 3.5% → 2.8% | TRIM 17 | analyst α +0.19 · momentum +0.07 |
| 🟢 Buy | +0.41 | **INTC**<br><small>Intel</small> | 55.68 USD | +109% | +8.7% | +171% | -36% | 31 | -0.62 | 1.6% → 1.6% | – | analyst α +0.36 · momentum +0.30 · ⚠️ rich valuation, high σ(e) |
| 🟢 Buy | +0.35 | **TSM**<br><small>TSMC</small> | 352.09 USD | +57% | -3.3% | +57% | -12% | 34 | +0.58 | 5.6% → 2.9% | TRIM 60 | quality +0.28 · analyst α -0.12 |
| 🟢 Buy | +0.30 | **LRCX**<br><small>Lam Research</small> | 203.64 USD | +84% | +2.9% | +83% | -28% | 36 | +0.02 | 1.5% → 1.9% | – | analyst α +0.15 · trend -0.12 |
| 🟢 Buy | +0.29 | **ASX**<br><small>ASE Technology</small> | 30.48 USD | +67% | -0.5% | +202% | -11% | 36 | -0.68 | 3.1% → 1.9% | TRIM 308 | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.27 | **Advantest**<br><small>6857.T</small> | 27,200 JPY | +57% | -4.1% | +66% | -8% | 38 | +0.33 | 2.1% → 1.2% | – | quality +0.16 · analyst α -0.15 · ⚠️ rich valuation |
| ⚪ Hold | +0.16 | **TER**<br><small>Teradyne</small> | 227.40 USD | +96% | +6.0% | +111% | -35% | 33 | -0.31 | 1.0% → 1.0% | – | analyst α +0.31 · trend -0.21 |
| ⚪ Hold | +0.14 | **KLAC**<br><small>KLA Corp</small> | 141.38 USD | +65% | -1.4% | +46% | -22% | 40 | +0.51 | 4.7% → 4.7% | – | quality +0.24 · momentum -0.10 |
| ⚪ Hold | +0.12 | **Infineon**<br><small>IFX.DE</small> | 49.35 EUR | +76% | +0.5% | +63% | -14% | 44 | -0.04 | 1.5% → 1.5% | – | analyst α +0.08 · quality -0.04 |
| ⚪ Hold | -0.10 | **ASML**<br><small>ASML Holding</small> | 1,355.88 USD | +55% | -4.3% | +68% | -15% | 34 | +0.42 | 0.0% → 0.0% | – | analyst α -0.27 · quality +0.18 |
| ⚪ Hold | -0.17 | **AMD**<br><small>Advanced Micro Devices</small> | 489.17 USD | +27% | -12.1% | +140% | +14% | 45 | -0.15 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.32 |
| 🔴 Sell | -0.33 | **GFS**<br><small>GlobalFoundries</small> | 38.96 USD | +95% | +5.7% | +46% | -29% | 39 | -0.21 | 0.0% → 0.0% | – | analyst α +0.27 · trend -0.16 |
| 🔴 Sell | -0.36 | **ENTG**<br><small>Entegris</small> | 138.02 USD | +26% | -11.3% | +103% | -1% | 45 | -0.02 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.21 |
| 🔴 Sell | -0.40 | **ASMI**<br><small>ASM.AS</small> | 690.80 EUR | +63% | -2.4% | +60% | -15% | 45 | -0.10 | 0.0% → 0.0% | – | analyst α -0.08 · quality -0.06 |
| 🔴 Sell | -0.49 | **Tokyo Electron**<br><small>8035.T</small> | 8,964 JPY | +70% | -0.4% | +54% | -14% | 43 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · momentum -0.07 |
| 🔴 Sell | -0.52 | **ARM**<br><small>Arm Holdings</small> | 177.29 USD | +63% | -4.2% | +67% | -24% | 38 | +0.04 | 0.0% → 0.0% | – | analyst α -0.19 · trend -0.09 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.66 | **Disco**<br><small>6146.T</small> | 45,400 JPY | +80% | +2.3% | +12% | -30% | 42 | +0.06 | 0.0% → 0.0% | – | momentum -0.26 · trend -0.18 |
| 🔴🔴 Strong Sell | -0.79 | **AMKR**<br><small>Amkor Technology</small> | 34.14 USD | +124% | +12.6% | +43% | -39% | 40 | -1.00 | 0.0% → 0.0% | – | analyst α +0.55 · quality -0.43 |
| 🔴🔴 Strong Sell | -0.89 | **QCOM**<br><small>Qualcomm</small> | 161.95 USD | +20% | -12.6% | +10% | -4% | 42 | +0.70 | 0.0% → 0.0% | – | analyst α -0.66 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.91 | **SNPS**<br><small>Synopsys</small> | 431.03 USD | +32% | -9.6% | +18% | -2% | 40 | +0.14 | 0.0% → 0.0% | – | analyst α -0.41 · momentum -0.23 |
| 🔴🔴 Strong Sell | -0.92 | **TXN**<br><small>Texas Instruments</small> | 285.75 USD | +14% | -13.8% | +84% | +8% | 46 | +0.24 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.25 |
| 🔴🔴 Strong Sell | -0.92 | **AVGO**<br><small>Broadcom</small> | 346.55 USD | +53% | -4.3% | -0% | -6% | 53 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.23 |
| 🔴🔴 Strong Sell | -1.08 | **CDNS**<br><small>Cadence Design Systems</small> | 304.79 USD | +33% | -9.3% | +8% | -7% | 40 | +0.31 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.35 |
| 🔴🔴 Strong Sell | -1.28 | **Shin-Etsu**<br><small>4063.T</small> | 5,541 JPY | +40% | -7.3% | +30% | -12% | 40 | -0.20 | 0.0% → 0.0% | – | analyst α -0.31 · momentum -0.17 |
| 🔴🔴 Strong Sell | -1.60 | **SMIC**<br><small>0981.HK</small> | 50.50 HKD | +90% | +5.7% | -31% | -23% | 52 | -0.99 | 0.0% → 0.0% | – | momentum -0.53 · quality -0.33 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.73"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 690.12 USD (+120%, 46 analysts); de-biased α +11.5% vs CAPM hurdle 14.0%. Downtrend -11% vs 200-day avg; 12-1 mom +300%; RSI 36. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.13"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 193,900 KRW (+146%, 36 analysts); de-biased α +18.8% vs CAPM hurdle 11.3%. Downtrend -18% vs 200-day avg; 12-1 mom +134%; RSI 39. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.53"
    **ADD 145 sh** → target 6.8% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 293.88 USD vs 138.36 USD (+112%, 43 analysts); de-biased α +9.6% vs CAPM hurdle 14.1%. Downtrend -27% vs 200-day avg; 12-1 mom +212%; RSI 32. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? success "NVDA (NVDA) — 🟢🟢 Strong Buy, score +1.26"
    **ADD 207 sh** → target 8.6% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 327.70 USD vs 146.00 USD (+124%, 59 analysts); de-biased α +12.6% vs CAPM hurdle 13.9%. Downtrend -28% vs 200-day avg; 12-1 mom +23%; RSI 20. Quality z +0.47 (ROE 101%). ⚠️ oversold.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.23"
    Within rebalance band of target 5.0%: no trade. No reliable analyst target: α set to 0. Downtrend -24% vs 200-day avg; 12-1 mom +124%; RSI 40. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "AMAT (AMAT) — 🟢 Buy, score +0.48"
    **TRIM 17 sh** → target 2.8% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 338.85 USD (+89%, 36 analysts); de-biased α +4.3% vs CAPM hurdle 11.6%. Downtrend -24% vs 200-day avg; 12-1 mom +83%; RSI 37. Quality z +0.03 (ROE 36%).

??? success "INTC (INTC) — 🟢 Buy, score +0.41"
    Within rebalance band of target 1.6%: no trade. Analyst target 116.37 USD vs 55.68 USD (+109%, 43 analysts); de-biased α +8.7% vs CAPM hurdle 14.0%. Downtrend -36% vs 200-day avg; 12-1 mom +171%; RSI 31. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "TSM (TSM) — 🟢 Buy, score +0.35"
    **TRIM 60 sh** → target 2.9% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 552.26 USD vs 352.09 USD (+57%, 20 analysts); de-biased α -3.3% vs CAPM hurdle 10.8%. Downtrend -12% vs 200-day avg; 12-1 mom +57%; RSI 34. Quality z +0.58 (ROE 35%).

??? success "LRCX (LRCX) — 🟢 Buy, score +0.30"
    Within rebalance band of target 1.9%: no trade. Analyst target 375.06 USD vs 203.64 USD (+84%, 31 analysts); de-biased α +2.9% vs CAPM hurdle 12.6%. Downtrend -28% vs 200-day avg; 12-1 mom +83%; RSI 36. Quality z +0.02 (ROE 65%).

??? success "ASX (ASX) — 🟢 Buy, score +0.29"
    **TRIM 308 sh** → target 1.9% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 51.00 USD vs 30.48 USD (+67%, 1 analysts); de-biased α -0.5% vs CAPM hurdle 11.9%. Downtrend -11% vs 200-day avg; 12-1 mom +202%; RSI 36. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.27"
    Within rebalance band of target 1.2%: no trade. Analyst target 42,686 JPY vs 27,200 JPY (+57%, 21 analysts); de-biased α -4.1% vs CAPM hurdle 13.4%. Downtrend -8% vs 200-day avg; 12-1 mom +66%; RSI 38. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "TER (TER) — ⚪ Hold, score +0.16"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 227.40 USD (+96%, 15 analysts); de-biased α +6.0% vs CAPM hurdle 12.3%. Downtrend -35% vs 200-day avg; 12-1 mom +111%; RSI 33. Quality z -0.31 (ROE 20%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.14"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 141.38 USD (+65%, 26 analysts); de-biased α -1.4% vs CAPM hurdle 11.1%. Downtrend -22% vs 200-day avg; 12-1 mom +46%; RSI 40. Quality z +0.51 (ROE 87%).

??? note "Infineon (IFX.DE) — ⚪ Hold, score +0.12"
    Hold zone: keep any existing position, no new money. Analyst target 86.74 EUR vs 49.35 EUR (+76%, 23 analysts); de-biased α +0.5% vs CAPM hurdle 14.1%. Downtrend -14% vs 200-day avg; 12-1 mom +63%; RSI 44. Quality z -0.04 (ROE 6%).

??? note "ASML (ASML) — ⚪ Hold, score -0.10"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,355.88 USD (+55%, 16 analysts); de-biased α -4.3% vs CAPM hurdle 12.3%. Downtrend -15% vs 200-day avg; 12-1 mom +68%; RSI 34. Quality z +0.42 (ROE 50%).

??? note "AMD (AMD) — ⚪ Hold, score -0.17"
    Hold zone: not owned, no entry. Analyst target 619.51 USD vs 489.17 USD (+27%, 50 analysts); de-biased α -12.1% vs CAPM hurdle 14.9%. Uptrend +14% vs 200-day avg; 12-1 mom +140%; RSI 45. Quality z -0.15 (ROE 7%).

??? failure "GFS (GFS) — 🔴 Sell, score -0.33"
    Avoid: not owned. Analyst target 76.00 USD vs 38.96 USD (+95%, 22 analysts); de-biased α +5.7% vs CAPM hurdle 12.4%. Downtrend -29% vs 200-day avg; 12-1 mom +46%; RSI 39. Quality z -0.21 (ROE 8%).

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.36"
    Avoid: not owned. Analyst target 173.36 USD vs 138.02 USD (+26%, 11 analysts); de-biased α -11.3% vs CAPM hurdle 11.0%. Downtrend -1% vs 200-day avg; 12-1 mom +103%; RSI 45. Quality z -0.02 (ROE 6%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.40"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 690.80 EUR (+63%, 19 analysts); de-biased α -2.4% vs CAPM hurdle 13.2%. Downtrend -15% vs 200-day avg; 12-1 mom +60%; RSI 45. Quality z -0.10 (ROE 19%).

??? failure "Tokyo Electron (8035.T) — 🔴 Sell, score -0.49"
    Avoid: not owned. Analyst target 15,275 JPY vs 8,964 JPY (+70%, 23 analysts); de-biased α -0.4% vs CAPM hurdle 12.8%. Downtrend -14% vs 200-day avg; 12-1 mom +54%; RSI 43. Quality z -0.28 (ROE 29%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.52"
    Avoid: not owned. Analyst target 288.70 USD vs 177.29 USD (+63%, 40 analysts); de-biased α -4.2% vs CAPM hurdle 19.6%. Downtrend -24% vs 200-day avg; 12-1 mom +67%; RSI 38. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "Disco (6146.T) — 🔴 Sell, score -0.66"
    Avoid: not owned. Analyst target 81,730 JPY vs 45,400 JPY (+80%, 20 analysts); de-biased α +2.3% vs CAPM hurdle 11.5%. Downtrend -30% vs 200-day avg; 12-1 mom +12%; RSI 42. Quality z +0.06 (ROE 25%).

??? failure "AMKR (AMKR) — 🔴🔴 Strong Sell, score -0.79"
    Avoid: not owned. Analyst target 76.40 USD vs 34.14 USD (+124%, 10 analysts); de-biased α +12.6% vs CAPM hurdle 14.0%. Downtrend -39% vs 200-day avg; 12-1 mom +43%; RSI 40. Quality z -1.00 (ROE 9%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.89"
    Avoid: not owned. Analyst target 194.13 USD vs 161.95 USD (+20%, 30 analysts); de-biased α -12.6% vs CAPM hurdle 11.9%. Downtrend -4% vs 200-day avg; 12-1 mom +10%; RSI 42. Quality z +0.70 (ROE 23%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.91"
    Avoid: not owned. Analyst target 569.78 USD vs 431.03 USD (+32%, 26 analysts); de-biased α -9.6% vs CAPM hurdle 10.3%. Downtrend -2% vs 200-day avg; 12-1 mom +18%; RSI 40. Quality z +0.14 (ROE 7%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -0.92"
    Avoid: not owned. Analyst target 324.71 USD vs 285.75 USD (+14%, 31 analysts); de-biased α -13.8% vs CAPM hurdle 10.8%. Uptrend +8% vs 200-day avg; 12-1 mom +84%; RSI 46. Quality z +0.24 (ROE 30%).

??? failure "AVGO (AVGO) — 🔴🔴 Strong Sell, score -0.92"
    Avoid: not owned. Analyst target 531.31 USD vs 346.55 USD (+53%, 47 analysts); de-biased α -4.3% vs CAPM hurdle 11.2%. Downtrend -6% vs 200-day avg; 12-1 mom -0%; RSI 53. Quality z +0.26 (ROE 31%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.08"
    Avoid: not owned. Analyst target 405.47 USD vs 304.79 USD (+33%, 26 analysts); de-biased α -9.3% vs CAPM hurdle 10.0%. Downtrend -7% vs 200-day avg; 12-1 mom +8%; RSI 40. Quality z +0.31 (ROE 22%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.28"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,541 JPY (+40%, 17 analysts); de-biased α -7.3% vs CAPM hurdle 10.8%. Downtrend -12% vs 200-day avg; 12-1 mom +30%; RSI 40. Quality z -0.20 (ROE 10%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.60"
    Avoid: not owned. Analyst target 95.99 HKD vs 50.50 HKD (+90%, 21 analysts); de-biased α +5.7% vs CAPM hurdle 7.3%. Downtrend -23% vs 200-day avg; 12-1 mom -31%; RSI 52. Quality z -0.99 (ROE 3%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 116 | 690.12 USD | $80,054 | 10.0% | Strong Buy |
| 005930.KS | Samsung Electronics | 458 | 193,900 KRW | $66,563 | 8.3% | Strong Buy |
| TSM | TSMC | 127 | 352.09 USD | $44,715 | 5.6% | Buy |
| NVDA | NVIDIA | 268 | 146.00 USD | $39,128 | 4.9% | Strong Buy |
| KLAC | KLA Corp | 268 | 141.38 USD | $37,890 | 4.7% | Hold |
| 000660.KS | SK hynix | 41 | 1,164,000 KRW | $35,771 | 4.5% | Strong Buy |
| MRVL | Marvell Technology | 248 | 138.36 USD | $34,313 | 4.3% | Strong Buy |
| AMAT | Applied Materials | 84 | 338.85 USD | $28,463 | 3.5% | Buy |
| ASX | ASE Technology | 805 | 30.48 USD | $24,536 | 3.1% | Buy |
| 6857.T | Advantest | 100 | 27,200 JPY | $17,035 | 2.1% | Buy |
| INTC | Intel | 230 | 55.68 USD | $12,806 | 1.6% | Buy |
| IFX.DE | Infineon Technologies | 225 | 49.35 EUR | $12,183 | 1.5% | Hold |
| LRCX | Lam Research | 58 | 203.64 USD | $11,811 | 1.5% | Buy |
| TER | Teradyne | 35 | 227.40 USD | $7,959 | 1.0% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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
| 2026-11-06 02:27 UTC | TRIM | 6857.T | -100 | 27,610.00 | $17,487 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 60.1%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
