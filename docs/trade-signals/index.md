---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-17 03:55 UTC (Mon Nov 16, 10:55 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Mon 22:55) · Tokyo 🟢 open (Tue 12:55) · Korea 🟢 open (Tue 12:55) · Hong Kong 🟢 open (Tue 11:55) · Xetra 🔴 closed (Tue 04:55) · Euronext Amsterdam 🔴 closed (Tue 04:55)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$816,740** | $350,409 (43%) | $466,331 (57%) | -18.33% | -75.03% | 🔴 Risk-off (-12.0%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $816,740), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **SK hynix**<br><small>000660.KS</small> | 47 | 1,144,000 KRW | $40,195 | Executed (paper) | quality +0.33 · momentum +0.23 · ⚠️ cycle-peak P/E, high σ(e) |
| ADD | **MRVL**<br><small>Marvell Technology</small> | 63 | 145.43 USD | $9,162 | Queued · NYSE/Nasdaq closed | analyst α +0.36 · momentum +0.35 · ⚠️ rich valuation |
| TRIM | **ASX**<br><small>ASE Technology</small> | 154 | 32.80 USD | $5,051 | Queued · NYSE/Nasdaq closed | momentum +0.41 · quality -0.28 · ⚠️ rich valuation |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +2.99 | **MU**<br><small>Micron Technology</small> | 719.07 USD | +111% | +9.9% | +271% | -6% | 38 | +0.12 | 10.2% → 10.0% | – | analyst α +0.55 · momentum +0.53 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.25 | **Samsung**<br><small>005930.KS</small> | 194,000 KRW | +146% | +19.4% | +122% | -18% | 37 | -0.26 | 8.1% → 10.0% | – | analyst α +0.85 · momentum +0.26 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.37 | **MRVL**<br><small>Marvell Technology</small> | 145.43 USD | +102% | +7.6% | +161% | -22% | 33 | -0.12 | 4.4% → 5.5% | ADD 63 | analyst α +0.36 · momentum +0.35 · ⚠️ rich valuation |
| 🟢🟢 Strong Buy | +1.13 | **SK hynix**<br><small>000660.KS</small> | 1,144,000 KRW | – | +0.0% | +121% | -25% | 38 | +0.62 | 4.3% → 4.2% | TRIM 47 | quality +0.33 · momentum +0.23 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +0.93 | **NVDA**<br><small>NVIDIA</small> | 156.16 USD | +110% | +9.6% | +15% | -23% | 23 | +0.47 | 5.1% → 5.8% | – | analyst α +0.48 · momentum -0.23 · ⚠️ oversold |
| 🟢 Buy | +0.63 | **AMAT**<br><small>Applied Materials</small> | 350.46 USD | +82% | +3.3% | +84% | -21% | 39 | +0.03 | 3.6% → 3.3% | – | analyst α +0.15 · momentum +0.14 |
| 🟢 Buy | +0.55 | **INTC**<br><small>Intel</small> | 55.46 USD | +110% | +9.5% | +150% | -37% | 30 | -0.62 | 1.6% → 2.0% | – | analyst α +0.41 · momentum +0.30 · ⚠️ oversold, rich valuation, high σ(e) |
| 🟢 Buy | +0.45 | **ASX**<br><small>ASE Technology</small> | 32.80 USD | +55% | -1.7% | +173% | -4% | 39 | -0.68 | 3.2% → 2.6% | TRIM 154 | momentum +0.41 · quality -0.28 · ⚠️ rich valuation |
| ⚪ Hold | +0.17 | **LRCX**<br><small>Lam Research</small> | 210.93 USD | +78% | +1.9% | +73% | -26% | 38 | +0.02 | 1.5% → 1.5% | – | trend -0.14 · analyst α +0.12 |
| ⚪ Hold | +0.14 | **KLAC**<br><small>KLA Corp</small> | 144.04 USD | +62% | -1.6% | +43% | -21% | 41 | +0.51 | 4.7% → 4.7% | – | quality +0.24 · momentum -0.10 |
| ⚪ Hold | +0.14 | **TSM**<br><small>TSMC</small> | 373.45 USD | +48% | -5.0% | +48% | -7% | 39 | +0.58 | 5.8% → 5.8% | – | quality +0.28 · analyst α -0.23 |
| ⚪ Hold | +0.12 | **Infineon**<br><small>IFX.DE</small> | 49.11 EUR | +77% | +1.3% | +54% | -15% | 43 | -0.04 | 1.5% → 1.5% | – | analyst α +0.08 · quality -0.04 |
| ⚪ Hold | +0.10 | **Advantest**<br><small>6857.T</small> | 26,070 JPY | +64% | -1.8% | +50% | -11% | 35 | +0.33 | 2.0% → 2.0% | – | quality +0.16 · analyst α -0.12 · ⚠️ rich valuation |
| ⚪ Hold | -0.04 | **TER**<br><small>Teradyne</small> | 232.07 USD | +92% | +5.6% | +92% | -34% | 34 | -0.31 | 1.0% → 1.0% | – | analyst α +0.23 · trend -0.21 |
| ⚪ Hold | -0.06 | **ASML**<br><small>ASML Holding</small> | 1,406.51 USD | +49% | -5.1% | +62% | -12% | 36 | +0.42 | 0.0% → 0.0% | – | analyst α -0.27 · quality +0.18 |
| 🔴 Sell | -0.27 | **Tokyo Electron**<br><small>8035.T</small> | 8,777 JPY | +74% | +1.1% | +58% | -15% | 40 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · analyst α +0.05 |
| 🔴 Sell | -0.27 | **ASMI**<br><small>ASM.AS</small> | 668.00 EUR | +69% | -0.4% | +53% | -18% | 39 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · momentum -0.03 |
| 🔴 Sell | -0.32 | **AMD**<br><small>Advanced Micro Devices</small> | 504.37 USD | +23% | -12.5% | +113% | +19% | 47 | -0.15 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.32 |
| 🔴 Sell | -0.34 | **GFS**<br><small>GlobalFoundries</small> | 39.43 USD | +93% | +5.7% | +43% | -28% | 40 | -0.21 | 0.0% → 0.0% | – | analyst α +0.27 · trend -0.16 |
| 🔴 Sell | -0.49 | **Disco**<br><small>6146.T</small> | 43,840 JPY | +86% | +4.5% | +5% | -32% | 38 | +0.06 | 0.0% → 0.0% | – | momentum -0.26 · analyst α +0.19 |
| 🔴 Sell | -0.53 | **ENTG**<br><small>Entegris</small> | 140.02 USD | +24% | -11.2% | +72% | +0% | 46 | -0.02 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.21 |
| 🔴 Sell | -0.55 | **AMKR**<br><small>Amkor Technology</small> | 34.04 USD | +124% | +13.3% | +32% | -40% | 39 | -1.00 | 0.0% → 0.0% | – | analyst α +0.66 · quality -0.43 |
| 🔴 Sell | -0.55 | **ARM**<br><small>Arm Holdings</small> | 175.03 USD | +65% | -3.1% | +62% | -25% | 36 | +0.04 | 0.0% → 0.0% | – | analyst α -0.19 · trend -0.12 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -0.85 | **SNPS**<br><small>Synopsys</small> | 441.33 USD | +29% | -9.8% | +15% | +0% | 44 | +0.14 | 0.0% → 0.0% | – | analyst α -0.41 · momentum -0.20 |
| 🔴🔴 Strong Sell | -0.91 | **AVGO**<br><small>Broadcom</small> | 333.70 USD | +59% | -2.3% | -3% | -9% | 49 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.15 |
| 🔴🔴 Strong Sell | -0.94 | **TXN**<br><small>Texas Instruments</small> | 294.25 USD | +10% | -14.1% | +73% | +12% | 50 | +0.24 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.25 |
| 🔴🔴 Strong Sell | -0.98 | **CDNS**<br><small>Cadence Design Systems</small> | 309.49 USD | +31% | -9.2% | +1% | -6% | 42 | +0.31 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.30 |
| 🔴🔴 Strong Sell | -1.02 | **QCOM**<br><small>Qualcomm</small> | 168.56 USD | +15% | -13.2% | +1% | -0% | 46 | +0.70 | 0.0% → 0.0% | – | analyst α -0.66 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.33 | **Shin-Etsu**<br><small>4063.T</small> | 5,586 JPY | +39% | -7.0% | +30% | -12% | 42 | -0.20 | 0.0% → 0.0% | – | analyst α -0.31 · momentum -0.17 |
| 🔴🔴 Strong Sell | -1.52 | **SMIC**<br><small>0981.HK</small> | 49.90 HKD | +92% | +6.8% | -31% | -24% | 50 | -0.99 | 0.0% → 0.0% | – | momentum -0.53 · quality -0.33 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.99"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 719.07 USD (+111%, 46 analysts); de-biased α +9.9% vs CAPM hurdle 14.0%. Downtrend -6% vs 200-day avg; 12-1 mom +271%; RSI 38. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.25"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 194,000 KRW (+146%, 36 analysts); de-biased α +19.4% vs CAPM hurdle 11.3%. Downtrend -18% vs 200-day avg; 12-1 mom +122%; RSI 37. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.37"
    **ADD 63 sh** → target 5.5% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 293.88 USD vs 145.43 USD (+102%, 43 analysts); de-biased α +7.6% vs CAPM hurdle 14.1%. Downtrend -22% vs 200-day avg; 12-1 mom +161%; RSI 33. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.13"
    **TRIM 47 sh** → target 4.2% of NAV (sized ∝ score ÷ σ(e), cap 10%). No reliable analyst target: α set to 0. Downtrend -25% vs 200-day avg; 12-1 mom +121%; RSI 38. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "NVDA (NVDA) — 🟢🟢 Strong Buy, score +0.93"
    Within rebalance band of target 5.8%: no trade. Analyst target 327.70 USD vs 156.16 USD (+110%, 59 analysts); de-biased α +9.6% vs CAPM hurdle 13.9%. Downtrend -23% vs 200-day avg; 12-1 mom +15%; RSI 23. Quality z +0.47 (ROE 101%). ⚠️ oversold.

