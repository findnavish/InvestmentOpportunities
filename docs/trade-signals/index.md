---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-06 02:27 UTC (Thu Nov 05, 09:27 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Thu 21:27) · Tokyo 🟢 open (Fri 11:27) · Korea 🟢 open (Fri 11:27) · Hong Kong 🟢 open (Fri 10:27) · Xetra 🔴 closed (Fri 03:27) · Euronext Amsterdam 🔴 closed (Fri 03:27)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$794,235** | $318,748 (40%) | $475,487 (60%) | -20.58% | -76.85% | 🔴 Risk-off (-17.8%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $794,235), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| ADD | **Samsung**<br><small>005930.KS</small> | 240 | 191,400 KRW | $33,864 | Executed (paper) | analyst α +0.85 · momentum +0.23 · ⚠️ cycle-peak P/E |
| TRIM | **SK hynix**<br><small>000660.KS</small> | 30 | 1,169,000 KRW | $25,854 | Executed (paper) | momentum +0.35 · quality +0.33 · ⚠️ cycle-peak P/E, high σ(e) |
| TRIM | **KLAC**<br><small>KLA Corp</small> | 151 | 129.63 USD | $19,574 | Queued · NYSE/Nasdaq closed | quality +0.24 · trend -0.10 · ⚠️ oversold |
| TRIM | **Advantest**<br><small>6857.T</small> | 100 | 27,610 JPY | $17,487 | Executed (paper) | analyst α -0.27 · momentum +0.17 · ⚠️ rich valuation |
| ADD | **LRCX**<br><small>Lam Research</small> | 56 | 184.59 USD | $10,337 | Queued · NYSE/Nasdaq closed | analyst α +0.27 · trend -0.16 · ⚠️ oversold |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +2.79 | **MU**<br><small>Micron Technology</small> | 658.70 USD | +131% | +12.5% | +400% | -13% | 27 | +0.12 | 9.6% → 10.0% | – | analyst α +0.66 · momentum +0.53 · ⚠️ oversold, cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.98 | **Samsung**<br><small>005930.KS</small> | 191,400 KRW | +149% | +18.0% | +170% | -19% | 33 | -0.26 | 10.0% → 10.0% | ADD 240 | analyst α +0.85 · momentum +0.23 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.58 | **MRVL**<br><small>Marvell Technology</small> | 133.32 USD | +120% | +9.9% | +225% | -28% | 23 | -0.12 | 5.4% → 6.7% | – | analyst α +0.48 · momentum +0.41 · ⚠️ oversold, rich valuation |
| 🟢🟢 Strong Buy | +1.35 | **SK hynix**<br><small>000660.KS</small> | 1,169,000 KRW | – | +0.0% | +223% | -22% | 34 | +0.62 | 5.4% → 5.3% | TRIM 30 | momentum +0.35 · quality +0.33 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +0.78 | **INTC**<br><small>Intel</small> | 52.12 USD | +123% | +10.6% | +205% | -40% | 21 | -0.62 | 2.9% → 2.9% | – | analyst α +0.55 · momentum +0.30 · ⚠️ oversold, rich valuation, high σ(e) |
| 🟢 Buy | +0.50 | **AMAT**<br><small>Applied Materials</small> | 319.33 USD | +100% | +5.5% | +127% | -28% | 26 | +0.03 | 2.9% → 2.8% | – | analyst α +0.19 · momentum +0.12 · ⚠️ oversold |
| 🟢 Buy | +0.45 | **Advantest**<br><small>6857.T</small> | 27,610 JPY | +55% | -6.3% | +145% | -5% | 34 | +0.33 | 2.2% → 2.0% | TRIM 100 | analyst α -0.27 · momentum +0.17 · ⚠️ rich valuation |
| 🟢 Buy | +0.43 | **LRCX**<br><small>Lam Research</small> | 184.59 USD | +103% | +6.0% | +112% | -35% | 23 | +0.02 | 1.3% → 2.7% | ADD 56 | analyst α +0.27 · trend -0.16 · ⚠️ oversold |
| 🟢 Buy | +0.31 | **KLAC**<br><small>KLA Corp</small> | 129.63 USD | +80% | +0.7% | +66% | -29% | 28 | +0.51 | 4.4% → 1.9% | TRIM 151 | quality +0.24 · trend -0.10 · ⚠️ oversold |
| ⚪ Hold | +0.20 | **Infineon**<br><small>IFX.DE</small> | 45.90 EUR | +89% | +2.2% | +81% | -20% | 33 | -0.04 | 1.5% → 1.5% | – | analyst α +0.15 · quality -0.04 |
| ⚪ Hold | +0.19 | **TER**<br><small>Teradyne</small> | 212.66 USD | +110% | +7.8% | +135% | -39% | 22 | -0.31 | 0.9% → 0.9% | – | analyst α +0.36 · trend -0.21 · ⚠️ oversold |
| ⚪ Hold | +0.13 | **TSM**<br><small>TSMC</small> | 352.03 USD | +57% | -5.0% | +62% | -12% | 26 | +0.58 | 5.6% → 5.6% | – | quality +0.28 · analyst α -0.19 · ⚠️ oversold |
| ⚪ Hold | -0.00 | **NVDA**<br><small>NVIDIA</small> | 181.60 USD | +80% | -0.0% | +20% | -11% | 25 | +0.47 | 1.4% → 1.4% | – | momentum -0.26 · quality +0.21 · ⚠️ oversold |
| ⚪ Hold | -0.01 | **AMD**<br><small>Advanced Micro Devices</small> | 402.51 USD | +54% | -6.9% | +158% | -3% | 30 | -0.15 | 0.0% → 0.0% | – | analyst α -0.31 · trend +0.21 · ⚠️ oversold |
| ⚪ Hold | -0.08 | **ASML**<br><small>ASML Holding</small> | 1,356.23 USD | +55% | -6.0% | +76% | -15% | 27 | +0.42 | 5.1% → 5.1% | – | analyst α -0.23 · quality +0.18 · ⚠️ oversold |
| ⚪ Hold | -0.08 | **Tokyo Electron**<br><small>8035.T</small> | 8,427 JPY | +81% | +0.7% | +112% | -19% | 33 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · momentum +0.07 |
| ⚪ Hold | -0.11 | **ASX**<br><small>ASE Technology</small> | 29.72 USD | +72% | -0.8% | +201% | -11% | 28 | -0.68 | 1.2% → 1.2% | – | quality -0.28 · momentum +0.26 · ⚠️ oversold, rich valuation |
| ⚪ Hold | -0.18 | **AVGO**<br><small>Broadcom</small> | 291.38 USD | +82% | +1.3% | +8% | -20% | 31 | +0.26 | 0.0% → 0.0% | – | momentum -0.30 · analyst α +0.12 |
| ⚪ Hold | -0.21 | **GFS**<br><small>GlobalFoundries</small> | 36.33 USD | +109% | +7.6% | +40% | -34% | 28 | -0.21 | 0.0% → 0.0% | – | analyst α +0.31 · momentum -0.14 · ⚠️ oversold |
| ⚪ Hold | -0.22 | **Disco**<br><small>6146.T</small> | 40,560 JPY | +102% | +6.0% | +25% | -38% | 26 | +0.06 | 0.0% → 0.0% | – | analyst α +0.23 · momentum -0.20 · ⚠️ oversold |
| 🔴 Sell | -0.38 | **ARM**<br><small>Arm Holdings</small> | 166.64 USD | +73% | -3.3% | +83% | -28% | 27 | +0.04 | 0.0% → 0.0% | – | analyst α -0.15 · trend -0.06 · ⚠️ oversold, rich valuation, high σ(e) |
| 🔴 Sell | -0.49 | **ASMI**<br><small>ASM.AS</small> | 632.80 EUR | +78% | -0.3% | +69% | -22% | 30 | -0.10 | 0.0% → 0.0% | – | analyst α -0.08 · quality -0.06 · ⚠️ oversold |
| 🔴 Sell | -0.58 | **ENTG**<br><small>Entegris</small> | 124.70 USD | +39% | -9.6% | +93% | -10% | 36 | -0.02 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.12 |
| 🔴🔴 Strong Sell | -0.87 | **TXN**<br><small>Texas Instruments</small> | 278.14 USD | +17% | -14.7% | +84% | +7% | 43 | +0.24 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -0.97 | **SNPS**<br><small>Synopsys</small> | 440.55 USD | +29% | -11.9% | +21% | -0% | 44 | +0.14 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.25 |
| 🔴🔴 Strong Sell | -1.09 | **QCOM**<br><small>Qualcomm</small> | 156.98 USD | +24% | -13.3% | +5% | -7% | 38 | +0.70 | 0.0% → 0.0% | – | analyst α -0.66 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.09 | **CDNS**<br><small>Cadence Design Systems</small> | 311.47 USD | +30% | -11.6% | +7% | -5% | 42 | +0.31 | 0.0% → 0.0% | – | analyst α -0.48 · momentum -0.35 |
| 🔴🔴 Strong Sell | -1.21 | **SMIC**<br><small>0981.HK</small> | 45.50 HKD | +111% | +9.2% | -24% | -32% | 36 | -0.99 | 0.0% → 0.0% | – | momentum -0.53 · analyst α +0.41 |
| 🔴🔴 Strong Sell | -1.31 | **Shin-Etsu**<br><small>4063.T</small> | 5,337 JPY | +45% | -7.6% | +30% | -16% | 27 | -0.20 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.17 · ⚠️ oversold |
| 🔴🔴 Strong Sell | -1.85 | **AMKR**<br><small>Amkor Technology</small> | 30.47 USD | – | +0.0% | +49% | -46% | 27 | -1.00 | 0.0% → 0.0% | – | quality -0.43 · trend -0.32 · ⚠️ oversold |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.79"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 658.70 USD (+131%, 46 analysts); de-biased α +12.5% vs CAPM hurdle 14.0%. Downtrend -13% vs 200-day avg; 12-1 mom +400%; RSI 27. Quality z +0.12 (ROE 17%). ⚠️ oversold; cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.98"
    **ADD 240 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 477,517 KRW vs 191,400 KRW (+149%, 36 analysts); de-biased α +18.0% vs CAPM hurdle 11.3%. Downtrend -19% vs 200-day avg; 12-1 mom +170%; RSI 33. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.58"
    Within rebalance band of target 6.7%: no trade. Analyst target 293.88 USD vs 133.32 USD (+120%, 43 analysts); de-biased α +9.9% vs CAPM hurdle 14.1%. Downtrend -28% vs 200-day avg; 12-1 mom +225%; RSI 23. Quality z -0.12 (ROE 19%). ⚠️ oversold; price implies 78% stage-1 growth (reverse DCF).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.35"
    **TRIM 30 sh** → target 5.3% of NAV (sized ∝ score ÷ σ(e), cap 10%). No reliable analyst target: α set to 0. Downtrend -22% vs 200-day avg; 12-1 mom +223%; RSI 34. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "INTC (INTC) — 🟢🟢 Strong Buy, score +0.78"
    Within rebalance band of target 2.9%: no trade. Analyst target 116.37 USD vs 52.12 USD (+123%, 43 analysts); de-biased α +10.6% vs CAPM hurdle 14.0%. Downtrend -40% vs 200-day avg; 12-1 mom +205%; RSI 21. Quality z -0.62 (ROE -0%). ⚠️ oversold; price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "AMAT (AMAT) — 🟢 Buy, score +0.50"
    Within rebalance band of target 2.8%: no trade. Analyst target 638.94 USD vs 319.33 USD (+100%, 36 analysts); de-biased α +5.5% vs CAPM hurdle 11.6%. Downtrend -28% vs 200-day avg; 12-1 mom +127%; RSI 26. Quality z +0.03 (ROE 36%). ⚠️ oversold.

