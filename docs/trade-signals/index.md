---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-01 19:32 UTC (Thu Oct 01, 03:32 PM ET) · refreshes hourly · weekly model inputs as of 2026-09-25
**Markets:** NYSE/Nasdaq 🟢 open (Thu 15:32) · Tokyo 🔴 closed (Fri 04:32) · Korea 🔴 closed (Fri 04:32) · Hong Kong 🔴 closed (Fri 03:32) · Xetra 🔴 closed (Thu 21:32) · Euronext Amsterdam 🔴 closed (Thu 21:32)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$1,027,937** | $90,580 (9%) | $937,358 (91%) | +2.79% | +1.89% | 🟢 Risk-on (+27.1%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $1,027,937), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| BUY (new) | **ASX**<br><small>ASE Technology</small> | 1,509 | 44.67 USD | $67,415 | Executed (paper) | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.05 | **SK hynix**<br><small>000660.KS</small> | 1,828,000 KRW | +74% | +11.4% | +388% | +29% | 55 | +0.63 | 9.7% → 10.0% | – | analyst α +0.66 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.10 | **Samsung**<br><small>005930.KS</small> | 275,500 KRW | +74% | +12.2% | +233% | +22% | 55 | -0.25 | 9.6% → 10.0% | – | analyst α +0.85 · momentum +0.30 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.00 | **MU**<br><small>Micron Technology</small> | 1,086.86 USD | +39% | +2.8% | +459% | +60% | 62 | +0.06 | 9.7% → 10.0% | – | momentum +0.53 · trend +0.21 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.58 | **TSM**<br><small>TSMC</small> | 458.06 USD | +21% | -0.9% | +49% | +19% | 66 | +0.58 | 8.3% → 10.0% | – | quality +0.28 · momentum -0.05 |
| 🟢 Buy | +0.48 | **NVDA**<br><small>NVIDIA</small> | 231.32 USD | +42% | +3.4% | +17% | +16% | 61 | +0.48 | 8.3% → 7.7% | – | analyst α +0.27 · momentum -0.23 |
| 🟢 Buy | +0.48 | **Advantest**<br><small>6857.T</small> | 37,430 JPY | +14% | -3.4% | +144% | +37% | 65 | +0.33 | 6.9% → 5.1% | – | analyst α -0.23 · momentum +0.17 · ⚠️ rich valuation |
| 🟢 Buy | +0.44 | **Infineon**<br><small>IFX.DE</small> | 59.60 EUR | +46% | +4.5% | +64% | +8% | 55 | -0.04 | 7.9% → 6.9% | – | analyst α +0.36 · trend -0.12 |
| 🟢 Buy | +0.43 | **ASX**<br><small>ASE Technology</small> | 44.67 USD | +14% | -1.4% | +241% | +47% | 63 | -0.68 | 6.6% → 6.6% | BUY 1,509 | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.33 | **Tokyo Electron**<br><small>8035.T</small> | 12,585 JPY | – | +0.0% | +137% | +30% | 73 | -0.28 | 4.6% → 4.5% | – | quality -0.18 · momentum +0.12 · ⚠️ rich valuation |
| 🟢 Buy | +0.32 | **AMAT**<br><small>Applied Materials</small> | 529.52 USD | +21% | -1.1% | +117% | +24% | 67 | +0.03 | 4.7% → 4.4% | – | momentum +0.07 · trend +0.06 |
| ⚪ Hold | +0.24 | **AVGO**<br><small>Broadcom</small> | 346.52 USD | +53% | +7.2% | +13% | -5% | 41 | +0.27 | 5.7% → 5.7% | – | analyst α +0.41 · momentum -0.26 |
| ⚪ Hold | +0.15 | **ASML**<br><small>ASML Holding</small> | 1,807.82 USD | +17% | -2.1% | +73% | +18% | 60 | +0.42 | 0.0% → 0.0% | – | quality +0.18 · analyst α -0.15 |
| ⚪ Hold | +0.13 | **KLAC**<br><small>KLA Corp</small> | 200.23 USD | +17% | -2.0% | +59% | +13% | 63 | +0.51 | 9.1% → 9.1% | – | quality +0.24 · analyst α -0.08 |
| ⚪ Hold | -0.12 | **Disco**<br><small>6146.T</small> | 60,500 JPY | +36% | +2.9% | +29% | -7% | 62 | +0.07 | 0.0% → 0.0% | – | analyst α +0.23 · trend -0.18 |
| ⚪ Hold | -0.14 | **AMD**<br><small>Advanced Micro Devices</small> | 615.24 USD | +1% | -7.2% | +184% | +65% | 67 | -0.15 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.32 |
| ⚪ Hold | -0.17 | **TXN**<br><small>Texas Instruments</small> | 281.74 USD | +15% | -1.9% | +41% | +14% | 62 | +0.24 | 0.0% → 0.0% | – | momentum -0.10 · quality +0.10 |
| ⚪ Hold | -0.19 | **ASMI**<br><small>ASM.AS</small> | 898.00 EUR | +25% | -0.4% | +43% | +14% | 62 | -0.10 | 0.0% → 0.0% | – | analyst α +0.08 · momentum -0.07 |
| ⚪ Hold | -0.21 | **GFS**<br><small>GlobalFoundries</small> | 48.70 USD | +56% | +7.4% | +23% | -10% | 54 | -0.21 | 0.0% → 0.0% | – | analyst α +0.48 · trend -0.25 |
| ⚪ Hold | -0.23 | **MRVL**<br><small>Marvell Technology</small> | 266.89 USD | +8% | -5.0% | +151% | +61% | 63 | -0.12 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.25 · ⚠️ rich valuation |
| 🔴 Sell | -0.37 | **LRCX**<br><small>Lam Research</small> | 338.52 USD | +10% | -4.0% | +117% | +24% | 65 | +0.03 | 0.0% → 0.0% | – | analyst α -0.31 · momentum +0.10 |
| 🔴 Sell | -0.49 | **Shin-Etsu**<br><small>4063.T</small> | 6,053 JPY | +28% | +1.3% | +35% | -2% | 57 | -0.19 | 0.0% → 0.0% | – | analyst α +0.15 · momentum -0.14 |
| 🔴 Sell | -0.66 | **QCOM**<br><small>Qualcomm</small> | 183.57 USD | +6% | -4.7% | +2% | +9% | 52 | +0.70 | 0.0% → 0.0% | – | quality +0.43 · analyst α -0.36 |
| 🔴 Sell | -0.68 | **AMKR**<br><small>Amkor Technology</small> | 52.99 USD | +44% | +4.2% | +62% | -7% | 53 | -1.00 | 0.0% → 0.0% | – | quality -0.43 · analyst α +0.31 |
| 🔴🔴 Strong Sell | -0.81 | **ENTG**<br><small>Entegris</small> | 158.49 USD | +9% | -3.8% | +41% | +20% | 64 | -0.02 | 0.0% → 0.0% | – | analyst α -0.27 · momentum -0.12 |
| 🔴🔴 Strong Sell | -0.84 | **TER**<br><small>Teradyne</small> | 415.88 USD | +7% | -4.8% | +144% | +25% | 63 | -0.31 | 0.0% → 0.0% | – | analyst α -0.41 · quality -0.21 |
| 🔴🔴 Strong Sell | -0.91 | **SMIC**<br><small>0981.HK</small> | 60.65 HKD | +56% | +8.5% | -1% | -13% | 37 | -0.98 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.35 |
| 🔴🔴 Strong Sell | -1.01 | **INTC**<br><small>Intel</small> | 120.58 USD | -3% | -7.9% | +165% | +49% | 62 | -0.62 | 0.0% → 0.0% | – | analyst α -0.66 · quality -0.24 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.02 | **CDNS**<br><small>Cadence Design Systems</small> | 350.38 USD | +16% | -2.1% | -11% | +8% | 70 | +0.31 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.13 |
| 🔴🔴 Strong Sell | -1.39 | **ARM**<br><small>Arm Holdings</small> | 292.24 USD | -1% | -8.8% | +66% | +36% | 54 | +0.04 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.12 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.47 | **SNPS**<br><small>Synopsys</small> | 492.89 USD | +12% | -3.0% | -16% | +11% | 75 | +0.14 | 0.0% → 0.0% | – | momentum -0.53 · analyst α -0.19 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.05"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,184,026 KRW vs 1,828,000 KRW (+74%, 37 analysts); de-biased α +11.4% vs CAPM hurdle 14.4%. Uptrend +29% vs 200-day avg; 12-1 mom +388%; RSI 55. Quality z +0.63 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.10"
    Within rebalance band of target 10.0%: no trade. Analyst target 478,628 KRW vs 275,500 KRW (+74%, 36 analysts); de-biased α +12.2% vs CAPM hurdle 11.4%. Uptrend +22% vs 200-day avg; 12-1 mom +233%; RSI 55. Quality z -0.25 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 4.0 (ch.17-18).

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.00"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,515.54 USD vs 1,086.86 USD (+39%, 46 analysts); de-biased α +2.8% vs CAPM hurdle 14.1%. Uptrend +60% vs 200-day avg; 12-1 mom +459%; RSI 62. Quality z +0.06 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 6.8 (ch.17-18).

