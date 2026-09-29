---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-09-29 20:48 UTC (Tue Sep 29, 04:48 PM ET) · refreshes hourly · weekly model inputs as of 2026-09-25
**Markets:** NYSE/Nasdaq 🔴 closed (Tue 16:48) · Tokyo 🔴 closed (Wed 05:48) · Korea 🔴 closed (Wed 05:48) · Hong Kong 🔴 closed (Wed 04:48) · Xetra 🔴 closed (Tue 22:48) · Euronext Amsterdam 🔴 closed (Tue 22:48)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$1,005,491** | $138,716 (14%) | $866,775 (86%) | +0.55% | +0.34% | 🟢 Risk-on (+25.9%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $1,005,491), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| – | No trades this hour | | | | | All positions are within their rebalance bands. |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.43 | **SK hynix**<br><small>000660.KS</small> | 1,757,000 KRW | +81% | +12.4% | +405% | +25% | 50 | +0.63 | 9.6% → 10.0% | – | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.03 | **MU**<br><small>Micron Technology</small> | 1,065.40 USD | +42% | +2.7% | +494% | +59% | 60 | +0.06 | 9.7% → 10.0% | – | momentum +0.53 · analyst α +0.23 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.82 | **Samsung**<br><small>005930.KS</small> | 270,500 KRW | +77% | +12.2% | +245% | +20% | 53 | -0.25 | 9.6% → 10.0% | – | analyst α +0.66 · momentum +0.35 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.72 | **Advantest**<br><small>6857.T</small> | 33,510 JPY | +27% | -0.9% | +149% | +23% | 53 | +0.33 | 8.5% → 10.0% | – | quality +0.16 · momentum +0.12 · ⚠️ rich valuation |
| 🟢 Buy | +0.44 | **NVDA**<br><small>NVIDIA</small> | 227.30 USD | +44% | +3.2% | +22% | +14% | 57 | +0.48 | 10.1% → 10.0% | – | analyst α +0.27 · momentum -0.23 |
| 🟢 Buy | +0.39 | **Infineon**<br><small>IFX.DE</small> | 59.16 EUR | +47% | +4.0% | +71% | +7% | 54 | -0.04 | 10.4% → 9.0% | – | analyst α +0.31 · trend -0.09 |
| 🟢 Buy | +0.34 | **TSM**<br><small>TSMC</small> | 457.05 USD | +21% | -1.7% | +54% | +19% | 65 | +0.58 | 8.5% → 9.8% | – | quality +0.28 · analyst α -0.08 |
| 🟢 Buy | +0.31 | **AVGO**<br><small>Broadcom</small> | 355.18 USD | +50% | +5.5% | +11% | -3% | 46 | +0.27 | 6.0% → 7.4% | – | analyst α +0.41 · momentum -0.26 |
| ⚪ Hold | +0.21 | **AMAT**<br><small>Applied Materials</small> | 512.15 USD | +25% | -0.9% | +128% | +21% | 63 | +0.03 | 4.6% → 4.6% | – | momentum +0.07 · trend +0.07 |
| ⚪ Hold | +0.18 | **Tokyo Electron**<br><small>8035.T</small> | 11,440 JPY | – | +0.0% | +153% | +19% | 62 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · momentum +0.17 · ⚠️ rich valuation |
| ⚪ Hold | +0.16 | **ASX**<br><small>ASE Technology</small> | 45.32 USD | +13% | -2.0% | +242% | +51% | 66 | -0.68 | 0.0% → 0.0% | – | momentum +0.30 · quality -0.28 · ⚠️ rich valuation |
| ⚪ Hold | +0.10 | **ASML**<br><small>ASML Holding</small> | 1,834.86 USD | +16% | -3.4% | +79% | +20% | 63 | +0.42 | 0.0% → 0.0% | – | analyst α -0.23 · quality +0.18 |
| ⚪ Hold | +0.03 | **KLAC**<br><small>KLA Corp</small> | 196.50 USD | +19% | -2.3% | +66% | +11% | 61 | +0.51 | 9.2% → 9.2% | – | quality +0.24 · analyst α -0.15 |
| ⚪ Hold | +0.01 | **Disco**<br><small>6146.T</small> | 56,590 JPY | +46% | +4.5% | +47% | -12% | 53 | +0.07 | 0.0% → 0.0% | – | analyst α +0.36 · trend -0.32 |
| ⚪ Hold | -0.10 | **MRVL**<br><small>Marvell Technology</small> | 263.28 USD | +10% | -5.4% | +161% | +60% | 62 | -0.12 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.25 · ⚠️ rich valuation |
| ⚪ Hold | -0.12 | **GFS**<br><small>GlobalFoundries</small> | 47.86 USD | +59% | +7.3% | +26% | -11% | 51 | -0.21 | 0.0% → 0.0% | – | analyst α +0.48 · trend -0.21 |
| ⚪ Hold | -0.14 | **AMD**<br><small>Advanced Micro Devices</small> | 607.77 USD | +2% | -7.6% | +192% | +65% | 66 | -0.15 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.32 |
| 🔴 Sell | -0.32 | **ASMI**<br><small>ASM.AS</small> | 883.40 EUR | +27% | -0.7% | +47% | +12% | 60 | -0.10 | 0.0% → 0.0% | – | momentum -0.07 · quality -0.06 |
| 🔴 Sell | -0.35 | **LRCX**<br><small>Lam Research</small> | 324.04 USD | +15% | -3.6% | +136% | +19% | 60 | +0.03 | 0.0% → 0.0% | – | analyst α -0.27 · momentum +0.10 |
| 🔴 Sell | -0.52 | **TER**<br><small>Teradyne</small> | 403.28 USD | +11% | -4.7% | +163% | +22% | 59 | -0.31 | 0.0% → 0.0% | – | analyst α -0.36 · momentum +0.23 |
| 🔴 Sell | -0.52 | **TXN**<br><small>Texas Instruments</small> | 281.82 USD | +15% | -2.7% | +44% | +15% | 63 | +0.24 | 0.0% → 0.0% | – | analyst α -0.19 · momentum -0.14 |
| 🔴 Sell | -0.62 | **Shin-Etsu**<br><small>4063.T</small> | 5,737 JPY | +36% | +2.3% | +38% | -7% | 40 | -0.19 | 0.0% → 0.0% | – | trend -0.18 · momentum -0.17 |
| 🔴 Sell | -0.64 | **SMIC**<br><small>0981.HK</small> | 61.05 HKD | +55% | +7.5% | +2% | -12% | 38 | -0.98 | 0.0% → 0.0% | – | analyst α +0.55 · quality -0.33 |
| 🔴 Sell | -0.66 | **CDNS**<br><small>Cadence Design Systems</small> | 324.24 USD | +25% | -0.6% | -3% | -0% | 60 | +0.31 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.13 |
| 🔴🔴 Strong Sell | -0.81 | **AMKR**<br><small>Amkor Technology</small> | 54.15 USD | +41% | +2.6% | +66% | -5% | 56 | -1.00 | 0.0% → 0.0% | – | quality -0.43 · analyst α +0.19 |
| 🔴🔴 Strong Sell | -0.93 | **ENTG**<br><small>Entegris</small> | 154.85 USD | +12% | -4.0% | +45% | +18% | 61 | -0.02 | 0.0% → 0.0% | – | analyst α -0.31 · momentum -0.12 |
| 🔴🔴 Strong Sell | -0.94 | **QCOM**<br><small>Qualcomm</small> | 184.19 USD | +5% | -5.6% | -1% | +10% | 52 | +0.70 | 0.0% → 0.0% | – | analyst α -0.48 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.99 | **SNPS**<br><small>Synopsys</small> | 415.05 USD | +33% | +1.4% | -9% | -7% | 54 | +0.14 | 0.0% → 0.0% | – | momentum -0.53 · trend -0.16 |
| 🔴🔴 Strong Sell | -1.20 | **INTC**<br><small>Intel</small> | 115.98 USD | +0% | -7.8% | +152% | +45% | 58 | -0.62 | 0.0% → 0.0% | – | analyst α -0.66 · quality -0.24 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.32 | **ARM**<br><small>Arm Holdings</small> | 293.67 USD | -2% | -9.8% | +71% | +38% | 55 | +0.04 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.14 · ⚠️ rich valuation, high σ(e) |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.43"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,184,026 KRW vs 1,757,000 KRW (+81%, 37 analysts); de-biased α +12.4% vs CAPM hurdle 14.4%. Uptrend +25% vs 200-day avg; 12-1 mom +405%; RSI 50. Quality z +0.63 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.03"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,515.54 USD vs 1,065.40 USD (+42%, 46 analysts); de-biased α +2.7% vs CAPM hurdle 14.1%. Uptrend +59% vs 200-day avg; 12-1 mom +494%; RSI 60. Quality z +0.06 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 6.8 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.82"
    Within rebalance band of target 10.0%: no trade. Analyst target 478,628 KRW vs 270,500 KRW (+77%, 36 analysts); de-biased α +12.2% vs CAPM hurdle 11.4%. Uptrend +20% vs 200-day avg; 12-1 mom +245%; RSI 53. Quality z -0.25 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 4.0 (ch.17-18).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.72"
    Within rebalance band of target 10.0%: no trade. Analyst target 42,567 JPY vs 33,510 JPY (+27%, 21 analysts); de-biased α -0.9% vs CAPM hurdle 13.3%. Uptrend +23% vs 200-day avg; 12-1 mom +149%; RSI 53. Quality z +0.33 (ROE 58%). ⚠️ price implies 76% stage-1 growth (reverse DCF).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.44"
    Within rebalance band of target 10.0%: no trade. Analyst target 327.70 USD vs 227.30 USD (+44%, 59 analysts); de-biased α +3.2% vs CAPM hurdle 14.0%. Uptrend +14% vs 200-day avg; 12-1 mom +22%; RSI 57. Quality z +0.48 (ROE 101%).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.39"
    Within rebalance band of target 9.0%: no trade. Analyst target 86.74 EUR vs 59.16 EUR (+47%, 23 analysts); de-biased α +4.0% vs CAPM hurdle 14.1%. Uptrend +7% vs 200-day avg; 12-1 mom +71%; RSI 54. Quality z -0.04 (ROE 6%).