??? success "Advantest (6857.T) — 🟢 Buy, score +0.45"
    **TRIM 100 sh** → target 2.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 42,686 JPY vs 27,610 JPY (+55%, 21 analysts); de-biased α -6.3% vs CAPM hurdle 13.4%. Downtrend -5% vs 200-day avg; 12-1 mom +145%; RSI 34. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? success "LRCX (LRCX) — 🟢 Buy, score +0.43"
    **ADD 56 sh** → target 2.7% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 375.06 USD vs 184.59 USD (+103%, 31 analysts); de-biased α +6.0% vs CAPM hurdle 12.6%. Downtrend -35% vs 200-day avg; 12-1 mom +112%; RSI 23. Quality z +0.02 (ROE 65%). ⚠️ oversold.

??? success "KLAC (KLAC) — 🟢 Buy, score +0.31"
    **TRIM 151 sh** → target 1.9% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 233.77 USD vs 129.63 USD (+80%, 26 analysts); de-biased α +0.7% vs CAPM hurdle 11.1%. Downtrend -29% vs 200-day avg; 12-1 mom +66%; RSI 28. Quality z +0.51 (ROE 87%). ⚠️ oversold.

??? note "Infineon (IFX.DE) — ⚪ Hold, score +0.20"
    Hold zone: keep any existing position, no new money. Analyst target 86.74 EUR vs 45.90 EUR (+89%, 23 analysts); de-biased α +2.2% vs CAPM hurdle 14.1%. Downtrend -20% vs 200-day avg; 12-1 mom +81%; RSI 33. Quality z -0.04 (ROE 6%).

