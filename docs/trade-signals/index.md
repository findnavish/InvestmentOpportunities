---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-09-29 15:53 UTC (Tue Sep 29, 11:53 AM ET) · refreshes hourly · weekly model inputs as of 2026-09-25
**Markets:** NYSE/Nasdaq 🟢 open (Tue 11:53) · Tokyo 🔴 closed (Wed 00:53) · Korea 🔴 closed (Wed 00:53) · Hong Kong 🔴 closed (Tue 23:53) · Xetra 🔴 closed (Tue 17:53) · Euronext Amsterdam 🔴 closed (Tue 17:53)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$1,005,255** | $138,716 (14%) | $866,539 (86%) | +0.53% | +0.74% | 🟢 Risk-on (+26.4%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $1,005,255), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| BUY (new) | **TSM**<br><small>TSMC</small> | 187 | 457.37 USD | $85,528 | Executed (paper) | quality +0.28 · analyst α -0.08 |
| BUY (new) | **Tokyo Electron**<br><small>8035.T</small> | 800 | 11,440 JPY | $58,096 | Queued · Tokyo closed | momentum +0.23 · quality -0.18 · ⚠️ rich valuation |
| TRIM | **AMAT**<br><small>Applied Materials</small> | 87 | 501.80 USD | $43,657 | Executed (paper) | momentum +0.07 · analyst α +0.05 |
| TRIM | **AVGO**<br><small>Broadcom</small> | 112 | 357.74 USD | $40,067 | Executed (paper) | analyst α +0.41 · momentum -0.26 |
| TRIM | **Infineon**<br><small>IFX.DE</small> | 452 | 59.16 EUR | $30,314 | Queued · Xetra closed | analyst α +0.31 · trend -0.09 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.39 | **SK hynix**<br><small>000660.KS</small> | 1,757,000 KRW | +81% | +12.4% | +465% | +26% | 50 | +0.63 | 9.5% → 10.0% | – | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.01 | **MU**<br><small>Micron Technology</small> | 1,065.09 USD | +42% | +2.8% | +494% | +59% | 60 | +0.06 | 9.7% → 10.0% | – | momentum +0.53 · analyst α +0.23 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.82 | **Samsung**<br><small>005930.KS</small> | 270,500 KRW | +77% | +12.2% | +267% | +21% | 53 | -0.25 | 9.6% → 10.0% | – | analyst α +0.66 · momentum +0.35 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.75 | **Advantest**<br><small>6857.T</small> | 33,510 JPY | +27% | -0.8% | +161% | +23% | 53 | +0.33 | 8.5% → 9.5% | – | momentum +0.17 · quality +0.16 · ⚠️ rich valuation |
| 🟢 Buy | +0.46 | **NVDA**<br><small>NVIDIA</small> | 230.51 USD | +42% | +2.8% | +22% | +15% | 60 | +0.48 | 10.3% → 8.8% | – | analyst α +0.27 · momentum -0.23 |
| 🟢 Buy | +0.39 | **Infineon**<br><small>IFX.DE</small> | 59.16 EUR | +47% | +4.0% | +71% | +7% | 54 | -0.04 | 10.4% → 7.3% | TRIM 452 | analyst α +0.31 · trend -0.09 |
| 🟢 Buy | +0.37 | **Tokyo Electron**<br><small>8035.T</small> | 11,440 JPY | – | +0.0% | +164% | +20% | 62 | -0.28 | 0.0% → 6.1% | BUY 800 | momentum +0.23 · quality -0.18 · ⚠️ rich valuation |
| 🟢 Buy | +0.37 | **TSM**<br><small>TSMC</small> | 457.37 USD | +21% | -1.7% | +54% | +19% | 65 | +0.58 | 8.5% → 8.5% | BUY 187 | quality +0.28 · analyst α -0.08 |
| 🟢 Buy | +0.30 | **AVGO**<br><small>Broadcom</small> | 357.74 USD | +49% | +5.3% | +11% | -2% | 48 | +0.27 | 6.0% → 6.0% | TRIM 112 | analyst α +0.41 · momentum -0.26 |
| 🟢 Buy | +0.28 | **AMAT**<br><small>Applied Materials</small> | 501.80 USD | +28% | -0.2% | +128% | +19% | 61 | +0.03 | 4.5% → 4.5% | TRIM 87 | momentum +0.07 · analyst α +0.05 |
| ⚪ Hold | +0.09 | **ASX**<br><small>ASE Technology</small> | 45.62 USD | +12% | -2.1% | +242% | +52% | 66 | -0.68 | 0.0% → 0.0% | – | momentum +0.30 · quality -0.28 · ⚠️ rich valuation |
| ⚪ Hold | +0.07 | **KLAC**<br><small>KLA Corp</small> | 195.28 USD | +20% | -2.1% | +66% | +11% | 60 | +0.51 | 9.1% → 9.1% | – | quality +0.24 · analyst α -0.12 |
| ⚪ Hold | +0.07 | **ASML**<br><small>ASML Holding</small> | 1,818.69 USD | +17% | -3.1% | +79% | +19% | 62 | +0.42 | 0.0% → 0.0% | – | analyst α -0.23 · quality +0.18 |
| ⚪ Hold | +0.05 | **Disco**<br><small>6146.T</small> | 56,590 JPY | +46% | +4.5% | +47% | -12% | 53 | +0.07 | 0.0% → 0.0% | – | analyst α +0.36 · trend -0.32 |
| ⚪ Hold | -0.12 | **GFS**<br><small>GlobalFoundries</small> | 48.02 USD | +58% | +7.2% | +26% | -11% | 52 | -0.21 | 0.0% → 0.0% | – | analyst α +0.48 · trend -0.21 |
| ⚪ Hold | -0.14 | **AMD**<br><small>Advanced Micro Devices</small> | 612.74 USD | +1% | -7.8% | +192% | +66% | 66 | -0.15 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.32 |
| ⚪ Hold | -0.20 | **MRVL**<br><small>Marvell Technology</small> | 261.98 USD | +10% | -5.2% | +161% | +60% | 61 | -0.12 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.25 · ⚠️ rich valuation |
| 🔴 Sell | -0.32 | **LRCX**<br><small>Lam Research</small> | 323.17 USD | +16% | -3.5% | +136% | +19% | 59 | +0.03 | 0.0% → 0.0% | – | analyst α -0.27 · momentum +0.10 |
| 🔴 Sell | -0.43 | **ASMI**<br><small>ASM.AS</small> | 883.40 EUR | +27% | -0.6% | +47% | +12% | 60 | -0.10 | 0.0% → 0.0% | – | momentum -0.10 · quality -0.06 |
| 🔴 Sell | -0.54 | **TXN**<br><small>Texas Instruments</small> | 280.98 USD | +16% | -2.6% | +44% | +14% | 62 | +0.24 | 0.0% → 0.0% | – | analyst α -0.19 · momentum -0.14 |
| 🔴 Sell | -0.57 | **TER**<br><small>Teradyne</small> | 406.36 USD | +10% | -4.9% | +163% | +23% | 60 | -0.31 | 0.0% → 0.0% | – | analyst α -0.36 · quality -0.21 |
| 🔴 Sell | -0.61 | **Shin-Etsu**<br><small>4063.T</small> | 5,737 JPY | +36% | +2.3% | +38% | -7% | 40 | -0.19 | 0.0% → 0.0% | – | trend -0.18 · momentum -0.17 |
| 🔴 Sell | -0.64 | **SMIC**<br><small>0981.HK</small> | 61.05 HKD | +55% | +7.5% | +2% | -12% | 38 | -0.98 | 0.0% → 0.0% | – | analyst α +0.55 · quality -0.33 |
| 🔴 Sell | -0.72 | **CDNS**<br><small>Cadence Design Systems</small> | 322.99 USD | +26% | -0.4% | -3% | -1% | 59 | +0.31 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.13 |
| 🔴🔴 Strong Sell | -0.80 | **AMKR**<br><small>Amkor Technology</small> | 54.34 USD | +41% | +2.5% | +66% | -5% | 56 | -1.00 | 0.0% → 0.0% | – | quality -0.43 · analyst α +0.19 |
| 🔴🔴 Strong Sell | -0.90 | **QCOM**<br><small>Qualcomm</small> | 186.65 USD | +4% | -5.9% | -1% | +11% | 54 | +0.70 | 0.0% → 0.0% | – | analyst α -0.48 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.92 | **ENTG**<br><small>Entegris</small> | 155.31 USD | +12% | -4.1% | +45% | +19% | 62 | -0.02 | 0.0% → 0.0% | – | analyst α -0.31 · momentum -0.12 |
| 🔴🔴 Strong Sell | -0.98 | **SNPS**<br><small>Synopsys</small> | 416.13 USD | +33% | +1.4% | -9% | -6% | 55 | +0.14 | 0.0% → 0.0% | – | momentum -0.53 · trend -0.16 |
| 🔴🔴 Strong Sell | -1.23 | **INTC**<br><small>Intel</small> | 116.42 USD | -0% | -7.8% | +152% | +46% | 59 | -0.62 | 0.0% → 0.0% | – | analyst α -0.66 · quality -0.24 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.31 | **ARM**<br><small>Arm Holdings</small> | 297.29 USD | -3% | -10.0% | +71% | +39% | 56 | +0.04 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.14 · ⚠️ rich valuation, high σ(e) |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.39"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,184,026 KRW vs 1,757,000 KRW (+81%, 37 analysts); de-biased α +12.4% vs CAPM hurdle 14.4%. Uptrend +26% vs 200-day avg; 12-1 mom +465%; RSI 50. Quality z +0.63 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.01"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,515.54 USD vs 1,065.09 USD (+42%, 46 analysts); de-biased α +2.8% vs CAPM hurdle 14.1%. Uptrend +59% vs 200-day avg; 12-1 mom +494%; RSI 60. Quality z +0.06 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 6.8 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.82"
    Within rebalance band of target 10.0%: no trade. Analyst target 478,628 KRW vs 270,500 KRW (+77%, 36 analysts); de-biased α +12.2% vs CAPM hurdle 11.4%. Uptrend +21% vs 200-day avg; 12-1 mom +267%; RSI 53. Quality z -0.25 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 4.0 (ch.17-18).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.75"
    Within rebalance band of target 9.5%: no trade. Analyst target 42,567 JPY vs 33,510 JPY (+27%, 21 analysts); de-biased α -0.8% vs CAPM hurdle 13.3%. Uptrend +23% vs 200-day avg; 12-1 mom +161%; RSI 53. Quality z +0.33 (ROE 58%). ⚠️ price implies 76% stage-1 growth (reverse DCF).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.46"
    Within rebalance band of target 8.8%: no trade. Analyst target 327.70 USD vs 230.51 USD (+42%, 59 analysts); de-biased α +2.8% vs CAPM hurdle 14.0%. Uptrend +15% vs 200-day avg; 12-1 mom +22%; RSI 60. Quality z +0.48 (ROE 101%).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.39"
    **TRIM 452 sh** → target 7.3% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 86.74 EUR vs 59.16 EUR (+47%, 23 analysts); de-biased α +4.0% vs CAPM hurdle 14.1%. Uptrend +7% vs 200-day avg; 12-1 mom +71%; RSI 54. Quality z -0.04 (ROE 6%).