??? success "AMAT (AMAT) — 🟢 Buy, score +0.63"
    Within rebalance band of target 3.3%: no trade. Analyst target 638.94 USD vs 350.46 USD (+82%, 36 analysts); de-biased α +3.3% vs CAPM hurdle 11.6%. Downtrend -21% vs 200-day avg; 12-1 mom +84%; RSI 39. Quality z +0.03 (ROE 36%).

??? success "INTC (INTC) — 🟢 Buy, score +0.55"
    Within rebalance band of target 2.0%: no trade. Analyst target 116.37 USD vs 55.46 USD (+110%, 43 analysts); de-biased α +9.5% vs CAPM hurdle 14.0%. Downtrend -37% vs 200-day avg; 12-1 mom +150%; RSI 30. Quality z -0.62 (ROE -0%). ⚠️ oversold; price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "ASX (ASX) — 🟢 Buy, score +0.45"
    **TRIM 154 sh** → target 2.6% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 51.00 USD vs 32.80 USD (+55%, 1 analysts); de-biased α -1.7% vs CAPM hurdle 11.9%. Downtrend -4% vs 200-day avg; 12-1 mom +173%; RSI 39. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.17"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 210.93 USD (+78%, 31 analysts); de-biased α +1.9% vs CAPM hurdle 12.6%. Downtrend -26% vs 200-day avg; 12-1 mom +73%; RSI 38. Quality z +0.02 (ROE 65%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.14"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 144.04 USD (+62%, 26 analysts); de-biased α -1.6% vs CAPM hurdle 11.1%. Downtrend -21% vs 200-day avg; 12-1 mom +43%; RSI 41. Quality z +0.51 (ROE 87%).

