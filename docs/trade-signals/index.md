---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-08 08:59 UTC (Thu Oct 08, 04:59 AM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Thu 04:59) · Tokyo 🔴 closed (Thu 17:59) · Korea 🔴 closed (Thu 17:59) · Hong Kong 🔴 closed (Thu 16:59) · Xetra 🟢 open (Thu 10:59) · Euronext Amsterdam 🟢 open (Thu 10:59)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$1,032,477** | $136,685 (13%) | $895,793 (87%) | +3.25% | +3.06% | 🟢 Risk-on (+26.9%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $1,032,477), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| BUY (new) | **ASML**<br><small>ASML Holding</small> | 25 | 1,804.70 USD | $45,117 | Queued · NYSE/Nasdaq closed | quality +0.18 · analyst α -0.08 |
| ADD | **Infineon**<br><small>IFX.DE</small> | 479 | 59.28 EUR | $31,780 | Executed (paper) | analyst α +0.41 · trend -0.10 |
| TRIM | **TSM**<br><small>TSMC</small> | 33 | 472.15 USD | $15,581 | Queued · NYSE/Nasdaq closed | quality +0.28 · momentum -0.12 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.33 | **SK hynix**<br><small>000660.KS</small> | 1,699,000 KRW | +85% | +14.1% | +371% | +18% | 45 | +0.62 | 9.1% → 10.0% | – | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.21 | **MU**<br><small>Micron Technology</small> | 1,087.83 USD | +40% | +2.9% | +454% | +56% | 60 | +0.12 | 9.7% → 10.0% | – | momentum +0.53 · analyst α +0.27 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.59 | **Samsung**<br><small>005930.KS</small> | 264,000 KRW | +81% | +14.0% | +210% | +15% | 49 | -0.26 | 9.2% → 10.0% | – | analyst α +0.66 · momentum +0.30 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.58 | **Infineon**<br><small>IFX.DE</small> | 59.28 EUR | +46% | +4.7% | +73% | +6% | 50 | -0.04 | 9.1% → 9.1% | ADD 479 | analyst α +0.41 · trend -0.10 |
| 🟢 Buy | +0.51 | **NVDA**<br><small>NVIDIA</small> | 237.36 USD | +38% | +2.5% | +21% | +18% | 64 | +0.47 | 8.5% → 8.0% | – | analyst α +0.23 · quality +0.21 |
| 🟢 Buy | +0.43 | **ASX**<br><small>ASE Technology</small> | 45.77 USD | +11% | -1.7% | +266% | +47% | 61 | -0.68 | 6.7% → 6.3% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.41 | **AMAT**<br><small>Applied Materials</small> | 520.65 USD | +23% | -0.7% | +112% | +21% | 60 | +0.03 | 6.5% → 5.5% | – | momentum +0.10 · analyst α +0.05 |
| 🟢 Buy | +0.37 | **TSM**<br><small>TSMC</small> | 472.15 USD | +17% | -1.8% | +49% | +21% | 65 | +0.58 | 8.6% → 7.0% | TRIM 33 | quality +0.28 · momentum -0.12 |
| 🟢 Buy | +0.36 | **KLAC**<br><small>KLA Corp</small> | 196.76 USD | +19% | -1.5% | +70% | +10% | 56 | +0.51 | 5.1% → 5.2% | – | quality +0.24 · trend -0.07 |
| 🟢 Buy | +0.25 | **ASML**<br><small>ASML Holding</small> | 1,804.70 USD | +16% | -2.4% | +74% | +16% | 56 | +0.42 | 0.0% → 4.4% | BUY 25 | quality +0.18 · analyst α -0.08 |
| ⚪ Hold | +0.16 | **Tokyo Electron**<br><small>8035.T</small> | 12,235 JPY | +25% | -0.2% | +99% | +25% | 61 | -0.28 | 4.5% → 4.5% | – | quality -0.18 · trend +0.10 |
| ⚪ Hold | +0.08 | **Advantest**<br><small>6857.T</small> | 41,060 JPY | +4% | -5.8% | +116% | +48% | 71 | +0.33 | 5.0% → 5.0% | – | analyst α -0.41 · trend +0.18 · ⚠️ rich valuation |
| ⚪ Hold | +0.07 | **AVGO**<br><small>Broadcom</small> | 376.27 USD | +41% | +4.2% | +9% | +3% | 59 | +0.26 | 4.9% → 4.9% | – | analyst α +0.31 · momentum -0.26 |
| ⚪ Hold | -0.10 | **GFS**<br><small>GlobalFoundries</small> | 48.06 USD | +58% | +8.0% | +32% | -12% | 51 | -0.21 | 0.0% → 0.0% | – | analyst α +0.48 · trend -0.25 |
| ⚪ Hold | -0.13 | **LRCX**<br><small>Lam Research</small> | 329.33 USD | +14% | -3.1% | +126% | +18% | 57 | +0.02 | 0.0% → 0.0% | – | analyst α -0.23 · momentum +0.14 |
| ⚪ Hold | -0.15 | **ASMI**<br><small>ASM.AS</small> | 891.20 EUR | +27% | -0.1% | +55% | +11% | 55 | -0.10 | 0.0% → 0.0% | – | analyst α +0.12 · momentum -0.07 |
| ⚪ Hold | -0.23 | **MRVL**<br><small>Marvell Technology</small> | 284.73 USD | +3% | -6.2% | +171% | +67% | 68 | -0.12 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.25 · ⚠️ rich valuation |
| 🔴 Sell | -0.36 | **Disco**<br><small>6146.T</small> | 61,360 JPY | +33% | +2.1% | +13% | -6% | 58 | +0.06 | 0.0% → 0.0% | – | momentum -0.23 · analyst α +0.19 |
| 🔴 Sell | -0.36 | **TXN**<br><small>Texas Instruments</small> | 288.95 USD | +12% | -2.7% | +52% | +16% | 62 | +0.24 | 0.0% → 0.0% | – | analyst α -0.15 · momentum -0.10 |
| 🔴 Sell | -0.45 | **AMKR**<br><small>Amkor Technology</small> | 52.30 USD | +46% | +4.7% | +74% | -9% | 50 | -1.00 | 0.0% → 0.0% | – | quality -0.43 · analyst α +0.36 |
| 🔴 Sell | -0.49 | **TER**<br><small>Teradyne</small> | 411.53 USD | +8% | -4.4% | +174% | +21% | 55 | -0.31 | 0.0% → 0.0% | – | analyst α -0.31 · momentum +0.23 |
| 🔴 Sell | -0.54 | **QCOM**<br><small>Qualcomm</small> | 177.12 USD | +10% | -3.6% | +5% | +5% | 46 | +0.70 | 0.0% → 0.0% | – | quality +0.43 · momentum -0.30 |
| 🔴 Sell | -0.55 | **AMD**<br><small>Advanced Micro Devices</small> | 645.83 USD | -4% | -8.3% | +146% | +68% | 71 | -0.15 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.32 |
| 🔴 Sell | -0.59 | **Shin-Etsu**<br><small>4063.T</small> | 6,130 JPY | +27% | +0.9% | +25% | -2% | 56 | -0.20 | 0.0% → 0.0% | – | momentum -0.17 · trend -0.16 |
| 🔴 Sell | -0.73 | **ENTG**<br><small>Entegris</small> | 166.23 USD | +4% | -5.1% | +56% | +24% | 68 | -0.02 | 0.0% → 0.0% | – | analyst α -0.36 · trend +0.09 |
| 🔴🔴 Strong Sell | -0.82 | **INTC**<br><small>Intel</small> | 113.06 USD | +3% | -6.3% | +186% | +37% | 53 | -0.62 | 0.0% → 0.0% | – | analyst α -0.55 · momentum +0.26 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -0.91 | **SMIC**<br><small>0981.HK</small> | 56.80 HKD | +69% | +11.9% | -10% | -18% | 30 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.35 |
| 🔴🔴 Strong Sell | -1.00 | **CDNS**<br><small>Cadence Design Systems</small> | 356.22 USD | +14% | -2.6% | -18% | +9% | 71 | +0.31 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.13 |
| 🔴🔴 Strong Sell | -1.43 | **SNPS**<br><small>Synopsys</small> | 502.51 USD | +13% | -2.8% | -18% | +13% | 75 | +0.14 | 0.0% → 0.0% | – | momentum -0.53 · analyst α -0.19 |
| 🔴🔴 Strong Sell | -1.53 | **ARM**<br><small>Arm Holdings</small> | 294.37 USD | -2% | -8.9% | +67% | +35% | 53 | +0.04 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.12 · ⚠️ rich valuation, high σ(e) |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.33"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,699,000 KRW (+85%, 38 analysts); de-biased α +14.1% vs CAPM hurdle 14.3%. Uptrend +18% vs 200-day avg; 12-1 mom +371%; RSI 45. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.21"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 1,087.83 USD (+40%, 46 analysts); de-biased α +2.9% vs CAPM hurdle 14.0%. Uptrend +56% vs 200-day avg; 12-1 mom +454%; RSI 60. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.59"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 264,000 KRW (+81%, 36 analysts); de-biased α +14.0% vs CAPM hurdle 11.3%. Uptrend +15% vs 200-day avg; 12-1 mom +210%; RSI 49. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.58"
    **ADD 479 sh** → target 9.1% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 86.74 EUR vs 59.28 EUR (+46%, 23 analysts); de-biased α +4.7% vs CAPM hurdle 14.1%. Uptrend +6% vs 200-day avg; 12-1 mom +73%; RSI 50. Quality z -0.04 (ROE 6%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.51"
    Within rebalance band of target 8.0%: no trade. Analyst target 327.70 USD vs 237.36 USD (+38%, 59 analysts); de-biased α +2.5% vs CAPM hurdle 13.9%. Uptrend +18% vs 200-day avg; 12-1 mom +21%; RSI 64. Quality z +0.47 (ROE 101%).

??? success "ASX (ASX) — 🟢 Buy, score +0.43"
    Within rebalance band of target 6.3%: no trade. Analyst target 51.00 USD vs 45.77 USD (+11%, 1 analysts); de-biased α -1.7% vs CAPM hurdle 11.9%. Uptrend +47% vs 200-day avg; 12-1 mom +266%; RSI 61. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.41"
    Within rebalance band of target 5.5%: no trade. Analyst target 638.94 USD vs 520.65 USD (+23%, 36 analysts); de-biased α -0.7% vs CAPM hurdle 11.6%. Uptrend +21% vs 200-day avg; 12-1 mom +112%; RSI 60. Quality z +0.03 (ROE 36%).

??? success "TSM (TSM) — 🟢 Buy, score +0.37"
    **TRIM 33 sh** → target 7.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 552.26 USD vs 472.15 USD (+17%, 20 analysts); de-biased α -1.8% vs CAPM hurdle 10.8%. Uptrend +21% vs 200-day avg; 12-1 mom +49%; RSI 65. Quality z +0.58 (ROE 35%).

??? success "KLAC (KLAC) — 🟢 Buy, score +0.36"
    Within rebalance band of target 5.2%: no trade. Analyst target 233.77 USD vs 196.76 USD (+19%, 26 analysts); de-biased α -1.5% vs CAPM hurdle 11.1%. Uptrend +10% vs 200-day avg; 12-1 mom +70%; RSI 56. Quality z +0.51 (ROE 87%).

??? success "ASML (ASML) — 🟢 Buy, score +0.25"
    **BUY (new) 25 sh** → target 4.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 2,096.77 USD vs 1,804.70 USD (+16%, 16 analysts); de-biased α -2.4% vs CAPM hurdle 12.3%. Uptrend +16% vs 200-day avg; 12-1 mom +74%; RSI 56. Quality z +0.42 (ROE 50%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.16"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 12,235 JPY (+25%, 23 analysts); de-biased α -0.2% vs CAPM hurdle 12.8%. Uptrend +25% vs 200-day avg; 12-1 mom +99%; RSI 61. Quality z -0.28 (ROE 29%).

??? note "Advantest (6857.T) — ⚪ Hold, score +0.08"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 41,060 JPY (+4%, 21 analysts); de-biased α -5.8% vs CAPM hurdle 13.4%. Uptrend +48% vs 200-day avg; 12-1 mom +116%; RSI 71. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "AVGO (AVGO) — ⚪ Hold, score +0.07"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 376.27 USD (+41%, 47 analysts); de-biased α +4.2% vs CAPM hurdle 11.2%. Uptrend +3% vs 200-day avg; 12-1 mom +9%; RSI 59. Quality z +0.26 (ROE 31%).

??? note "GFS (GFS) — ⚪ Hold, score -0.10"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 48.06 USD (+58%, 22 analysts); de-biased α +8.0% vs CAPM hurdle 12.4%. Downtrend -12% vs 200-day avg; 12-1 mom +32%; RSI 51. Quality z -0.21 (ROE 8%).

??? note "LRCX (LRCX) — ⚪ Hold, score -0.13"
    Hold zone: not owned, no entry. Analyst target 375.06 USD vs 329.33 USD (+14%, 31 analysts); de-biased α -3.1% vs CAPM hurdle 12.6%. Uptrend +18% vs 200-day avg; 12-1 mom +126%; RSI 57. Quality z +0.02 (ROE 65%).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.15"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 891.20 EUR (+27%, 19 analysts); de-biased α -0.1% vs CAPM hurdle 13.2%. Uptrend +11% vs 200-day avg; 12-1 mom +55%; RSI 55. Quality z -0.10 (ROE 19%).

??? note "MRVL (MRVL) — ⚪ Hold, score -0.23"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 284.73 USD (+3%, 43 analysts); de-biased α -6.2% vs CAPM hurdle 14.1%. Uptrend +67% vs 200-day avg; 12-1 mom +171%; RSI 68. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.36"
    Avoid: not owned. Analyst target 81,730 JPY vs 61,360 JPY (+33%, 20 analysts); de-biased α +2.1% vs CAPM hurdle 11.5%. Downtrend -6% vs 200-day avg; 12-1 mom +13%; RSI 58. Quality z +0.06 (ROE 25%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.36"
    Avoid: not owned. Analyst target 324.71 USD vs 288.95 USD (+12%, 31 analysts); de-biased α -2.7% vs CAPM hurdle 10.8%. Uptrend +16% vs 200-day avg; 12-1 mom +52%; RSI 62. Quality z +0.24 (ROE 30%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.45"
    Avoid: not owned. Analyst target 76.40 USD vs 52.30 USD (+46%, 10 analysts); de-biased α +4.7% vs CAPM hurdle 14.0%. Downtrend -9% vs 200-day avg; 12-1 mom +74%; RSI 50. Quality z -1.00 (ROE 9%).

??? failure "TER (TER) — 🔴 Sell, score -0.49"
    Avoid: not owned. Analyst target 446.47 USD vs 411.53 USD (+8%, 15 analysts); de-biased α -4.4% vs CAPM hurdle 12.3%. Uptrend +21% vs 200-day avg; 12-1 mom +174%; RSI 55. Quality z -0.31 (ROE 20%).

??? failure "QCOM (QCOM) — 🔴 Sell, score -0.54"
    Avoid: not owned. Analyst target 194.13 USD vs 177.12 USD (+10%, 30 analysts); de-biased α -3.6% vs CAPM hurdle 11.9%. Uptrend +5% vs 200-day avg; 12-1 mom +5%; RSI 46. Quality z +0.70 (ROE 23%).

??? failure "AMD (AMD) — 🔴 Sell, score -0.55"
    Avoid: not owned. Analyst target 619.51 USD vs 645.83 USD (-4%, 50 analysts); de-biased α -8.3% vs CAPM hurdle 14.9%. Uptrend +68% vs 200-day avg; 12-1 mom +146%; RSI 71. Quality z -0.15 (ROE 7%).

??? failure "Shin-Etsu (4063.T) — 🔴 Sell, score -0.59"
    Avoid: not owned. Analyst target 7,763 JPY vs 6,130 JPY (+27%, 17 analysts); de-biased α +0.9% vs CAPM hurdle 10.8%. Downtrend -2% vs 200-day avg; 12-1 mom +25%; RSI 56. Quality z -0.20 (ROE 10%).

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.73"
    Avoid: not owned. Analyst target 173.36 USD vs 166.23 USD (+4%, 11 analysts); de-biased α -5.1% vs CAPM hurdle 11.0%. Uptrend +24% vs 200-day avg; 12-1 mom +56%; RSI 68. Quality z -0.02 (ROE 6%).

??? failure "INTC (INTC) — 🔴🔴 Strong Sell, score -0.82"
    Avoid: not owned. Analyst target 116.37 USD vs 113.06 USD (+3%, 43 analysts); de-biased α -6.3% vs CAPM hurdle 14.0%. Uptrend +37% vs 200-day avg; 12-1 mom +186%; RSI 53. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -0.91"
    Avoid: not owned. Analyst target 95.99 HKD vs 56.80 HKD (+69%, 21 analysts); de-biased α +11.9% vs CAPM hurdle 7.3%. Downtrend -18% vs 200-day avg; 12-1 mom -10%; RSI 30. Quality z -0.99 (ROE 3%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.00"
    Avoid: not owned. Analyst target 405.47 USD vs 356.22 USD (+14%, 26 analysts); de-biased α -2.6% vs CAPM hurdle 10.0%. Uptrend +9% vs 200-day avg; 12-1 mom -18%; RSI 71. Quality z +0.31 (ROE 22%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.43"
    Avoid: not owned. Analyst target 569.78 USD vs 502.51 USD (+13%, 26 analysts); de-biased α -2.8% vs CAPM hurdle 10.3%. Uptrend +13% vs 200-day avg; 12-1 mom -18%; RSI 75. Quality z +0.14 (ROE 7%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.53"
    Avoid: not owned. Analyst target 288.70 USD vs 294.37 USD (-2%, 40 analysts); de-biased α -8.9% vs CAPM hurdle 19.6%. Uptrend +35% vs 200-day avg; 12-1 mom +67%; RSI 53. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 92 | 1,087.83 USD | $100,081 | 9.7% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 264,000 KRW | $95,354 | 9.2% | Strong Buy |
| 000660.KS | SK hynix | 74 | 1,699,000 KRW | $93,631 | 9.1% | Strong Buy |
| IFX.DE | Infineon Technologies | 1,411 | 59.28 EUR | $93,614 | 9.1% | Buy |
| TSM | TSMC | 187 | 472.15 USD | $88,292 | 8.6% | Buy |
| NVDA | NVIDIA | 371 | 237.36 USD | $88,061 | 8.5% | Buy |
| ASX | ASE Technology | 1,509 | 45.77 USD | $69,067 | 6.7% | Buy |
| AMAT | Applied Materials | 128 | 520.65 USD | $66,643 | 6.5% | Buy |
| KLAC | KLA Corp | 266 | 196.76 USD | $52,338 | 5.1% | Buy |
| 6857.T | Advantest | 200 | 41,060 JPY | $51,897 | 5.0% | Hold |
| AVGO | Broadcom | 134 | 376.27 USD | $50,421 | 4.9% | Hold |
| 8035.T | Tokyo Electron | 600 | 12,235 JPY | $46,393 | 4.5% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-10-08 08:59 UTC | ADD | IFX.DE | 479 | 59.28 | $31,780 |
| 2026-10-07 16:29 UTC | TRIM | KLAC | -184 | 195.46 | $35,964 |
| 2026-10-06 17:12 UTC | ADD | KLAC | 189 | 198.10 | $37,441 |
| 2026-10-06 17:12 UTC | TRIM | AVGO | -36 | 377.64 | $13,595 |
| 2026-10-06 10:19 UTC | ADD | IFX.DE | 316 | 63.45 | $22,554 |
| 2026-10-05 16:01 UTC | TRIM | KLAC | -208 | 203.82 | $42,395 |
| 2026-10-02 18:25 UTC | ADD | AMAT | 37 | 538.40 | $19,921 |
| 2026-10-02 12:37 UTC | TRIM | IFX.DE | -589 | 62.56 | $41,458 |
| 2026-10-02 05:39 UTC | TRIM | 6857.T | -100 | 38,710.00 | $24,524 |
| 2026-10-01 19:32 UTC | BUY (new) | ASX | 1,509 | 44.67 | $67,415 |
| 2026-10-01 05:56 UTC | TRIM | 6857.T | -100 | 37,090.00 | $23,417 |
| 2026-10-01 05:56 UTC | TRIM | 8035.T | -100 | 12,505.00 | $7,895 |
| 2026-09-30 19:21 UTC | TRIM | NVDA | -76 | 230.81 | $17,541 |
| 2026-09-30 13:45 UTC | TRIM | IFX.DE | -347 | 59.55 | $23,474 |
| 2026-09-30 00:28 UTC | BUY (new) | 8035.T | 700 | 11,900.00 | $52,952 |
| 2026-09-29 15:53 UTC | BUY (new) | TSM | 187 | 457.37 | $85,528 |
| 2026-09-29 15:53 UTC | TRIM | AMAT | -87 | 501.81 | $43,657 |
| 2026-09-29 15:53 UTC | TRIM | AVGO | -112 | 357.74 | $40,067 |
| 2026-09-28 15:29 UTC | BUY (new) | AVGO | 282 | 349.88 | $98,666 |
| 2026-09-28 00:48 UTC | BUY (new) | 005930.KS | 485 | 280,750.00 | $100,255 |
| 2026-09-28 00:48 UTC | BUY (new) | 6857.T | 400 | 34,870.00 | $88,422 |
| 2026-09-28 00:48 UTC | BUY (new) | 000660.KS | 74 | 1,818,500.00 | $99,080 |
| 2026-09-25 14:37 UTC | BUY (new) | KLAC | 469 | 186.53 | $87,480 |
| 2026-09-25 14:37 UTC | BUY (new) | NVDA | 447 | 223.82 | $100,048 |
| 2026-09-25 14:37 UTC | BUY (new) | AMAT | 178 | 479.88 | $85,419 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 14.1%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
