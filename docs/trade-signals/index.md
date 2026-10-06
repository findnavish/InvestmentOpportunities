---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-06 02:59 UTC (Mon Oct 05, 10:59 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Mon 22:59) · Tokyo 🟢 open (Tue 11:59) · Korea 🟢 open (Tue 11:59) · Hong Kong 🟢 open (Tue 10:59) · Xetra 🔴 closed (Tue 04:59) · Euronext Amsterdam 🔴 closed (Tue 04:59)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$1,054,312** | $178,971 (17%) | $875,342 (83%) | +5.43% | +4.26% | 🟢 Risk-on (+29.2%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $1,054,312), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| ADD | **Infineon**<br><small>IFX.DE</small> | 312 | 63.57 EUR | $22,248 | Queued · Xetra closed | analyst α +0.23 · trend -0.07 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +2.99 | **SK hynix**<br><small>000660.KS</small> | 1,792,000 KRW | +75% | +12.5% | +385% | +26% | 52 | +0.62 | 9.4% → 10.0% | – | analyst α +0.66 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.41 | **MU**<br><small>Micron Technology</small> | 1,063.75 USD | +43% | +4.5% | +422% | +55% | 57 | +0.12 | 9.3% → 10.0% | – | momentum +0.53 · analyst α +0.36 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.05 | **Samsung**<br><small>005930.KS</small> | 272,750 KRW | +75% | +13.3% | +224% | +20% | 54 | -0.26 | 9.3% → 10.0% | – | analyst α +0.85 · momentum +0.30 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.54 | **NVDA**<br><small>NVIDIA</small> | 239.11 USD | +37% | +3.1% | +21% | +19% | 67 | +0.47 | 8.4% → 9.9% | – | analyst α +0.27 · quality +0.21 |
| 🟢 Buy | +0.49 | **AMAT**<br><small>Applied Materials</small> | 542.28 USD | +18% | -1.1% | +96% | +27% | 70 | +0.03 | 6.6% → 7.7% | – | analyst α +0.08 · momentum +0.07 |
| 🟢 Buy | +0.41 | **ASX**<br><small>ASE Technology</small> | 47.53 USD | +7% | -1.8% | +239% | +55% | 69 | -0.68 | 6.8% → 7.0% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.35 | **Infineon**<br><small>IFX.DE</small> | 63.57 EUR | +36% | +3.0% | +68% | +14% | 62 | -0.04 | 4.2% → 6.3% | ADD 312 | analyst α +0.23 · trend -0.07 |
| 🟢 Buy | +0.30 | **Tokyo Electron**<br><small>8035.T</small> | 12,665 JPY | +21% | -0.5% | +111% | +30% | 68 | -0.28 | 4.6% → 4.7% | – | quality -0.18 · momentum +0.12 |
| ⚪ Hold | +0.24 | **AVGO**<br><small>Broadcom</small> | 362.88 USD | +46% | +6.2% | +6% | -1% | 52 | +0.26 | 5.9% → 5.9% | – | analyst α +0.41 · momentum -0.26 |
| ⚪ Hold | +0.11 | **MRVL**<br><small>Marvell Technology</small> | 271.29 USD | +8% | -4.2% | +143% | +62% | 64 | -0.12 | 0.0% → 0.0% | – | analyst α -0.31 · trend +0.25 · ⚠️ rich valuation |
| ⚪ Hold | +0.08 | **Advantest**<br><small>6857.T</small> | 40,990 JPY | +4% | -5.0% | +117% | +49% | 73 | +0.33 | 4.9% → 4.9% | – | analyst α -0.41 · quality +0.16 · ⚠️ rich valuation |
| ⚪ Hold | +0.06 | **KLAC**<br><small>KLA Corp</small> | 206.85 USD | +13% | -2.2% | +53% | +16% | 67 | +0.51 | 5.1% → 5.1% | – | quality +0.24 · analyst α -0.12 |
| ⚪ Hold | +0.06 | **TSM**<br><small>TSMC</small> | 485.91 USD | +14% | -1.8% | +46% | +26% | 76 | +0.58 | 8.6% → 8.6% | – | quality +0.28 · analyst α -0.08 · ⚠️ overbought |
| ⚪ Hold | +0.06 | **ASML**<br><small>ASML Holding</small> | 1,860.68 USD | +13% | -2.5% | +61% | +21% | 64 | +0.42 | 0.0% → 0.0% | – | analyst α -0.19 · quality +0.18 |
| ⚪ Hold | -0.15 | **GFS**<br><small>GlobalFoundries</small> | 48.57 USD | +56% | +8.3% | +25% | -10% | 53 | -0.21 | 0.0% → 0.0% | – | analyst α +0.48 · trend -0.25 |
| ⚪ Hold | -0.19 | **ASMI**<br><small>ASM.AS</small> | 945.40 EUR | +19% | -1.1% | +51% | +19% | 69 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · momentum -0.05 |
| 🔴 Sell | -0.34 | **LRCX**<br><small>Lam Research</small> | 345.80 USD | +8% | -3.7% | +100% | +26% | 67 | +0.02 | 0.0% → 0.0% | – | analyst α -0.27 · momentum +0.10 |
| 🔴 Sell | -0.36 | **Disco**<br><small>6146.T</small> | 63,690 JPY | +28% | +1.7% | +17% | -2% | 68 | +0.06 | 0.0% → 0.0% | – | momentum -0.23 · analyst α +0.19 |
| 🔴 Sell | -0.36 | **AMD**<br><small>Advanced Micro Devices</small> | 631.91 USD | -2% | -7.0% | +169% | +68% | 69 | -0.15 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.32 |
| 🔴 Sell | -0.41 | **TXN**<br><small>Texas Instruments</small> | 295.07 USD | +10% | -2.5% | +43% | +19% | 71 | +0.24 | 0.0% → 0.0% | – | analyst α -0.15 · momentum -0.10 |
| 🔴 Sell | -0.45 | **QCOM**<br><small>Qualcomm</small> | 180.84 USD | +7% | -3.4% | +2% | +8% | 49 | +0.70 | 0.0% → 0.0% | – | quality +0.43 · momentum -0.30 |
| 🔴 Sell | -0.50 | **Shin-Etsu**<br><small>4063.T</small> | 6,305 JPY | +23% | +0.8% | +29% | +1% | 67 | -0.20 | 0.0% → 0.0% | – | analyst α +0.15 · momentum -0.14 |
| 🔴 Sell | -0.64 | **AMKR**<br><small>Amkor Technology</small> | 54.68 USD | +40% | +3.8% | +59% | -4% | 55 | -1.00 | 0.0% → 0.0% | – | quality -0.43 · analyst α +0.31 |
| 🔴 Sell | -0.70 | **SNPS**<br><small>Synopsys</small> | 488.57 USD | +17% | -1.2% | -12% | +10% | 73 | +0.14 | 0.0% → 0.0% | – | momentum -0.35 · trend -0.09 |
| 🔴🔴 Strong Sell | -0.82 | **CDNS**<br><small>Cadence Design Systems</small> | 353.62 USD | +15% | -1.6% | -12% | +9% | 72 | +0.31 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.13 |
| 🔴🔴 Strong Sell | -0.86 | **TER**<br><small>Teradyne</small> | 444.60 USD | +0% | -5.7% | +135% | +32% | 68 | -0.31 | 0.0% → 0.0% | – | analyst α -0.48 · quality -0.21 |
| 🔴🔴 Strong Sell | -0.89 | **INTC**<br><small>Intel</small> | 116.28 USD | +0% | -6.2% | +146% | +43% | 57 | -0.62 | 0.0% → 0.0% | – | analyst α -0.55 · quality -0.24 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -0.93 | **ENTG**<br><small>Entegris</small> | 167.03 USD | +4% | -4.5% | +35% | +26% | 69 | -0.02 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.12 |
| 🔴🔴 Strong Sell | -1.30 | **SMIC**<br><small>0981.HK</small> | 61.55 HKD | +56% | +9.4% | -12% | -11% | 41 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.53 |
| 🔴🔴 Strong Sell | -1.49 | **ARM**<br><small>Arm Holdings</small> | 303.04 USD | -5% | -8.8% | +59% | +40% | 57 | +0.04 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.12 · ⚠️ rich valuation, high σ(e) |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +2.99"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,792,000 KRW (+75%, 38 analysts); de-biased α +12.5% vs CAPM hurdle 14.3%. Uptrend +26% vs 200-day avg; 12-1 mom +385%; RSI 52. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.41"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 1,063.75 USD (+43%, 46 analysts); de-biased α +4.5% vs CAPM hurdle 14.0%. Uptrend +55% vs 200-day avg; 12-1 mom +422%; RSI 57. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.05"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 272,750 KRW (+75%, 36 analysts); de-biased α +13.3% vs CAPM hurdle 11.3%. Uptrend +20% vs 200-day avg; 12-1 mom +224%; RSI 54. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.54"
    Within rebalance band of target 9.9%: no trade. Analyst target 327.70 USD vs 239.11 USD (+37%, 59 analysts); de-biased α +3.1% vs CAPM hurdle 13.9%. Uptrend +19% vs 200-day avg; 12-1 mom +21%; RSI 67. Quality z +0.47 (ROE 101%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.49"
    Within rebalance band of target 7.7%: no trade. Analyst target 638.94 USD vs 542.28 USD (+18%, 36 analysts); de-biased α -1.1% vs CAPM hurdle 11.6%. Uptrend +27% vs 200-day avg; 12-1 mom +96%; RSI 70. Quality z +0.03 (ROE 36%).

??? success "ASX (ASX) — 🟢 Buy, score +0.41"
    Within rebalance band of target 7.0%: no trade. Analyst target 51.00 USD vs 47.53 USD (+7%, 1 analysts); de-biased α -1.8% vs CAPM hurdle 11.9%. Uptrend +55% vs 200-day avg; 12-1 mom +239%; RSI 69. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.35"
    **ADD 312 sh** → target 6.3% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 86.74 EUR vs 63.57 EUR (+36%, 23 analysts); de-biased α +3.0% vs CAPM hurdle 14.1%. Uptrend +14% vs 200-day avg; 12-1 mom +68%; RSI 62. Quality z -0.04 (ROE 6%).

??? success "Tokyo Electron (8035.T) — 🟢 Buy, score +0.30"
    Within rebalance band of target 4.7%: no trade. Analyst target 15,275 JPY vs 12,665 JPY (+21%, 23 analysts); de-biased α -0.5% vs CAPM hurdle 12.8%. Uptrend +30% vs 200-day avg; 12-1 mom +111%; RSI 68. Quality z -0.28 (ROE 29%).

??? note "AVGO (AVGO) — ⚪ Hold, score +0.24"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 362.88 USD (+46%, 47 analysts); de-biased α +6.2% vs CAPM hurdle 11.2%. Downtrend -1% vs 200-day avg; 12-1 mom +6%; RSI 52. Quality z +0.26 (ROE 31%).

??? note "MRVL (MRVL) — ⚪ Hold, score +0.11"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 271.29 USD (+8%, 43 analysts); de-biased α -4.2% vs CAPM hurdle 14.1%. Uptrend +62% vs 200-day avg; 12-1 mom +143%; RSI 64. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "Advantest (6857.T) — ⚪ Hold, score +0.08"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 40,990 JPY (+4%, 21 analysts); de-biased α -5.0% vs CAPM hurdle 13.4%. Uptrend +49% vs 200-day avg; 12-1 mom +117%; RSI 73. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.06"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 206.85 USD (+13%, 26 analysts); de-biased α -2.2% vs CAPM hurdle 11.1%. Uptrend +16% vs 200-day avg; 12-1 mom +53%; RSI 67. Quality z +0.51 (ROE 87%).

??? note "TSM (TSM) — ⚪ Hold, score +0.06"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 485.91 USD (+14%, 20 analysts); de-biased α -1.8% vs CAPM hurdle 10.8%. Uptrend +26% vs 200-day avg; 12-1 mom +46%; RSI 76. Quality z +0.58 (ROE 35%). ⚠️ overbought (RSI penalty applied).

??? note "ASML (ASML) — ⚪ Hold, score +0.06"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,860.68 USD (+13%, 16 analysts); de-biased α -2.5% vs CAPM hurdle 12.3%. Uptrend +21% vs 200-day avg; 12-1 mom +61%; RSI 64. Quality z +0.42 (ROE 50%).

??? note "GFS (GFS) — ⚪ Hold, score -0.15"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 48.57 USD (+56%, 22 analysts); de-biased α +8.3% vs CAPM hurdle 12.4%. Downtrend -10% vs 200-day avg; 12-1 mom +25%; RSI 53. Quality z -0.21 (ROE 8%).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.19"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 945.40 EUR (+19%, 19 analysts); de-biased α -1.1% vs CAPM hurdle 13.2%. Uptrend +19% vs 200-day avg; 12-1 mom +51%; RSI 69. Quality z -0.10 (ROE 19%).

??? failure "LRCX (LRCX) — 🔴 Sell, score -0.34"
    Avoid: not owned. Analyst target 375.06 USD vs 345.80 USD (+8%, 31 analysts); de-biased α -3.7% vs CAPM hurdle 12.6%. Uptrend +26% vs 200-day avg; 12-1 mom +100%; RSI 67. Quality z +0.02 (ROE 65%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.36"
    Avoid: not owned. Analyst target 81,730 JPY vs 63,690 JPY (+28%, 20 analysts); de-biased α +1.7% vs CAPM hurdle 11.5%. Downtrend -2% vs 200-day avg; 12-1 mom +17%; RSI 68. Quality z +0.06 (ROE 25%).

??? failure "AMD (AMD) — 🔴 Sell, score -0.36"
    Avoid: not owned. Analyst target 619.51 USD vs 631.91 USD (-2%, 50 analysts); de-biased α -7.0% vs CAPM hurdle 14.9%. Uptrend +68% vs 200-day avg; 12-1 mom +169%; RSI 69. Quality z -0.15 (ROE 7%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.41"
    Avoid: not owned. Analyst target 324.71 USD vs 295.07 USD (+10%, 31 analysts); de-biased α -2.5% vs CAPM hurdle 10.8%. Uptrend +19% vs 200-day avg; 12-1 mom +43%; RSI 71. Quality z +0.24 (ROE 30%).

??? failure "QCOM (QCOM) — 🔴 Sell, score -0.45"
    Avoid: not owned. Analyst target 194.13 USD vs 180.84 USD (+7%, 30 analysts); de-biased α -3.4% vs CAPM hurdle 11.9%. Uptrend +8% vs 200-day avg; 12-1 mom +2%; RSI 49. Quality z +0.70 (ROE 23%).

??? failure "Shin-Etsu (4063.T) — 🔴 Sell, score -0.50"
    Avoid: not owned. Analyst target 7,763 JPY vs 6,305 JPY (+23%, 17 analysts); de-biased α +0.8% vs CAPM hurdle 10.8%. Uptrend +1% vs 200-day avg; 12-1 mom +29%; RSI 67. Quality z -0.20 (ROE 10%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.64"
    Avoid: not owned. Analyst target 76.40 USD vs 54.68 USD (+40%, 10 analysts); de-biased α +3.8% vs CAPM hurdle 14.0%. Downtrend -4% vs 200-day avg; 12-1 mom +59%; RSI 55. Quality z -1.00 (ROE 9%).

??? failure "SNPS (SNPS) — 🔴 Sell, score -0.70"
    Avoid: not owned. Analyst target 569.78 USD vs 488.57 USD (+17%, 26 analysts); de-biased α -1.2% vs CAPM hurdle 10.3%. Uptrend +10% vs 200-day avg; 12-1 mom -12%; RSI 73. Quality z +0.14 (ROE 7%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -0.82"
    Avoid: not owned. Analyst target 405.47 USD vs 353.62 USD (+15%, 26 analysts); de-biased α -1.6% vs CAPM hurdle 10.0%. Uptrend +9% vs 200-day avg; 12-1 mom -12%; RSI 72. Quality z +0.31 (ROE 22%).

??? failure "TER (TER) — 🔴🔴 Strong Sell, score -0.86"
    Avoid: not owned. Analyst target 446.47 USD vs 444.60 USD (+0%, 15 analysts); de-biased α -5.7% vs CAPM hurdle 12.3%. Uptrend +32% vs 200-day avg; 12-1 mom +135%; RSI 68. Quality z -0.31 (ROE 20%).

??? failure "INTC (INTC) — 🔴🔴 Strong Sell, score -0.89"
    Avoid: not owned. Analyst target 116.37 USD vs 116.28 USD (+0%, 43 analysts); de-biased α -6.2% vs CAPM hurdle 14.0%. Uptrend +43% vs 200-day avg; 12-1 mom +146%; RSI 57. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.93"
    Avoid: not owned. Analyst target 173.36 USD vs 167.03 USD (+4%, 11 analysts); de-biased α -4.5% vs CAPM hurdle 11.0%. Uptrend +26% vs 200-day avg; 12-1 mom +35%; RSI 69. Quality z -0.02 (ROE 6%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.30"
    Avoid: not owned. Analyst target 95.99 HKD vs 61.55 HKD (+56%, 21 analysts); de-biased α +9.4% vs CAPM hurdle 7.3%. Downtrend -11% vs 200-day avg; 12-1 mom -12%; RSI 41. Quality z -0.99 (ROE 3%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.49"
    Avoid: not owned. Analyst target 288.70 USD vs 303.04 USD (-5%, 40 analysts); de-biased α -8.8% vs CAPM hurdle 19.6%. Uptrend +40% vs 200-day avg; 12-1 mom +59%; RSI 57. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 74 | 1,792,000 KRW | $98,715 | 9.4% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 272,750 KRW | $98,474 | 9.3% | Strong Buy |
| MU | Micron Technology | 92 | 1,063.75 USD | $97,865 | 9.3% | Strong Buy |
| TSM | TSMC | 187 | 485.91 USD | $90,865 | 8.6% | Hold |
| NVDA | NVIDIA | 371 | 239.11 USD | $88,710 | 8.4% | Buy |
| ASX | ASE Technology | 1,509 | 47.53 USD | $71,715 | 6.8% | Buy |
| AMAT | Applied Materials | 128 | 542.28 USD | $69,412 | 6.6% | Buy |
| AVGO | Broadcom | 170 | 362.88 USD | $61,689 | 5.9% | Hold |
| KLAC | KLA Corp | 261 | 206.85 USD | $53,988 | 5.1% | Hold |
| 6857.T | Advantest | 200 | 40,990 JPY | $51,888 | 4.9% | Hold |
| 8035.T | Tokyo Electron | 600 | 12,665 JPY | $48,096 | 4.6% | Buy |
| IFX.DE | Infineon Technologies | 616 | 63.57 EUR | $43,925 | 4.2% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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
| 2026-09-25 14:37 UTC | BUY (new) | MU | 92 | 1,083.05 | $99,641 |
| 2026-09-24 08:59 UTC | BUY (new) | IFX.DE | 1,552 | 56.56 | $99,956 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 11.0%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
