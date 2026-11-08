---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-08 15:13 UTC (Sun Nov 08, 10:13 AM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Sun 10:13) · Tokyo 🔴 closed (Mon 00:13) · Korea 🔴 closed (Mon 00:13) · Hong Kong 🔴 closed (Sun 23:13) · Xetra 🔴 closed (Sun 16:13) · Euronext Amsterdam 🔴 closed (Sun 16:13)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$810,565** | $364,913 (45%) | $445,651 (55%) | -18.94% | -75.88% | 🔴 Risk-off (-14.5%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $810,565), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| ADD | **Infineon**<br><small>IFX.DE</small> | 163 | 45.92 EUR | $8,340 | Queued · Xetra closed | analyst α +0.19 · quality -0.04 |
| ADD | **INTC**<br><small>Intel</small> | 79 | 56.34 USD | $4,451 | Queued · NYSE/Nasdaq closed | analyst α +0.41 · momentum +0.26 · ⚠️ oversold, rich valuation, high σ(e) |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.36 | **MU**<br><small>Micron Technology</small> | 689.42 USD | +120% | +11.7% | +332% | -9% | 31 | +0.12 | 9.9% → 10.0% | – | analyst α +0.66 · momentum +0.53 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.64 | **MRVL**<br><small>Marvell Technology</small> | 141.19 USD | +108% | +8.6% | +195% | -24% | 26 | -0.12 | 5.6% → 6.7% | – | analyst α +0.48 · momentum +0.30 · ⚠️ oversold, rich valuation |
| 🟢🟢 Strong Buy | +1.63 | **SK hynix**<br><small>000660.KS</small> | 1,144,000 KRW | – | +0.0% | +224% | -24% | 34 | +0.62 | 5.2% → 6.2% | – | momentum +0.41 · quality +0.33 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢 Buy | +0.72 | **AMAT**<br><small>Applied Materials</small> | 332.81 USD | +92% | +5.2% | +118% | -25% | 30 | +0.03 | 3.7% → 3.9% | – | analyst α +0.23 · momentum +0.14 |
| 🟢 Buy | +0.69 | **Advantest**<br><small>6857.T</small> | 28,200 JPY | +51% | -5.4% | +151% | -3% | 35 | +0.33 | 2.2% → 2.9% | – | analyst α -0.19 · momentum +0.17 · ⚠️ rich valuation |
| 🟢 Buy | +0.66 | **INTC**<br><small>Intel</small> | 56.34 USD | +107% | +8.2% | +181% | -35% | 26 | -0.62 | 1.8% → 2.4% | ADD 79 | analyst α +0.41 · momentum +0.26 · ⚠️ oversold, rich valuation, high σ(e) |
| 🟢 Buy | +0.39 | **Infineon**<br><small>IFX.DE</small> | 45.92 EUR | +89% | +3.9% | +78% | -20% | 33 | -0.04 | 1.4% → 2.5% | ADD 163 | analyst α +0.19 · quality -0.04 |
| 🟢 Buy | +0.27 | **NVDA**<br><small>NVIDIA</small> | 186.68 USD | +76% | +0.5% | +22% | -9% | 31 | +0.47 | 1.4% → 1.7% | – | momentum -0.23 · quality +0.21 |
| 🟢 Buy | +0.26 | **LRCX**<br><small>Lam Research</small> | 200.35 USD | +87% | +3.8% | +97% | -29% | 30 | +0.02 | 1.4% → 1.5% | – | analyst α +0.15 · trend -0.12 |
| ⚪ Hold | +0.17 | **ASX**<br><small>ASE Technology</small> | 31.62 USD | +61% | -1.2% | +205% | -6% | 33 | -0.68 | 1.2% → 1.2% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| ⚪ Hold | +0.14 | **Samsung**<br><small>005930.KS</small> | 190,400 KRW | – | +0.0% | +170% | -19% | 33 | -0.26 | 9.7% → 9.7% | – | momentum +0.23 · quality -0.16 · ⚠️ cycle-peak P/E |
| ⚪ Hold | +0.13 | **TSM**<br><small>TSMC</small> | 375.29 USD | +47% | -5.7% | +58% | -6% | 36 | +0.58 | 5.9% → 5.9% | – | quality +0.28 · analyst α -0.23 |
| ⚪ Hold | +0.09 | **KLAC**<br><small>KLA Corp</small> | 138.49 USD | +69% | -0.5% | +61% | -24% | 35 | +0.51 | 4.6% → 4.6% | – | quality +0.24 · analyst α -0.08 |
| ⚪ Hold | +0.07 | **TER**<br><small>Teradyne</small> | 218.20 USD | +105% | +8.1% | +118% | -38% | 24 | -0.31 | 0.9% → 0.9% | – | analyst α +0.36 · trend -0.25 · ⚠️ oversold |
| ⚪ Hold | +0.04 | **Tokyo Electron**<br><small>8035.T</small> | 8,290 JPY | +84% | +3.2% | +114% | -20% | 32 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · analyst α +0.12 |
| ⚪ Hold | +0.01 | **AMD**<br><small>Advanced Micro Devices</small> | 449.03 USD | +38% | -9.2% | +156% | +8% | 38 | -0.15 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.32 |
| ⚪ Hold | -0.09 | **AMKR**<br><small>Amkor Technology</small> | 32.82 USD | +133% | +14.9% | +41% | -42% | 33 | -1.00 | 0.0% → 0.0% | – | analyst α +0.85 · quality -0.43 |
| 🔴 Sell | -0.25 | **ASML**<br><small>ASML Holding</small> | 1,424.75 USD | +47% | -6.1% | +70% | -11% | 35 | +0.42 | 0.0% → 0.0% | – | analyst α -0.31 · quality +0.18 |
| 🔴 Sell | -0.27 | **ASMI**<br><small>ASM.AS</small> | 649.60 EUR | +74% | +0.2% | +70% | -20% | 33 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · trend -0.03 |
| 🔴 Sell | -0.29 | **Disco**<br><small>6146.T</small> | 40,820 JPY | +100% | +7.4% | +22% | -37% | 27 | +0.06 | 0.0% → 0.0% | – | analyst α +0.31 · momentum -0.26 · ⚠️ oversold |
| 🔴 Sell | -0.31 | **GFS**<br><small>GlobalFoundries</small> | 38.60 USD | +97% | +6.2% | +41% | -30% | 36 | -0.21 | 0.0% → 0.0% | – | analyst α +0.27 · trend -0.14 |
| 🔴 Sell | -0.53 | **AVGO**<br><small>Broadcom</small> | 293.33 USD | +81% | +2.7% | +2% | -20% | 33 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.11 |
| 🔴 Sell | -0.64 | **ENTG**<br><small>Entegris</small> | 128.00 USD | +35% | -8.8% | +94% | -8% | 38 | -0.02 | 0.0% → 0.0% | – | analyst α -0.36 · trend +0.09 |
| 🔴 Sell | -0.69 | **ARM**<br><small>Arm Holdings</small> | 174.53 USD | +65% | -3.5% | +68% | -24% | 31 | +0.04 | 0.0% → 0.0% | – | analyst α -0.15 · trend -0.09 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.73 | **TXN**<br><small>Texas Instruments</small> | 277.35 USD | +17% | -12.9% | +79% | +7% | 43 | +0.24 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.25 |
| 🔴🔴 Strong Sell | -1.19 | **SMIC**<br><small>0981.HK</small> | 45.58 HKD | +111% | +10.9% | -24% | -32% | 37 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.53 |
| 🔴🔴 Strong Sell | -1.19 | **SNPS**<br><small>Synopsys</small> | 450.19 USD | +27% | -10.9% | +29% | +2% | 48 | +0.14 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.21 |
| 🔴🔴 Strong Sell | -1.24 | **CDNS**<br><small>Cadence Design Systems</small> | 319.81 USD | +27% | -10.8% | +9% | -2% | 46 | +0.31 | 0.0% → 0.0% | – | analyst α -0.48 · momentum -0.30 |
| 🔴🔴 Strong Sell | -1.34 | **Shin-Etsu**<br><small>4063.T</small> | 5,329 JPY | +46% | -5.8% | +29% | -16% | 28 | -0.20 | 0.0% → 0.0% | – | analyst α -0.27 · momentum -0.17 · ⚠️ oversold |
| 🔴🔴 Strong Sell | -1.52 | **QCOM**<br><small>Qualcomm</small> | 165.59 USD | +17% | -13.2% | +3% | -2% | 44 | +0.70 | 0.0% → 0.0% | – | analyst α -0.85 · quality +0.43 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +3.36"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 689.42 USD (+120%, 46 analysts); de-biased α +11.7% vs CAPM hurdle 14.0%. Downtrend -9% vs 200-day avg; 12-1 mom +332%; RSI 31. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.64"
    Within rebalance band of target 6.7%: no trade. Analyst target 293.88 USD vs 141.19 USD (+108%, 43 analysts); de-biased α +8.6% vs CAPM hurdle 14.1%. Downtrend -24% vs 200-day avg; 12-1 mom +195%; RSI 26. Quality z -0.12 (ROE 19%). ⚠️ oversold; price implies 78% stage-1 growth (reverse DCF).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.63"
    Within rebalance band of target 6.2%: no trade. No reliable analyst target: α set to 0. Downtrend -24% vs 200-day avg; 12-1 mom +224%; RSI 34. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "AMAT (AMAT) — 🟢 Buy, score +0.72"
    Within rebalance band of target 3.9%: no trade. Analyst target 638.94 USD vs 332.81 USD (+92%, 36 analysts); de-biased α +5.2% vs CAPM hurdle 11.6%. Downtrend -25% vs 200-day avg; 12-1 mom +118%; RSI 30. Quality z +0.03 (ROE 36%).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.69"
    Within rebalance band of target 2.9%: no trade. Analyst target 42,686 JPY vs 28,200 JPY (+51%, 21 analysts); de-biased α -5.4% vs CAPM hurdle 13.4%. Downtrend -3% vs 200-day avg; 12-1 mom +151%; RSI 35. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? success "INTC (INTC) — 🟢 Buy, score +0.66"
    **ADD 79 sh** → target 2.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 116.37 USD vs 56.34 USD (+107%, 43 analysts); de-biased α +8.2% vs CAPM hurdle 14.0%. Downtrend -35% vs 200-day avg; 12-1 mom +181%; RSI 26. Quality z -0.62 (ROE -0%). ⚠️ oversold; price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.39"
    **ADD 163 sh** → target 2.5% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 86.74 EUR vs 45.92 EUR (+89%, 23 analysts); de-biased α +3.9% vs CAPM hurdle 14.1%. Downtrend -20% vs 200-day avg; 12-1 mom +78%; RSI 33. Quality z -0.04 (ROE 6%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.27"
    Within rebalance band of target 1.7%: no trade. Analyst target 327.70 USD vs 186.68 USD (+76%, 59 analysts); de-biased α +0.5% vs CAPM hurdle 13.9%. Downtrend -9% vs 200-day avg; 12-1 mom +22%; RSI 31. Quality z +0.47 (ROE 101%).

??? success "LRCX (LRCX) — 🟢 Buy, score +0.26"
    Within rebalance band of target 1.5%: no trade. Analyst target 375.06 USD vs 200.35 USD (+87%, 31 analysts); de-biased α +3.8% vs CAPM hurdle 12.6%. Downtrend -29% vs 200-day avg; 12-1 mom +97%; RSI 30. Quality z +0.02 (ROE 65%).

??? note "ASX (ASX) — ⚪ Hold, score +0.17"
    Hold zone: keep any existing position, no new money. Analyst target 51.00 USD vs 31.62 USD (+61%, 1 analysts); de-biased α -1.2% vs CAPM hurdle 11.9%. Downtrend -6% vs 200-day avg; 12-1 mom +205%; RSI 33. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? note "Samsung (005930.KS) — ⚪ Hold, score +0.14"
    Hold zone: keep any existing position, no new money. No reliable analyst target: α set to 0. Downtrend -19% vs 200-day avg; 12-1 mom +170%; RSI 33. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? note "TSM (TSM) — ⚪ Hold, score +0.13"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 375.29 USD (+47%, 20 analysts); de-biased α -5.7% vs CAPM hurdle 10.8%. Downtrend -6% vs 200-day avg; 12-1 mom +58%; RSI 36. Quality z +0.58 (ROE 35%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.09"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 138.49 USD (+69%, 26 analysts); de-biased α -0.5% vs CAPM hurdle 11.1%. Downtrend -24% vs 200-day avg; 12-1 mom +61%; RSI 35. Quality z +0.51 (ROE 87%).

??? note "TER (TER) — ⚪ Hold, score +0.07"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 218.20 USD (+105%, 15 analysts); de-biased α +8.1% vs CAPM hurdle 12.3%. Downtrend -38% vs 200-day avg; 12-1 mom +118%; RSI 24. Quality z -0.31 (ROE 20%). ⚠️ oversold.

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.04"
    Hold zone: not owned, no entry. Analyst target 15,275 JPY vs 8,290 JPY (+84%, 23 analysts); de-biased α +3.2% vs CAPM hurdle 12.8%. Downtrend -20% vs 200-day avg; 12-1 mom +114%; RSI 32. Quality z -0.28 (ROE 29%).

??? note "AMD (AMD) — ⚪ Hold, score +0.01"
    Hold zone: not owned, no entry. Analyst target 619.51 USD vs 449.03 USD (+38%, 50 analysts); de-biased α -9.2% vs CAPM hurdle 14.9%. Uptrend +8% vs 200-day avg; 12-1 mom +156%; RSI 38. Quality z -0.15 (ROE 7%).

??? note "AMKR (AMKR) — ⚪ Hold, score -0.09"
    Hold zone: not owned, no entry. Analyst target 76.40 USD vs 32.82 USD (+133%, 10 analysts); de-biased α +14.9% vs CAPM hurdle 14.0%. Downtrend -42% vs 200-day avg; 12-1 mom +41%; RSI 33. Quality z -1.00 (ROE 9%).

??? failure "ASML (ASML) — 🔴 Sell, score -0.25"
    Avoid: not owned. Analyst target 2,096.77 USD vs 1,424.75 USD (+47%, 16 analysts); de-biased α -6.1% vs CAPM hurdle 12.3%. Downtrend -11% vs 200-day avg; 12-1 mom +70%; RSI 35. Quality z +0.42 (ROE 50%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.27"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 649.60 EUR (+74%, 19 analysts); de-biased α +0.2% vs CAPM hurdle 13.2%. Downtrend -20% vs 200-day avg; 12-1 mom +70%; RSI 33. Quality z -0.10 (ROE 19%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.29"
    Avoid: not owned. Analyst target 81,730 JPY vs 40,820 JPY (+100%, 20 analysts); de-biased α +7.4% vs CAPM hurdle 11.5%. Downtrend -37% vs 200-day avg; 12-1 mom +22%; RSI 27. Quality z +0.06 (ROE 25%). ⚠️ oversold.

??? failure "GFS (GFS) — 🔴 Sell, score -0.31"
    Avoid: not owned. Analyst target 76.00 USD vs 38.60 USD (+97%, 22 analysts); de-biased α +6.2% vs CAPM hurdle 12.4%. Downtrend -30% vs 200-day avg; 12-1 mom +41%; RSI 36. Quality z -0.21 (ROE 8%).

??? failure "AVGO (AVGO) — 🔴 Sell, score -0.53"
    Avoid: not owned. Analyst target 531.31 USD vs 293.33 USD (+81%, 47 analysts); de-biased α +2.7% vs CAPM hurdle 11.2%. Downtrend -20% vs 200-day avg; 12-1 mom +2%; RSI 33. Quality z +0.26 (ROE 31%).

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.64"
    Avoid: not owned. Analyst target 173.36 USD vs 128.00 USD (+35%, 11 analysts); de-biased α -8.8% vs CAPM hurdle 11.0%. Downtrend -8% vs 200-day avg; 12-1 mom +94%; RSI 38. Quality z -0.02 (ROE 6%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.69"
    Avoid: not owned. Analyst target 288.70 USD vs 174.53 USD (+65%, 40 analysts); de-biased α -3.5% vs CAPM hurdle 19.6%. Downtrend -24% vs 200-day avg; 12-1 mom +68%; RSI 31. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "TXN (TXN) — 🔴 Sell, score -0.73"
    Avoid: not owned. Analyst target 324.71 USD vs 277.35 USD (+17%, 31 analysts); de-biased α -12.9% vs CAPM hurdle 10.8%. Uptrend +7% vs 200-day avg; 12-1 mom +79%; RSI 43. Quality z +0.24 (ROE 30%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.19"
    Avoid: not owned. Analyst target 95.99 HKD vs 45.58 HKD (+111%, 21 analysts); de-biased α +10.9% vs CAPM hurdle 7.3%. Downtrend -32% vs 200-day avg; 12-1 mom -24%; RSI 37. Quality z -0.99 (ROE 3%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.19"
    Avoid: not owned. Analyst target 569.78 USD vs 450.19 USD (+27%, 26 analysts); de-biased α -10.9% vs CAPM hurdle 10.3%. Uptrend +2% vs 200-day avg; 12-1 mom +29%; RSI 48. Quality z +0.14 (ROE 7%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.24"
    Avoid: not owned. Analyst target 405.47 USD vs 319.81 USD (+27%, 26 analysts); de-biased α -10.8% vs CAPM hurdle 10.0%. Downtrend -2% vs 200-day avg; 12-1 mom +9%; RSI 46. Quality z +0.31 (ROE 22%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.34"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,329 JPY (+46%, 17 analysts); de-biased α -5.8% vs CAPM hurdle 10.8%. Downtrend -16% vs 200-day avg; 12-1 mom +29%; RSI 28. Quality z -0.20 (ROE 10%). ⚠️ oversold.

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.52"
    Avoid: not owned. Analyst target 194.13 USD vs 165.59 USD (+17%, 30 analysts); de-biased α -13.2% vs CAPM hurdle 11.9%. Downtrend -2% vs 200-day avg; 12-1 mom +3%; RSI 44. Quality z +0.70 (ROE 23%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 116 | 689.42 USD | $79,973 | 9.9% | Strong Buy |
| 005930.KS | Samsung Electronics | 562 | 190,400 KRW | $78,469 | 9.7% | Hold |
| TSM | TSMC | 127 | 375.29 USD | $47,661 | 5.9% | Hold |
| MRVL | Marvell Technology | 324 | 141.19 USD | $45,746 | 5.6% | Strong Buy |
| 000660.KS | SK hynix | 50 | 1,144,000 KRW | $41,946 | 5.2% | Strong Buy |
| KLAC | KLA Corp | 268 | 138.49 USD | $37,115 | 4.6% | Hold |
| AMAT | Applied Materials | 91 | 332.81 USD | $30,286 | 3.7% | Buy |
| 6857.T | Advantest | 100 | 28,200 JPY | $17,800 | 2.2% | Buy |
| INTC | Intel | 263 | 56.34 USD | $14,817 | 1.8% | Buy |
| LRCX | Lam Research | 58 | 200.35 USD | $11,620 | 1.4% | Buy |
| IFX.DE | Infineon Technologies | 225 | 45.92 EUR | $11,512 | 1.4% | Buy |
| NVDA | NVIDIA | 60 | 186.68 USD | $11,201 | 1.4% | Buy |
| ASX | ASE Technology | 312 | 31.62 USD | $9,867 | 1.2% | Hold |
| TER | Teradyne | 35 | 218.20 USD | $7,637 | 0.9% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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
| 2026-11-02 06:06 UTC | SELL (exit) | 8035.T | -500 | 10,115.00 | $32,062 |
| 2026-10-30 19:24 UTC | TRIM | MU | -28 | 866.70 | $24,267 |
| 2026-10-30 19:24 UTC | TRIM | AMAT | -65 | 385.15 | $25,035 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 59.9%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
