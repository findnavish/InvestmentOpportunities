---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-30 14:10 UTC (Fri Oct 30, 10:10 AM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🟢 open (Fri 10:10) · Tokyo 🔴 closed (Fri 23:10) · Korea 🔴 closed (Fri 23:10) · Hong Kong 🔴 closed (Fri 22:10) · Xetra 🟢 open (Fri 15:10) · Euronext Amsterdam 🟢 open (Fri 15:10)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$900,645** | $84,739 (9%) | $815,906 (91%) | -9.94% | -15.45% | 🟢 Risk-on (+0.4%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $900,645), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| BUY (new) | **INTC**<br><small>Intel</small> | 521 | 65.38 USD | $34,063 | Executed (paper) | analyst α +0.36 · momentum +0.26 · ⚠️ oversold, rich valuation, high σ(e) |
| TRIM | **AMAT**<br><small>Applied Materials</small> | 33 | 399.62 USD | $13,187 | Executed (paper) | momentum +0.14 · analyst α +0.08 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.24 | **SK hynix**<br><small>000660.KS</small> | 1,404,000 KRW | +124% | +17.1% | +265% | -6% | 45 | +0.62 | 11.4% → 10.0% | – | analyst α +0.66 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.45 | **MU**<br><small>Micron Technology</small> | 897.48 USD | +69% | +3.5% | +385% | +20% | 43 | +0.12 | 9.2% → 10.0% | – | momentum +0.53 · analyst α +0.27 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.38 | **Samsung**<br><small>005930.KS</small> | 222,250 KRW | +115% | +15.7% | +180% | -6% | 43 | -0.26 | 9.0% → 10.0% | – | analyst α +0.55 · momentum +0.23 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.58 | **MRVL**<br><small>Marvell Technology</small> | 202.76 USD | +45% | -2.6% | +198% | +11% | 35 | -0.12 | 4.9% → 5.3% | – | momentum +0.30 · trend +0.12 · ⚠️ rich valuation |
| 🟢 Buy | +0.50 | **Infineon**<br><small>IFX.DE</small> | 51.10 EUR | +70% | +3.7% | +74% | -11% | 41 | -0.04 | 8.2% → 7.0% | – | analyst α +0.31 · trend -0.09 |
| 🟢 Buy | +0.46 | **INTC**<br><small>Intel</small> | 65.38 USD | +78% | +5.7% | +190% | -25% | 25 | -0.62 | 3.8% → 3.8% | BUY 521 | analyst α +0.36 · momentum +0.26 · ⚠️ oversold, rich valuation, high σ(e) |
| 🟢 Buy | +0.45 | **ASX**<br><small>ASE Technology</small> | 40.26 USD | +27% | -3.2% | +213% | +21% | 45 | -0.68 | 5.9% → 6.0% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.41 | **AMAT**<br><small>Applied Materials</small> | 399.62 USD | +60% | +1.8% | +126% | -10% | 38 | +0.03 | 5.0% → 4.9% | TRIM 33 | momentum +0.14 · analyst α +0.08 |
| 🟢 Buy | +0.30 | **NVDA**<br><small>NVIDIA</small> | 207.56 USD | +58% | +0.7% | +12% | +2% | 37 | +0.47 | 4.6% → 4.3% | – | quality +0.21 · momentum -0.20 |
| ⚪ Hold | +0.20 | **TSM**<br><small>TSMC</small> | 415.10 USD | +33% | -4.6% | +52% | +4% | 41 | +0.58 | 5.9% → 5.9% | – | quality +0.28 · analyst α -0.15 |
| ⚪ Hold | +0.15 | **Tokyo Electron**<br><small>8035.T</small> | 9,459 JPY | +61% | +2.1% | +104% | -6% | 39 | -0.28 | 3.3% → 3.3% | – | quality -0.18 · analyst α +0.15 |
| ⚪ Hold | +0.08 | **KLAC**<br><small>KLA Corp</small> | 162.45 USD | +44% | -2.0% | +63% | -11% | 43 | +0.51 | 4.8% → 4.8% | – | quality +0.24 · trend -0.10 |
| ⚪ Hold | +0.02 | **LRCX**<br><small>Lam Research</small> | 241.96 USD | +55% | +0.4% | +113% | -15% | 35 | +0.02 | 4.4% → 4.4% | – | momentum +0.12 · trend -0.12 |
| ⚪ Hold | -0.01 | **Advantest**<br><small>6857.T</small> | 34,710 JPY | +23% | -7.9% | +96% | +20% | 49 | +0.33 | 4.9% → 4.9% | – | analyst α -0.41 · trend +0.18 · ⚠️ rich valuation |
| ⚪ Hold | -0.04 | **GFS**<br><small>GlobalFoundries</small> | 42.50 USD | +79% | +6.3% | +42% | -23% | 38 | -0.21 | 0.0% → 0.0% | – | analyst α +0.41 · trend -0.16 |
| ⚪ Hold | -0.06 | **TER**<br><small>Teradyne</small> | 275.77 USD | +62% | +2.1% | +140% | -21% | 29 | -0.31 | 0.0% → 0.0% | – | quality -0.21 · momentum +0.20 · ⚠️ oversold |
| ⚪ Hold | -0.13 | **ASML**<br><small>ASML Holding</small> | 1,594.28 USD | +32% | -5.4% | +70% | +0% | 41 | +0.42 | 5.3% → 5.3% | – | analyst α -0.27 · quality +0.18 |
| ⚪ Hold | -0.19 | **AMD**<br><small>Advanced Micro Devices</small> | 514.96 USD | +20% | -9.0% | +133% | +25% | 41 | -0.15 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.32 |
| 🔴 Sell | -0.37 | **Disco**<br><small>6146.T</small> | 49,340 JPY | +66% | +3.4% | +8% | -25% | 38 | +0.06 | 0.0% → 0.0% | – | analyst α +0.23 · momentum -0.23 |
| 🔴 Sell | -0.41 | **AVGO**<br><small>Broadcom</small> | 329.25 USD | +61% | +2.4% | -10% | -10% | 42 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · analyst α +0.19 |
| 🔴 Sell | -0.47 | **ASMI**<br><small>ASM.AS</small> | 741.00 EUR | +52% | -0.5% | +61% | -9% | 41 | -0.10 | 0.0% → 0.0% | – | momentum -0.10 · quality -0.06 |
| 🔴 Sell | -0.54 | **ARM**<br><small>Arm Holdings</small> | 206.70 USD | +40% | -5.3% | +72% | -10% | 35 | +0.04 | 0.0% → 0.0% | – | analyst α -0.23 · trend -0.04 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.62 | **AMKR**<br><small>Amkor Technology</small> | 40.04 USD | +91% | +9.0% | +63% | -30% | 39 | -1.00 | 0.0% → 0.0% | – | analyst α +0.48 · quality -0.43 |
| 🔴🔴 Strong Sell | -0.75 | **SMIC**<br><small>0981.HK</small> | 42.98 HKD | +123% | +18.7% | -18% | -37% | 22 | -0.99 | 0.0% → 0.0% | – | analyst α +0.85 · momentum -0.53 · ⚠️ oversold |
| 🔴🔴 Strong Sell | -0.90 | **QCOM**<br><small>Qualcomm</small> | 168.53 USD | +15% | -9.0% | +4% | +0% | 41 | +0.70 | 0.0% → 0.0% | – | analyst α -0.55 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.01 | **SNPS**<br><small>Synopsys</small> | 467.38 USD | +22% | -7.4% | +8% | +5% | 53 | +0.14 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.26 |
| 🔴🔴 Strong Sell | -1.07 | **CDNS**<br><small>Cadence Design Systems</small> | 329.61 USD | +23% | -7.1% | +3% | +1% | 50 | +0.31 | 0.0% → 0.0% | – | momentum -0.35 · analyst α -0.31 |
| 🔴🔴 Strong Sell | -1.07 | **Shin-Etsu**<br><small>4063.T</small> | 5,936 JPY | +31% | -4.9% | +21% | -6% | 49 | -0.20 | 0.0% → 0.0% | – | analyst α -0.19 · momentum -0.17 |
| 🔴🔴 Strong Sell | -1.25 | **TXN**<br><small>Texas Instruments</small> | 303.79 USD | +7% | -10.8% | +80% | +18% | 62 | +0.24 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.16 |
| 🔴🔴 Strong Sell | -1.33 | **ENTG**<br><small>Entegris</small> | 154.18 USD | +12% | -9.9% | +68% | +12% | 53 | -0.02 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.14 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.24"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,404,000 KRW (+124%, 38 analysts); de-biased α +17.1% vs CAPM hurdle 14.3%. Downtrend -6% vs 200-day avg; 12-1 mom +265%; RSI 45. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.45"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 897.48 USD (+69%, 46 analysts); de-biased α +3.5% vs CAPM hurdle 14.0%. Uptrend +20% vs 200-day avg; 12-1 mom +385%; RSI 43. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.38"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 222,250 KRW (+115%, 36 analysts); de-biased α +15.7% vs CAPM hurdle 11.3%. Downtrend -6% vs 200-day avg; 12-1 mom +180%; RSI 43. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "MRVL (MRVL) — 🟢 Buy, score +0.58"
    Within rebalance band of target 5.3%: no trade. Analyst target 293.88 USD vs 202.76 USD (+45%, 43 analysts); de-biased α -2.6% vs CAPM hurdle 14.1%. Uptrend +11% vs 200-day avg; 12-1 mom +198%; RSI 35. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.50"
    Within rebalance band of target 7.0%: no trade. Analyst target 86.74 EUR vs 51.10 EUR (+70%, 23 analysts); de-biased α +3.7% vs CAPM hurdle 14.1%. Downtrend -11% vs 200-day avg; 12-1 mom +74%; RSI 41. Quality z -0.04 (ROE 6%).

??? success "INTC (INTC) — 🟢 Buy, score +0.46"
    **BUY (new) 521 sh** → target 3.8% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 116.37 USD vs 65.38 USD (+78%, 43 analysts); de-biased α +5.7% vs CAPM hurdle 14.0%. Downtrend -25% vs 200-day avg; 12-1 mom +190%; RSI 25. Quality z -0.62 (ROE -0%). ⚠️ oversold; price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "ASX (ASX) — 🟢 Buy, score +0.45"
    Within rebalance band of target 6.0%: no trade. Analyst target 51.00 USD vs 40.26 USD (+27%, 1 analysts); de-biased α -3.2% vs CAPM hurdle 11.9%. Uptrend +21% vs 200-day avg; 12-1 mom +213%; RSI 45. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.41"
    **TRIM 33 sh** → target 4.9% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 399.62 USD (+60%, 36 analysts); de-biased α +1.8% vs CAPM hurdle 11.6%. Downtrend -10% vs 200-day avg; 12-1 mom +126%; RSI 38. Quality z +0.03 (ROE 36%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.30"
    Within rebalance band of target 4.3%: no trade. Analyst target 327.70 USD vs 207.56 USD (+58%, 59 analysts); de-biased α +0.7% vs CAPM hurdle 13.9%. Uptrend +2% vs 200-day avg; 12-1 mom +12%; RSI 37. Quality z +0.47 (ROE 101%).

??? note "TSM (TSM) — ⚪ Hold, score +0.20"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 415.10 USD (+33%, 20 analysts); de-biased α -4.6% vs CAPM hurdle 10.8%. Uptrend +4% vs 200-day avg; 12-1 mom +52%; RSI 41. Quality z +0.58 (ROE 35%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.15"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 9,459 JPY (+61%, 23 analysts); de-biased α +2.1% vs CAPM hurdle 12.8%. Downtrend -6% vs 200-day avg; 12-1 mom +104%; RSI 39. Quality z -0.28 (ROE 29%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.08"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 162.45 USD (+44%, 26 analysts); de-biased α -2.0% vs CAPM hurdle 11.1%. Downtrend -11% vs 200-day avg; 12-1 mom +63%; RSI 43. Quality z +0.51 (ROE 87%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.02"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 241.96 USD (+55%, 31 analysts); de-biased α +0.4% vs CAPM hurdle 12.6%. Downtrend -15% vs 200-day avg; 12-1 mom +113%; RSI 35. Quality z +0.02 (ROE 65%).

??? note "Advantest (6857.T) — ⚪ Hold, score -0.01"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 34,710 JPY (+23%, 21 analysts); de-biased α -7.9% vs CAPM hurdle 13.4%. Uptrend +20% vs 200-day avg; 12-1 mom +96%; RSI 49. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "GFS (GFS) — ⚪ Hold, score -0.04"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 42.50 USD (+79%, 22 analysts); de-biased α +6.3% vs CAPM hurdle 12.4%. Downtrend -23% vs 200-day avg; 12-1 mom +42%; RSI 38. Quality z -0.21 (ROE 8%).

??? note "TER (TER) — ⚪ Hold, score -0.06"
    Hold zone: not owned, no entry. Analyst target 446.47 USD vs 275.77 USD (+62%, 15 analysts); de-biased α +2.1% vs CAPM hurdle 12.3%. Downtrend -21% vs 200-day avg; 12-1 mom +140%; RSI 29. Quality z -0.31 (ROE 20%). ⚠️ oversold.

??? note "ASML (ASML) — ⚪ Hold, score -0.13"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,594.28 USD (+32%, 16 analysts); de-biased α -5.4% vs CAPM hurdle 12.3%. Uptrend +0% vs 200-day avg; 12-1 mom +70%; RSI 41. Quality z +0.42 (ROE 50%).

??? note "AMD (AMD) — ⚪ Hold, score -0.19"
    Hold zone: not owned, no entry. Analyst target 619.51 USD vs 514.96 USD (+20%, 50 analysts); de-biased α -9.0% vs CAPM hurdle 14.9%. Uptrend +25% vs 200-day avg; 12-1 mom +133%; RSI 41. Quality z -0.15 (ROE 7%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.37"
    Avoid: not owned. Analyst target 81,730 JPY vs 49,340 JPY (+66%, 20 analysts); de-biased α +3.4% vs CAPM hurdle 11.5%. Downtrend -25% vs 200-day avg; 12-1 mom +8%; RSI 38. Quality z +0.06 (ROE 25%).

??? failure "AVGO (AVGO) — 🔴 Sell, score -0.41"
    Avoid: not owned. Analyst target 531.31 USD vs 329.25 USD (+61%, 47 analysts); de-biased α +2.4% vs CAPM hurdle 11.2%. Downtrend -10% vs 200-day avg; 12-1 mom -10%; RSI 42. Quality z +0.26 (ROE 31%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.47"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 741.00 EUR (+52%, 19 analysts); de-biased α -0.5% vs CAPM hurdle 13.2%. Downtrend -9% vs 200-day avg; 12-1 mom +61%; RSI 41. Quality z -0.10 (ROE 19%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.54"
    Avoid: not owned. Analyst target 288.70 USD vs 206.70 USD (+40%, 40 analysts); de-biased α -5.3% vs CAPM hurdle 19.6%. Downtrend -10% vs 200-day avg; 12-1 mom +72%; RSI 35. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.62"
    Avoid: not owned. Analyst target 76.40 USD vs 40.04 USD (+91%, 10 analysts); de-biased α +9.0% vs CAPM hurdle 14.0%. Downtrend -30% vs 200-day avg; 12-1 mom +63%; RSI 39. Quality z -1.00 (ROE 9%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -0.75"
    Avoid: not owned. Analyst target 95.99 HKD vs 42.98 HKD (+123%, 21 analysts); de-biased α +18.7% vs CAPM hurdle 7.3%. Downtrend -37% vs 200-day avg; 12-1 mom -18%; RSI 22. Quality z -0.99 (ROE 3%). ⚠️ oversold.

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.90"
    Avoid: not owned. Analyst target 194.13 USD vs 168.53 USD (+15%, 30 analysts); de-biased α -9.0% vs CAPM hurdle 11.9%. Uptrend +0% vs 200-day avg; 12-1 mom +4%; RSI 41. Quality z +0.70 (ROE 23%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.01"
    Avoid: not owned. Analyst target 569.78 USD vs 467.38 USD (+22%, 26 analysts); de-biased α -7.4% vs CAPM hurdle 10.3%. Uptrend +5% vs 200-day avg; 12-1 mom +8%; RSI 53. Quality z +0.14 (ROE 7%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.07"
    Avoid: not owned. Analyst target 405.47 USD vs 329.61 USD (+23%, 26 analysts); de-biased α -7.1% vs CAPM hurdle 10.0%. Uptrend +1% vs 200-day avg; 12-1 mom +3%; RSI 50. Quality z +0.31 (ROE 22%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.07"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,936 JPY (+31%, 17 analysts); de-biased α -4.9% vs CAPM hurdle 10.8%. Downtrend -6% vs 200-day avg; 12-1 mom +21%; RSI 49. Quality z -0.20 (ROE 10%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -1.25"
    Avoid: not owned. Analyst target 324.71 USD vs 303.79 USD (+7%, 31 analysts); de-biased α -10.8% vs CAPM hurdle 10.8%. Uptrend +18% vs 200-day avg; 12-1 mom +80%; RSI 62. Quality z +0.24 (ROE 30%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -1.33"
    Avoid: not owned. Analyst target 173.36 USD vs 154.18 USD (+12%, 11 analysts); de-biased α -9.9% vs CAPM hurdle 11.0%. Uptrend +12% vs 200-day avg; 12-1 mom +68%; RSI 53. Quality z -0.02 (ROE 6%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 98 | 1,404,000 KRW | $103,113 | 11.4% | Strong Buy |
| MU | Micron Technology | 92 | 897.48 USD | $82,568 | 9.2% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 222,250 KRW | $80,780 | 9.0% | Strong Buy |
| IFX.DE | Infineon Technologies | 1,301 | 51.10 EUR | $74,057 | 8.2% | Buy |
| ASX | ASE Technology | 1,320 | 40.26 USD | $53,137 | 5.9% | Buy |
| TSM | TSMC | 127 | 415.10 USD | $52,718 | 5.9% | Hold |
| ASML | ASML Holding | 30 | 1,594.28 USD | $47,828 | 5.3% | Hold |
| AMAT | Applied Materials | 112 | 399.62 USD | $44,757 | 5.0% | Buy |
| MRVL | Marvell Technology | 218 | 202.76 USD | $44,202 | 4.9% | Buy |
| 6857.T | Advantest | 200 | 34,710 JPY | $44,151 | 4.9% | Hold |
| KLAC | KLA Corp | 268 | 162.45 USD | $43,535 | 4.8% | Hold |
| NVDA | NVIDIA | 201 | 207.56 USD | $41,720 | 4.6% | Buy |
| LRCX | Lam Research | 162 | 241.96 USD | $39,198 | 4.4% | Hold |
| INTC | Intel | 521 | 65.38 USD | $34,063 | 3.8% | Buy |
| 8035.T | Tokyo Electron | 500 | 9,459 JPY | $30,080 | 3.3% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-10-30 14:10 UTC | BUY (new) | INTC | 521 | 65.38 | $34,063 |
| 2026-10-30 14:10 UTC | TRIM | AMAT | -33 | 399.62 | $13,187 |
| 2026-10-29 14:21 UTC | BUY (new) | MRVL | 218 | 219.82 | $47,921 |
| 2026-10-29 14:21 UTC | TRIM | NVDA | -84 | 213.56 | $17,939 |
| 2026-10-29 14:21 UTC | SELL (exit) | AVGO | -100 | 342.58 | $34,258 |
| 2026-10-28 16:04 UTC | ADD | NVDA | 117 | 217.19 | $25,411 |
| 2026-10-26 19:22 UTC | TRIM | AMAT | -57 | 391.16 | $22,296 |
| 2026-10-26 19:22 UTC | TRIM | NVDA | -58 | 216.65 | $12,566 |
| 2026-10-26 19:22 UTC | TRIM | ASX | -395 | 40.15 | $15,859 |
| 2026-10-26 06:15 UTC | ADD | 6857.T | 100 | 31,220.00 | $19,871 |
| 2026-10-23 19:14 UTC | ADD | KLAC | 57 | 145.31 | $8,282 |
| 2026-10-23 15:05 UTC | ADD | ASX | 383 | 38.70 | $14,822 |
| 2026-10-23 15:05 UTC | TRIM | NVDA | -68 | 212.70 | $14,464 |
| 2026-10-22 15:18 UTC | ADD | LRCX | 57 | 234.49 | $13,366 |
| 2026-10-22 15:18 UTC | ADD | AMAT | 46 | 380.67 | $17,511 |
| 2026-10-22 15:18 UTC | TRIM | TSM | -27 | 414.23 | $11,184 |
| 2026-10-21 19:21 UTC | ADD | TSM | 37 | 430.88 | $15,943 |
| 2026-10-21 15:16 UTC | TRIM | KLAC | -68 | 164.22 | $11,167 |
| 2026-10-20 17:08 UTC | BUY (new) | LRCX | 105 | 263.68 | $27,686 |
| 2026-10-20 17:08 UTC | TRIM | AVGO | -34 | 334.29 | $11,366 |
| 2026-10-20 17:08 UTC | TRIM | NVDA | -77 | 216.83 | $16,696 |
| 2026-10-19 15:37 UTC | TRIM | TSM | -25 | 426.75 | $10,669 |
| 2026-10-19 15:37 UTC | TRIM | ASX | -465 | 41.40 | $19,251 |
| 2026-10-19 01:19 UTC | TRIM | 8035.T | -100 | 10,325.00 | $6,537 |
| 2026-10-16 17:25 UTC | ADD | ASX | 558 | 39.86 | $22,242 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 41.3%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
