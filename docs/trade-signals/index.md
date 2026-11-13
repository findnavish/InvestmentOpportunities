---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-13 07:59 UTC (Fri Nov 13, 02:59 AM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Fri 02:59) · Tokyo 🔴 closed (Fri 16:59) · Korea 🔴 closed (Fri 16:59) · Hong Kong 🟢 open (Fri 15:59) · Xetra 🔴 closed (Fri 08:59) · Euronext Amsterdam 🔴 closed (Fri 08:59)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$861,968** | $322,195 (37%) | $539,772 (63%) | -13.80% | -72.59% | 🔴 Risk-off (-3.2%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $861,968), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **SK hynix**<br><small>000660.KS</small> | 47 | 1,216,000 KRW | $42,718 | Queued · Korea closed | quality +0.33 · momentum +0.23 · ⚠️ cycle-peak P/E, high σ(e) |
| ADD | **INTC**<br><small>Intel</small> | 70 | 61.22 USD | $4,285 | Queued · NYSE/Nasdaq closed | analyst α +0.36 · momentum +0.30 · ⚠️ rich valuation, high σ(e) |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +2.89 | **MU**<br><small>Micron Technology</small> | 798.90 USD | +90% | +8.0% | +281% | +4% | 44 | +0.12 | 10.8% → 10.0% | – | momentum +0.53 · analyst α +0.41 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.24 | **Samsung**<br><small>005930.KS</small> | 207,000 KRW | +131% | +18.9% | +94% | -13% | 43 | -0.26 | 8.2% → 10.0% | – | analyst α +0.85 · momentum +0.20 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.35 | **MRVL**<br><small>Marvell Technology</small> | 164.48 USD | +79% | +5.1% | +171% | -12% | 37 | -0.12 | 4.7% → 5.3% | – | momentum +0.35 · analyst α +0.27 · ⚠️ rich valuation |
| 🟢🟢 Strong Buy | +1.18 | **SK hynix**<br><small>000660.KS</small> | 1,216,000 KRW | – | +0.0% | +104% | -20% | 40 | +0.62 | 9.3% → 4.3% | TRIM 47 | quality +0.33 · momentum +0.23 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +0.93 | **NVDA**<br><small>NVIDIA</small> | 166.04 USD | +97% | +9.8% | +12% | -19% | 26 | +0.47 | 5.0% → 5.7% | – | analyst α +0.48 · momentum -0.23 · ⚠️ oversold |
| 🟢 Buy | +0.61 | **AMAT**<br><small>Applied Materials</small> | 381.28 USD | +68% | +3.0% | +87% | -15% | 45 | +0.03 | 2.7% → 3.2% | – | analyst α +0.15 · momentum +0.14 |
| 🟢 Buy | +0.60 | **ASX**<br><small>ASE Technology</small> | 36.29 USD | +41% | -1.9% | +199% | +7% | 45 | -0.68 | 3.6% → 3.4% | – | momentum +0.41 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.45 | **INTC**<br><small>Intel</small> | 61.22 USD | +90% | +7.9% | +152% | -30% | 33 | -0.62 | 1.1% → 1.6% | ADD 70 | analyst α +0.36 · momentum +0.30 · ⚠️ rich valuation, high σ(e) |
| 🟢 Buy | +0.37 | **Advantest**<br><small>6857.T</small> | 30,730 JPY | +39% | -4.7% | +83% | +5% | 44 | +0.33 | 2.2% → 1.5% | – | analyst α -0.27 · quality +0.16 · ⚠️ rich valuation |
| ⚪ Hold | +0.14 | **Infineon**<br><small>IFX.DE</small> | 52.29 EUR | +66% | +2.0% | +55% | -9% | 50 | -0.04 | 1.5% → 1.5% | – | analyst α +0.12 · momentum -0.05 |
| ⚪ Hold | +0.12 | **KLAC**<br><small>KLA Corp</small> | 157.31 USD | +49% | -1.6% | +46% | -13% | 48 | +0.51 | 4.9% → 4.9% | – | quality +0.24 · momentum -0.10 |
| ⚪ Hold | +0.12 | **TSM**<br><small>TSMC</small> | 405.65 USD | +36% | -4.6% | +47% | +1% | 47 | +0.58 | 6.0% → 6.0% | – | quality +0.28 · analyst α -0.23 |
| ⚪ Hold | +0.10 | **ASML**<br><small>ASML Holding</small> | 1,497.12 USD | +40% | -4.0% | +62% | -6% | 42 | +0.42 | 0.0% → 0.0% | – | quality +0.18 · analyst α -0.15 |
| ⚪ Hold | +0.05 | **Tokyo Electron**<br><small>8035.T</small> | 9,404 JPY | +62% | +1.6% | +76% | -9% | 45 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · momentum +0.10 |
| ⚪ Hold | -0.01 | **TER**<br><small>Teradyne</small> | 263.74 USD | +69% | +3.2% | +92% | -25% | 40 | -0.31 | 1.1% → 1.1% | – | quality -0.21 · analyst α +0.19 |
| ⚪ Hold | -0.03 | **LRCX**<br><small>Lam Research</small> | 233.79 USD | +60% | +0.9% | +73% | -18% | 44 | +0.02 | 1.6% → 1.6% | – | trend -0.09 · analyst α +0.05 |
| ⚪ Hold | -0.20 | **GFS**<br><small>GlobalFoundries</small> | 42.64 USD | +78% | +5.4% | +43% | -22% | 47 | -0.21 | 0.0% → 0.0% | – | analyst α +0.31 · trend -0.14 |
| ⚪ Hold | -0.24 | **ASMI**<br><small>ASM.AS</small> | 726.80 EUR | +55% | -0.5% | +65% | -10% | 47 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · analyst α -0.02 |
| 🔴 Sell | -0.51 | **Disco**<br><small>6146.T</small> | 47,440 JPY | +72% | +4.3% | +4% | -27% | 44 | +0.06 | 0.0% → 0.0% | – | momentum -0.26 · analyst α +0.23 |
| 🔴 Sell | -0.57 | **ENTG**<br><small>Entegris</small> | 153.26 USD | +13% | -10.5% | +75% | +10% | 54 | -0.02 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.21 |
| 🔴 Sell | -0.67 | **AMKR**<br><small>Amkor Technology</small> | 37.11 USD | +106% | +12.0% | +29% | -34% | 44 | -1.00 | 0.0% → 0.0% | – | analyst α +0.66 · quality -0.43 |
| 🔴 Sell | -0.69 | **TXN**<br><small>Texas Instruments</small> | 312.50 USD | +4% | -12.3% | +74% | +19% | 61 | +0.24 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.25 |
| 🔴🔴 Strong Sell | -0.80 | **QCOM**<br><small>Qualcomm</small> | 177.16 USD | +10% | -11.2% | +3% | +5% | 52 | +0.70 | 0.0% → 0.0% | – | analyst α -0.55 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.85 | **SNPS**<br><small>Synopsys</small> | 462.65 USD | +23% | -7.9% | +17% | +5% | 52 | +0.14 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.20 |
| 🔴🔴 Strong Sell | -0.87 | **ARM**<br><small>Arm Holdings</small> | 199.82 USD | +44% | -4.9% | +65% | -14% | 43 | +0.04 | 0.0% → 0.0% | – | analyst α -0.31 · trend -0.06 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -0.93 | **AVGO**<br><small>Broadcom</small> | 364.38 USD | +46% | -2.3% | -2% | -1% | 60 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.12 |
| 🔴🔴 Strong Sell | -0.96 | **AMD**<br><small>Advanced Micro Devices</small> | 585.58 USD | +6% | -13.4% | +117% | +38% | 58 | -0.15 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -1.15 | **Shin-Etsu**<br><small>4063.T</small> | 5,676 JPY | +37% | -4.2% | +35% | -10% | 45 | -0.20 | 0.0% → 0.0% | – | analyst α -0.19 · momentum -0.14 |
| 🔴🔴 Strong Sell | -1.27 | **SMIC**<br><small>0981.HK</small> | 48.38 HKD | +98% | +11.7% | -24% | -27% | 45 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.53 |
| 🔴🔴 Strong Sell | -1.41 | **CDNS**<br><small>Cadence Design Systems</small> | 333.23 USD | +22% | -8.2% | +3% | +2% | 53 | +0.31 | 0.0% → 0.0% | – | analyst α -0.41 · momentum -0.35 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.89"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 798.90 USD (+90%, 46 analysts); de-biased α +8.0% vs CAPM hurdle 14.0%. Uptrend +4% vs 200-day avg; 12-1 mom +281%; RSI 44. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.24"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 207,000 KRW (+131%, 36 analysts); de-biased α +18.9% vs CAPM hurdle 11.3%. Downtrend -13% vs 200-day avg; 12-1 mom +94%; RSI 43. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.35"
    Within rebalance band of target 5.3%: no trade. Analyst target 293.88 USD vs 164.48 USD (+79%, 43 analysts); de-biased α +5.1% vs CAPM hurdle 14.1%. Downtrend -12% vs 200-day avg; 12-1 mom +171%; RSI 37. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.18"
    **TRIM 47 sh** → target 4.3% of NAV (sized ∝ score ÷ σ(e), cap 10%). No reliable analyst target: α set to 0. Downtrend -20% vs 200-day avg; 12-1 mom +104%; RSI 40. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "NVDA (NVDA) — 🟢🟢 Strong Buy, score +0.93"
    Within rebalance band of target 5.7%: no trade. Analyst target 327.70 USD vs 166.04 USD (+97%, 59 analysts); de-biased α +9.8% vs CAPM hurdle 13.9%. Downtrend -19% vs 200-day avg; 12-1 mom +12%; RSI 26. Quality z +0.47 (ROE 101%). ⚠️ oversold.