??? note "TER (TER) — ⚪ Hold, score +0.19"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 212.66 USD (+110%, 15 analysts); de-biased α +7.8% vs CAPM hurdle 12.3%. Downtrend -39% vs 200-day avg; 12-1 mom +135%; RSI 22. Quality z -0.31 (ROE 20%). ⚠️ oversold.

??? note "TSM (TSM) — ⚪ Hold, score +0.13"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 352.03 USD (+57%, 20 analysts); de-biased α -5.0% vs CAPM hurdle 10.8%. Downtrend -12% vs 200-day avg; 12-1 mom +62%; RSI 26. Quality z +0.58 (ROE 35%). ⚠️ oversold.

??? note "NVDA (NVDA) — ⚪ Hold, score -0.00"
    Hold zone: keep any existing position, no new money. Analyst target 327.70 USD vs 181.60 USD (+80%, 59 analysts); de-biased α -0.0% vs CAPM hurdle 13.9%. Downtrend -11% vs 200-day avg; 12-1 mom +20%; RSI 25. Quality z +0.47 (ROE 101%). ⚠️ oversold.

??? note "AMD (AMD) — ⚪ Hold, score -0.01"
    Hold zone: not owned, no entry. Analyst target 619.51 USD vs 402.51 USD (+54%, 50 analysts); de-biased α -6.9% vs CAPM hurdle 14.9%. Downtrend -3% vs 200-day avg; 12-1 mom +158%; RSI 30. Quality z -0.15 (ROE 7%). ⚠️ oversold.

