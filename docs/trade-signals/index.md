---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-01 05:56 UTC (Thu Oct 01, 01:56 AM ET) · refreshes hourly · weekly model inputs as of 2026-09-25
**Markets:** NYSE/Nasdaq 🔴 closed (Thu 01:56) · Tokyo 🟢 open (Thu 14:56) · Korea 🟢 open (Thu 14:56) · Hong Kong 🔴 closed (Thu 13:56) · Xetra 🔴 closed (Thu 07:56) · Euronext Amsterdam 🔴 closed (Thu 07:56)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$1,020,137** | $158,028 (15%) | $862,109 (85%) | +2.01% | +0.46% | 🟢 Risk-on (+25.7%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $1,020,137), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **Advantest**<br><small>6857.T</small> | 100 | 37,090 JPY | $23,417 | Executed (paper) | analyst α -0.27 · quality +0.16 · ⚠️ rich valuation |
| ADD | **Infineon**<br><small>IFX.DE</small> | 314 | 59.28 EUR | $21,076 | Queued · Xetra closed | analyst α +0.36 · trend -0.09 |
| ADD | **AMAT**<br><small>Applied Materials</small> | 36 | 511.67 USD | $18,420 | Queued · NYSE/Nasdaq closed | momentum +0.07 · analyst α +0.05 |
| TRIM | **Tokyo Electron**<br><small>8035.T</small> | 100 | 12,505 JPY | $7,895 | Executed (paper) | quality -0.18 · momentum +0.12 · ⚠️ rich valuation |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.08 | **SK hynix**<br><small>000660.KS</small> | 1,829,000 KRW | +74% | +11.0% | +407% | +30% | 55 | +0.63 | 9.7% → 10.0% | – | analyst α +0.66 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.31 | **Samsung**<br><small>005930.KS</small> | 275,500 KRW | +74% | +11.7% | +244% | +22% | 56 | -0.25 | 9.6% → 10.0% | – | analyst α +0.85 · momentum +0.35 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.10 | **MU**<br><small>Micron Technology</small> | 1,067.49 USD | +42% | +3.0% | +459% | +58% | 60 | +0.06 | 9.6% → 10.0% | – | momentum +0.53 · analyst α +0.23 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.55 | **Infineon**<br><small>IFX.DE</small> | 59.28 EUR | +46% | +4.2% | +67% | +7% | 54 | -0.04 | 7.9% → 10.0% | ADD 314 | analyst α +0.36 · trend -0.09 |
| 🟢 Buy | +0.48 | **NVDA**<br><small>NVIDIA</small> | 228.29 USD | +44% | +3.4% | +17% | +14% | 58 | +0.48 | 8.3% → 9.8% | – | analyst α +0.27 · momentum -0.23 |
| 🟢 Buy | +0.40 | **TSM**<br><small>TSMC</small> | 456.28 USD | +21% | -1.3% | +49% | +19% | 65 | +0.58 | 8.4% → 9.9% | – | quality +0.28 · momentum -0.05 |
| 🟢 Buy | +0.37 | **AMAT**<br><small>Applied Materials</small> | 511.67 USD | +25% | -0.5% | +117% | +20% | 63 | +0.03 | 4.6% → 6.4% | ADD 36 | momentum +0.07 · analyst α +0.05 |
| 🟢 Buy | +0.34 | **Advantest**<br><small>6857.T</small> | 37,090 JPY | +15% | -3.6% | +150% | +36% | 65 | +0.33 | 6.9% → 4.7% | TRIM 100 | analyst α -0.27 · quality +0.16 · ⚠️ rich valuation |
| 🟢 Buy | +0.26 | **Tokyo Electron**<br><small>8035.T</small> | 12,505 JPY | – | +0.0% | +149% | +30% | 72 | -0.28 | 4.6% → 4.5% | TRIM 100 | quality -0.18 · momentum +0.12 · ⚠️ rich valuation |
| ⚪ Hold | +0.24 | **AVGO**<br><small>Broadcom</small> | 351.29 USD | +51% | +6.2% | +13% | -4% | 44 | +0.27 | 5.9% → 5.9% | – | analyst α +0.41 · momentum -0.26 |
| ⚪ Hold | +0.19 | **ASX**<br><small>ASE Technology</small> | 44.49 USD | +15% | -1.6% | +241% | +47% | 62 | -0.68 | 0.0% → 0.0% | – | momentum +0.30 · quality -0.28 · ⚠️ rich valuation |
| ⚪ Hold | +0.10 | **ASML**<br><small>ASML Holding</small> | 1,811.25 USD | +17% | -2.7% | +73% | +18% | 60 | +0.42 | 0.0% → 0.0% | – | analyst α -0.19 · quality +0.18 |
| ⚪ Hold | +0.06 | **KLAC**<br><small>KLA Corp</small> | 195.03 USD | +20% | -1.7% | +59% | +10% | 59 | +0.51 | 9.0% → 9.0% | – | quality +0.24 · analyst α -0.12 |
| ⚪ Hold | -0.15 | **AMD**<br><small>Advanced Micro Devices</small> | 611.74 USD | +1% | -7.5% | +184% | +64% | 66 | -0.15 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.32 |
| ⚪ Hold | -0.16 | **MRVL**<br><small>Marvell Technology</small> | 264.21 USD | +9% | -5.2% | +157% | +60% | 62 | -0.12 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.25 · ⚠️ rich valuation |
| ⚪ Hold | -0.20 | **Disco**<br><small>6146.T</small> | 60,350 JPY | +37% | +2.6% | +35% | -7% | 62 | +0.07 | 0.0% → 0.0% | – | analyst α +0.19 · trend -0.18 |
| ⚪ Hold | -0.21 | **GFS**<br><small>GlobalFoundries</small> | 47.91 USD | +59% | +7.6% | +23% | -11% | 51 | -0.21 | 0.0% → 0.0% | – | analyst α +0.48 · trend -0.25 |
| 🔴 Sell | -0.34 | **ASMI**<br><small>ASM.AS</small> | 889.80 EUR | +27% | -0.6% | +44% | +13% | 61 | -0.10 | 0.0% → 0.0% | – | momentum -0.07 · quality -0.06 |
| 🔴 Sell | -0.39 | **TXN**<br><small>Texas Instruments</small> | 280.03 USD | +16% | -2.2% | +41% | +14% | 61 | +0.24 | 0.0% → 0.0% | – | analyst α -0.15 · momentum -0.10 |
| 🔴 Sell | -0.40 | **LRCX**<br><small>Lam Research</small> | 328.61 USD | +14% | -3.6% | +117% | +20% | 61 | +0.03 | 0.0% → 0.0% | – | analyst α -0.31 · momentum +0.10 |
| 🔴 Sell | -0.50 | **Shin-Etsu**<br><small>4063.T</small> | 6,044 JPY | +29% | +0.9% | +35% | -2% | 57 | -0.19 | 0.0% → 0.0% | – | analyst α +0.15 · momentum -0.14 |
| 🔴 Sell | -0.65 | **TER**<br><small>Teradyne</small> | 400.91 USD | +11% | -4.2% | +161% | +21% | 58 | -0.31 | 0.0% → 0.0% | – | analyst α -0.36 · quality -0.21 |
| 🔴 Sell | -0.69 | **AMKR**<br><small>Amkor Technology</small> | 52.37 USD | +46% | +4.1% | +62% | -8% | 51 | -1.00 | 0.0% → 0.0% | – | quality -0.43 · analyst α +0.31 |
| 🔴🔴 Strong Sell | -0.79 | **ENTG**<br><small>Entegris</small> | 154.14 USD | +12% | -3.5% | +41% | +17% | 61 | -0.02 | 0.0% → 0.0% | – | analyst α -0.23 · momentum -0.12 |
| 🔴🔴 Strong Sell | -0.82 | **CDNS**<br><small>Cadence Design Systems</small> | 330.18 USD | +23% | -0.8% | -11% | +1% | 63 | +0.31 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.13 |
| 🔴🔴 Strong Sell | -0.87 | **QCOM**<br><small>Qualcomm</small> | 184.06 USD | +5% | -5.2% | +2% | +10% | 52 | +0.70 | 0.0% → 0.0% | – | analyst α -0.48 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.92 | **SMIC**<br><small>0981.HK</small> | 60.65 HKD | +56% | +8.1% | -1% | -13% | 37 | -0.98 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.35 |
| 🔴🔴 Strong Sell | -0.94 | **SNPS**<br><small>Synopsys</small> | 435.07 USD | +27% | +0.2% | -16% | -2% | 62 | +0.14 | 0.0% → 0.0% | – | momentum -0.53 · analyst α +0.12 |
| 🔴🔴 Strong Sell | -1.02 | **INTC**<br><small>Intel</small> | 120.16 USD | -3% | -8.3% | +165% | +49% | 62 | -0.62 | 0.0% → 0.0% | – | analyst α -0.66 · quality -0.24 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.45 | **ARM**<br><small>Arm Holdings</small> | 289.76 USD | -0% | -9.1% | +66% | +35% | 53 | +0.04 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.12 · ⚠️ rich valuation, high σ(e) |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.08"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,184,026 KRW vs 1,829,000 KRW (+74%, 37 analysts); de-biased α +11.0% vs CAPM hurdle 14.4%. Uptrend +30% vs 200-day avg; 12-1 mom +407%; RSI 55. Quality z +0.63 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.31"
    Within rebalance band of target 10.0%: no trade. Analyst target 478,628 KRW vs 275,500 KRW (+74%, 36 analysts); de-biased α +11.7% vs CAPM hurdle 11.4%. Uptrend +22% vs 200-day avg; 12-1 mom +244%; RSI 56. Quality z -0.25 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 4.0 (ch.17-18).

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.10"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,515.54 USD vs 1,067.49 USD (+42%, 46 analysts); de-biased α +3.0% vs CAPM hurdle 14.1%. Uptrend +58% vs 200-day avg; 12-1 mom +459%; RSI 60. Quality z +0.06 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 6.8 (ch.17-18).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.55"
    **ADD 314 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 86.74 EUR vs 59.28 EUR (+46%, 23 analysts); de-biased α +4.2% vs CAPM hurdle 14.1%. Uptrend +7% vs 200-day avg; 12-1 mom +67%; RSI 54. Quality z -0.04 (ROE 6%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.48"
    Within rebalance band of target 9.8%: no trade. Analyst target 327.70 USD vs 228.29 USD (+44%, 59 analysts); de-biased α +3.4% vs CAPM hurdle 14.0%. Uptrend +14% vs 200-day avg; 12-1 mom +17%; RSI 58. Quality z +0.48 (ROE 101%).

??? success "TSM (TSM) — 🟢 Buy, score +0.40"
    Within rebalance band of target 9.9%: no trade. Analyst target 552.26 USD vs 456.28 USD (+21%, 20 analysts); de-biased α -1.3% vs CAPM hurdle 10.9%. Uptrend +19% vs 200-day avg; 12-1 mom +49%; RSI 65. Quality z +0.58 (ROE 35%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.37"
    **ADD 36 sh** → target 6.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 640.89 USD vs 511.67 USD (+25%, 35 analysts); de-biased α -0.5% vs CAPM hurdle 11.7%. Uptrend +20% vs 200-day avg; 12-1 mom +117%; RSI 63. Quality z +0.03 (ROE 36%).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.34"
    **TRIM 100 sh** → target 4.7% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 42,567 JPY vs 37,090 JPY (+15%, 21 analysts); de-biased α -3.6% vs CAPM hurdle 13.3%. Uptrend +36% vs 200-day avg; 12-1 mom +150%; RSI 65. Quality z +0.33 (ROE 58%). ⚠️ price implies 76% stage-1 growth (reverse DCF).

??? success "Tokyo Electron (8035.T) — 🟢 Buy, score +0.26"
    **TRIM 100 sh** → target 4.5% of NAV (sized ∝ score ÷ σ(e), cap 10%). No reliable analyst target: α set to 0. Uptrend +30% vs 200-day avg; 12-1 mom +149%; RSI 72. Quality z -0.28 (ROE 29%). ⚠️ price implies 72% stage-1 growth (reverse DCF).

??? note "AVGO (AVGO) — ⚪ Hold, score +0.24"
    Hold zone: keep any existing position, no new money. Analyst target 531.85 USD vs 351.29 USD (+51%, 47 analysts); de-biased α +6.2% vs CAPM hurdle 11.2%. Downtrend -4% vs 200-day avg; 12-1 mom +13%; RSI 44. Quality z +0.27 (ROE 31%).

??? note "ASX (ASX) — ⚪ Hold, score +0.19"
    Hold zone: not owned, no entry. Analyst target 51.00 USD vs 44.49 USD (+15%, 1 analysts); de-biased α -1.6% vs CAPM hurdle 12.1%. Uptrend +47% vs 200-day avg; 12-1 mom +241%; RSI 62. Quality z -0.68 (ROE 12%). ⚠️ price implies 67% stage-1 growth (reverse DCF).

??? note "ASML (ASML) — ⚪ Hold, score +0.10"
    Hold zone: not owned, no entry. Analyst target 2,123.54 USD vs 1,811.25 USD (+17%, 16 analysts); de-biased α -2.7% vs CAPM hurdle 12.4%. Uptrend +18% vs 200-day avg; 12-1 mom +73%; RSI 60. Quality z +0.42 (ROE 50%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.06"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 195.03 USD (+20%, 26 analysts); de-biased α -1.7% vs CAPM hurdle 11.2%. Uptrend +10% vs 200-day avg; 12-1 mom +59%; RSI 59. Quality z +0.51 (ROE 87%).

??? note "AMD (AMD) — ⚪ Hold, score -0.15"
    Hold zone: not owned, no entry. Analyst target 618.51 USD vs 611.74 USD (+1%, 50 analysts); de-biased α -7.5% vs CAPM hurdle 15.0%. Uptrend +64% vs 200-day avg; 12-1 mom +184%; RSI 66. Quality z -0.15 (ROE 7%).

??? note "MRVL (MRVL) — ⚪ Hold, score -0.16"
    Hold zone: not owned, no entry. Analyst target 289.11 USD vs 264.21 USD (+9%, 43 analysts); de-biased α -5.2% vs CAPM hurdle 14.2%. Uptrend +60% vs 200-day avg; 12-1 mom +157%; RSI 62. Quality z -0.12 (ROE 19%). ⚠️ price implies 76% stage-1 growth (reverse DCF).

??? note "Disco (6146.T) — ⚪ Hold, score -0.20"
    Hold zone: not owned, no entry. Analyst target 82,580 JPY vs 60,350 JPY (+37%, 20 analysts); de-biased α +2.6% vs CAPM hurdle 11.6%. Downtrend -7% vs 200-day avg; 12-1 mom +35%; RSI 62. Quality z +0.07 (ROE 25%).

??? note "GFS (GFS) — ⚪ Hold, score -0.21"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 47.91 USD (+59%, 22 analysts); de-biased α +7.6% vs CAPM hurdle 12.5%. Downtrend -11% vs 200-day avg; 12-1 mom +23%; RSI 51. Quality z -0.21 (ROE 8%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.34"
    Avoid: not owned. Analyst target 1,125.89 EUR vs 889.80 EUR (+27%, 19 analysts); de-biased α -0.6% vs CAPM hurdle 13.2%. Uptrend +13% vs 200-day avg; 12-1 mom +44%; RSI 61. Quality z -0.10 (ROE 19%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.39"
    Avoid: not owned. Analyst target 324.71 USD vs 280.03 USD (+16%, 31 analysts); de-biased α -2.2% vs CAPM hurdle 10.8%. Uptrend +14% vs 200-day avg; 12-1 mom +41%; RSI 61. Quality z +0.24 (ROE 30%).

??? failure "LRCX (LRCX) — 🔴 Sell, score -0.40"
    Avoid: not owned. Analyst target 373.77 USD vs 328.61 USD (+14%, 31 analysts); de-biased α -3.6% vs CAPM hurdle 12.7%. Uptrend +20% vs 200-day avg; 12-1 mom +117%; RSI 61. Quality z +0.03 (ROE 65%).

??? failure "Shin-Etsu (4063.T) — 🔴 Sell, score -0.50"
    Avoid: not owned. Analyst target 7,775 JPY vs 6,044 JPY (+29%, 17 analysts); de-biased α +0.9% vs CAPM hurdle 10.8%. Downtrend -2% vs 200-day avg; 12-1 mom +35%; RSI 57. Quality z -0.19 (ROE 10%).

??? failure "TER (TER) — 🔴 Sell, score -0.65"
    Avoid: not owned. Analyst target 446.47 USD vs 400.91 USD (+11%, 15 analysts); de-biased α -4.2% vs CAPM hurdle 12.5%. Uptrend +21% vs 200-day avg; 12-1 mom +161%; RSI 58. Quality z -0.31 (ROE 20%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.69"
    Avoid: not owned. Analyst target 76.40 USD vs 52.37 USD (+46%, 10 analysts); de-biased α +4.1% vs CAPM hurdle 14.1%. Downtrend -8% vs 200-day avg; 12-1 mom +62%; RSI 51. Quality z -1.00 (ROE 9%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.79"
    Avoid: not owned. Analyst target 173.36 USD vs 154.14 USD (+12%, 11 analysts); de-biased α -3.5% vs CAPM hurdle 10.9%. Uptrend +17% vs 200-day avg; 12-1 mom +41%; RSI 61. Quality z -0.02 (ROE 6%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -0.82"
    Avoid: not owned. Analyst target 405.47 USD vs 330.18 USD (+23%, 26 analysts); de-biased α -0.8% vs CAPM hurdle 10.1%. Uptrend +1% vs 200-day avg; 12-1 mom -11%; RSI 63. Quality z +0.31 (ROE 22%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.87"
    Avoid: not owned. Analyst target 194.13 USD vs 184.06 USD (+5%, 30 analysts); de-biased α -5.2% vs CAPM hurdle 12.1%. Uptrend +10% vs 200-day avg; 12-1 mom +2%; RSI 52. Quality z +0.70 (ROE 23%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -0.92"
    Avoid: not owned. Analyst target 94.39 HKD vs 60.65 HKD (+56%, 22 analysts); de-biased α +8.1% vs CAPM hurdle 7.4%. Downtrend -13% vs 200-day avg; 12-1 mom -1%; RSI 37. Quality z -0.98 (ROE 3%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.94"
    Avoid: not owned. Analyst target 553.77 USD vs 435.07 USD (+27%, 25 analysts); de-biased α +0.2% vs CAPM hurdle 10.4%. Downtrend -2% vs 200-day avg; 12-1 mom -16%; RSI 62. Quality z +0.14 (ROE 7%).

??? failure "INTC (INTC) — 🔴🔴 Strong Sell, score -1.02"
    Avoid: not owned. Analyst target 116.37 USD vs 120.16 USD (-3%, 43 analysts); de-biased α -8.3% vs CAPM hurdle 14.1%. Uptrend +49% vs 200-day avg; 12-1 mom +165%; RSI 62. Quality z -0.62 (ROE -0%). ⚠️ price implies 87% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 61% → smaller size.

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.45"
    Avoid: not owned. Analyst target 288.70 USD vs 289.76 USD (-0%, 40 analysts); de-biased α -9.1% vs CAPM hurdle 20.0%. Uptrend +35% vs 200-day avg; 12-1 mom +66%; RSI 53. Quality z +0.04 (ROE 12%). ⚠️ price implies 115% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 74 | 1,829,000 KRW | $99,450 | 9.7% | Strong Buy |
| MU | Micron Technology | 92 | 1,067.49 USD | $98,209 | 9.6% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 275,500 KRW | $98,180 | 9.6% | Strong Buy |
| KLAC | KLA Corp | 469 | 195.03 USD | $91,469 | 9.0% | Hold |
| TSM | TSMC | 187 | 456.28 USD | $85,324 | 8.4% | Buy |
| NVDA | NVIDIA | 371 | 228.29 USD | $84,696 | 8.3% | Buy |
| IFX.DE | Infineon Technologies | 1,205 | 59.28 EUR | $80,879 | 7.9% | Buy |
| 6857.T | Advantest | 300 | 37,090 JPY | $70,250 | 6.9% | Buy |
| AVGO | Broadcom | 170 | 351.29 USD | $59,719 | 5.9% | Hold |
| 8035.T | Tokyo Electron | 600 | 12,505 JPY | $47,370 | 4.6% | Buy |
| AMAT | Applied Materials | 91 | 511.67 USD | $46,562 | 4.6% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 4.07%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 16.0%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