??? success "TSM (TSM) — 🟢 Buy, score +0.34"
    Within rebalance band of target 9.8%: no trade. Analyst target 552.26 USD vs 457.05 USD (+21%, 20 analysts); de-biased α -1.7% vs CAPM hurdle 10.9%. Uptrend +19% vs 200-day avg; 12-1 mom +54%; RSI 65. Quality z +0.58 (ROE 35%).

??? success "AVGO (AVGO) — 🟢 Buy, score +0.31"
    Within rebalance band of target 7.4%: no trade. Analyst target 531.85 USD vs 355.18 USD (+50%, 47 analysts); de-biased α +5.5% vs CAPM hurdle 11.2%. Downtrend -3% vs 200-day avg; 12-1 mom +11%; RSI 46. Quality z +0.27 (ROE 31%).

??? note "AMAT (AMAT) — ⚪ Hold, score +0.21"
    Hold zone: keep any existing position, no new money. Analyst target 640.89 USD vs 512.15 USD (+25%, 35 analysts); de-biased α -0.9% vs CAPM hurdle 11.7%. Uptrend +21% vs 200-day avg; 12-1 mom +128%; RSI 63. Quality z +0.03 (ROE 36%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.18"
    Hold zone: not owned, no entry. No reliable analyst target: α set to 0. Uptrend +19% vs 200-day avg; 12-1 mom +153%; RSI 62. Quality z -0.28 (ROE 29%). ⚠️ price implies 72% stage-1 growth (reverse DCF).

??? note "ASX (ASX) — ⚪ Hold, score +0.16"
    Hold zone: not owned, no entry. Analyst target 51.00 USD vs 45.32 USD (+13%, 1 analysts); de-biased α -2.0% vs CAPM hurdle 12.1%. Uptrend +51% vs 200-day avg; 12-1 mom +242%; RSI 66. Quality z -0.68 (ROE 12%). ⚠️ price implies 67% stage-1 growth (reverse DCF).

??? note "ASML (ASML) — ⚪ Hold, score +0.10"
    Hold zone: not owned, no entry. Analyst target 2,123.54 USD vs 1,834.86 USD (+16%, 16 analysts); de-biased α -3.4% vs CAPM hurdle 12.4%. Uptrend +20% vs 200-day avg; 12-1 mom +79%; RSI 63. Quality z +0.42 (ROE 50%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.03"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 196.50 USD (+19%, 26 analysts); de-biased α -2.3% vs CAPM hurdle 11.2%. Uptrend +11% vs 200-day avg; 12-1 mom +66%; RSI 61. Quality z +0.51 (ROE 87%).

??? note "Disco (6146.T) — ⚪ Hold, score +0.01"
    Hold zone: not owned, no entry. Analyst target 82,580 JPY vs 56,590 JPY (+46%, 20 analysts); de-biased α +4.5% vs CAPM hurdle 11.6%. Downtrend -12% vs 200-day avg; 12-1 mom +47%; RSI 53. Quality z +0.07 (ROE 25%).

??? note "MRVL (MRVL) — ⚪ Hold, score -0.10"
    Hold zone: not owned, no entry. Analyst target 289.11 USD vs 263.28 USD (+10%, 43 analysts); de-biased α -5.4% vs CAPM hurdle 14.2%. Uptrend +60% vs 200-day avg; 12-1 mom +161%; RSI 62. Quality z -0.12 (ROE 19%). ⚠️ price implies 76% stage-1 growth (reverse DCF).

??? note "GFS (GFS) — ⚪ Hold, score -0.12"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 47.86 USD (+59%, 22 analysts); de-biased α +7.3% vs CAPM hurdle 12.5%. Downtrend -11% vs 200-day avg; 12-1 mom +26%; RSI 51. Quality z -0.21 (ROE 8%).

??? note "AMD (AMD) — ⚪ Hold, score -0.14"
    Hold zone: not owned, no entry. Analyst target 618.51 USD vs 607.77 USD (+2%, 50 analysts); de-biased α -7.6% vs CAPM hurdle 15.0%. Uptrend +65% vs 200-day avg; 12-1 mom +192%; RSI 66. Quality z -0.15 (ROE 7%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.32"
    Avoid: not owned. Analyst target 1,125.89 EUR vs 883.40 EUR (+27%, 19 analysts); de-biased α -0.7% vs CAPM hurdle 13.2%. Uptrend +12% vs 200-day avg; 12-1 mom +47%; RSI 60. Quality z -0.10 (ROE 19%).

??? failure "LRCX (LRCX) — 🔴 Sell, score -0.35"
    Avoid: not owned. Analyst target 373.77 USD vs 324.04 USD (+15%, 31 analysts); de-biased α -3.6% vs CAPM hurdle 12.7%. Uptrend +19% vs 200-day avg; 12-1 mom +136%; RSI 60. Quality z +0.03 (ROE 65%).

??? failure "TER (TER) — 🔴 Sell, score -0.52"
    Avoid: not owned. Analyst target 446.47 USD vs 403.28 USD (+11%, 15 analysts); de-biased α -4.7% vs CAPM hurdle 12.5%. Uptrend +22% vs 200-day avg; 12-1 mom +163%; RSI 59. Quality z -0.31 (ROE 20%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.52"
    Avoid: not owned. Analyst target 324.71 USD vs 281.82 USD (+15%, 31 analysts); de-biased α -2.7% vs CAPM hurdle 10.8%. Uptrend +15% vs 200-day avg; 12-1 mom +44%; RSI 63. Quality z +0.24 (ROE 30%).

??? failure "Shin-Etsu (4063.T) — 🔴 Sell, score -0.62"
    Avoid: not owned. Analyst target 7,775 JPY vs 5,737 JPY (+36%, 17 analysts); de-biased α +2.3% vs CAPM hurdle 10.8%. Downtrend -7% vs 200-day avg; 12-1 mom +38%; RSI 40. Quality z -0.19 (ROE 10%).

??? failure "SMIC (0981.HK) — 🔴 Sell, score -0.64"
    Avoid: not owned. Analyst target 94.39 HKD vs 61.05 HKD (+55%, 22 analysts); de-biased α +7.5% vs CAPM hurdle 7.4%. Downtrend -12% vs 200-day avg; 12-1 mom +2%; RSI 38. Quality z -0.98 (ROE 3%).

??? failure "CDNS (CDNS) — 🔴 Sell, score -0.66"
    Avoid: not owned. Analyst target 405.47 USD vs 324.24 USD (+25%, 26 analysts); de-biased α -0.6% vs CAPM hurdle 10.1%. Downtrend -0% vs 200-day avg; 12-1 mom -3%; RSI 60. Quality z +0.31 (ROE 22%).

??? failure "AMKR (AMKR) — 🔴🔴 Strong Sell, score -0.81"
    Avoid: not owned. Analyst target 76.40 USD vs 54.15 USD (+41%, 10 analysts); de-biased α +2.6% vs CAPM hurdle 14.1%. Downtrend -5% vs 200-day avg; 12-1 mom +66%; RSI 56. Quality z -1.00 (ROE 9%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.93"
    Avoid: not owned. Analyst target 173.36 USD vs 154.85 USD (+12%, 11 analysts); de-biased α -4.0% vs CAPM hurdle 10.9%. Uptrend +18% vs 200-day avg; 12-1 mom +45%; RSI 61. Quality z -0.02 (ROE 6%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.94"
    Avoid: not owned. Analyst target 194.13 USD vs 184.19 USD (+5%, 30 analysts); de-biased α -5.6% vs CAPM hurdle 12.1%. Uptrend +10% vs 200-day avg; 12-1 mom -1%; RSI 52. Quality z +0.70 (ROE 23%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.99"
    Avoid: not owned. Analyst target 553.77 USD vs 415.05 USD (+33%, 25 analysts); de-biased α +1.4% vs CAPM hurdle 10.4%. Downtrend -7% vs 200-day avg; 12-1 mom -9%; RSI 54. Quality z +0.14 (ROE 7%).

??? failure "INTC (INTC) — 🔴🔴 Strong Sell, score -1.20"
    Avoid: not owned. Analyst target 116.37 USD vs 115.98 USD (+0%, 43 analysts); de-biased α -7.8% vs CAPM hurdle 14.1%. Uptrend +45% vs 200-day avg; 12-1 mom +152%; RSI 58. Quality z -0.62 (ROE -0%). ⚠️ price implies 87% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 61% → smaller size.

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.32"
    Avoid: not owned. Analyst target 288.70 USD vs 293.67 USD (-2%, 40 analysts); de-biased α -9.8% vs CAPM hurdle 20.0%. Uptrend +38% vs 200-day avg; 12-1 mom +71%; RSI 55. Quality z +0.04 (ROE 12%). ⚠️ price implies 115% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| IFX.DE | Infineon Technologies | 1,552 | 59.16 EUR | $104,147 | 10.4% | Buy |
| NVDA | NVIDIA | 447 | 227.30 USD | $101,603 | 10.1% | Buy |
| MU | Micron Technology | 92 | 1,065.40 USD | $98,017 | 9.7% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 270,500 KRW | $97,024 | 9.6% | Strong Buy |
| 000660.KS | SK hynix | 74 | 1,757,000 KRW | $96,155 | 9.6% | Strong Buy |
| KLAC | KLA Corp | 469 | 196.50 USD | $92,158 | 9.2% | Hold |
| TSM | TSMC | 187 | 457.05 USD | $85,468 | 8.5% | Buy |
| 6857.T | Advantest | 400 | 33,510 JPY | $85,216 | 8.5% | Buy |
| AVGO | Broadcom | 170 | 355.18 USD | $60,381 | 6.0% | Buy |
| AMAT | Applied Materials | 91 | 512.15 USD | $46,606 | 4.6% | Hold |

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

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 4.07%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 17.3%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