??? note "ASML (ASML) — ⚪ Hold, score -0.08"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,356.23 USD (+55%, 16 analysts); de-biased α -6.0% vs CAPM hurdle 12.3%. Downtrend -15% vs 200-day avg; 12-1 mom +76%; RSI 27. Quality z +0.42 (ROE 50%). ⚠️ oversold.

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score -0.08"
    Hold zone: not owned, no entry. Analyst target 15,275 JPY vs 8,427 JPY (+81%, 23 analysts); de-biased α +0.7% vs CAPM hurdle 12.8%. Downtrend -19% vs 200-day avg; 12-1 mom +112%; RSI 33. Quality z -0.28 (ROE 29%).

??? note "ASX (ASX) — ⚪ Hold, score -0.11"
    Hold zone: keep any existing position, no new money. Analyst target 51.00 USD vs 29.72 USD (+72%, 1 analysts); de-biased α -0.8% vs CAPM hurdle 11.9%. Downtrend -11% vs 200-day avg; 12-1 mom +201%; RSI 28. Quality z -0.68 (ROE 12%). ⚠️ oversold; price implies 69% stage-1 growth (reverse DCF).

??? note "AVGO (AVGO) — ⚪ Hold, score -0.18"
    Hold zone: not owned, no entry. Analyst target 531.31 USD vs 291.38 USD (+82%, 47 analysts); de-biased α +1.3% vs CAPM hurdle 11.2%. Downtrend -20% vs 200-day avg; 12-1 mom +8%; RSI 31. Quality z +0.26 (ROE 31%).

??? note "GFS (GFS) — ⚪ Hold, score -0.21"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 36.33 USD (+109%, 22 analysts); de-biased α +7.6% vs CAPM hurdle 12.4%. Downtrend -34% vs 200-day avg; 12-1 mom +40%; RSI 28. Quality z -0.21 (ROE 8%). ⚠️ oversold.

??? note "Disco (6146.T) — ⚪ Hold, score -0.22"
    Hold zone: not owned, no entry. Analyst target 81,730 JPY vs 40,560 JPY (+102%, 20 analysts); de-biased α +6.0% vs CAPM hurdle 11.5%. Downtrend -38% vs 200-day avg; 12-1 mom +25%; RSI 26. Quality z +0.06 (ROE 25%). ⚠️ oversold.

