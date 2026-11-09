---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-09 17:30 UTC (Mon Nov 09, 12:30 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🟢 open (Mon 12:30) · Tokyo 🔴 closed (Tue 02:30) · Korea 🔴 closed (Tue 02:30) · Hong Kong 🔴 closed (Tue 01:30) · Xetra 🔴 closed (Mon 18:30) · Euronext Amsterdam 🔴 closed (Mon 18:30)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$833,585** | $343,857 (41%) | $489,727 (59%) | -16.64% | -74.18% | 🔴 Risk-off (-8.5%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $833,585), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| ADD | **NVDA**<br><small>NVIDIA</small> | 119 | 177.94 USD | $21,175 | Executed (paper) | analyst α +0.23 · momentum -0.23 · ⚠️ oversold |
| TRIM | **AMAT**<br><small>Applied Materials</small> | 18 | 370.39 USD | $6,667 | Executed (paper) | momentum +0.14 · analyst α +0.12 |
| ADD | **INTC**<br><small>Intel</small> | 112 | 58.31 USD | $6,531 | Executed (paper) | analyst α +0.48 · momentum +0.26 · ⚠️ oversold, rich valuation, high σ(e) |
| ADD | **Infineon**<br><small>IFX.DE</small> | 83 | 48.53 EUR | $4,515 | Queued · Xetra closed | analyst α +0.15 · quality -0.04 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.37 | **MU**<br><small>Micron Technology</small> | 733.40 USD | +107% | +10.6% | +332% | -3% | 36 | +0.12 | 10.2% → 10.0% | – | analyst α +0.55 · momentum +0.53 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.63 | **SK hynix**<br><small>000660.KS</small> | 1,144,000 KRW | – | +0.0% | +224% | -24% | 34 | +0.62 | 5.1% → 5.6% | – | momentum +0.41 · quality +0.33 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +1.59 | **MRVL**<br><small>Marvell Technology</small> | 154.61 USD | +90% | +6.3% | +195% | -17% | 32 | -0.12 | 6.0% → 5.9% | – | analyst α +0.36 · momentum +0.30 · ⚠️ rich valuation |
| 🟢🟢 Strong Buy | +0.80 | **INTC**<br><small>Intel</small> | 58.31 USD | +100% | +8.7% | +181% | -33% | 28 | -0.62 | 2.6% → 2.6% | ADD 112 | analyst α +0.48 · momentum +0.26 · ⚠️ oversold, rich valuation, high σ(e) |
| 🟢 Buy | +0.71 | **Advantest**<br><small>6857.T</small> | 28,275 JPY | +51% | -3.3% | +151% | -3% | 35 | +0.33 | 2.1% → 2.7% | – | momentum +0.17 · quality +0.16 · ⚠️ rich valuation |
| 🟢 Buy | +0.67 | **NVDA**<br><small>NVIDIA</small> | 177.94 USD | +84% | +4.9% | +22% | -13% | 27 | +0.47 | 3.8% → 3.8% | ADD 119 | analyst α +0.23 · momentum -0.23 · ⚠️ oversold |
| 🟢 Buy | +0.66 | **AMAT**<br><small>Applied Materials</small> | 370.39 USD | +73% | +2.6% | +118% | -17% | 41 | +0.03 | 3.2% → 3.2% | TRIM 18 | momentum +0.14 · analyst α +0.12 |
| 🟢 Buy | +0.36 | **Infineon**<br><small>IFX.DE</small> | 48.53 EUR | +79% | +3.6% | +78% | -15% | 41 | -0.04 | 1.5% → 2.0% | ADD 83 | analyst α +0.15 · quality -0.04 |
| ⚪ Hold | +0.19 | **ASX**<br><small>ASE Technology</small> | 34.26 USD | +49% | -1.6% | +205% | +2% | 40 | -0.68 | 1.3% → 1.3% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| ⚪ Hold | +0.14 | **LRCX**<br><small>Lam Research</small> | 217.99 USD | +72% | +2.3% | +97% | -23% | 38 | +0.02 | 1.5% → 1.5% | – | trend -0.10 · analyst α +0.08 |
| ⚪ Hold | +0.14 | **Tokyo Electron**<br><small>8035.T</small> | 8,445 JPY | +81% | +4.6% | +114% | -18% | 34 | -0.28 | 0.0% → 0.0% | – | analyst α +0.19 · quality -0.18 |
| ⚪ Hold | +0.10 | **KLAC**<br><small>KLA Corp</small> | 150.60 USD | +55% | -1.6% | +63% | -17% | 43 | +0.51 | 4.8% → 4.8% | – | quality +0.24 · analyst α -0.08 |
| ⚪ Hold | +0.03 | **TSM**<br><small>TSMC</small> | 390.12 USD | +42% | -4.8% | +58% | -3% | 42 | +0.58 | 5.9% → 5.9% | – | quality +0.28 · analyst α -0.27 |
| ⚪ Hold | +0.01 | **TER**<br><small>Teradyne</small> | 238.85 USD | +87% | +6.0% | +118% | -32% | 32 | -0.31 | 1.0% → 1.0% | – | analyst α +0.27 · quality -0.21 |
| ⚪ Hold | -0.04 | **AMKR**<br><small>Amkor Technology</small> | 34.80 USD | +120% | +13.9% | +41% | -39% | 38 | -1.00 | 0.0% → 0.0% | – | analyst α +0.85 · quality -0.43 |
| ⚪ Hold | -0.14 | **Disco**<br><small>6146.T</small> | 42,140 JPY | +94% | +8.1% | +22% | -35% | 31 | +0.06 | 0.0% → 0.0% | – | analyst α +0.41 · momentum -0.26 |
| ⚪ Hold | -0.14 | **Samsung**<br><small>005930.KS</small> | 190,100 KRW | – | +0.0% | +170% | -19% | 33 | -0.26 | 9.5% → 9.5% | – | momentum +0.23 · quality -0.16 · ⚠️ cycle-peak P/E |
| ⚪ Hold | -0.24 | **ASML**<br><small>ASML Holding</small> | 1,514.51 USD | +38% | -6.0% | +74% | -5% | 43 | +0.42 | 0.0% → 0.0% | – | analyst α -0.31 · quality +0.18 |
| 🔴 Sell | -0.26 | **ASMI**<br><small>ASM.AS</small> | 676.20 EUR | +67% | +0.8% | +70% | -17% | 38 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · momentum -0.03 |
| 🔴 Sell | -0.28 | **GFS**<br><small>GlobalFoundries</small> | 40.64 USD | +87% | +6.0% | +41% | -26% | 41 | -0.21 | 0.0% → 0.0% | – | analyst α +0.31 · momentum -0.14 |
| 🔴 Sell | -0.37 | **AMD**<br><small>Advanced Micro Devices</small> | 502.48 USD | +23% | -10.6% | +156% | +20% | 47 | -0.15 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.32 |
| 🔴 Sell | -0.56 | **AVGO**<br><small>Broadcom</small> | 320.99 USD | +66% | +1.1% | +2% | -12% | 45 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.11 |
| 🔴🔴 Strong Sell | -0.75 | **SNPS**<br><small>Synopsys</small> | 468.19 USD | +22% | -9.8% | +29% | +6% | 53 | +0.14 | 0.0% → 0.0% | – | analyst α -0.36 · trend +0.21 |
| 🔴🔴 Strong Sell | -0.79 | **TXN**<br><small>Texas Instruments</small> | 291.43 USD | +11% | -12.1% | +79% | +12% | 51 | +0.24 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.25 |
| 🔴🔴 Strong Sell | -0.80 | **ARM**<br><small>Arm Holdings</small> | 187.51 USD | +54% | -4.1% | +68% | -19% | 37 | +0.04 | 0.0% → 0.0% | – | analyst α -0.19 · trend -0.07 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -0.81 | **ENTG**<br><small>Entegris</small> | 142.96 USD | +21% | -10.0% | +94% | +3% | 48 | -0.02 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.16 |
| 🔴🔴 Strong Sell | -0.99 | **SMIC**<br><small>0981.HK</small> | 46.04 HKD | +108% | +12.6% | -28% | -31% | 38 | -0.99 | 0.0% → 0.0% | – | analyst α +0.66 · momentum -0.53 |
| 🔴🔴 Strong Sell | -1.22 | **CDNS**<br><small>Cadence Design Systems</small> | 335.52 USD | +21% | -10.0% | +9% | +2% | 54 | +0.31 | 0.0% → 0.0% | – | analyst α -0.41 · momentum -0.30 |
| 🔴🔴 Strong Sell | -1.37 | **Shin-Etsu**<br><small>4063.T</small> | 5,450 JPY | +42% | -4.3% | +29% | -14% | 34 | -0.20 | 0.0% → 0.0% | – | analyst α -0.23 · momentum -0.17 |
| 🔴🔴 Strong Sell | -1.64 | **QCOM**<br><small>Qualcomm</small> | 174.32 USD | +11% | -12.3% | +3% | +3% | 50 | +0.70 | 0.0% → 0.0% | – | analyst α -0.85 · quality +0.43 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +3.37"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 733.40 USD (+107%, 46 analysts); de-biased α +10.6% vs CAPM hurdle 14.0%. Downtrend -3% vs 200-day avg; 12-1 mom +332%; RSI 36. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.63"
    Within rebalance band of target 5.6%: no trade. No reliable analyst target: α set to 0. Downtrend -24% vs 200-day avg; 12-1 mom +224%; RSI 34. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.59"
    Within rebalance band of target 5.9%: no trade. Analyst target 293.88 USD vs 154.61 USD (+90%, 43 analysts); de-biased α +6.3% vs CAPM hurdle 14.1%. Downtrend -17% vs 200-day avg; 12-1 mom +195%; RSI 32. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? success "INTC (INTC) — 🟢🟢 Strong Buy, score +0.80"
    **ADD 112 sh** → target 2.6% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 116.37 USD vs 58.31 USD (+100%, 43 analysts); de-biased α +8.7% vs CAPM hurdle 14.0%. Downtrend -33% vs 200-day avg; 12-1 mom +181%; RSI 28. Quality z -0.62 (ROE -0%). ⚠️ oversold; price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "Advantest (6857.T) — 🟢 Buy, score +0.71"
    Within rebalance band of target 2.7%: no trade. Analyst target 42,686 JPY vs 28,275 JPY (+51%, 21 analysts); de-biased α -3.3% vs CAPM hurdle 13.4%. Downtrend -3% vs 200-day avg; 12-1 mom +151%; RSI 35. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.67"
    **ADD 119 sh** → target 3.8% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 327.70 USD vs 177.94 USD (+84%, 59 analysts); de-biased α +4.9% vs CAPM hurdle 13.9%. Downtrend -13% vs 200-day avg; 12-1 mom +22%; RSI 27. Quality z +0.47 (ROE 101%). ⚠️ oversold.

??? success "AMAT (AMAT) — 🟢 Buy, score +0.66"
    **TRIM 18 sh** → target 3.2% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 370.39 USD (+73%, 36 analysts); de-biased α +2.6% vs CAPM hurdle 11.6%. Downtrend -17% vs 200-day avg; 12-1 mom +118%; RSI 41. Quality z +0.03 (ROE 36%).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.36"
    **ADD 83 sh** → target 2.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 86.74 EUR vs 48.53 EUR (+79%, 23 analysts); de-biased α +3.6% vs CAPM hurdle 14.1%. Downtrend -15% vs 200-day avg; 12-1 mom +78%; RSI 41. Quality z -0.04 (ROE 6%).

??? note "ASX (ASX) — ⚪ Hold, score +0.19"
    Hold zone: keep any existing position, no new money. Analyst target 51.00 USD vs 34.26 USD (+49%, 1 analysts); de-biased α -1.6% vs CAPM hurdle 11.9%. Uptrend +2% vs 200-day avg; 12-1 mom +205%; RSI 40. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.14"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 217.99 USD (+72%, 31 analysts); de-biased α +2.3% vs CAPM hurdle 12.6%. Downtrend -23% vs 200-day avg; 12-1 mom +97%; RSI 38. Quality z +0.02 (ROE 65%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.14"
    Hold zone: not owned, no entry. Analyst target 15,275 JPY vs 8,445 JPY (+81%, 23 analysts); de-biased α +4.6% vs CAPM hurdle 12.8%. Downtrend -18% vs 200-day avg; 12-1 mom +114%; RSI 34. Quality z -0.28 (ROE 29%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.10"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 150.60 USD (+55%, 26 analysts); de-biased α -1.6% vs CAPM hurdle 11.1%. Downtrend -17% vs 200-day avg; 12-1 mom +63%; RSI 43. Quality z +0.51 (ROE 87%).

??? note "TSM (TSM) — ⚪ Hold, score +0.03"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 390.12 USD (+42%, 20 analysts); de-biased α -4.8% vs CAPM hurdle 10.8%. Downtrend -3% vs 200-day avg; 12-1 mom +58%; RSI 42. Quality z +0.58 (ROE 35%).

??? note "TER (TER) — ⚪ Hold, score +0.01"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 238.85 USD (+87%, 15 analysts); de-biased α +6.0% vs CAPM hurdle 12.3%. Downtrend -32% vs 200-day avg; 12-1 mom +118%; RSI 32. Quality z -0.31 (ROE 20%).

??? note "AMKR (AMKR) — ⚪ Hold, score -0.04"
    Hold zone: not owned, no entry. Analyst target 76.40 USD vs 34.80 USD (+120%, 10 analysts); de-biased α +13.9% vs CAPM hurdle 14.0%. Downtrend -39% vs 200-day avg; 12-1 mom +41%; RSI 38. Quality z -1.00 (ROE 9%).

??? note "Disco (6146.T) — ⚪ Hold, score -0.14"
    Hold zone: not owned, no entry. Analyst target 81,730 JPY vs 42,140 JPY (+94%, 20 analysts); de-biased α +8.1% vs CAPM hurdle 11.5%. Downtrend -35% vs 200-day avg; 12-1 mom +22%; RSI 31. Quality z +0.06 (ROE 25%).

??? note "Samsung (005930.KS) — ⚪ Hold, score -0.14"
    Hold zone: keep any existing position, no new money. No reliable analyst target: α set to 0. Downtrend -19% vs 200-day avg; 12-1 mom +170%; RSI 33. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? note "ASML (ASML) — ⚪ Hold, score -0.24"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,514.51 USD (+38%, 16 analysts); de-biased α -6.0% vs CAPM hurdle 12.3%. Downtrend -5% vs 200-day avg; 12-1 mom +74%; RSI 43. Quality z +0.42 (ROE 50%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.26"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 676.20 EUR (+67%, 19 analysts); de-biased α +0.8% vs CAPM hurdle 13.2%. Downtrend -17% vs 200-day avg; 12-1 mom +70%; RSI 38. Quality z -0.10 (ROE 19%).

??? failure "GFS (GFS) — 🔴 Sell, score -0.28"
    Avoid: not owned. Analyst target 76.00 USD vs 40.64 USD (+87%, 22 analysts); de-biased α +6.0% vs CAPM hurdle 12.4%. Downtrend -26% vs 200-day avg; 12-1 mom +41%; RSI 41. Quality z -0.21 (ROE 8%).

??? failure "AMD (AMD) — 🔴 Sell, score -0.37"
    Avoid: not owned. Analyst target 619.51 USD vs 502.48 USD (+23%, 50 analysts); de-biased α -10.6% vs CAPM hurdle 14.9%. Uptrend +20% vs 200-day avg; 12-1 mom +156%; RSI 47. Quality z -0.15 (ROE 7%).

??? failure "AVGO (AVGO) — 🔴 Sell, score -0.56"
    Avoid: not owned. Analyst target 531.31 USD vs 320.99 USD (+66%, 47 analysts); de-biased α +1.1% vs CAPM hurdle 11.2%. Downtrend -12% vs 200-day avg; 12-1 mom +2%; RSI 45. Quality z +0.26 (ROE 31%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.75"
    Avoid: not owned. Analyst target 569.78 USD vs 468.19 USD (+22%, 26 analysts); de-biased α -9.8% vs CAPM hurdle 10.3%. Uptrend +6% vs 200-day avg; 12-1 mom +29%; RSI 53. Quality z +0.14 (ROE 7%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -0.79"
    Avoid: not owned. Analyst target 324.71 USD vs 291.43 USD (+11%, 31 analysts); de-biased α -12.1% vs CAPM hurdle 10.8%. Uptrend +12% vs 200-day avg; 12-1 mom +79%; RSI 51. Quality z +0.24 (ROE 30%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -0.80"
    Avoid: not owned. Analyst target 288.70 USD vs 187.51 USD (+54%, 40 analysts); de-biased α -4.1% vs CAPM hurdle 19.6%. Downtrend -19% vs 200-day avg; 12-1 mom +68%; RSI 37. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.81"
    Avoid: not owned. Analyst target 173.36 USD vs 142.96 USD (+21%, 11 analysts); de-biased α -10.0% vs CAPM hurdle 11.0%. Uptrend +3% vs 200-day avg; 12-1 mom +94%; RSI 48. Quality z -0.02 (ROE 6%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -0.99"
    Avoid: not owned. Analyst target 95.99 HKD vs 46.04 HKD (+108%, 21 analysts); de-biased α +12.6% vs CAPM hurdle 7.3%. Downtrend -31% vs 200-day avg; 12-1 mom -28%; RSI 38. Quality z -0.99 (ROE 3%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.22"
    Avoid: not owned. Analyst target 405.47 USD vs 335.52 USD (+21%, 26 analysts); de-biased α -10.0% vs CAPM hurdle 10.0%. Uptrend +2% vs 200-day avg; 12-1 mom +9%; RSI 54. Quality z +0.31 (ROE 22%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.37"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,450 JPY (+42%, 17 analysts); de-biased α -4.3% vs CAPM hurdle 10.8%. Downtrend -14% vs 200-day avg; 12-1 mom +29%; RSI 34. Quality z -0.20 (ROE 10%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.64"
    Avoid: not owned. Analyst target 194.13 USD vs 174.32 USD (+11%, 30 analysts); de-biased α -12.3% vs CAPM hurdle 11.9%. Uptrend +3% vs 200-day avg; 12-1 mom +3%; RSI 50. Quality z +0.70 (ROE 23%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 116 | 733.40 USD | $85,074 | 10.2% | Strong Buy |
| 005930.KS | Samsung Electronics | 562 | 190,100 KRW | $79,500 | 9.5% | Hold |
| MRVL | Marvell Technology | 324 | 154.61 USD | $50,095 | 6.0% | Strong Buy |
| TSM | TSMC | 127 | 390.12 USD | $49,545 | 5.9% | Hold |
| 000660.KS | SK hynix | 50 | 1,144,000 KRW | $42,564 | 5.1% | Strong Buy |
| KLAC | KLA Corp | 268 | 150.60 USD | $40,362 | 4.8% | Hold |
| NVDA | NVIDIA | 179 | 177.94 USD | $31,851 | 3.8% | Buy |
| AMAT | Applied Materials | 73 | 370.39 USD | $27,038 | 3.2% | Buy |
| INTC | Intel | 375 | 58.31 USD | $21,866 | 2.6% | Strong Buy |
| 6857.T | Advantest | 100 | 28,275 JPY | $17,899 | 2.1% | Buy |
| LRCX | Lam Research | 58 | 217.99 USD | $12,643 | 1.5% | Hold |
| IFX.DE | Infineon Technologies | 225 | 48.53 EUR | $12,240 | 1.5% | Buy |
| ASX | ASE Technology | 312 | 34.26 USD | $10,689 | 1.3% | Hold |
| TER | Teradyne | 35 | 238.85 USD | $8,360 | 1.0% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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
| 2026-11-03 15:09 UTC | ADD | INTC | 106 | 62.03 | $6,576 |
| 2026-11-03 15:09 UTC | ADD | MRVL | 50 | 172.03 | $8,602 |
| 2026-11-03 15:09 UTC | ADD | AMAT | 15 | 385.21 | $5,778 |
| 2026-11-03 15:09 UTC | TRIM | NVDA | -141 | 208.26 | $29,365 |
| 2026-11-02 15:55 UTC | BUY (new) | TER | 35 | 270.99 | $9,485 |
| 2026-11-02 15:55 UTC | ADD | MRVL | 35 | 184.11 | $6,444 |
| 2026-11-02 15:55 UTC | TRIM | IFX.DE | -1,076 | 52.66 | $63,473 |
| 2026-11-02 06:06 UTC | TRIM | 000660.KS | -18 | 1,490,500.00 | $20,008 |
| 2026-11-02 06:06 UTC | TRIM | 005930.KS | -163 | 231,750.00 | $28,171 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 50.8%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