??? success "AMAT (AMAT) — 🟢 Buy, score +0.61"
    Within rebalance band of target 3.2%: no trade. Analyst target 638.94 USD vs 381.28 USD (+68%, 36 analysts); de-biased α +3.0% vs CAPM hurdle 11.6%. Downtrend -15% vs 200-day avg; 12-1 mom +87%; RSI 45. Quality z +0.03 (ROE 36%).

??? success "ASX (ASX) — 🟢 Buy, score +0.60"
    Within rebalance band of target 3.4%: no trade. Analyst target 51.00 USD vs 36.29 USD (+41%, 1 analysts); de-biased α -1.9% vs CAPM hurdle 11.9%. Uptrend +7% vs 200-day avg; 12-1 mom +199%; RSI 45. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "INTC (INTC) — 🟢 Buy, score +0.45"
    **ADD 70 sh** → target 1.6% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 116.37 USD vs 61.22 USD (+90%, 43 analysts); de-biased α +7.9% vs CAPM hurdle 14.0%. Downtrend -30% vs 200-day avg; 12-1 mom +152%; RSI 33. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "Advantest (6857.T) — 🟢 Buy, score +0.37"
    Within rebalance band of target 1.5%: no trade. Analyst target 42,686 JPY vs 30,730 JPY (+39%, 21 analysts); de-biased α -4.7% vs CAPM hurdle 13.4%. Uptrend +5% vs 200-day avg; 12-1 mom +83%; RSI 44. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "Infineon (IFX.DE) — ⚪ Hold, score +0.14"
    Hold zone: keep any existing position, no new money. Analyst target 86.74 EUR vs 52.29 EUR (+66%, 23 analysts); de-biased α +2.0% vs CAPM hurdle 14.1%. Downtrend -9% vs 200-day avg; 12-1 mom +55%; RSI 50. Quality z -0.04 (ROE 6%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.12"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 157.31 USD (+49%, 26 analysts); de-biased α -1.6% vs CAPM hurdle 11.1%. Downtrend -13% vs 200-day avg; 12-1 mom +46%; RSI 48. Quality z +0.51 (ROE 87%).

??? note "TSM (TSM) — ⚪ Hold, score +0.12"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 405.65 USD (+36%, 20 analysts); de-biased α -4.6% vs CAPM hurdle 10.8%. Uptrend +1% vs 200-day avg; 12-1 mom +47%; RSI 47. Quality z +0.58 (ROE 35%).

??? note "ASML (ASML) — ⚪ Hold, score +0.10"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,497.12 USD (+40%, 16 analysts); de-biased α -4.0% vs CAPM hurdle 12.3%. Downtrend -6% vs 200-day avg; 12-1 mom +62%; RSI 42. Quality z +0.42 (ROE 50%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.05"
    Hold zone: not owned, no entry. Analyst target 15,275 JPY vs 9,404 JPY (+62%, 23 analysts); de-biased α +1.6% vs CAPM hurdle 12.8%. Downtrend -9% vs 200-day avg; 12-1 mom +76%; RSI 45. Quality z -0.28 (ROE 29%).

??? note "TER (TER) — ⚪ Hold, score -0.01"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 263.74 USD (+69%, 15 analysts); de-biased α +3.2% vs CAPM hurdle 12.3%. Downtrend -25% vs 200-day avg; 12-1 mom +92%; RSI 40. Quality z -0.31 (ROE 20%).

??? note "LRCX (LRCX) — ⚪ Hold, score -0.03"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 233.79 USD (+60%, 31 analysts); de-biased α +0.9% vs CAPM hurdle 12.6%. Downtrend -18% vs 200-day avg; 12-1 mom +73%; RSI 44. Quality z +0.02 (ROE 65%).

??? note "GFS (GFS) — ⚪ Hold, score -0.20"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 42.64 USD (+78%, 22 analysts); de-biased α +5.4% vs CAPM hurdle 12.4%. Downtrend -22% vs 200-day avg; 12-1 mom +43%; RSI 47. Quality z -0.21 (ROE 8%).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.24"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 726.80 EUR (+55%, 19 analysts); de-biased α -0.5% vs CAPM hurdle 13.2%. Downtrend -10% vs 200-day avg; 12-1 mom +65%; RSI 47. Quality z -0.10 (ROE 19%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.51"
    Avoid: not owned. Analyst target 81,730 JPY vs 47,440 JPY (+72%, 20 analysts); de-biased α +4.3% vs CAPM hurdle 11.5%. Downtrend -27% vs 200-day avg; 12-1 mom +4%; RSI 44. Quality z +0.06 (ROE 25%).

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.57"
    Avoid: not owned. Analyst target 173.36 USD vs 153.26 USD (+13%, 11 analysts); de-biased α -10.5% vs CAPM hurdle 11.0%. Uptrend +10% vs 200-day avg; 12-1 mom +75%; RSI 54. Quality z -0.02 (ROE 6%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.67"
    Avoid: not owned. Analyst target 76.40 USD vs 37.11 USD (+106%, 10 analysts); de-biased α +12.0% vs CAPM hurdle 14.0%. Downtrend -34% vs 200-day avg; 12-1 mom +29%; RSI 44. Quality z -1.00 (ROE 9%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.69"
    Avoid: not owned. Analyst target 324.71 USD vs 312.50 USD (+4%, 31 analysts); de-biased α -12.3% vs CAPM hurdle 10.8%. Uptrend +19% vs 200-day avg; 12-1 mom +74%; RSI 61. Quality z +0.24 (ROE 30%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.80"
    Avoid: not owned. Analyst target 194.13 USD vs 177.16 USD (+10%, 30 analysts); de-biased α -11.2% vs CAPM hurdle 11.9%. Uptrend +5% vs 200-day avg; 12-1 mom +3%; RSI 52. Quality z +0.70 (ROE 23%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.85"
    Avoid: not owned. Analyst target 569.78 USD vs 462.65 USD (+23%, 26 analysts); de-biased α -7.9% vs CAPM hurdle 10.3%. Uptrend +5% vs 200-day avg; 12-1 mom +17%; RSI 52. Quality z +0.14 (ROE 7%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -0.87"
    Avoid: not owned. Analyst target 288.70 USD vs 199.82 USD (+44%, 40 analysts); de-biased α -4.9% vs CAPM hurdle 19.6%. Downtrend -14% vs 200-day avg; 12-1 mom +65%; RSI 43. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "AVGO (AVGO) — 🔴🔴 Strong Sell, score -0.93"
    Avoid: not owned. Analyst target 531.31 USD vs 364.38 USD (+46%, 47 analysts); de-biased α -2.3% vs CAPM hurdle 11.2%. Downtrend -1% vs 200-day avg; 12-1 mom -2%; RSI 60. Quality z +0.26 (ROE 31%).

??? failure "AMD (AMD) — 🔴🔴 Strong Sell, score -0.96"
    Avoid: not owned. Analyst target 619.51 USD vs 585.58 USD (+6%, 50 analysts); de-biased α -13.4% vs CAPM hurdle 14.9%. Uptrend +38% vs 200-day avg; 12-1 mom +117%; RSI 58. Quality z -0.15 (ROE 7%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.15"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,676 JPY (+37%, 17 analysts); de-biased α -4.2% vs CAPM hurdle 10.8%. Downtrend -10% vs 200-day avg; 12-1 mom +35%; RSI 45. Quality z -0.20 (ROE 10%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.27"
    Avoid: not owned. Analyst target 95.99 HKD vs 48.38 HKD (+98%, 21 analysts); de-biased α +11.7% vs CAPM hurdle 7.3%. Downtrend -27% vs 200-day avg; 12-1 mom -24%; RSI 45. Quality z -0.99 (ROE 3%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.41"
    Avoid: not owned. Analyst target 405.47 USD vs 333.23 USD (+22%, 26 analysts); de-biased α -8.2% vs CAPM hurdle 10.0%. Uptrend +2% vs 200-day avg; 12-1 mom +3%; RSI 53. Quality z +0.31 (ROE 22%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 116 | 798.90 USD | $92,672 | 10.8% | Strong Buy |
| 000660.KS | SK hynix | 88 | 1,216,000 KRW | $79,983 | 9.3% | Strong Buy |
| 005930.KS | Samsung Electronics | 458 | 207,000 KRW | $70,863 | 8.2% | Strong Buy |
| TSM | TSMC | 127 | 405.65 USD | $51,518 | 6.0% | Hold |
| NVDA | NVIDIA | 258 | 166.04 USD | $42,838 | 5.0% | Strong Buy |
| KLAC | KLA Corp | 268 | 157.31 USD | $42,159 | 4.9% | Hold |
| MRVL | Marvell Technology | 248 | 164.48 USD | $40,791 | 4.7% | Strong Buy |
| ASX | ASE Technology | 864 | 36.29 USD | $31,355 | 3.6% | Buy |
| AMAT | Applied Materials | 61 | 381.28 USD | $23,258 | 2.7% | Buy |
| 6857.T | Advantest | 100 | 30,730 JPY | $19,224 | 2.2% | Buy |
| LRCX | Lam Research | 58 | 233.79 USD | $13,560 | 1.6% | Hold |
| IFX.DE | Infineon Technologies | 225 | 52.29 EUR | $13,015 | 1.5% | Hold |
| INTC | Intel | 152 | 61.22 USD | $9,305 | 1.1% | Buy |
| TER | Teradyne | 35 | 263.74 USD | $9,231 | 1.1% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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
| 2026-11-05 15:28 UTC | ADD | INTC | 309 | 52.94 | $16,359 |
| 2026-11-05 15:28 UTC | ADD | MRVL | 160 | 140.70 | $22,512 |
| 2026-11-05 15:28 UTC | ADD | MU | 52 | 693.52 | $36,063 |
| 2026-11-05 15:28 UTC | ADD | AMAT | 21 | 332.95 | $6,992 |
| 2026-11-05 15:28 UTC | TRIM | LRCX | -104 | 195.72 | $20,355 |
| 2026-11-04 17:18 UTC | TRIM | AMAT | -12 | 366.64 | $4,400 |
| 2026-11-04 17:18 UTC | TRIM | INTC | -98 | 57.47 | $5,632 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 44.4%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