??? failure "ARM (ARM) — 🔴 Sell, score -0.38"
    Avoid: not owned. Analyst target 288.70 USD vs 166.64 USD (+73%, 40 analysts); de-biased α -3.3% vs CAPM hurdle 19.6%. Downtrend -28% vs 200-day avg; 12-1 mom +83%; RSI 27. Quality z +0.04 (ROE 12%). ⚠️ oversold; price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.49"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 632.80 EUR (+78%, 19 analysts); de-biased α -0.3% vs CAPM hurdle 13.2%. Downtrend -22% vs 200-day avg; 12-1 mom +69%; RSI 30. Quality z -0.10 (ROE 19%). ⚠️ oversold.

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.58"
    Avoid: not owned. Analyst target 173.36 USD vs 124.70 USD (+39%, 11 analysts); de-biased α -9.6% vs CAPM hurdle 11.0%. Downtrend -10% vs 200-day avg; 12-1 mom +93%; RSI 36. Quality z -0.02 (ROE 6%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -0.87"
    Avoid: not owned. Analyst target 324.71 USD vs 278.14 USD (+17%, 31 analysts); de-biased α -14.7% vs CAPM hurdle 10.8%. Uptrend +7% vs 200-day avg; 12-1 mom +84%; RSI 43. Quality z +0.24 (ROE 30%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.97"
    Avoid: not owned. Analyst target 569.78 USD vs 440.55 USD (+29%, 26 analysts); de-biased α -11.9% vs CAPM hurdle 10.3%. Downtrend -0% vs 200-day avg; 12-1 mom +21%; RSI 44. Quality z +0.14 (ROE 7%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.09"
    Avoid: not owned. Analyst target 194.13 USD vs 156.98 USD (+24%, 30 analysts); de-biased α -13.3% vs CAPM hurdle 11.9%. Downtrend -7% vs 200-day avg; 12-1 mom +5%; RSI 38. Quality z +0.70 (ROE 23%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.09"
    Avoid: not owned. Analyst target 405.47 USD vs 311.47 USD (+30%, 26 analysts); de-biased α -11.6% vs CAPM hurdle 10.0%. Downtrend -5% vs 200-day avg; 12-1 mom +7%; RSI 42. Quality z +0.31 (ROE 22%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.21"
    Avoid: not owned. Analyst target 95.99 HKD vs 45.50 HKD (+111%, 21 analysts); de-biased α +9.2% vs CAPM hurdle 7.3%. Downtrend -32% vs 200-day avg; 12-1 mom -24%; RSI 36. Quality z -0.99 (ROE 3%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.31"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,337 JPY (+45%, 17 analysts); de-biased α -7.6% vs CAPM hurdle 10.8%. Downtrend -16% vs 200-day avg; 12-1 mom +30%; RSI 27. Quality z -0.20 (ROE 10%). ⚠️ oversold.

??? failure "AMKR (AMKR) — 🔴🔴 Strong Sell, score -1.85"
    Avoid: not owned. No reliable analyst target: α set to 0. Downtrend -46% vs 200-day avg; 12-1 mom +49%; RSI 27. Quality z -1.00 (ROE 9%). ⚠️ oversold.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 005930.KS | Samsung Electronics | 562 | 191,400 KRW | $79,298 | 10.0% | Strong Buy |
| MU | Micron Technology | 116 | 658.70 USD | $76,409 | 9.6% | Strong Buy |
| TSM | TSMC | 127 | 352.03 USD | $44,708 | 5.6% | Hold |
| MRVL | Marvell Technology | 324 | 133.32 USD | $43,196 | 5.4% | Strong Buy |
| 000660.KS | SK hynix | 50 | 1,169,000 KRW | $43,089 | 5.4% | Strong Buy |
| ASML | ASML Holding | 30 | 1,356.23 USD | $40,687 | 5.1% | Hold |
| KLAC | KLA Corp | 268 | 129.63 USD | $34,741 | 4.4% | Buy |
| INTC | Intel | 447 | 52.12 USD | $23,300 | 2.9% | Strong Buy |
| AMAT | Applied Materials | 71 | 319.33 USD | $22,672 | 2.9% | Buy |
| 6857.T | Advantest | 100 | 27,610 JPY | $17,487 | 2.2% | Buy |
| IFX.DE | Infineon Technologies | 225 | 45.90 EUR | $11,583 | 1.5% | Hold |
| NVDA | NVIDIA | 60 | 181.60 USD | $10,896 | 1.4% | Hold |
| LRCX | Lam Research | 58 | 184.59 USD | $10,706 | 1.3% | Buy |
| ASX | ASE Technology | 312 | 29.72 USD | $9,271 | 1.2% | Hold |
| TER | Teradyne | 35 | 212.66 USD | $7,443 | 0.9% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-11-06 02:27 UTC | ADD | 005930.KS | 240 | 191,400.00 | $33,864 |
| 2026-11-06 02:27 UTC | TRIM | 000660.KS | -30 | 1,169,000.00 | $25,854 |
| 2026-11-06 02:27 UTC | TRIM | 6857.T | -100 | 27,610.00 | $17,487 |
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

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 66.7%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