??? note "TSM (TSM) — ⚪ Hold, score +0.14"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 373.45 USD (+48%, 20 analysts); de-biased α -5.0% vs CAPM hurdle 10.8%. Downtrend -7% vs 200-day avg; 12-1 mom +48%; RSI 39. Quality z +0.58 (ROE 35%).

??? note "Infineon (IFX.DE) — ⚪ Hold, score +0.12"
    Hold zone: keep any existing position, no new money. Analyst target 86.74 EUR vs 49.11 EUR (+77%, 23 analysts); de-biased α +1.3% vs CAPM hurdle 14.1%. Downtrend -15% vs 200-day avg; 12-1 mom +54%; RSI 43. Quality z -0.04 (ROE 6%).

??? note "Advantest (6857.T) — ⚪ Hold, score +0.10"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 26,070 JPY (+64%, 21 analysts); de-biased α -1.8% vs CAPM hurdle 13.4%. Downtrend -11% vs 200-day avg; 12-1 mom +50%; RSI 35. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "TER (TER) — ⚪ Hold, score -0.04"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 232.07 USD (+92%, 15 analysts); de-biased α +5.6% vs CAPM hurdle 12.3%. Downtrend -34% vs 200-day avg; 12-1 mom +92%; RSI 34. Quality z -0.31 (ROE 20%).