??? success "Tokyo Electron (8035.T) — 🟢 Buy, score +0.37"
    **BUY (new) 800 sh** → target 6.1% of NAV (sized ∝ score ÷ σ(e), cap 10%). No reliable analyst target: α set to 0. Uptrend +20% vs 200-day avg; 12-1 mom +164%; RSI 62. Quality z -0.28 (ROE 29%). ⚠️ price implies 72% stage-1 growth (reverse DCF).

??? success "TSM (TSM) — 🟢 Buy, score +0.37"
    **BUY (new) 187 sh** → target 8.5% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 552.26 USD vs 457.37 USD (+21%, 20 analysts); de-biased α -1.7% vs CAPM hurdle 10.9%. Uptrend +19% vs 200-day avg; 12-1 mom +54%; RSI 65. Quality z +0.58 (ROE 35%).

??? success "AVGO (AVGO) — 🟢 Buy, score +0.30"
    **TRIM 112 sh** → target 6.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 531.85 USD vs 357.74 USD (+49%, 47 analysts); de-biased α +5.3% vs CAPM hurdle 11.2%. Downtrend -2% vs 200-day avg; 12-1 mom +11%; RSI 48. Quality z +0.27 (ROE 31%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.28"
    **TRIM 87 sh** → target 4.5% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 640.89 USD vs 501.80 USD (+28%, 35 analysts); de-biased α -0.2% vs CAPM hurdle 11.7%. Uptrend +19% vs 200-day avg; 12-1 mom +128%; RSI 61. Quality z +0.03 (ROE 36%).

??? note "ASX (ASX) — ⚪ Hold, score +0.09"
    Hold zone: not owned, no entry. Analyst target 51.00 USD vs 45.62 USD (+12%, 1 analysts); de-biased α -2.1% vs CAPM hurdle 12.1%. Uptrend +52% vs 200-day avg; 12-1 mom +242%; RSI 66. Quality z -0.68 (ROE 12%). ⚠️ price implies 67% stage-1 growth (reverse DCF).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.07"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 195.28 USD (+20%, 26 analysts); de-biased α -2.1% vs CAPM hurdle 11.2%. Uptrend +11% vs 200-day avg; 12-1 mom +66%; RSI 60. Quality z +0.51 (ROE 87%).

??? note "ASML (ASML) — ⚪ Hold, score +0.07"
    Hold zone: not owned, no entry. Analyst target 2,123.54 USD vs 1,818.69 USD (+17%, 16 analysts); de-biased α -3.1% vs CAPM hurdle 12.4%. Uptrend +19% vs 200-day avg; 12-1 mom +79%; RSI 62. Quality z +0.42 (ROE 50%).

??? note "Disco (6146.T) — ⚪ Hold, score +0.05"
    Hold zone: not owned, no entry. Analyst target 82,580 JPY vs 56,590 JPY (+46%, 20 analysts); de-biased α +4.5% vs CAPM hurdle 11.6%. Downtrend -12% vs 200-day avg; 12-1 mom +47%; RSI 53. Quality z +0.07 (ROE 25%).

??? note "GFS (GFS) — ⚪ Hold, score -0.12"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 48.02 USD (+58%, 22 analysts); de-biased α +7.2% vs CAPM hurdle 12.5%. Downtrend -11% vs 200-day avg; 12-1 mom +26%; RSI 52. Quality z -0.21 (ROE 8%).

??? note "AMD (AMD) — ⚪ Hold, score -0.14"
    Hold zone: not owned, no entry. Analyst target 618.51 USD vs 612.74 USD (+1%, 50 analysts); de-biased α -7.8% vs CAPM hurdle 15.0%. Uptrend +66% vs 200-day avg; 12-1 mom +192%; RSI 66. Quality z -0.15 (ROE 7%).

??? note "MRVL (MRVL) — ⚪ Hold, score -0.20"
    Hold zone: not owned, no entry. Analyst target 289.11 USD vs 261.98 USD (+10%, 43 analysts); de-biased α -5.2% vs CAPM hurdle 14.2%. Uptrend +60% vs 200-day avg; 12-1 mom +161%; RSI 61. Quality z -0.12 (ROE 19%). ⚠️ price implies 76% stage-1 growth (reverse DCF).

??? failure "LRCX (LRCX) — 🔴 Sell, score -0.32"
    Avoid: not owned. Analyst target 373.77 USD vs 323.17 USD (+16%, 31 analysts); de-biased α -3.5% vs CAPM hurdle 12.7%. Uptrend +19% vs 200-day avg; 12-1 mom +136%; RSI 59. Quality z +0.03 (ROE 65%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.43"
    Avoid: not owned. Analyst target 1,125.89 EUR vs 883.40 EUR (+27%, 19 analysts); de-biased α -0.6% vs CAPM hurdle 13.2%. Uptrend +12% vs 200-day avg; 12-1 mom +47%; RSI 60. Quality z -0.10 (ROE 19%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.54"
    Avoid: not owned. Analyst target 324.71 USD vs 280.98 USD (+16%, 31 analysts); de-biased α -2.6% vs CAPM hurdle 10.8%. Uptrend +14% vs 200-day avg; 12-1 mom +44%; RSI 62. Quality z +0.24 (ROE 30%).

??? failure "TER (TER) — 🔴 Sell, score -0.57"
    Avoid: not owned. Analyst target 446.47 USD vs 406.36 USD (+10%, 15 analysts); de-biased α -4.9% vs CAPM hurdle 12.5%. Uptrend +23% vs 200-day avg; 12-1 mom +163%; RSI 60. Quality z -0.31 (ROE 20%).

??? failure "Shin-Etsu (4063.T) — 🔴 Sell, score -0.61"
    Avoid: not owned. Analyst target 7,775 JPY vs 5,737 JPY (+36%, 17 analysts); de-biased α +2.3% vs CAPM hurdle 10.8%. Downtrend -7% vs 200-day avg; 12-1 mom +38%; RSI 40. Quality z -0.19 (ROE 10%).

??? failure "SMIC (0981.HK) — 🔴 Sell, score -0.64"
    Avoid: not owned. Analyst target 94.39 HKD vs 61.05 HKD (+55%, 22 analysts); de-biased α +7.5% vs CAPM hurdle 7.4%. Downtrend -12% vs 200-day avg; 12-1 mom +2%; RSI 38. Quality z -0.98 (ROE 3%).

??? failure "CDNS (CDNS) — 🔴 Sell, score -0.72"
    Avoid: not owned. Analyst target 405.47 USD vs 322.99 USD (+26%, 26 analysts); de-biased α -0.4% vs CAPM hurdle 10.1%. Downtrend -1% vs 200-day avg; 12-1 mom -3%; RSI 59. Quality z +0.31 (ROE 22%).

??? failure "AMKR (AMKR) — 🔴🔴 Strong Sell, score -0.80"
    Avoid: not owned. Analyst target 76.40 USD vs 54.34 USD (+41%, 10 analysts); de-biased α +2.5% vs CAPM hurdle 14.1%. Downtrend -5% vs 200-day avg; 12-1 mom +66%; RSI 56. Quality z -1.00 (ROE 9%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.90"
    Avoid: not owned. Analyst target 194.13 USD vs 186.65 USD (+4%, 30 analysts); de-biased α -5.9% vs CAPM hurdle 12.1%. Uptrend +11% vs 200-day avg; 12-1 mom -1%; RSI 54. Quality z +0.70 (ROE 23%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.92"
    Avoid: not owned. Analyst target 173.36 USD vs 155.31 USD (+12%, 11 analysts); de-biased α -4.1% vs CAPM hurdle 10.9%. Uptrend +19% vs 200-day avg; 12-1 mom +45%; RSI 62. Quality z -0.02 (ROE 6%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.98"
    Avoid: not owned. Analyst target 553.77 USD vs 416.13 USD (+33%, 25 analysts); de-biased α +1.4% vs CAPM hurdle 10.4%. Downtrend -6% vs 200-day avg; 12-1 mom -9%; RSI 55. Quality z +0.14 (ROE 7%).

??? failure "INTC (INTC) — 🔴🔴 Strong Sell, score -1.23"
    Avoid: not owned. Analyst target 116.37 USD vs 116.42 USD (-0%, 43 analysts); de-biased α -7.8% vs CAPM hurdle 14.1%. Uptrend +46% vs 200-day avg; 12-1 mom +152%; RSI 59. Quality z -0.62 (ROE -0%). ⚠️ price implies 87% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 61% → smaller size.

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.31"
    Avoid: not owned. Analyst target 288.70 USD vs 297.29 USD (-3%, 40 analysts); de-biased α -10.0% vs CAPM hurdle 20.0%. Uptrend +39% vs 200-day avg; 12-1 mom +71%; RSI 56. Quality z +0.04 (ROE 12%). ⚠️ price implies 115% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| IFX.DE | Infineon Technologies | 1,552 | 59.16 EUR | $104,088 | 10.4% | Buy |
| NVDA | NVIDIA | 447 | 230.51 USD | $103,040 | 10.3% | Buy |
| MU | Micron Technology | 92 | 1,065.09 USD | $97,988 | 9.7% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 270,500 KRW | $96,803 | 9.6% | Strong Buy |
| 000660.KS | SK hynix | 74 | 1,757,000 KRW | $95,937 | 9.5% | Strong Buy |
| KLAC | KLA Corp | 469 | 195.28 USD | $91,586 | 9.1% | Hold |
| TSM | TSMC | 187 | 457.37 USD | $85,528 | 8.5% | Buy |
| 6857.T | Advantest | 400 | 33,510 JPY | $85,087 | 8.5% | Buy |
| AVGO | Broadcom | 170 | 357.74 USD | $60,816 | 6.0% | Buy |
| AMAT | Applied Materials | 91 | 501.80 USD | $45,664 | 4.5% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 4.07%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 17.2%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
