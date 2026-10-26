---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-26 19:22 UTC (Mon Oct 26, 03:22 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🟢 open (Mon 15:22) · Tokyo 🔴 closed (Tue 04:22) · Korea 🔴 closed (Tue 04:22) · Hong Kong 🔴 closed (Tue 03:22) · Xetra 🔴 closed (Mon 20:22) · Euronext Amsterdam 🔴 closed (Mon 20:22)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$886,434** | $126,836 (14%) | $759,598 (86%) | -11.36% | -12.35% | 🟢 Risk-on (+4.9%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $886,434), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **AMAT**<br><small>Applied Materials</small> | 57 | 391.16 USD | $22,296 | Executed (paper) | analyst α +0.19 · momentum +0.12 |
| ADD | **Tokyo Electron**<br><small>8035.T</small> | 300 | 9,139 JPY | $17,412 | Queued · Tokyo closed | analyst α +0.31 · quality -0.18 |
| TRIM | **ASX**<br><small>ASE Technology</small> | 395 | 40.15 USD | $15,859 | Executed (paper) | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| TRIM | **NVDA**<br><small>NVIDIA</small> | 58 | 216.65 USD | $12,566 | Executed (paper) | quality +0.21 · momentum -0.17 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.27 | **SK hynix**<br><small>000660.KS</small> | 1,285,000 KRW | +144% | +22.6% | +337% | -13% | 34 | +0.62 | 10.7% → 10.0% | – | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.28 | **MU**<br><small>Micron Technology</small> | 912.40 USD | +67% | +3.2% | +424% | +24% | 44 | +0.12 | 9.5% → 10.0% | – | momentum +0.53 · analyst α +0.23 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.54 | **Samsung**<br><small>005930.KS</small> | 213,500 KRW | +124% | +18.3% | +193% | -9% | 35 | -0.26 | 8.8% → 10.0% | – | analyst α +0.66 · momentum +0.23 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.60 | **Infineon**<br><small>IFX.DE</small> | 50.48 EUR | +72% | +4.6% | +67% | -11% | 37 | -0.04 | 8.3% → 8.6% | – | analyst α +0.41 · trend -0.07 |
| 🟢 Buy | +0.52 | **AMAT**<br><small>Applied Materials</small> | 391.16 USD | +63% | +3.1% | +113% | -11% | 32 | +0.03 | 6.4% → 6.4% | TRIM 57 | analyst α +0.19 · momentum +0.12 |
| 🟢 Buy | +0.50 | **Advantest**<br><small>6857.T</small> | 31,070 JPY | +37% | -3.9% | +84% | +8% | 36 | +0.33 | 4.5% → 4.9% | – | quality +0.16 · trend +0.14 · ⚠️ rich valuation |
| 🟢 Buy | +0.47 | **Tokyo Electron**<br><small>8035.T</small> | 9,139 JPY | +67% | +3.9% | +95% | -9% | 32 | -0.28 | 3.3% → 5.8% | ADD 300 | analyst α +0.31 · quality -0.18 |
| 🟢 Buy | +0.44 | **ASX**<br><small>ASE Technology</small> | 40.15 USD | +27% | -3.0% | +249% | +23% | 45 | -0.68 | 6.0% → 6.0% | TRIM 395 | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.28 | **NVDA**<br><small>NVIDIA</small> | 216.65 USD | +51% | -0.6% | +24% | +6% | 45 | +0.47 | 4.1% → 4.1% | TRIM 58 | quality +0.21 · momentum -0.17 |
| ⚪ Hold | +0.24 | **TSM**<br><small>TSMC</small> | 428.45 USD | +29% | -5.3% | +57% | +8% | 47 | +0.58 | 6.1% → 6.1% | – | quality +0.28 · analyst α -0.19 |
| ⚪ Hold | +0.17 | **ASML**<br><small>ASML Holding</small> | 1,595.95 USD | +31% | -5.1% | +69% | +1% | 39 | +0.42 | 5.4% → 5.4% | – | quality +0.18 · analyst α -0.15 |
| ⚪ Hold | +0.15 | **KLAC**<br><small>KLA Corp</small> | 150.09 USD | +56% | +1.3% | +63% | -17% | 29 | +0.51 | 4.5% → 4.5% | – | quality +0.24 · trend -0.18 · ⚠️ oversold |
| ⚪ Hold | +0.11 | **LRCX**<br><small>Lam Research</small> | 239.79 USD | +56% | +1.1% | +115% | -15% | 30 | +0.02 | 4.4% → 4.4% | – | momentum +0.14 · trend -0.14 |
| ⚪ Hold | +0.03 | **MRVL**<br><small>Marvell Technology</small> | 236.36 USD | +24% | -7.4% | +217% | +31% | 45 | -0.12 | 0.0% → 0.0% | – | analyst α -0.41 · momentum +0.26 · ⚠️ rich valuation |
| ⚪ Hold | -0.08 | **AVGO**<br><small>Broadcom</small> | 331.06 USD | +60% | +2.5% | +3% | -10% | 41 | +0.26 | 3.7% → 3.7% | – | momentum -0.26 · analyst α +0.15 |
| ⚪ Hold | -0.19 | **TER**<br><small>Teradyne</small> | 311.31 USD | +43% | -2.1% | +175% | -10% | 34 | -0.31 | 0.0% → 0.0% | – | quality -0.21 · momentum +0.20 |
| ⚪ Hold | -0.23 | **Disco**<br><small>6146.T</small> | 48,400 JPY | +69% | +4.6% | +2% | -26% | 32 | +0.06 | 0.0% → 0.0% | – | analyst α +0.36 · momentum -0.30 |
| 🔴 Sell | -0.36 | **AMD**<br><small>Advanced Micro Devices</small> | 532.47 USD | +16% | -9.6% | +168% | +32% | 43 | -0.15 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.32 |
| 🔴 Sell | -0.36 | **ASMI**<br><small>ASM.AS</small> | 708.60 EUR | +59% | +1.6% | +55% | -13% | 32 | -0.10 | 0.0% → 0.0% | – | momentum -0.12 · analyst α +0.12 |
| 🔴 Sell | -0.36 | **GFS**<br><small>GlobalFoundries</small> | 45.70 USD | +66% | +3.6% | +40% | -17% | 46 | -0.21 | 0.0% → 0.0% | – | analyst α +0.27 · trend -0.16 |
| 🔴 Sell | -0.37 | **INTC**<br><small>Intel</small> | 91.62 USD | +27% | -6.7% | +222% | +6% | 40 | -0.62 | 0.0% → 0.0% | – | analyst α -0.31 · momentum +0.30 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.57 | **AMKR**<br><small>Amkor Technology</small> | 37.26 USD | +105% | +13.0% | +69% | -35% | 28 | -1.00 | 0.0% → 0.0% | – | analyst α +0.48 · quality -0.43 · ⚠️ oversold |
| 🔴🔴 Strong Sell | -0.75 | **ENTG**<br><small>Entegris</small> | 141.64 USD | +22% | -7.0% | +68% | +3% | 46 | -0.02 | 0.0% → 0.0% | – | analyst α -0.36 · trend +0.06 |
| 🔴🔴 Strong Sell | -0.82 | **ARM**<br><small>Arm Holdings</small> | 225.12 USD | +28% | -7.8% | +86% | -1% | 39 | +0.04 | 0.0% → 0.0% | – | analyst α -0.48 · momentum +0.07 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -0.95 | **Shin-Etsu**<br><small>4063.T</small> | 5,788 JPY | +34% | -3.7% | +18% | -8% | 41 | -0.20 | 0.0% → 0.0% | – | momentum -0.23 · quality -0.11 |
| 🔴🔴 Strong Sell | -1.00 | **CDNS**<br><small>Cadence Design Systems</small> | 329.42 USD | +23% | -6.7% | -3% | +1% | 52 | +0.31 | 0.0% → 0.0% | – | momentum -0.35 · analyst α -0.27 |
| 🔴🔴 Strong Sell | -1.02 | **TXN**<br><small>Texas Instruments</small> | 298.42 USD | +9% | -10.0% | +66% | +17% | 65 | +0.24 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.16 |
| 🔴🔴 Strong Sell | -1.15 | **SNPS**<br><small>Synopsys</small> | 457.32 USD | +25% | -6.4% | -7% | +3% | 52 | +0.14 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.23 |
| 🔴🔴 Strong Sell | -1.15 | **QCOM**<br><small>Qualcomm</small> | 179.67 USD | +8% | -10.4% | +21% | +7% | 52 | +0.70 | 0.0% → 0.0% | – | analyst α -0.85 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.23 | **SMIC**<br><small>0981.HK</small> | 45.92 HKD | +109% | +15.5% | -16% | -33% | 18 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.53 · ⚠️ oversold |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.27"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,285,000 KRW (+144%, 38 analysts); de-biased α +22.6% vs CAPM hurdle 14.3%. Downtrend -13% vs 200-day avg; 12-1 mom +337%; RSI 34. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.28"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 912.40 USD (+67%, 46 analysts); de-biased α +3.2% vs CAPM hurdle 14.0%. Uptrend +24% vs 200-day avg; 12-1 mom +424%; RSI 44. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.54"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 213,500 KRW (+124%, 36 analysts); de-biased α +18.3% vs CAPM hurdle 11.3%. Downtrend -9% vs 200-day avg; 12-1 mom +193%; RSI 35. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.60"
    Within rebalance band of target 8.6%: no trade. Analyst target 86.74 EUR vs 50.48 EUR (+72%, 23 analysts); de-biased α +4.6% vs CAPM hurdle 14.1%. Downtrend -11% vs 200-day avg; 12-1 mom +67%; RSI 37. Quality z -0.04 (ROE 6%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.52"
    **TRIM 57 sh** → target 6.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 391.16 USD (+63%, 36 analysts); de-biased α +3.1% vs CAPM hurdle 11.6%. Downtrend -11% vs 200-day avg; 12-1 mom +113%; RSI 32. Quality z +0.03 (ROE 36%).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.50"
    Within rebalance band of target 4.9%: no trade. Analyst target 42,686 JPY vs 31,070 JPY (+37%, 21 analysts); de-biased α -3.9% vs CAPM hurdle 13.4%. Uptrend +8% vs 200-day avg; 12-1 mom +84%; RSI 36. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? success "Tokyo Electron (8035.T) — 🟢 Buy, score +0.47"
    **ADD 300 sh** → target 5.8% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 15,275 JPY vs 9,139 JPY (+67%, 23 analysts); de-biased α +3.9% vs CAPM hurdle 12.8%. Downtrend -9% vs 200-day avg; 12-1 mom +95%; RSI 32. Quality z -0.28 (ROE 29%).

??? success "ASX (ASX) — 🟢 Buy, score +0.44"
    **TRIM 395 sh** → target 6.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 51.00 USD vs 40.15 USD (+27%, 1 analysts); de-biased α -3.0% vs CAPM hurdle 11.9%. Uptrend +23% vs 200-day avg; 12-1 mom +249%; RSI 45. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.28"
    **TRIM 58 sh** → target 4.1% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 327.70 USD vs 216.65 USD (+51%, 59 analysts); de-biased α -0.6% vs CAPM hurdle 13.9%. Uptrend +6% vs 200-day avg; 12-1 mom +24%; RSI 45. Quality z +0.47 (ROE 101%).

??? note "TSM (TSM) — ⚪ Hold, score +0.24"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 428.45 USD (+29%, 20 analysts); de-biased α -5.3% vs CAPM hurdle 10.8%. Uptrend +8% vs 200-day avg; 12-1 mom +57%; RSI 47. Quality z +0.58 (ROE 35%).

??? note "ASML (ASML) — ⚪ Hold, score +0.17"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,595.95 USD (+31%, 16 analysts); de-biased α -5.1% vs CAPM hurdle 12.3%. Uptrend +1% vs 200-day avg; 12-1 mom +69%; RSI 39. Quality z +0.42 (ROE 50%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.15"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 150.09 USD (+56%, 26 analysts); de-biased α +1.3% vs CAPM hurdle 11.1%. Downtrend -17% vs 200-day avg; 12-1 mom +63%; RSI 29. Quality z +0.51 (ROE 87%). ⚠️ oversold.

??? note "LRCX (LRCX) — ⚪ Hold, score +0.11"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 239.79 USD (+56%, 31 analysts); de-biased α +1.1% vs CAPM hurdle 12.6%. Downtrend -15% vs 200-day avg; 12-1 mom +115%; RSI 30. Quality z +0.02 (ROE 65%).

??? note "MRVL (MRVL) — ⚪ Hold, score +0.03"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 236.36 USD (+24%, 43 analysts); de-biased α -7.4% vs CAPM hurdle 14.1%. Uptrend +31% vs 200-day avg; 12-1 mom +217%; RSI 45. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "AVGO (AVGO) — ⚪ Hold, score -0.08"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 331.06 USD (+60%, 47 analysts); de-biased α +2.5% vs CAPM hurdle 11.2%. Downtrend -10% vs 200-day avg; 12-1 mom +3%; RSI 41. Quality z +0.26 (ROE 31%).

??? note "TER (TER) — ⚪ Hold, score -0.19"
    Hold zone: not owned, no entry. Analyst target 446.47 USD vs 311.31 USD (+43%, 15 analysts); de-biased α -2.1% vs CAPM hurdle 12.3%. Downtrend -10% vs 200-day avg; 12-1 mom +175%; RSI 34. Quality z -0.31 (ROE 20%).

??? note "Disco (6146.T) — ⚪ Hold, score -0.23"
    Hold zone: not owned, no entry. Analyst target 81,730 JPY vs 48,400 JPY (+69%, 20 analysts); de-biased α +4.6% vs CAPM hurdle 11.5%. Downtrend -26% vs 200-day avg; 12-1 mom +2%; RSI 32. Quality z +0.06 (ROE 25%).

??? failure "AMD (AMD) — 🔴 Sell, score -0.36"
    Avoid: not owned. Analyst target 619.51 USD vs 532.47 USD (+16%, 50 analysts); de-biased α -9.6% vs CAPM hurdle 14.9%. Uptrend +32% vs 200-day avg; 12-1 mom +168%; RSI 43. Quality z -0.15 (ROE 7%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.36"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 708.60 EUR (+59%, 19 analysts); de-biased α +1.6% vs CAPM hurdle 13.2%. Downtrend -13% vs 200-day avg; 12-1 mom +55%; RSI 32. Quality z -0.10 (ROE 19%).

??? failure "GFS (GFS) — 🔴 Sell, score -0.36"
    Avoid: not owned. Analyst target 76.00 USD vs 45.70 USD (+66%, 22 analysts); de-biased α +3.6% vs CAPM hurdle 12.4%. Downtrend -17% vs 200-day avg; 12-1 mom +40%; RSI 46. Quality z -0.21 (ROE 8%).

??? failure "INTC (INTC) — 🔴 Sell, score -0.37"
    Avoid: not owned. Analyst target 116.37 USD vs 91.62 USD (+27%, 43 analysts); de-biased α -6.7% vs CAPM hurdle 14.0%. Uptrend +6% vs 200-day avg; 12-1 mom +222%; RSI 40. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.57"
    Avoid: not owned. Analyst target 76.40 USD vs 37.26 USD (+105%, 10 analysts); de-biased α +13.0% vs CAPM hurdle 14.0%. Downtrend -35% vs 200-day avg; 12-1 mom +69%; RSI 28. Quality z -1.00 (ROE 9%). ⚠️ oversold.

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.75"
    Avoid: not owned. Analyst target 173.36 USD vs 141.64 USD (+22%, 11 analysts); de-biased α -7.0% vs CAPM hurdle 11.0%. Uptrend +3% vs 200-day avg; 12-1 mom +68%; RSI 46. Quality z -0.02 (ROE 6%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -0.82"
    Avoid: not owned. Analyst target 288.70 USD vs 225.12 USD (+28%, 40 analysts); de-biased α -7.8% vs CAPM hurdle 19.6%. Downtrend -1% vs 200-day avg; 12-1 mom +86%; RSI 39. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -0.95"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,788 JPY (+34%, 17 analysts); de-biased α -3.7% vs CAPM hurdle 10.8%. Downtrend -8% vs 200-day avg; 12-1 mom +18%; RSI 41. Quality z -0.20 (ROE 10%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.00"
    Avoid: not owned. Analyst target 405.47 USD vs 329.42 USD (+23%, 26 analysts); de-biased α -6.7% vs CAPM hurdle 10.0%. Uptrend +1% vs 200-day avg; 12-1 mom -3%; RSI 52. Quality z +0.31 (ROE 22%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -1.02"
    Avoid: not owned. Analyst target 324.71 USD vs 298.42 USD (+9%, 31 analysts); de-biased α -10.0% vs CAPM hurdle 10.8%. Uptrend +17% vs 200-day avg; 12-1 mom +66%; RSI 65. Quality z +0.24 (ROE 30%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.15"
    Avoid: not owned. Analyst target 569.78 USD vs 457.32 USD (+25%, 26 analysts); de-biased α -6.4% vs CAPM hurdle 10.3%. Uptrend +3% vs 200-day avg; 12-1 mom -7%; RSI 52. Quality z +0.14 (ROE 7%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.15"
    Avoid: not owned. Analyst target 194.13 USD vs 179.67 USD (+8%, 30 analysts); de-biased α -10.4% vs CAPM hurdle 11.9%. Uptrend +7% vs 200-day avg; 12-1 mom +21%; RSI 52. Quality z +0.70 (ROE 23%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.23"
    Avoid: not owned. Analyst target 95.99 HKD vs 45.92 HKD (+109%, 21 analysts); de-biased α +15.5% vs CAPM hurdle 7.3%. Downtrend -33% vs 200-day avg; 12-1 mom -16%; RSI 18. Quality z -0.99 (ROE 3%). ⚠️ oversold.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 98 | 1,285,000 KRW | $95,019 | 10.7% | Strong Buy |
| MU | Micron Technology | 92 | 912.40 USD | $83,941 | 9.5% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 213,500 KRW | $78,130 | 8.8% | Strong Buy |
| IFX.DE | Infineon Technologies | 1,301 | 50.48 EUR | $73,445 | 8.3% | Buy |
| AMAT | Applied Materials | 145 | 391.16 USD | $56,718 | 6.4% | Buy |
| TSM | TSMC | 127 | 428.45 USD | $54,413 | 6.1% | Hold |
| ASX | ASE Technology | 1,320 | 40.15 USD | $52,998 | 6.0% | Buy |
| ASML | ASML Holding | 30 | 1,595.95 USD | $47,878 | 5.4% | Hold |
| KLAC | KLA Corp | 268 | 150.09 USD | $40,224 | 4.5% | Hold |
| 6857.T | Advantest | 200 | 31,070 JPY | $39,464 | 4.5% | Buy |
| LRCX | Lam Research | 162 | 239.79 USD | $38,845 | 4.4% | Hold |
| NVDA | NVIDIA | 168 | 216.65 USD | $36,397 | 4.1% | Buy |
| AVGO | Broadcom | 100 | 331.06 USD | $33,106 | 3.7% | Hold |
| 8035.T | Tokyo Electron | 500 | 9,139 JPY | $29,020 | 3.3% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-10-26 19:22 UTC | TRIM | AMAT | -57 | 391.16 | $22,296 |
| 2026-10-26 19:22 UTC | TRIM | NVDA | -58 | 216.65 | $12,566 |
| 2026-10-26 19:22 UTC | TRIM | ASX | -395 | 40.15 | $15,859 |
| 2026-10-26 06:15 UTC | ADD | 6857.T | 100 | 31,220.00 | $19,871 |
| 2026-10-23 19:14 UTC | ADD | KLAC | 57 | 145.31 | $8,282 |
| 2026-10-23 15:05 UTC | ADD | ASX | 383 | 38.70 | $14,822 |
| 2026-10-23 15:05 UTC | TRIM | NVDA | -68 | 212.70 | $14,464 |
| 2026-10-22 15:18 UTC | ADD | LRCX | 57 | 234.49 | $13,366 |
| 2026-10-22 15:18 UTC | ADD | AMAT | 46 | 380.67 | $17,511 |
| 2026-10-22 15:18 UTC | TRIM | TSM | -27 | 414.23 | $11,184 |
| 2026-10-21 19:21 UTC | ADD | TSM | 37 | 430.88 | $15,943 |
| 2026-10-21 15:16 UTC | TRIM | KLAC | -68 | 164.22 | $11,167 |
| 2026-10-20 17:08 UTC | BUY (new) | LRCX | 105 | 263.68 | $27,686 |
| 2026-10-20 17:08 UTC | TRIM | AVGO | -34 | 334.29 | $11,366 |
| 2026-10-20 17:08 UTC | TRIM | NVDA | -77 | 216.83 | $16,696 |
| 2026-10-19 15:37 UTC | TRIM | TSM | -25 | 426.75 | $10,669 |
| 2026-10-19 15:37 UTC | TRIM | ASX | -465 | 41.40 | $19,251 |
| 2026-10-19 01:19 UTC | TRIM | 8035.T | -100 | 10,325.00 | $6,537 |
| 2026-10-16 17:25 UTC | ADD | ASX | 558 | 39.86 | $22,242 |
| 2026-10-16 17:25 UTC | TRIM | TSM | -45 | 412.93 | $18,582 |
| 2026-10-16 12:26 UTC | TRIM | IFX.DE | -293 | 52.84 | $17,423 |
| 2026-10-15 15:02 UTC | ADD | ASX | 339 | 41.52 | $14,077 |
| 2026-10-15 15:02 UTC | TRIM | KLAC | -93 | 172.43 | $16,036 |
| 2026-10-15 04:41 UTC | BUY (new) | 6857.T | 100 | 34,860.00 | $22,075 |
| 2026-10-15 04:41 UTC | ADD | 000660.KS | 24 | 1,270,000.00 | $22,625 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 39.9%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
