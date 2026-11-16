---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-16 20:30 UTC (Mon Nov 16, 03:30 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🟢 open (Mon 15:30) · Tokyo 🔴 closed (Tue 05:30) · Korea 🔴 closed (Tue 05:30) · Hong Kong 🔴 closed (Tue 04:30) · Xetra 🔴 closed (Mon 21:30) · Euronext Amsterdam 🔴 closed (Mon 21:30)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$817,072** | $310,234 (38%) | $506,839 (62%) | -18.29% | -74.97% | 🔴 Risk-off (-11.7%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $817,072), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **SK hynix**<br><small>000660.KS</small> | 43 | 1,117,000 KRW | $35,970 | Queued · Korea closed | quality +0.33 · momentum +0.26 · ⚠️ cycle-peak P/E, high σ(e) |
| TRIM | **NVDA**<br><small>NVIDIA</small> | 69 | 155.52 USD | $10,731 | Executed (paper) | analyst α +0.41 · momentum -0.23 · ⚠️ oversold |
| ADD | **ASX**<br><small>ASE Technology</small> | 231 | 32.86 USD | $7,591 | Executed (paper) | momentum +0.41 · quality -0.28 · ⚠️ rich valuation |
| ADD | **INTC**<br><small>Intel</small> | 78 | 55.61 USD | $4,338 | Executed (paper) | analyst α +0.36 · momentum +0.30 · ⚠️ oversold, rich valuation, high σ(e) |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +2.99 | **MU**<br><small>Micron Technology</small> | 719.88 USD | +111% | +9.9% | +271% | -6% | 38 | +0.12 | 10.2% → 10.0% | – | momentum +0.53 · analyst α +0.48 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.26 | **Samsung**<br><small>005930.KS</small> | 195,700 KRW | +144% | +18.9% | +111% | -17% | 38 | -0.26 | 8.2% → 10.0% | – | analyst α +0.85 · momentum +0.20 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.34 | **MRVL**<br><small>Marvell Technology</small> | 145.99 USD | +101% | +7.4% | +161% | -22% | 33 | -0.12 | 4.4% → 5.3% | – | momentum +0.35 · analyst α +0.31 · ⚠️ rich valuation |
| 🟢🟢 Strong Buy | +1.25 | **SK hynix**<br><small>000660.KS</small> | 1,117,000 KRW | – | +0.0% | +118% | -27% | 36 | +0.62 | 9.0% → 4.6% | TRIM 43 | quality +0.33 · momentum +0.26 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +0.83 | **NVDA**<br><small>NVIDIA</small> | 155.52 USD | +111% | +9.8% | +15% | -24% | 23 | +0.47 | 5.1% → 5.1% | TRIM 69 | analyst α +0.41 · momentum -0.23 · ⚠️ oversold |
| 🟢 Buy | +0.67 | **AMAT**<br><small>Applied Materials</small> | 351.85 USD | +82% | +3.2% | +84% | -21% | 39 | +0.03 | 3.6% → 3.5% | – | analyst α +0.15 · momentum +0.14 |
| 🟢 Buy | +0.56 | **ASX**<br><small>ASE Technology</small> | 32.86 USD | +55% | -1.7% | +173% | -4% | 39 | -0.68 | 3.2% → 3.2% | ADD 231 | momentum +0.41 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.44 | **INTC**<br><small>Intel</small> | 55.61 USD | +109% | +9.4% | +150% | -36% | 30 | -0.62 | 1.6% → 1.6% | ADD 78 | analyst α +0.36 · momentum +0.30 · ⚠️ oversold, rich valuation, high σ(e) |
| 🟢 Buy | +0.27 | **LRCX**<br><small>Lam Research</small> | 211.63 USD | +77% | +1.8% | +73% | -25% | 38 | +0.02 | 1.5% → 1.5% | – | analyst α +0.12 · trend -0.10 |
| ⚪ Hold | +0.15 | **TSM**<br><small>TSMC</small> | 373.54 USD | +48% | -5.0% | +48% | -7% | 39 | +0.58 | 5.8% → 5.8% | – | quality +0.28 · analyst α -0.23 |
| ⚪ Hold | +0.08 | **Infineon**<br><small>IFX.DE</small> | 49.11 EUR | +77% | +1.3% | +54% | -15% | 43 | -0.04 | 1.5% → 1.5% | – | analyst α +0.08 · quality -0.04 |
| ⚪ Hold | +0.07 | **Advantest**<br><small>6857.T</small> | 27,200 JPY | +57% | -3.5% | +55% | -7% | 37 | +0.33 | 2.1% → 2.1% | – | analyst α -0.19 · quality +0.16 · ⚠️ rich valuation |
| ⚪ Hold | +0.07 | **KLAC**<br><small>KLA Corp</small> | 144.85 USD | +61% | -1.8% | +43% | -20% | 41 | +0.51 | 4.8% → 4.8% | – | quality +0.24 · momentum -0.10 |
| ⚪ Hold | +0.06 | **TER**<br><small>Teradyne</small> | 233.07 USD | +92% | +5.4% | +92% | -33% | 34 | -0.31 | 1.0% → 1.0% | – | analyst α +0.27 · trend -0.21 |
| ⚪ Hold | -0.07 | **ASML**<br><small>ASML Holding</small> | 1,414.38 USD | +48% | -5.3% | +62% | -11% | 37 | +0.42 | 0.0% → 0.0% | – | analyst α -0.27 · quality +0.18 |
| 🔴 Sell | -0.27 | **AMD**<br><small>Advanced Micro Devices</small> | 504.65 USD | +23% | -12.4% | +113% | +19% | 47 | -0.15 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.32 |
| 🔴 Sell | -0.29 | **Tokyo Electron**<br><small>8035.T</small> | 8,791 JPY | +74% | +1.1% | +60% | -15% | 40 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · analyst α +0.05 |
| 🔴 Sell | -0.38 | **ASMI**<br><small>ASM.AS</small> | 668.00 EUR | +69% | -0.4% | +53% | -18% | 39 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · momentum -0.05 |
| 🔴 Sell | -0.41 | **GFS**<br><small>GlobalFoundries</small> | 39.77 USD | +91% | +5.3% | +43% | -27% | 41 | -0.21 | 0.0% → 0.0% | – | analyst α +0.23 · trend -0.14 |
| 🔴 Sell | -0.41 | **ARM**<br><small>Arm Holdings</small> | 175.73 USD | +64% | -3.2% | +62% | -25% | 37 | +0.04 | 0.0% → 0.0% | – | analyst α -0.15 · trend -0.09 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.52 | **Disco**<br><small>6146.T</small> | 43,990 JPY | +86% | +4.4% | +4% | -32% | 38 | +0.06 | 0.0% → 0.0% | – | momentum -0.26 · analyst α +0.19 |
| 🔴 Sell | -0.56 | **ENTG**<br><small>Entegris</small> | 140.86 USD | +23% | -11.3% | +72% | +1% | 47 | -0.02 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.21 |
| 🔴 Sell | -0.59 | **AMKR**<br><small>Amkor Technology</small> | 34.16 USD | +124% | +13.1% | +32% | -39% | 39 | -1.00 | 0.0% → 0.0% | – | analyst α +0.66 · quality -0.43 |
| 🔴🔴 Strong Sell | -0.91 | **AVGO**<br><small>Broadcom</small> | 332.33 USD | +60% | -2.1% | -3% | -9% | 49 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.12 |
| 🔴🔴 Strong Sell | -0.97 | **SNPS**<br><small>Synopsys</small> | 441.30 USD | +29% | -9.7% | +15% | +0% | 44 | +0.14 | 0.0% → 0.0% | – | analyst α -0.41 · momentum -0.20 |
| 🔴🔴 Strong Sell | -1.00 | **TXN**<br><small>Texas Instruments</small> | 294.50 USD | +10% | -14.1% | +73% | +12% | 50 | +0.24 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.25 |
| 🔴🔴 Strong Sell | -1.02 | **QCOM**<br><small>Qualcomm</small> | 169.90 USD | +14% | -13.3% | +1% | +0% | 47 | +0.70 | 0.0% → 0.0% | – | analyst α -0.66 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.04 | **CDNS**<br><small>Cadence Design Systems</small> | 308.07 USD | +32% | -9.0% | +1% | -6% | 41 | +0.31 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.30 |
| 🔴🔴 Strong Sell | -1.18 | **SMIC**<br><small>0981.HK</small> | 46.08 HKD | +108% | +10.8% | -32% | -30% | 40 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.53 |
| 🔴🔴 Strong Sell | -1.41 | **Shin-Etsu**<br><small>4063.T</small> | 5,629 JPY | +38% | -7.2% | +31% | -11% | 43 | -0.20 | 0.0% → 0.0% | – | analyst α -0.31 · momentum -0.17 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.99"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 719.88 USD (+111%, 46 analysts); de-biased α +9.9% vs CAPM hurdle 14.0%. Downtrend -6% vs 200-day avg; 12-1 mom +271%; RSI 38. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.26"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 195,700 KRW (+144%, 36 analysts); de-biased α +18.9% vs CAPM hurdle 11.3%. Downtrend -17% vs 200-day avg; 12-1 mom +111%; RSI 38. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.34"
    Within rebalance band of target 5.3%: no trade. Analyst target 293.88 USD vs 145.99 USD (+101%, 43 analysts); de-biased α +7.4% vs CAPM hurdle 14.1%. Downtrend -22% vs 200-day avg; 12-1 mom +161%; RSI 33. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.25"
    **TRIM 43 sh** → target 4.6% of NAV (sized ∝ score ÷ σ(e), cap 10%). No reliable analyst target: α set to 0. Downtrend -27% vs 200-day avg; 12-1 mom +118%; RSI 36. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "NVDA (NVDA) — 🟢🟢 Strong Buy, score +0.83"
    **TRIM 69 sh** → target 5.1% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 327.70 USD vs 155.52 USD (+111%, 59 analysts); de-biased α +9.8% vs CAPM hurdle 13.9%. Downtrend -24% vs 200-day avg; 12-1 mom +15%; RSI 23. Quality z +0.47 (ROE 101%). ⚠️ oversold.

??? success "AMAT (AMAT) — 🟢 Buy, score +0.67"
    Within rebalance band of target 3.5%: no trade. Analyst target 638.94 USD vs 351.85 USD (+82%, 36 analysts); de-biased α +3.2% vs CAPM hurdle 11.6%. Downtrend -21% vs 200-day avg; 12-1 mom +84%; RSI 39. Quality z +0.03 (ROE 36%).

??? success "ASX (ASX) — 🟢 Buy, score +0.56"
    **ADD 231 sh** → target 3.2% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 51.00 USD vs 32.86 USD (+55%, 1 analysts); de-biased α -1.7% vs CAPM hurdle 11.9%. Downtrend -4% vs 200-day avg; 12-1 mom +173%; RSI 39. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "INTC (INTC) — 🟢 Buy, score +0.44"
    **ADD 78 sh** → target 1.6% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 116.37 USD vs 55.61 USD (+109%, 43 analysts); de-biased α +9.4% vs CAPM hurdle 14.0%. Downtrend -36% vs 200-day avg; 12-1 mom +150%; RSI 30. Quality z -0.62 (ROE -0%). ⚠️ oversold; price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "LRCX (LRCX) — 🟢 Buy, score +0.27"
    Within rebalance band of target 1.5%: no trade. Analyst target 375.06 USD vs 211.63 USD (+77%, 31 analysts); de-biased α +1.8% vs CAPM hurdle 12.6%. Downtrend -25% vs 200-day avg; 12-1 mom +73%; RSI 38. Quality z +0.02 (ROE 65%).

??? note "TSM (TSM) — ⚪ Hold, score +0.15"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 373.54 USD (+48%, 20 analysts); de-biased α -5.0% vs CAPM hurdle 10.8%. Downtrend -7% vs 200-day avg; 12-1 mom +48%; RSI 39. Quality z +0.58 (ROE 35%).

??? note "Infineon (IFX.DE) — ⚪ Hold, score +0.08"
    Hold zone: keep any existing position, no new money. Analyst target 86.74 EUR vs 49.11 EUR (+77%, 23 analysts); de-biased α +1.3% vs CAPM hurdle 14.1%. Downtrend -15% vs 200-day avg; 12-1 mom +54%; RSI 43. Quality z -0.04 (ROE 6%).

??? note "Advantest (6857.T) — ⚪ Hold, score +0.07"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 27,200 JPY (+57%, 21 analysts); de-biased α -3.5% vs CAPM hurdle 13.4%. Downtrend -7% vs 200-day avg; 12-1 mom +55%; RSI 37. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.07"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 144.85 USD (+61%, 26 analysts); de-biased α -1.8% vs CAPM hurdle 11.1%. Downtrend -20% vs 200-day avg; 12-1 mom +43%; RSI 41. Quality z +0.51 (ROE 87%).

??? note "TER (TER) — ⚪ Hold, score +0.06"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 233.07 USD (+92%, 15 analysts); de-biased α +5.4% vs CAPM hurdle 12.3%. Downtrend -33% vs 200-day avg; 12-1 mom +92%; RSI 34. Quality z -0.31 (ROE 20%).

??? note "ASML (ASML) — ⚪ Hold, score -0.07"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,414.38 USD (+48%, 16 analysts); de-biased α -5.3% vs CAPM hurdle 12.3%. Downtrend -11% vs 200-day avg; 12-1 mom +62%; RSI 37. Quality z +0.42 (ROE 50%).

??? failure "AMD (AMD) — 🔴 Sell, score -0.27"
    Avoid: not owned. Analyst target 619.51 USD vs 504.65 USD (+23%, 50 analysts); de-biased α -12.4% vs CAPM hurdle 14.9%. Uptrend +19% vs 200-day avg; 12-1 mom +113%; RSI 47. Quality z -0.15 (ROE 7%).

??? failure "Tokyo Electron (8035.T) — 🔴 Sell, score -0.29"
    Avoid: not owned. Analyst target 15,275 JPY vs 8,791 JPY (+74%, 23 analysts); de-biased α +1.1% vs CAPM hurdle 12.8%. Downtrend -15% vs 200-day avg; 12-1 mom +60%; RSI 40. Quality z -0.28 (ROE 29%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.38"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 668.00 EUR (+69%, 19 analysts); de-biased α -0.4% vs CAPM hurdle 13.2%. Downtrend -18% vs 200-day avg; 12-1 mom +53%; RSI 39. Quality z -0.10 (ROE 19%).

??? failure "GFS (GFS) — 🔴 Sell, score -0.41"
    Avoid: not owned. Analyst target 76.00 USD vs 39.77 USD (+91%, 22 analysts); de-biased α +5.3% vs CAPM hurdle 12.4%. Downtrend -27% vs 200-day avg; 12-1 mom +43%; RSI 41. Quality z -0.21 (ROE 8%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.41"
    Avoid: not owned. Analyst target 288.70 USD vs 175.73 USD (+64%, 40 analysts); de-biased α -3.2% vs CAPM hurdle 19.6%. Downtrend -25% vs 200-day avg; 12-1 mom +62%; RSI 37. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "Disco (6146.T) — 🔴 Sell, score -0.52"
    Avoid: not owned. Analyst target 81,730 JPY vs 43,990 JPY (+86%, 20 analysts); de-biased α +4.4% vs CAPM hurdle 11.5%. Downtrend -32% vs 200-day avg; 12-1 mom +4%; RSI 38. Quality z +0.06 (ROE 25%).

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.56"
    Avoid: not owned. Analyst target 173.36 USD vs 140.86 USD (+23%, 11 analysts); de-biased α -11.3% vs CAPM hurdle 11.0%. Uptrend +1% vs 200-day avg; 12-1 mom +72%; RSI 47. Quality z -0.02 (ROE 6%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.59"
    Avoid: not owned. Analyst target 76.40 USD vs 34.16 USD (+124%, 10 analysts); de-biased α +13.1% vs CAPM hurdle 14.0%. Downtrend -39% vs 200-day avg; 12-1 mom +32%; RSI 39. Quality z -1.00 (ROE 9%).

??? failure "AVGO (AVGO) — 🔴🔴 Strong Sell, score -0.91"
    Avoid: not owned. Analyst target 531.31 USD vs 332.33 USD (+60%, 47 analysts); de-biased α -2.1% vs CAPM hurdle 11.2%. Downtrend -9% vs 200-day avg; 12-1 mom -3%; RSI 49. Quality z +0.26 (ROE 31%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.97"
    Avoid: not owned. Analyst target 569.78 USD vs 441.30 USD (+29%, 26 analysts); de-biased α -9.7% vs CAPM hurdle 10.3%. Uptrend +0% vs 200-day avg; 12-1 mom +15%; RSI 44. Quality z +0.14 (ROE 7%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -1.00"
    Avoid: not owned. Analyst target 324.71 USD vs 294.50 USD (+10%, 31 analysts); de-biased α -14.1% vs CAPM hurdle 10.8%. Uptrend +12% vs 200-day avg; 12-1 mom +73%; RSI 50. Quality z +0.24 (ROE 30%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.02"
    Avoid: not owned. Analyst target 194.13 USD vs 169.90 USD (+14%, 30 analysts); de-biased α -13.3% vs CAPM hurdle 11.9%. Uptrend +0% vs 200-day avg; 12-1 mom +1%; RSI 47. Quality z +0.70 (ROE 23%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.04"
    Avoid: not owned. Analyst target 405.47 USD vs 308.07 USD (+32%, 26 analysts); de-biased α -9.0% vs CAPM hurdle 10.0%. Downtrend -6% vs 200-day avg; 12-1 mom +1%; RSI 41. Quality z +0.31 (ROE 22%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.18"
    Avoid: not owned. Analyst target 95.99 HKD vs 46.08 HKD (+108%, 21 analysts); de-biased α +10.8% vs CAPM hurdle 7.3%. Downtrend -30% vs 200-day avg; 12-1 mom -32%; RSI 40. Quality z -0.99 (ROE 3%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.41"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,629 JPY (+38%, 17 analysts); de-biased α -7.2% vs CAPM hurdle 10.8%. Downtrend -11% vs 200-day avg; 12-1 mom +31%; RSI 43. Quality z -0.20 (ROE 10%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 116 | 719.88 USD | $83,506 | 10.2% | Strong Buy |
| 000660.KS | SK hynix | 88 | 1,117,000 KRW | $73,614 | 9.0% | Strong Buy |
| 005930.KS | Samsung Electronics | 458 | 195,700 KRW | $67,124 | 8.2% | Strong Buy |
| TSM | TSMC | 127 | 373.54 USD | $47,440 | 5.8% | Hold |
| NVDA | NVIDIA | 268 | 155.52 USD | $41,679 | 5.1% | Strong Buy |
| KLAC | KLA Corp | 268 | 144.85 USD | $38,820 | 4.8% | Hold |
| MRVL | Marvell Technology | 248 | 145.99 USD | $36,207 | 4.4% | Strong Buy |
| AMAT | Applied Materials | 84 | 351.85 USD | $29,555 | 3.6% | Buy |
| ASX | ASE Technology | 805 | 32.86 USD | $26,452 | 3.2% | Buy |
| 6857.T | Advantest | 100 | 27,200 JPY | $17,060 | 2.1% | Hold |
| INTC | Intel | 230 | 55.61 USD | $12,790 | 1.6% | Buy |
| LRCX | Lam Research | 58 | 211.63 USD | $12,275 | 1.5% | Buy |
| IFX.DE | Infineon Technologies | 225 | 49.11 EUR | $12,159 | 1.5% | Hold |
| TER | Teradyne | 35 | 233.07 USD | $8,157 | 1.0% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-11-16 20:30 UTC | ADD | ASX | 231 | 32.86 | $7,591 |
| 2026-11-16 20:30 UTC | ADD | INTC | 78 | 55.61 | $4,338 |
| 2026-11-16 20:30 UTC | TRIM | NVDA | -69 | 155.52 | $10,731 |
| 2026-11-13 16:26 UTC | ADD | NVDA | 79 | 159.94 | $12,635 |
| 2026-11-13 16:26 UTC | ADD | AMAT | 23 | 357.03 | $8,212 |
| 2026-11-13 16:26 UTC | TRIM | ASX | -290 | 34.86 | $10,109 |
| 2026-11-13 00:26 UTC | TRIM | 005930.KS | -104 | 214,000.00 | $16,663 |
| 2026-11-12 18:57 UTC | ADD | NVDA | 79 | 164.84 | $13,022 |
| 2026-11-12 18:57 UTC | ADD | AMAT | 20 | 386.98 | $7,740 |
| 2026-11-11 15:13 UTC | TRIM | AMAT | -32 | 387.02 | $12,385 |
| 2026-11-11 15:13 UTC | TRIM | MRVL | -76 | 165.15 | $12,551 |
| 2026-11-11 15:13 UTC | TRIM | INTC | -83 | 61.66 | $5,118 |
| 2026-11-11 06:23 UTC | ADD | 000660.KS | 38 | 1,277,000.00 | $36,371 |
| 2026-11-10 17:51 UTC | ADD | ASX | 552 | 34.76 | $19,188 |
| 2026-11-10 17:51 UTC | TRIM | INTC | -140 | 57.20 | $8,008 |
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

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 57.7%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
