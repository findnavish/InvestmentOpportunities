---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-08 16:29 UTC (Thu Oct 08, 12:29 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🟢 open (Thu 12:29) · Tokyo 🔴 closed (Fri 01:29) · Korea 🔴 closed (Fri 01:29) · Hong Kong 🔴 closed (Fri 00:29) · Xetra 🔴 closed (Thu 18:29) · Euronext Amsterdam 🔴 closed (Thu 18:29)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$1,029,772** | $119,972 (12%) | $909,800 (88%) | +2.98% | +1.69% | 🟢 Risk-on (+24.9%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $1,029,772), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| SELL (exit) | **Advantest**<br><small>6857.T</small> | 200 | 41,060 JPY | $51,916 | Queued · Tokyo closed | analyst α -0.55 · quality +0.16 · ⚠️ rich valuation |
| ADD | **AMAT**<br><small>Applied Materials</small> | 32 | 522.02 USD | $16,705 | Executed (paper) | momentum +0.12 · trend +0.07 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.35 | **SK hynix**<br><small>000660.KS</small> | 1,699,000 KRW | +85% | +14.0% | +371% | +18% | 45 | +0.62 | 9.1% → 10.0% | – | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.23 | **MU**<br><small>Micron Technology</small> | 1,072.70 USD | +42% | +3.3% | +454% | +54% | 57 | +0.12 | 9.6% → 10.0% | – | momentum +0.53 · analyst α +0.27 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.60 | **Samsung**<br><small>005930.KS</small> | 264,000 KRW | +81% | +13.9% | +210% | +15% | 49 | -0.26 | 9.3% → 10.0% | – | analyst α +0.66 · momentum +0.30 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.59 | **Infineon**<br><small>IFX.DE</small> | 58.89 EUR | +47% | +4.8% | +73% | +5% | 49 | -0.04 | 9.0% → 10.0% | – | analyst α +0.41 · trend -0.10 |
| 🟢 Buy | +0.52 | **AMAT**<br><small>Applied Materials</small> | 522.02 USD | +22% | -0.8% | +123% | +21% | 60 | +0.03 | 8.1% → 8.1% | ADD 32 | momentum +0.12 · trend +0.07 |
| 🟢 Buy | +0.49 | **NVDA**<br><small>NVIDIA</small> | 235.52 USD | +39% | +2.7% | +21% | +17% | 61 | +0.47 | 8.5% → 9.0% | – | analyst α +0.23 · quality +0.21 |
| 🟢 Buy | +0.48 | **ASX**<br><small>ASE Technology</small> | 46.03 USD | +11% | -1.8% | +266% | +48% | 62 | -0.68 | 6.7% → 8.3% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.46 | **TSM**<br><small>TSMC</small> | 464.28 USD | +19% | -1.4% | +49% | +19% | 59 | +0.58 | 8.4% → 10.0% | – | quality +0.28 · momentum -0.12 |
| ⚪ Hold | +0.25 | **KLAC**<br><small>KLA Corp</small> | 201.37 USD | +16% | -2.3% | +70% | +12% | 60 | +0.51 | 5.2% → 5.2% | – | quality +0.24 · trend -0.06 |
| ⚪ Hold | +0.21 | **ASML**<br><small>ASML Holding</small> | 1,818.23 USD | +15% | -2.7% | +74% | +17% | 57 | +0.42 | 0.0% → 0.0% | – | quality +0.18 · analyst α -0.12 |
| ⚪ Hold | +0.16 | **Tokyo Electron**<br><small>8035.T</small> | 12,235 JPY | +25% | -0.3% | +99% | +25% | 61 | -0.28 | 4.5% → 4.5% | – | quality -0.18 · trend +0.10 |
| ⚪ Hold | +0.07 | **AVGO**<br><small>Broadcom</small> | 372.57 USD | +43% | +4.4% | +9% | +2% | 57 | +0.26 | 4.8% → 4.8% | – | analyst α +0.31 · momentum -0.26 |
| ⚪ Hold | -0.02 | **GFS**<br><small>GlobalFoundries</small> | 50.12 USD | +52% | +6.3% | +32% | -8% | 57 | -0.21 | 0.0% → 0.0% | – | analyst α +0.48 · trend -0.21 |
| ⚪ Hold | -0.13 | **LRCX**<br><small>Lam Research</small> | 329.45 USD | +14% | -3.2% | +126% | +18% | 57 | +0.02 | 0.0% → 0.0% | – | analyst α -0.23 · momentum +0.14 |
| ⚪ Hold | -0.18 | **ASMI**<br><small>ASM.AS</small> | 893.80 EUR | +26% | -0.3% | +55% | +12% | 56 | -0.10 | 0.0% → 0.0% | – | analyst α +0.12 · momentum -0.07 |
| ⚪ Hold | -0.23 | **MRVL**<br><small>Marvell Technology</small> | 277.73 USD | +6% | -5.7% | +171% | +63% | 63 | -0.12 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.25 · ⚠️ rich valuation |
| 🔴 Sell | -0.30 | **Advantest**<br><small>6857.T</small> | 41,060 JPY | +4% | -5.9% | +116% | +48% | 71 | +0.33 | 5.0% → 0.0% | SELL 200 | analyst α -0.55 · quality +0.16 · ⚠️ rich valuation |
| 🔴 Sell | -0.36 | **Disco**<br><small>6146.T</small> | 61,360 JPY | +33% | +2.0% | +13% | -6% | 58 | +0.06 | 0.0% → 0.0% | – | momentum -0.23 · analyst α +0.19 |
| 🔴 Sell | -0.36 | **TXN**<br><small>Texas Instruments</small> | 289.81 USD | +12% | -2.8% | +52% | +16% | 62 | +0.24 | 0.0% → 0.0% | – | analyst α -0.15 · momentum -0.10 |
| 🔴 Sell | -0.38 | **QCOM**<br><small>Qualcomm</small> | 173.82 USD | +12% | -3.2% | +9% | +3% | 43 | +0.70 | 0.0% → 0.0% | – | quality +0.43 · momentum -0.30 |
| 🔴 Sell | -0.49 | **TER**<br><small>Teradyne</small> | 407.45 USD | +10% | -4.3% | +174% | +20% | 54 | -0.31 | 0.0% → 0.0% | – | analyst α -0.31 · momentum +0.23 |
| 🔴 Sell | -0.54 | **INTC**<br><small>Intel</small> | 109.57 USD | +6% | -5.6% | +186% | +32% | 48 | -0.62 | 0.0% → 0.0% | – | analyst α -0.41 · momentum +0.26 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.54 | **AMKR**<br><small>Amkor Technology</small> | 52.07 USD | +47% | +4.7% | +74% | -9% | 49 | -1.00 | 0.0% → 0.0% | – | quality -0.43 · analyst α +0.36 |
| 🔴 Sell | -0.59 | **Shin-Etsu**<br><small>4063.T</small> | 6,130 JPY | +27% | +0.8% | +25% | -2% | 56 | -0.20 | 0.0% → 0.0% | – | momentum -0.17 · trend -0.16 |
| 🔴 Sell | -0.74 | **ENTG**<br><small>Entegris</small> | 164.96 USD | +5% | -5.0% | +56% | +23% | 66 | -0.02 | 0.0% → 0.0% | – | analyst α -0.36 · trend +0.09 |
| 🔴🔴 Strong Sell | -0.92 | **SMIC**<br><small>0981.HK</small> | 56.80 HKD | +69% | +11.8% | -10% | -18% | 30 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.35 |
| 🔴🔴 Strong Sell | -0.93 | **CDNS**<br><small>Cadence Design Systems</small> | 354.57 USD | +14% | -2.5% | -18% | +9% | 69 | +0.31 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.13 |
| 🔴🔴 Strong Sell | -0.96 | **AMD**<br><small>Advanced Micro Devices</small> | 633.28 USD | -2% | -7.9% | +146% | +65% | 66 | -0.15 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -1.14 | **ARM**<br><small>Arm Holdings</small> | 281.20 USD | +3% | -7.8% | +66% | +28% | 49 | +0.04 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.12 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.85 | **SNPS**<br><small>Synopsys</small> | 509.77 USD | +12% | -3.3% | -18% | +14% | 76 | +0.14 | 0.0% → 0.0% | – | momentum -0.53 · analyst α -0.27 · ⚠️ overbought |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.35"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,699,000 KRW (+85%, 38 analysts); de-biased α +14.0% vs CAPM hurdle 14.3%. Uptrend +18% vs 200-day avg; 12-1 mom +371%; RSI 45. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.23"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 1,072.70 USD (+42%, 46 analysts); de-biased α +3.3% vs CAPM hurdle 14.0%. Uptrend +54% vs 200-day avg; 12-1 mom +454%; RSI 57. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.60"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 264,000 KRW (+81%, 36 analysts); de-biased α +13.9% vs CAPM hurdle 11.3%. Uptrend +15% vs 200-day avg; 12-1 mom +210%; RSI 49. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.59"
    Within rebalance band of target 10.0%: no trade. Analyst target 86.74 EUR vs 58.89 EUR (+47%, 23 analysts); de-biased α +4.8% vs CAPM hurdle 14.1%. Uptrend +5% vs 200-day avg; 12-1 mom +73%; RSI 49. Quality z -0.04 (ROE 6%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.52"
    **ADD 32 sh** → target 8.1% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 522.02 USD (+22%, 36 analysts); de-biased α -0.8% vs CAPM hurdle 11.6%. Uptrend +21% vs 200-day avg; 12-1 mom +123%; RSI 60. Quality z +0.03 (ROE 36%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.49"
    Within rebalance band of target 9.0%: no trade. Analyst target 327.70 USD vs 235.52 USD (+39%, 59 analysts); de-biased α +2.7% vs CAPM hurdle 13.9%. Uptrend +17% vs 200-day avg; 12-1 mom +21%; RSI 61. Quality z +0.47 (ROE 101%).

??? success "ASX (ASX) — 🟢 Buy, score +0.48"
    Within rebalance band of target 8.3%: no trade. Analyst target 51.00 USD vs 46.03 USD (+11%, 1 analysts); de-biased α -1.8% vs CAPM hurdle 11.9%. Uptrend +48% vs 200-day avg; 12-1 mom +266%; RSI 62. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "TSM (TSM) — 🟢 Buy, score +0.46"
    Within rebalance band of target 10.0%: no trade. Analyst target 552.26 USD vs 464.28 USD (+19%, 20 analysts); de-biased α -1.4% vs CAPM hurdle 10.8%. Uptrend +19% vs 200-day avg; 12-1 mom +49%; RSI 59. Quality z +0.58 (ROE 35%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.25"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 201.37 USD (+16%, 26 analysts); de-biased α -2.3% vs CAPM hurdle 11.1%. Uptrend +12% vs 200-day avg; 12-1 mom +70%; RSI 60. Quality z +0.51 (ROE 87%).

??? note "ASML (ASML) — ⚪ Hold, score +0.21"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,818.23 USD (+15%, 16 analysts); de-biased α -2.7% vs CAPM hurdle 12.3%. Uptrend +17% vs 200-day avg; 12-1 mom +74%; RSI 57. Quality z +0.42 (ROE 50%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.16"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 12,235 JPY (+25%, 23 analysts); de-biased α -0.3% vs CAPM hurdle 12.8%. Uptrend +25% vs 200-day avg; 12-1 mom +99%; RSI 61. Quality z -0.28 (ROE 29%).

??? note "AVGO (AVGO) — ⚪ Hold, score +0.07"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 372.57 USD (+43%, 47 analysts); de-biased α +4.4% vs CAPM hurdle 11.2%. Uptrend +2% vs 200-day avg; 12-1 mom +9%; RSI 57. Quality z +0.26 (ROE 31%).

??? note "GFS (GFS) — ⚪ Hold, score -0.02"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 50.12 USD (+52%, 22 analysts); de-biased α +6.3% vs CAPM hurdle 12.4%. Downtrend -8% vs 200-day avg; 12-1 mom +32%; RSI 57. Quality z -0.21 (ROE 8%).

??? note "LRCX (LRCX) — ⚪ Hold, score -0.13"
    Hold zone: not owned, no entry. Analyst target 375.06 USD vs 329.45 USD (+14%, 31 analysts); de-biased α -3.2% vs CAPM hurdle 12.6%. Uptrend +18% vs 200-day avg; 12-1 mom +126%; RSI 57. Quality z +0.02 (ROE 65%).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.18"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 893.80 EUR (+26%, 19 analysts); de-biased α -0.3% vs CAPM hurdle 13.2%. Uptrend +12% vs 200-day avg; 12-1 mom +55%; RSI 56. Quality z -0.10 (ROE 19%).

??? note "MRVL (MRVL) — ⚪ Hold, score -0.23"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 277.73 USD (+6%, 43 analysts); de-biased α -5.7% vs CAPM hurdle 14.1%. Uptrend +63% vs 200-day avg; 12-1 mom +171%; RSI 63. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? failure "Advantest (6857.T) — 🔴 Sell, score -0.30"
    **SELL (exit) 200 sh** → target 0.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 42,686 JPY vs 41,060 JPY (+4%, 21 analysts); de-biased α -5.9% vs CAPM hurdle 13.4%. Uptrend +48% vs 200-day avg; 12-1 mom +116%; RSI 71. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.36"
    Avoid: not owned. Analyst target 81,730 JPY vs 61,360 JPY (+33%, 20 analysts); de-biased α +2.0% vs CAPM hurdle 11.5%. Downtrend -6% vs 200-day avg; 12-1 mom +13%; RSI 58. Quality z +0.06 (ROE 25%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.36"
    Avoid: not owned. Analyst target 324.71 USD vs 289.81 USD (+12%, 31 analysts); de-biased α -2.8% vs CAPM hurdle 10.8%. Uptrend +16% vs 200-day avg; 12-1 mom +52%; RSI 62. Quality z +0.24 (ROE 30%).

??? failure "QCOM (QCOM) — 🔴 Sell, score -0.38"
    Avoid: not owned. Analyst target 194.13 USD vs 173.82 USD (+12%, 30 analysts); de-biased α -3.2% vs CAPM hurdle 11.9%. Uptrend +3% vs 200-day avg; 12-1 mom +9%; RSI 43. Quality z +0.70 (ROE 23%).

??? failure "TER (TER) — 🔴 Sell, score -0.49"
    Avoid: not owned. Analyst target 446.47 USD vs 407.45 USD (+10%, 15 analysts); de-biased α -4.3% vs CAPM hurdle 12.3%. Uptrend +20% vs 200-day avg; 12-1 mom +174%; RSI 54. Quality z -0.31 (ROE 20%).

??? failure "INTC (INTC) — 🔴 Sell, score -0.54"
    Avoid: not owned. Analyst target 116.37 USD vs 109.57 USD (+6%, 43 analysts); de-biased α -5.6% vs CAPM hurdle 14.0%. Uptrend +32% vs 200-day avg; 12-1 mom +186%; RSI 48. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.54"
    Avoid: not owned. Analyst target 76.40 USD vs 52.07 USD (+47%, 10 analysts); de-biased α +4.7% vs CAPM hurdle 14.0%. Downtrend -9% vs 200-day avg; 12-1 mom +74%; RSI 49. Quality z -1.00 (ROE 9%).

??? failure "Shin-Etsu (4063.T) — 🔴 Sell, score -0.59"
    Avoid: not owned. Analyst target 7,763 JPY vs 6,130 JPY (+27%, 17 analysts); de-biased α +0.8% vs CAPM hurdle 10.8%. Downtrend -2% vs 200-day avg; 12-1 mom +25%; RSI 56. Quality z -0.20 (ROE 10%).

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.74"
    Avoid: not owned. Analyst target 173.36 USD vs 164.96 USD (+5%, 11 analysts); de-biased α -5.0% vs CAPM hurdle 11.0%. Uptrend +23% vs 200-day avg; 12-1 mom +56%; RSI 66. Quality z -0.02 (ROE 6%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -0.92"
    Avoid: not owned. Analyst target 95.99 HKD vs 56.80 HKD (+69%, 21 analysts); de-biased α +11.8% vs CAPM hurdle 7.3%. Downtrend -18% vs 200-day avg; 12-1 mom -10%; RSI 30. Quality z -0.99 (ROE 3%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -0.93"
    Avoid: not owned. Analyst target 405.47 USD vs 354.57 USD (+14%, 26 analysts); de-biased α -2.5% vs CAPM hurdle 10.0%. Uptrend +9% vs 200-day avg; 12-1 mom -18%; RSI 69. Quality z +0.31 (ROE 22%).

??? failure "AMD (AMD) — 🔴🔴 Strong Sell, score -0.96"
    Avoid: not owned. Analyst target 619.51 USD vs 633.28 USD (-2%, 50 analysts); de-biased α -7.9% vs CAPM hurdle 14.9%. Uptrend +65% vs 200-day avg; 12-1 mom +146%; RSI 66. Quality z -0.15 (ROE 7%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.14"
    Avoid: not owned. Analyst target 288.70 USD vs 281.20 USD (+3%, 40 analysts); de-biased α -7.8% vs CAPM hurdle 19.6%. Uptrend +28% vs 200-day avg; 12-1 mom +66%; RSI 49. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.85"
    Avoid: not owned. Analyst target 569.78 USD vs 509.77 USD (+12%, 26 analysts); de-biased α -3.3% vs CAPM hurdle 10.3%. Uptrend +14% vs 200-day avg; 12-1 mom -18%; RSI 76. Quality z +0.14 (ROE 7%). ⚠️ overbought (RSI penalty applied).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 92 | 1,072.70 USD | $98,688 | 9.6% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 264,000 KRW | $95,415 | 9.3% | Strong Buy |
| 000660.KS | SK hynix | 74 | 1,699,000 KRW | $93,690 | 9.1% | Strong Buy |
| IFX.DE | Infineon Technologies | 1,411 | 58.89 EUR | $93,019 | 9.0% | Buy |
| NVDA | NVIDIA | 371 | 235.52 USD | $87,378 | 8.5% | Buy |
| TSM | TSMC | 187 | 464.28 USD | $86,820 | 8.4% | Buy |
| AMAT | Applied Materials | 160 | 522.02 USD | $83,523 | 8.1% | Buy |
| ASX | ASE Technology | 1,509 | 46.03 USD | $69,452 | 6.7% | Buy |
| KLAC | KLA Corp | 266 | 201.37 USD | $53,564 | 5.2% | Hold |
| 6857.T | Advantest | 200 | 41,060 JPY | $51,916 | 5.0% | Sell |
| AVGO | Broadcom | 134 | 372.57 USD | $49,924 | 4.8% | Hold |
| 8035.T | Tokyo Electron | 600 | 12,235 JPY | $46,410 | 4.5% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-10-08 16:29 UTC | ADD | AMAT | 32 | 522.02 | $16,705 |
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

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 14.5%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