??? success "TSM (TSM) — 🟢 Buy, score +0.58"
    Within rebalance band of target 10.0%: no trade. Analyst target 552.26 USD vs 458.06 USD (+21%, 20 analysts); de-biased α -0.9% vs CAPM hurdle 10.9%. Uptrend +19% vs 200-day avg; 12-1 mom +49%; RSI 66. Quality z +0.58 (ROE 35%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.48"
    Within rebalance band of target 7.7%: no trade. Analyst target 327.70 USD vs 231.32 USD (+42%, 59 analysts); de-biased α +3.4% vs CAPM hurdle 14.0%. Uptrend +16% vs 200-day avg; 12-1 mom +17%; RSI 61. Quality z +0.48 (ROE 101%).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.48"
    Within rebalance band of target 5.1%: no trade. Analyst target 42,567 JPY vs 37,430 JPY (+14%, 21 analysts); de-biased α -3.4% vs CAPM hurdle 13.3%. Uptrend +37% vs 200-day avg; 12-1 mom +144%; RSI 65. Quality z +0.33 (ROE 58%). ⚠️ price implies 76% stage-1 growth (reverse DCF).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.44"
    Within rebalance band of target 6.9%: no trade. Analyst target 86.74 EUR vs 59.60 EUR (+46%, 23 analysts); de-biased α +4.5% vs CAPM hurdle 14.1%. Uptrend +8% vs 200-day avg; 12-1 mom +64%; RSI 55. Quality z -0.04 (ROE 6%).

??? success "ASX (ASX) — 🟢 Buy, score +0.43"
    **BUY (new) 1,509 sh** → target 6.6% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 51.00 USD vs 44.67 USD (+14%, 1 analysts); de-biased α -1.4% vs CAPM hurdle 12.1%. Uptrend +47% vs 200-day avg; 12-1 mom +241%; RSI 63. Quality z -0.68 (ROE 12%). ⚠️ price implies 67% stage-1 growth (reverse DCF).

??? success "Tokyo Electron (8035.T) — 🟢 Buy, score +0.33"
    Within rebalance band of target 4.5%: no trade. No reliable analyst target: α set to 0. Uptrend +30% vs 200-day avg; 12-1 mom +137%; RSI 73. Quality z -0.28 (ROE 29%). ⚠️ price implies 72% stage-1 growth (reverse DCF).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.32"
    Within rebalance band of target 4.4%: no trade. Analyst target 640.89 USD vs 529.52 USD (+21%, 35 analysts); de-biased α -1.1% vs CAPM hurdle 11.7%. Uptrend +24% vs 200-day avg; 12-1 mom +117%; RSI 67. Quality z +0.03 (ROE 36%).

??? note "AVGO (AVGO) — ⚪ Hold, score +0.24"
    Hold zone: keep any existing position, no new money. Analyst target 531.85 USD vs 346.52 USD (+53%, 47 analysts); de-biased α +7.2% vs CAPM hurdle 11.2%. Downtrend -5% vs 200-day avg; 12-1 mom +13%; RSI 41. Quality z +0.27 (ROE 31%).

??? note "ASML (ASML) — ⚪ Hold, score +0.15"
    Hold zone: not owned, no entry. Analyst target 2,123.54 USD vs 1,807.82 USD (+17%, 16 analysts); de-biased α -2.1% vs CAPM hurdle 12.4%. Uptrend +18% vs 200-day avg; 12-1 mom +73%; RSI 60. Quality z +0.42 (ROE 50%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.13"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 200.23 USD (+17%, 26 analysts); de-biased α -2.0% vs CAPM hurdle 11.2%. Uptrend +13% vs 200-day avg; 12-1 mom +59%; RSI 63. Quality z +0.51 (ROE 87%).

??? note "Disco (6146.T) — ⚪ Hold, score -0.12"
    Hold zone: not owned, no entry. Analyst target 82,580 JPY vs 60,500 JPY (+36%, 20 analysts); de-biased α +2.9% vs CAPM hurdle 11.6%. Downtrend -7% vs 200-day avg; 12-1 mom +29%; RSI 62. Quality z +0.07 (ROE 25%).

??? note "AMD (AMD) — ⚪ Hold, score -0.14"
    Hold zone: not owned, no entry. Analyst target 618.51 USD vs 615.24 USD (+1%, 50 analysts); de-biased α -7.2% vs CAPM hurdle 15.0%. Uptrend +65% vs 200-day avg; 12-1 mom +184%; RSI 67. Quality z -0.15 (ROE 7%).

??? note "TXN (TXN) — ⚪ Hold, score -0.17"
    Hold zone: not owned, no entry. Analyst target 324.71 USD vs 281.74 USD (+15%, 31 analysts); de-biased α -1.9% vs CAPM hurdle 10.8%. Uptrend +14% vs 200-day avg; 12-1 mom +41%; RSI 62. Quality z +0.24 (ROE 30%).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.19"
    Hold zone: not owned, no entry. Analyst target 1,125.89 EUR vs 898.00 EUR (+25%, 19 analysts); de-biased α -0.4% vs CAPM hurdle 13.2%. Uptrend +14% vs 200-day avg; 12-1 mom +43%; RSI 62. Quality z -0.10 (ROE 19%).

??? note "GFS (GFS) — ⚪ Hold, score -0.21"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 48.70 USD (+56%, 22 analysts); de-biased α +7.4% vs CAPM hurdle 12.5%. Downtrend -10% vs 200-day avg; 12-1 mom +23%; RSI 54. Quality z -0.21 (ROE 8%).

??? note "MRVL (MRVL) — ⚪ Hold, score -0.23"
    Hold zone: not owned, no entry. Analyst target 289.11 USD vs 266.89 USD (+8%, 43 analysts); de-biased α -5.0% vs CAPM hurdle 14.2%. Uptrend +61% vs 200-day avg; 12-1 mom +151%; RSI 63. Quality z -0.12 (ROE 19%). ⚠️ price implies 76% stage-1 growth (reverse DCF).

??? failure "LRCX (LRCX) — 🔴 Sell, score -0.37"
    Avoid: not owned. Analyst target 373.77 USD vs 338.52 USD (+10%, 31 analysts); de-biased α -4.0% vs CAPM hurdle 12.7%. Uptrend +24% vs 200-day avg; 12-1 mom +117%; RSI 65. Quality z +0.03 (ROE 65%).

??? failure "Shin-Etsu (4063.T) — 🔴 Sell, score -0.49"
    Avoid: not owned. Analyst target 7,775 JPY vs 6,053 JPY (+28%, 17 analysts); de-biased α +1.3% vs CAPM hurdle 10.8%. Downtrend -2% vs 200-day avg; 12-1 mom +35%; RSI 57. Quality z -0.19 (ROE 10%).

??? failure "QCOM (QCOM) — 🔴 Sell, score -0.66"
    Avoid: not owned. Analyst target 194.13 USD vs 183.57 USD (+6%, 30 analysts); de-biased α -4.7% vs CAPM hurdle 12.1%. Uptrend +9% vs 200-day avg; 12-1 mom +2%; RSI 52. Quality z +0.70 (ROE 23%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.68"
    Avoid: not owned. Analyst target 76.40 USD vs 52.99 USD (+44%, 10 analysts); de-biased α +4.2% vs CAPM hurdle 14.1%. Downtrend -7% vs 200-day avg; 12-1 mom +62%; RSI 53. Quality z -1.00 (ROE 9%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.81"
    Avoid: not owned. Analyst target 173.36 USD vs 158.49 USD (+9%, 11 analysts); de-biased α -3.8% vs CAPM hurdle 10.9%. Uptrend +20% vs 200-day avg; 12-1 mom +41%; RSI 64. Quality z -0.02 (ROE 6%).

??? failure "TER (TER) — 🔴🔴 Strong Sell, score -0.84"
    Avoid: not owned. Analyst target 446.47 USD vs 415.88 USD (+7%, 15 analysts); de-biased α -4.8% vs CAPM hurdle 12.5%. Uptrend +25% vs 200-day avg; 12-1 mom +144%; RSI 63. Quality z -0.31 (ROE 20%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -0.91"
    Avoid: not owned. Analyst target 94.39 HKD vs 60.65 HKD (+56%, 22 analysts); de-biased α +8.5% vs CAPM hurdle 7.4%. Downtrend -13% vs 200-day avg; 12-1 mom -1%; RSI 37. Quality z -0.98 (ROE 3%).

??? failure "INTC (INTC) — 🔴🔴 Strong Sell, score -1.01"
    Avoid: not owned. Analyst target 116.37 USD vs 120.58 USD (-3%, 43 analysts); de-biased α -7.9% vs CAPM hurdle 14.1%. Uptrend +49% vs 200-day avg; 12-1 mom +165%; RSI 62. Quality z -0.62 (ROE -0%). ⚠️ price implies 87% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 61% → smaller size.

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.02"
    Avoid: not owned. Analyst target 405.47 USD vs 350.38 USD (+16%, 26 analysts); de-biased α -2.1% vs CAPM hurdle 10.1%. Uptrend +8% vs 200-day avg; 12-1 mom -11%; RSI 70. Quality z +0.31 (ROE 22%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.39"
    Avoid: not owned. Analyst target 288.70 USD vs 292.24 USD (-1%, 40 analysts); de-biased α -8.8% vs CAPM hurdle 20.0%. Uptrend +36% vs 200-day avg; 12-1 mom +66%; RSI 54. Quality z +0.04 (ROE 12%). ⚠️ price implies 115% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.47"
    Avoid: not owned. Analyst target 553.77 USD vs 492.89 USD (+12%, 25 analysts); de-biased α -3.0% vs CAPM hurdle 10.4%. Uptrend +11% vs 200-day avg; 12-1 mom -16%; RSI 75. Quality z +0.14 (ROE 7%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 92 | 1,086.86 USD | $99,991 | 9.7% | Strong Buy |
| 000660.KS | SK hynix | 74 | 1,828,000 KRW | $99,531 | 9.7% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 275,500 KRW | $98,314 | 9.6% | Strong Buy |
| KLAC | KLA Corp | 469 | 200.23 USD | $93,908 | 9.1% | Hold |
| NVDA | NVIDIA | 371 | 231.32 USD | $85,820 | 8.3% | Buy |
| TSM | TSMC | 187 | 458.06 USD | $85,657 | 8.3% | Buy |
| IFX.DE | Infineon Technologies | 1,205 | 59.60 EUR | $80,776 | 7.9% | Buy |
| 6857.T | Advantest | 300 | 37,430 JPY | $71,064 | 6.9% | Buy |
| ASX | ASE Technology | 1,509 | 44.67 USD | $67,415 | 6.6% | Buy |
| AVGO | Broadcom | 170 | 346.52 USD | $58,909 | 5.7% | Hold |
| AMAT | Applied Materials | 91 | 529.52 USD | $48,186 | 4.7% | Buy |
| 8035.T | Tokyo Electron | 600 | 12,585 JPY | $47,787 | 4.6% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 4.07%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 14.1%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