??? note "ASML (ASML) — ⚪ Hold, score -0.06"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,406.51 USD (+49%, 16 analysts); de-biased α -5.1% vs CAPM hurdle 12.3%. Downtrend -12% vs 200-day avg; 12-1 mom +62%; RSI 36. Quality z +0.42 (ROE 50%).

??? failure "Tokyo Electron (8035.T) — 🔴 Sell, score -0.27"
    Avoid: not owned. Analyst target 15,275 JPY vs 8,777 JPY (+74%, 23 analysts); de-biased α +1.1% vs CAPM hurdle 12.8%. Downtrend -15% vs 200-day avg; 12-1 mom +58%; RSI 40. Quality z -0.28 (ROE 29%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.27"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 668.00 EUR (+69%, 19 analysts); de-biased α -0.4% vs CAPM hurdle 13.2%. Downtrend -18% vs 200-day avg; 12-1 mom +53%; RSI 39. Quality z -0.10 (ROE 19%).

??? failure "AMD (AMD) — 🔴 Sell, score -0.32"
    Avoid: not owned. Analyst target 619.51 USD vs 504.37 USD (+23%, 50 analysts); de-biased α -12.5% vs CAPM hurdle 14.9%. Uptrend +19% vs 200-day avg; 12-1 mom +113%; RSI 47. Quality z -0.15 (ROE 7%).

??? failure "GFS (GFS) — 🔴 Sell, score -0.34"
    Avoid: not owned. Analyst target 76.00 USD vs 39.43 USD (+93%, 22 analysts); de-biased α +5.7% vs CAPM hurdle 12.4%. Downtrend -28% vs 200-day avg; 12-1 mom +43%; RSI 40. Quality z -0.21 (ROE 8%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.49"
    Avoid: not owned. Analyst target 81,730 JPY vs 43,840 JPY (+86%, 20 analysts); de-biased α +4.5% vs CAPM hurdle 11.5%. Downtrend -32% vs 200-day avg; 12-1 mom +5%; RSI 38. Quality z +0.06 (ROE 25%).

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.53"
    Avoid: not owned. Analyst target 173.36 USD vs 140.02 USD (+24%, 11 analysts); de-biased α -11.2% vs CAPM hurdle 11.0%. Uptrend +0% vs 200-day avg; 12-1 mom +72%; RSI 46. Quality z -0.02 (ROE 6%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.55"
    Avoid: not owned. Analyst target 76.40 USD vs 34.04 USD (+124%, 10 analysts); de-biased α +13.3% vs CAPM hurdle 14.0%. Downtrend -40% vs 200-day avg; 12-1 mom +32%; RSI 39. Quality z -1.00 (ROE 9%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.55"
    Avoid: not owned. Analyst target 288.70 USD vs 175.03 USD (+65%, 40 analysts); de-biased α -3.1% vs CAPM hurdle 19.6%. Downtrend -25% vs 200-day avg; 12-1 mom +62%; RSI 36. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.85"
    Avoid: not owned. Analyst target 569.78 USD vs 441.33 USD (+29%, 26 analysts); de-biased α -9.8% vs CAPM hurdle 10.3%. Uptrend +0% vs 200-day avg; 12-1 mom +15%; RSI 44. Quality z +0.14 (ROE 7%).

??? failure "AVGO (AVGO) — 🔴🔴 Strong Sell, score -0.91"
    Avoid: not owned. Analyst target 531.31 USD vs 333.70 USD (+59%, 47 analysts); de-biased α -2.3% vs CAPM hurdle 11.2%. Downtrend -9% vs 200-day avg; 12-1 mom -3%; RSI 49. Quality z +0.26 (ROE 31%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -0.94"
    Avoid: not owned. Analyst target 324.71 USD vs 294.25 USD (+10%, 31 analysts); de-biased α -14.1% vs CAPM hurdle 10.8%. Uptrend +12% vs 200-day avg; 12-1 mom +73%; RSI 50. Quality z +0.24 (ROE 30%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -0.98"
    Avoid: not owned. Analyst target 405.47 USD vs 309.49 USD (+31%, 26 analysts); de-biased α -9.2% vs CAPM hurdle 10.0%. Downtrend -6% vs 200-day avg; 12-1 mom +1%; RSI 42. Quality z +0.31 (ROE 22%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.02"
    Avoid: not owned. Analyst target 194.13 USD vs 168.56 USD (+15%, 30 analysts); de-biased α -13.2% vs CAPM hurdle 11.9%. Downtrend -0% vs 200-day avg; 12-1 mom +1%; RSI 46. Quality z +0.70 (ROE 23%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.33"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,586 JPY (+39%, 17 analysts); de-biased α -7.0% vs CAPM hurdle 10.8%. Downtrend -12% vs 200-day avg; 12-1 mom +30%; RSI 42. Quality z -0.20 (ROE 10%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.52"
    Avoid: not owned. Analyst target 95.99 HKD vs 49.90 HKD (+92%, 21 analysts); de-biased α +6.8% vs CAPM hurdle 7.3%. Downtrend -24% vs 200-day avg; 12-1 mom -31%; RSI 50. Quality z -0.99 (ROE 3%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 116 | 719.07 USD | $83,412 | 10.2% | Strong Buy |
| 005930.KS | Samsung Electronics | 458 | 194,000 KRW | $66,422 | 8.1% | Strong Buy |
| TSM | TSMC | 127 | 373.45 USD | $47,429 | 5.8% | Hold |
| NVDA | NVIDIA | 268 | 156.16 USD | $41,851 | 5.1% | Strong Buy |
| KLAC | KLA Corp | 268 | 144.04 USD | $38,603 | 4.7% | Hold |
| MRVL | Marvell Technology | 248 | 145.43 USD | $36,067 | 4.4% | Strong Buy |
| 000660.KS | SK hynix | 41 | 1,144,000 KRW | $35,064 | 4.3% | Strong Buy |
| AMAT | Applied Materials | 84 | 350.46 USD | $29,439 | 3.6% | Buy |
| ASX | ASE Technology | 805 | 32.80 USD | $26,404 | 3.2% | Buy |
| 6857.T | Advantest | 100 | 26,070 JPY | $16,364 | 2.0% | Hold |
| INTC | Intel | 230 | 55.46 USD | $12,756 | 1.6% | Buy |
| LRCX | Lam Research | 58 | 210.93 USD | $12,234 | 1.5% | Hold |
| IFX.DE | Infineon Technologies | 225 | 49.11 EUR | $12,165 | 1.5% | Hold |
| TER | Teradyne | 35 | 232.07 USD | $8,122 | 1.0% | Hold |

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

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 57.8%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
