---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-05 15:28 UTC (Thu Nov 05, 10:28 AM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🟢 open (Thu 10:28) · Tokyo 🔴 closed (Fri 00:28) · Korea 🔴 closed (Fri 00:28) · Hong Kong 🔴 closed (Thu 23:28) · Xetra 🟢 open (Thu 16:28) · Euronext Amsterdam 🟢 open (Thu 16:28)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$817,807** | $309,310 (38%) | $508,498 (62%) | -18.22% | -75.97% | 🔴 Risk-off (-71.5%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $817,807), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| ADD | **MU**<br><small>Micron Technology</small> | 52 | 693.52 USD | $36,063 | Executed (paper) | momentum +0.53 · analyst α +0.48 · ⚠️ oversold, cycle-peak P/E |
| ADD | **Samsung**<br><small>005930.KS</small> | 180 | 199,900 KRW | $26,612 | Queued · Korea closed | analyst α +0.66 · momentum +0.23 · ⚠️ cycle-peak P/E |
| TRIM | **SK hynix**<br><small>000660.KS</small> | 27 | 1,255,000 KRW | $25,061 | Queued · Korea closed | momentum +0.41 · quality +0.33 · ⚠️ cycle-peak P/E, high σ(e) |
| ADD | **MRVL**<br><small>Marvell Technology</small> | 160 | 140.70 USD | $22,512 | Executed (paper) | analyst α +0.41 · momentum +0.35 · ⚠️ oversold, rich valuation |
| TRIM | **LRCX**<br><small>Lam Research</small> | 104 | 195.72 USD | $20,355 | Executed (paper) | analyst α +0.15 · trend -0.14 · ⚠️ oversold |
| TRIM | **Advantest**<br><small>6857.T</small> | 100 | 29,375 JPY | $18,601 | Queued · Tokyo closed | analyst α -0.31 · trend +0.25 · ⚠️ rich valuation |
| ADD | **INTC**<br><small>Intel</small> | 309 | 52.94 USD | $16,359 | Executed (paper) | analyst α +0.55 · momentum +0.30 · ⚠️ oversold, rich valuation, high σ(e) |
| ADD | **AMAT**<br><small>Applied Materials</small> | 21 | 332.95 USD | $6,992 | Executed (paper) | analyst α +0.19 · momentum +0.12 · ⚠️ oversold |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +2.78 | **MU**<br><small>Micron Technology</small> | 693.52 USD | +119% | +10.5% | +400% | -8% | 29 | +0.12 | 9.8% → 9.9% | ADD 52 | momentum +0.53 · analyst α +0.48 · ⚠️ oversold, cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.80 | **Samsung**<br><small>005930.KS</small> | 199,900 KRW | +139% | +16.3% | +182% | -15% | 35 | -0.26 | 5.8% → 9.1% | ADD 180 | analyst α +0.66 · momentum +0.23 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.73 | **SK hynix**<br><small>000660.KS</small> | 1,255,000 KRW | – | +0.0% | +249% | -17% | 38 | +0.62 | 9.1% → 5.9% | TRIM 27 | momentum +0.41 · quality +0.33 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +1.51 | **MRVL**<br><small>Marvell Technology</small> | 140.70 USD | +109% | +7.9% | +225% | -24% | 24 | -0.12 | 5.6% → 5.6% | ADD 160 | analyst α +0.41 · momentum +0.35 · ⚠️ oversold, rich valuation |
| 🟢🟢 Strong Buy | +0.88 | **INTC**<br><small>Intel</small> | 52.94 USD | +120% | +10.7% | +205% | -39% | 21 | -0.62 | 2.9% → 2.9% | ADD 309 | analyst α +0.55 · momentum +0.30 · ⚠️ oversold, rich valuation, high σ(e) |
| 🟢 Buy | +0.60 | **AMAT**<br><small>Applied Materials</small> | 332.95 USD | +92% | +4.4% | +127% | -25% | 28 | +0.03 | 2.9% → 2.9% | ADD 21 | analyst α +0.19 · momentum +0.12 · ⚠️ oversold |
| 🟢 Buy | +0.56 | **Advantest**<br><small>6857.T</small> | 29,375 JPY | +45% | -7.7% | +132% | +1% | 37 | +0.33 | 4.5% → 2.2% | TRIM 100 | analyst α -0.31 · trend +0.25 · ⚠️ rich valuation |
| 🟢 Buy | +0.26 | **LRCX**<br><small>Lam Research</small> | 195.72 USD | +92% | +4.1% | +112% | -31% | 24 | +0.02 | 1.4% → 1.4% | TRIM 104 | analyst α +0.15 · trend -0.14 · ⚠️ oversold |
| ⚪ Hold | +0.15 | **TSM**<br><small>TSMC</small> | 363.97 USD | +52% | -5.3% | +62% | -9% | 28 | +0.58 | 5.7% → 5.7% | – | quality +0.28 · analyst α -0.19 · ⚠️ oversold |
| ⚪ Hold | +0.09 | **AMD**<br><small>Advanced Micro Devices</small> | 417.64 USD | +48% | -7.4% | +158% | +1% | 31 | -0.15 | 0.0% → 0.0% | – | analyst α -0.27 · trend +0.21 |
| ⚪ Hold | +0.08 | **Infineon**<br><small>IFX.DE</small> | 45.90 EUR | +89% | +3.1% | +81% | -20% | 33 | -0.04 | 1.4% → 1.4% | – | analyst α +0.12 · quality -0.04 |
| ⚪ Hold | +0.03 | **TER**<br><small>Teradyne</small> | 223.65 USD | +100% | +6.1% | +135% | -36% | 23 | -0.31 | 1.0% → 1.0% | – | analyst α +0.23 · quality -0.21 · ⚠️ oversold |
| ⚪ Hold | -0.01 | **KLAC**<br><small>KLA Corp</small> | 135.95 USD | +72% | -0.5% | +66% | -25% | 30 | +0.51 | 4.5% → 4.5% | – | quality +0.24 · trend -0.09 |
| ⚪ Hold | -0.03 | **AMKR**<br><small>Amkor Technology</small> | 31.58 USD | +142% | +16.4% | +49% | -44% | 28 | -1.00 | 0.0% → 0.0% | – | analyst α +0.85 · quality -0.43 · ⚠️ oversold |
| ⚪ Hold | -0.04 | **ASX**<br><small>ASE Technology</small> | 31.84 USD | +60% | -1.7% | +201% | -5% | 31 | -0.68 | 1.2% → 1.2% | – | quality -0.28 · momentum +0.26 · ⚠️ rich valuation |
| ⚪ Hold | -0.11 | **NVDA**<br><small>NVIDIA</small> | 185.39 USD | +77% | -0.0% | +20% | -9% | 27 | +0.47 | 1.4% → 1.4% | – | momentum -0.26 · quality +0.21 · ⚠️ oversold |
| ⚪ Hold | -0.12 | **ASML**<br><small>ASML Holding</small> | 1,386.63 USD | +51% | -5.9% | +76% | -13% | 28 | +0.42 | 5.1% → 5.1% | – | analyst α -0.23 · quality +0.18 · ⚠️ oversold |
| ⚪ Hold | -0.17 | **ASMI**<br><small>ASM.AS</small> | 630.80 EUR | +79% | +0.7% | +69% | -22% | 29 | -0.10 | 0.0% → 0.0% | – | analyst α +0.08 · quality -0.06 · ⚠️ oversold |
| ⚪ Hold | -0.20 | **Tokyo Electron**<br><small>8035.T</small> | 8,690 JPY | +76% | +0.3% | +111% | -16% | 35 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · momentum +0.07 |
| ⚪ Hold | -0.22 | **Disco**<br><small>6146.T</small> | 41,150 JPY | +99% | +6.2% | +22% | -37% | 27 | +0.06 | 0.0% → 0.0% | – | analyst α +0.27 · trend -0.21 · ⚠️ oversold |
| 🔴 Sell | -0.29 | **GFS**<br><small>GlobalFoundries</small> | 37.44 USD | +103% | +6.9% | +40% | -32% | 30 | -0.21 | 0.0% → 0.0% | – | analyst α +0.31 · trend -0.16 · ⚠️ oversold |
| 🔴 Sell | -0.37 | **AVGO**<br><small>Broadcom</small> | 301.40 USD | +76% | +0.7% | +8% | -18% | 34 | +0.26 | 0.0% → 0.0% | – | momentum -0.30 · quality +0.11 |
| 🔴 Sell | -0.53 | **ARM**<br><small>Arm Holdings</small> | 168.10 USD | +72% | -2.7% | +83% | -27% | 27 | +0.04 | 0.0% → 0.0% | – | analyst α -0.15 · trend -0.10 · ⚠️ oversold, rich valuation, high σ(e) |
| 🔴 Sell | -0.61 | **ENTG**<br><small>Entegris</small> | 132.72 USD | +31% | -10.8% | +93% | -4% | 40 | -0.02 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.14 |
| 🔴🔴 Strong Sell | -0.98 | **TXN**<br><small>Texas Instruments</small> | 291.94 USD | +11% | -15.2% | +84% | +13% | 51 | +0.24 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -1.26 | **SNPS**<br><small>Synopsys</small> | 444.88 USD | +28% | -11.3% | +21% | +1% | 45 | +0.14 | 0.0% → 0.0% | – | analyst α -0.55 · momentum -0.23 |
| 🔴🔴 Strong Sell | -1.28 | **CDNS**<br><small>Cadence Design Systems</small> | 314.36 USD | +29% | -11.0% | +7% | -4% | 43 | +0.31 | 0.0% → 0.0% | – | analyst α -0.48 · momentum -0.35 |
| 🔴🔴 Strong Sell | -1.31 | **QCOM**<br><small>Qualcomm</small> | 154.99 USD | +25% | -11.9% | +5% | -8% | 37 | +0.70 | 0.0% → 0.0% | – | analyst α -0.66 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.45 | **Shin-Etsu**<br><small>4063.T</small> | 5,710 JPY | +36% | -9.0% | +28% | -10% | 38 | -0.20 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.17 |
| 🔴🔴 Strong Sell | -1.49 | **SMIC**<br><small>0981.HK</small> | 47.50 HKD | +102% | +7.9% | -26% | -29% | 40 | -0.99 | 0.0% → 0.0% | – | momentum -0.53 · analyst α +0.36 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.78"
    **ADD 52 sh** → target 9.9% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 1,520.02 USD vs 693.52 USD (+119%, 46 analysts); de-biased α +10.5% vs CAPM hurdle 14.0%. Downtrend -8% vs 200-day avg; 12-1 mom +400%; RSI 29. Quality z +0.12 (ROE 17%). ⚠️ oversold; cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.80"
    **ADD 180 sh** → target 9.1% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 477,517 KRW vs 199,900 KRW (+139%, 36 analysts); de-biased α +16.3% vs CAPM hurdle 11.3%. Downtrend -15% vs 200-day avg; 12-1 mom +182%; RSI 35. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.73"
    **TRIM 27 sh** → target 5.9% of NAV (sized ∝ score ÷ σ(e), cap 10%). No reliable analyst target: α set to 0. Downtrend -17% vs 200-day avg; 12-1 mom +249%; RSI 38. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.51"
    **ADD 160 sh** → target 5.6% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 293.88 USD vs 140.70 USD (+109%, 43 analysts); de-biased α +7.9% vs CAPM hurdle 14.1%. Downtrend -24% vs 200-day avg; 12-1 mom +225%; RSI 24. Quality z -0.12 (ROE 19%). ⚠️ oversold; price implies 78% stage-1 growth (reverse DCF).

??? success "INTC (INTC) — 🟢🟢 Strong Buy, score +0.88"
    **ADD 309 sh** → target 2.9% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 116.37 USD vs 52.94 USD (+120%, 43 analysts); de-biased α +10.7% vs CAPM hurdle 14.0%. Downtrend -39% vs 200-day avg; 12-1 mom +205%; RSI 21. Quality z -0.62 (ROE -0%). ⚠️ oversold; price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "AMAT (AMAT) — 🟢 Buy, score +0.60"
    **ADD 21 sh** → target 2.9% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 332.95 USD (+92%, 36 analysts); de-biased α +4.4% vs CAPM hurdle 11.6%. Downtrend -25% vs 200-day avg; 12-1 mom +127%; RSI 28. Quality z +0.03 (ROE 36%). ⚠️ oversold.

??? success "Advantest (6857.T) — 🟢 Buy, score +0.56"
    **TRIM 100 sh** → target 2.2% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 42,686 JPY vs 29,375 JPY (+45%, 21 analysts); de-biased α -7.7% vs CAPM hurdle 13.4%. Uptrend +1% vs 200-day avg; 12-1 mom +132%; RSI 37. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? success "LRCX (LRCX) — 🟢 Buy, score +0.26"
    **TRIM 104 sh** → target 1.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 375.06 USD vs 195.72 USD (+92%, 31 analysts); de-biased α +4.1% vs CAPM hurdle 12.6%. Downtrend -31% vs 200-day avg; 12-1 mom +112%; RSI 24. Quality z +0.02 (ROE 65%). ⚠️ oversold.

??? note "TSM (TSM) — ⚪ Hold, score +0.15"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 363.97 USD (+52%, 20 analysts); de-biased α -5.3% vs CAPM hurdle 10.8%. Downtrend -9% vs 200-day avg; 12-1 mom +62%; RSI 28. Quality z +0.58 (ROE 35%). ⚠️ oversold.

??? note "AMD (AMD) — ⚪ Hold, score +0.09"
    Hold zone: not owned, no entry. Analyst target 619.51 USD vs 417.64 USD (+48%, 50 analysts); de-biased α -7.4% vs CAPM hurdle 14.9%. Uptrend +1% vs 200-day avg; 12-1 mom +158%; RSI 31. Quality z -0.15 (ROE 7%).

??? note "Infineon (IFX.DE) — ⚪ Hold, score +0.08"
    Hold zone: keep any existing position, no new money. Analyst target 86.74 EUR vs 45.90 EUR (+89%, 23 analysts); de-biased α +3.1% vs CAPM hurdle 14.1%. Downtrend -20% vs 200-day avg; 12-1 mom +81%; RSI 33. Quality z -0.04 (ROE 6%).

??? note "TER (TER) — ⚪ Hold, score +0.03"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 223.65 USD (+100%, 15 analysts); de-biased α +6.1% vs CAPM hurdle 12.3%. Downtrend -36% vs 200-day avg; 12-1 mom +135%; RSI 23. Quality z -0.31 (ROE 20%). ⚠️ oversold.

??? note "KLAC (KLAC) — ⚪ Hold, score -0.01"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 135.95 USD (+72%, 26 analysts); de-biased α -0.5% vs CAPM hurdle 11.1%. Downtrend -25% vs 200-day avg; 12-1 mom +66%; RSI 30. Quality z +0.51 (ROE 87%).

??? note "AMKR (AMKR) — ⚪ Hold, score -0.03"
    Hold zone: not owned, no entry. Analyst target 76.40 USD vs 31.58 USD (+142%, 10 analysts); de-biased α +16.4% vs CAPM hurdle 14.0%. Downtrend -44% vs 200-day avg; 12-1 mom +49%; RSI 28. Quality z -1.00 (ROE 9%). ⚠️ oversold.

??? note "ASX (ASX) — ⚪ Hold, score -0.04"
    Hold zone: keep any existing position, no new money. Analyst target 51.00 USD vs 31.84 USD (+60%, 1 analysts); de-biased α -1.7% vs CAPM hurdle 11.9%. Downtrend -5% vs 200-day avg; 12-1 mom +201%; RSI 31. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? note "NVDA (NVDA) — ⚪ Hold, score -0.11"
    Hold zone: keep any existing position, no new money. Analyst target 327.70 USD vs 185.39 USD (+77%, 59 analysts); de-biased α -0.0% vs CAPM hurdle 13.9%. Downtrend -9% vs 200-day avg; 12-1 mom +20%; RSI 27. Quality z +0.47 (ROE 101%). ⚠️ oversold.

??? note "ASML (ASML) — ⚪ Hold, score -0.12"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,386.63 USD (+51%, 16 analysts); de-biased α -5.9% vs CAPM hurdle 12.3%. Downtrend -13% vs 200-day avg; 12-1 mom +76%; RSI 28. Quality z +0.42 (ROE 50%). ⚠️ oversold.

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.17"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 630.80 EUR (+79%, 19 analysts); de-biased α +0.7% vs CAPM hurdle 13.2%. Downtrend -22% vs 200-day avg; 12-1 mom +69%; RSI 29. Quality z -0.10 (ROE 19%). ⚠️ oversold.

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score -0.20"
    Hold zone: not owned, no entry. Analyst target 15,275 JPY vs 8,690 JPY (+76%, 23 analysts); de-biased α +0.3% vs CAPM hurdle 12.8%. Downtrend -16% vs 200-day avg; 12-1 mom +111%; RSI 35. Quality z -0.28 (ROE 29%).

??? note "Disco (6146.T) — ⚪ Hold, score -0.22"
    Hold zone: not owned, no entry. Analyst target 81,730 JPY vs 41,150 JPY (+99%, 20 analysts); de-biased α +6.2% vs CAPM hurdle 11.5%. Downtrend -37% vs 200-day avg; 12-1 mom +22%; RSI 27. Quality z +0.06 (ROE 25%). ⚠️ oversold.

??? failure "GFS (GFS) — 🔴 Sell, score -0.29"
    Avoid: not owned. Analyst target 76.00 USD vs 37.44 USD (+103%, 22 analysts); de-biased α +6.9% vs CAPM hurdle 12.4%. Downtrend -32% vs 200-day avg; 12-1 mom +40%; RSI 30. Quality z -0.21 (ROE 8%). ⚠️ oversold.

??? failure "AVGO (AVGO) — 🔴 Sell, score -0.37"
    Avoid: not owned. Analyst target 531.31 USD vs 301.40 USD (+76%, 47 analysts); de-biased α +0.7% vs CAPM hurdle 11.2%. Downtrend -18% vs 200-day avg; 12-1 mom +8%; RSI 34. Quality z +0.26 (ROE 31%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.53"
    Avoid: not owned. Analyst target 288.70 USD vs 168.10 USD (+72%, 40 analysts); de-biased α -2.7% vs CAPM hurdle 19.6%. Downtrend -27% vs 200-day avg; 12-1 mom +83%; RSI 27. Quality z +0.04 (ROE 12%). ⚠️ oversold; price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.61"
    Avoid: not owned. Analyst target 173.36 USD vs 132.72 USD (+31%, 11 analysts); de-biased α -10.8% vs CAPM hurdle 11.0%. Downtrend -4% vs 200-day avg; 12-1 mom +93%; RSI 40. Quality z -0.02 (ROE 6%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -0.98"
    Avoid: not owned. Analyst target 324.71 USD vs 291.94 USD (+11%, 31 analysts); de-biased α -15.2% vs CAPM hurdle 10.8%. Uptrend +13% vs 200-day avg; 12-1 mom +84%; RSI 51. Quality z +0.24 (ROE 30%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.26"
    Avoid: not owned. Analyst target 569.78 USD vs 444.88 USD (+28%, 26 analysts); de-biased α -11.3% vs CAPM hurdle 10.3%. Uptrend +1% vs 200-day avg; 12-1 mom +21%; RSI 45. Quality z +0.14 (ROE 7%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.28"
    Avoid: not owned. Analyst target 405.47 USD vs 314.36 USD (+29%, 26 analysts); de-biased α -11.0% vs CAPM hurdle 10.0%. Downtrend -4% vs 200-day avg; 12-1 mom +7%; RSI 43. Quality z +0.31 (ROE 22%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.31"
    Avoid: not owned. Analyst target 194.13 USD vs 154.99 USD (+25%, 30 analysts); de-biased α -11.9% vs CAPM hurdle 11.9%. Downtrend -8% vs 200-day avg; 12-1 mom +5%; RSI 37. Quality z +0.70 (ROE 23%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.45"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,710 JPY (+36%, 17 analysts); de-biased α -9.0% vs CAPM hurdle 10.8%. Downtrend -10% vs 200-day avg; 12-1 mom +28%; RSI 38. Quality z -0.20 (ROE 10%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.49"
    Avoid: not owned. Analyst target 95.99 HKD vs 47.50 HKD (+102%, 21 analysts); de-biased α +7.9% vs CAPM hurdle 7.3%. Downtrend -29% vs 200-day avg; 12-1 mom -26%; RSI 40. Quality z -0.99 (ROE 3%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 116 | 693.52 USD | $80,448 | 9.8% | Strong Buy |
| 000660.KS | SK hynix | 80 | 1,255,000 KRW | $74,256 | 9.1% | Strong Buy |
| 005930.KS | Samsung Electronics | 322 | 199,900 KRW | $47,607 | 5.8% | Strong Buy |
| TSM | TSMC | 127 | 363.97 USD | $46,224 | 5.7% | Hold |
| MRVL | Marvell Technology | 324 | 140.70 USD | $45,586 | 5.6% | Strong Buy |
| ASML | ASML Holding | 30 | 1,386.63 USD | $41,599 | 5.1% | Hold |
| 6857.T | Advantest | 200 | 29,375 JPY | $37,202 | 4.5% | Buy |
| KLAC | KLA Corp | 268 | 135.95 USD | $36,435 | 4.5% | Hold |
| INTC | Intel | 447 | 52.94 USD | $23,665 | 2.9% | Strong Buy |
| AMAT | Applied Materials | 71 | 332.95 USD | $23,640 | 2.9% | Buy |
| IFX.DE | Infineon Technologies | 225 | 45.90 EUR | $11,597 | 1.4% | Hold |
| LRCX | Lam Research | 58 | 195.72 USD | $11,352 | 1.4% | Buy |
| NVDA | NVIDIA | 60 | 185.39 USD | $11,123 | 1.4% | Hold |
| ASX | ASE Technology | 312 | 31.84 USD | $9,936 | 1.2% | Hold |
| TER | Teradyne | 35 | 223.65 USD | $7,828 | 1.0% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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
| 2026-10-30 19:24 UTC | TRIM | MRVL | -139 | 193.20 | $26,855 |
| 2026-10-30 19:24 UTC | TRIM | INTC | -391 | 63.40 | $24,787 |
| 2026-10-30 19:24 UTC | TRIM | ASX | -1,008 | 38.89 | $39,201 |
| 2026-10-30 14:10 UTC | BUY (new) | INTC | 521 | 65.38 | $34,063 |
| 2026-10-30 14:10 UTC | TRIM | AMAT | -33 | 399.62 | $13,187 |
| 2026-10-29 14:21 UTC | BUY (new) | MRVL | 218 | 219.82 | $47,921 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 63.0%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
