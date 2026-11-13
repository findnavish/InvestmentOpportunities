---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-13 16:26 UTC (Fri Nov 13, 11:26 AM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🟢 open (Fri 11:26) · Tokyo 🔴 closed (Sat 01:26) · Korea 🔴 closed (Sat 01:26) · Hong Kong 🔴 closed (Sat 00:26) · Xetra 🟢 open (Fri 17:26) · Euronext Amsterdam 🟢 open (Fri 17:26)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$843,542** | $311,442 (37%) | $532,099 (63%) | -15.65% | -74.15% | 🔴 Risk-off (-8.8%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $843,542), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **SK hynix**<br><small>000660.KS</small> | 44 | 1,216,000 KRW | $40,024 | Queued · Korea closed | quality +0.33 · momentum +0.23 · ⚠️ cycle-peak P/E, high σ(e) |
| ADD | **NVDA**<br><small>NVIDIA</small> | 79 | 159.94 USD | $12,635 | Executed (paper) | analyst α +0.55 · momentum -0.23 · ⚠️ oversold |
| TRIM | **ASX**<br><small>ASE Technology</small> | 290 | 34.86 USD | $10,109 | Executed (paper) | momentum +0.41 · quality -0.28 · ⚠️ rich valuation |
| ADD | **AMAT**<br><small>Applied Materials</small> | 23 | 357.03 USD | $8,212 | Executed (paper) | analyst α +0.19 · momentum +0.14 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +2.77 | **MU**<br><small>Micron Technology</small> | 756.00 USD | +101% | +9.0% | +281% | -1% | 41 | +0.12 | 10.4% → 10.0% | – | momentum +0.53 · analyst α +0.41 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.24 | **Samsung**<br><small>005930.KS</small> | 207,000 KRW | +131% | +17.2% | +94% | -13% | 43 | -0.26 | 8.4% → 10.0% | – | analyst α +0.85 · momentum +0.20 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.34 | **MRVL**<br><small>Marvell Technology</small> | 152.21 USD | +93% | +7.0% | +171% | -19% | 34 | -0.12 | 4.5% → 5.1% | – | momentum +0.35 · analyst α +0.31 · ⚠️ rich valuation |
| 🟢🟢 Strong Buy | +1.33 | **SK hynix**<br><small>000660.KS</small> | 1,216,000 KRW | – | +0.0% | +104% | -20% | 40 | +0.62 | 9.5% → 4.7% | TRIM 44 | quality +0.33 · momentum +0.23 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +1.08 | **NVDA**<br><small>NVIDIA</small> | 159.94 USD | +105% | +10.0% | +12% | -22% | 24 | +0.47 | 6.4% → 6.4% | ADD 79 | analyst α +0.55 · momentum -0.23 · ⚠️ oversold |
| 🟢 Buy | +0.71 | **AMAT**<br><small>Applied Materials</small> | 357.03 USD | +79% | +4.2% | +87% | -20% | 40 | +0.03 | 3.6% → 3.6% | ADD 23 | analyst α +0.19 · momentum +0.14 |
| 🟢 Buy | +0.43 | **INTC**<br><small>Intel</small> | 57.88 USD | +101% | +9.0% | +152% | -34% | 31 | -0.62 | 1.0% → 1.5% | – | analyst α +0.36 · momentum +0.30 · ⚠️ rich valuation, high σ(e) |
| 🟢 Buy | +0.43 | **ASX**<br><small>ASE Technology</small> | 34.86 USD | +46% | -2.0% | +182% | +3% | 42 | -0.68 | 2.4% → 2.4% | TRIM 290 | momentum +0.41 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.42 | **Advantest**<br><small>6857.T</small> | 30,730 JPY | +39% | -6.3% | +83% | +5% | 44 | +0.33 | 2.3% → 1.7% | – | analyst α -0.31 · trend +0.21 · ⚠️ rich valuation |
| ⚪ Hold | +0.15 | **KLAC**<br><small>KLA Corp</small> | 148.90 USD | +57% | -1.2% | +46% | -18% | 43 | +0.51 | 4.7% → 4.7% | – | quality +0.24 · momentum -0.10 |
| ⚪ Hold | +0.15 | **TSM**<br><small>TSMC</small> | 394.62 USD | +40% | -5.3% | +47% | -2% | 44 | +0.58 | 5.9% → 5.9% | – | quality +0.28 · analyst α -0.23 |
| ⚪ Hold | +0.06 | **ASML**<br><small>ASML Holding</small> | 1,472.96 USD | +42% | -5.1% | +61% | -8% | 41 | +0.42 | 0.0% → 0.0% | – | analyst α -0.19 · quality +0.18 |
| ⚪ Hold | +0.04 | **Infineon**<br><small>IFX.DE</small> | 49.83 EUR | +74% | +2.4% | +50% | -13% | 45 | -0.04 | 1.5% → 1.5% | – | analyst α +0.12 · momentum -0.05 |
| ⚪ Hold | -0.03 | **LRCX**<br><small>Lam Research</small> | 220.79 USD | +70% | +1.7% | +73% | -22% | 40 | +0.02 | 1.5% → 1.5% | – | trend -0.12 · analyst α +0.08 |
| ⚪ Hold | -0.04 | **TER**<br><small>Teradyne</small> | 244.63 USD | +83% | +4.9% | +92% | -30% | 36 | -0.31 | 1.0% → 1.0% | – | analyst α +0.23 · trend -0.21 |
| ⚪ Hold | -0.09 | **Tokyo Electron**<br><small>8035.T</small> | 9,404 JPY | +62% | -0.1% | +76% | -9% | 45 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · momentum +0.10 |
| 🔴 Sell | -0.30 | **GFS**<br><small>GlobalFoundries</small> | 40.60 USD | +87% | +6.0% | +43% | -26% | 42 | -0.21 | 0.0% → 0.0% | – | analyst α +0.27 · trend -0.14 |
| 🔴 Sell | -0.32 | **ASMI**<br><small>ASM.AS</small> | 693.40 EUR | +63% | -0.3% | +57% | -15% | 42 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · momentum -0.03 |
| 🔴 Sell | -0.44 | **AMD**<br><small>Advanced Micro Devices</small> | 526.06 USD | +18% | -12.0% | +117% | +24% | 49 | -0.15 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.32 |
| 🔴 Sell | -0.51 | **ARM**<br><small>Arm Holdings</small> | 185.83 USD | +55% | -3.8% | +65% | -20% | 39 | +0.04 | 0.0% → 0.0% | – | analyst α -0.15 · trend -0.09 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.60 | **Disco**<br><small>6146.T</small> | 47,440 JPY | +72% | +2.7% | +4% | -27% | 44 | +0.06 | 0.0% → 0.0% | – | momentum -0.26 · trend -0.18 |
| 🔴 Sell | -0.62 | **ENTG**<br><small>Entegris</small> | 144.23 USD | +20% | -10.4% | +75% | +4% | 49 | -0.02 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.18 |
| 🔴 Sell | -0.64 | **AMKR**<br><small>Amkor Technology</small> | 35.44 USD | +116% | +12.8% | +29% | -37% | 41 | -1.00 | 0.0% → 0.0% | – | analyst α +0.66 · quality -0.43 |
| 🔴🔴 Strong Sell | -0.77 | **QCOM**<br><small>Qualcomm</small> | 169.25 USD | +15% | -11.5% | +3% | +0% | 47 | +0.70 | 0.0% → 0.0% | – | analyst α -0.55 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.81 | **AVGO**<br><small>Broadcom</small> | 340.89 USD | +56% | -1.4% | -2% | -7% | 51 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.11 |
| 🔴🔴 Strong Sell | -0.86 | **SNPS**<br><small>Synopsys</small> | 449.14 USD | +27% | -8.6% | +17% | +2% | 47 | +0.14 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.20 |
| 🔴🔴 Strong Sell | -1.14 | **TXN**<br><small>Texas Instruments</small> | 297.23 USD | +9% | -12.6% | +74% | +13% | 52 | +0.24 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.25 |
| 🔴🔴 Strong Sell | -1.27 | **Shin-Etsu**<br><small>4063.T</small> | 5,676 JPY | +37% | -5.8% | +35% | -10% | 45 | -0.20 | 0.0% → 0.0% | – | analyst α -0.27 · momentum -0.14 |
| 🔴🔴 Strong Sell | -1.35 | **SMIC**<br><small>0981.HK</small> | 48.52 HKD | +98% | +9.9% | -24% | -27% | 45 | -0.99 | 0.0% → 0.0% | – | momentum -0.53 · analyst α +0.48 |
| 🔴🔴 Strong Sell | -1.38 | **CDNS**<br><small>Cadence Design Systems</small> | 321.43 USD | +26% | -8.7% | +3% | -2% | 47 | +0.31 | 0.0% → 0.0% | – | analyst α -0.41 · momentum -0.35 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.77"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 756.00 USD (+101%, 46 analysts); de-biased α +9.0% vs CAPM hurdle 14.0%. Downtrend -1% vs 200-day avg; 12-1 mom +281%; RSI 41. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.24"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 207,000 KRW (+131%, 36 analysts); de-biased α +17.2% vs CAPM hurdle 11.3%. Downtrend -13% vs 200-day avg; 12-1 mom +94%; RSI 43. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.34"
    Within rebalance band of target 5.1%: no trade. Analyst target 293.88 USD vs 152.21 USD (+93%, 43 analysts); de-biased α +7.0% vs CAPM hurdle 14.1%. Downtrend -19% vs 200-day avg; 12-1 mom +171%; RSI 34. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.33"
    **TRIM 44 sh** → target 4.7% of NAV (sized ∝ score ÷ σ(e), cap 10%). No reliable analyst target: α set to 0. Downtrend -20% vs 200-day avg; 12-1 mom +104%; RSI 40. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "NVDA (NVDA) — 🟢🟢 Strong Buy, score +1.08"
    **ADD 79 sh** → target 6.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 327.70 USD vs 159.94 USD (+105%, 59 analysts); de-biased α +10.0% vs CAPM hurdle 13.9%. Downtrend -22% vs 200-day avg; 12-1 mom +12%; RSI 24. Quality z +0.47 (ROE 101%). ⚠️ oversold.

??? success "AMAT (AMAT) — 🟢 Buy, score +0.71"
    **ADD 23 sh** → target 3.6% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 357.03 USD (+79%, 36 analysts); de-biased α +4.2% vs CAPM hurdle 11.6%. Downtrend -20% vs 200-day avg; 12-1 mom +87%; RSI 40. Quality z +0.03 (ROE 36%).

??? success "INTC (INTC) — 🟢 Buy, score +0.43"
    Within rebalance band of target 1.5%: no trade. Analyst target 116.37 USD vs 57.88 USD (+101%, 43 analysts); de-biased α +9.0% vs CAPM hurdle 14.0%. Downtrend -34% vs 200-day avg; 12-1 mom +152%; RSI 31. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "ASX (ASX) — 🟢 Buy, score +0.43"
    **TRIM 290 sh** → target 2.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 51.00 USD vs 34.86 USD (+46%, 1 analysts); de-biased α -2.0% vs CAPM hurdle 11.9%. Uptrend +3% vs 200-day avg; 12-1 mom +182%; RSI 42. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.42"
    Within rebalance band of target 1.7%: no trade. Analyst target 42,686 JPY vs 30,730 JPY (+39%, 21 analysts); de-biased α -6.3% vs CAPM hurdle 13.4%. Uptrend +5% vs 200-day avg; 12-1 mom +83%; RSI 44. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.15"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 148.90 USD (+57%, 26 analysts); de-biased α -1.2% vs CAPM hurdle 11.1%. Downtrend -18% vs 200-day avg; 12-1 mom +46%; RSI 43. Quality z +0.51 (ROE 87%).

??? note "TSM (TSM) — ⚪ Hold, score +0.15"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 394.62 USD (+40%, 20 analysts); de-biased α -5.3% vs CAPM hurdle 10.8%. Downtrend -2% vs 200-day avg; 12-1 mom +47%; RSI 44. Quality z +0.58 (ROE 35%).

??? note "ASML (ASML) — ⚪ Hold, score +0.06"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,472.96 USD (+42%, 16 analysts); de-biased α -5.1% vs CAPM hurdle 12.3%. Downtrend -8% vs 200-day avg; 12-1 mom +61%; RSI 41. Quality z +0.42 (ROE 50%).

??? note "Infineon (IFX.DE) — ⚪ Hold, score +0.04"
    Hold zone: keep any existing position, no new money. Analyst target 86.74 EUR vs 49.83 EUR (+74%, 23 analysts); de-biased α +2.4% vs CAPM hurdle 14.1%. Downtrend -13% vs 200-day avg; 12-1 mom +50%; RSI 45. Quality z -0.04 (ROE 6%).

??? note "LRCX (LRCX) — ⚪ Hold, score -0.03"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 220.79 USD (+70%, 31 analysts); de-biased α +1.7% vs CAPM hurdle 12.6%. Downtrend -22% vs 200-day avg; 12-1 mom +73%; RSI 40. Quality z +0.02 (ROE 65%).

??? note "TER (TER) — ⚪ Hold, score -0.04"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 244.63 USD (+83%, 15 analysts); de-biased α +4.9% vs CAPM hurdle 12.3%. Downtrend -30% vs 200-day avg; 12-1 mom +92%; RSI 36. Quality z -0.31 (ROE 20%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score -0.09"
    Hold zone: not owned, no entry. Analyst target 15,275 JPY vs 9,404 JPY (+62%, 23 analysts); de-biased α -0.1% vs CAPM hurdle 12.8%. Downtrend -9% vs 200-day avg; 12-1 mom +76%; RSI 45. Quality z -0.28 (ROE 29%).

??? failure "GFS (GFS) — 🔴 Sell, score -0.30"
    Avoid: not owned. Analyst target 76.00 USD vs 40.60 USD (+87%, 22 analysts); de-biased α +6.0% vs CAPM hurdle 12.4%. Downtrend -26% vs 200-day avg; 12-1 mom +43%; RSI 42. Quality z -0.21 (ROE 8%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.32"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 693.40 EUR (+63%, 19 analysts); de-biased α -0.3% vs CAPM hurdle 13.2%. Downtrend -15% vs 200-day avg; 12-1 mom +57%; RSI 42. Quality z -0.10 (ROE 19%).

??? failure "AMD (AMD) — 🔴 Sell, score -0.44"
    Avoid: not owned. Analyst target 619.51 USD vs 526.06 USD (+18%, 50 analysts); de-biased α -12.0% vs CAPM hurdle 14.9%. Uptrend +24% vs 200-day avg; 12-1 mom +117%; RSI 49. Quality z -0.15 (ROE 7%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.51"
    Avoid: not owned. Analyst target 288.70 USD vs 185.83 USD (+55%, 40 analysts); de-biased α -3.8% vs CAPM hurdle 19.6%. Downtrend -20% vs 200-day avg; 12-1 mom +65%; RSI 39. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "Disco (6146.T) — 🔴 Sell, score -0.60"
    Avoid: not owned. Analyst target 81,730 JPY vs 47,440 JPY (+72%, 20 analysts); de-biased α +2.7% vs CAPM hurdle 11.5%. Downtrend -27% vs 200-day avg; 12-1 mom +4%; RSI 44. Quality z +0.06 (ROE 25%).

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.62"
    Avoid: not owned. Analyst target 173.36 USD vs 144.23 USD (+20%, 11 analysts); de-biased α -10.4% vs CAPM hurdle 11.0%. Uptrend +4% vs 200-day avg; 12-1 mom +75%; RSI 49. Quality z -0.02 (ROE 6%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.64"
    Avoid: not owned. Analyst target 76.40 USD vs 35.44 USD (+116%, 10 analysts); de-biased α +12.8% vs CAPM hurdle 14.0%. Downtrend -37% vs 200-day avg; 12-1 mom +29%; RSI 41. Quality z -1.00 (ROE 9%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.77"
    Avoid: not owned. Analyst target 194.13 USD vs 169.25 USD (+15%, 30 analysts); de-biased α -11.5% vs CAPM hurdle 11.9%. Uptrend +0% vs 200-day avg; 12-1 mom +3%; RSI 47. Quality z +0.70 (ROE 23%).

??? failure "AVGO (AVGO) — 🔴🔴 Strong Sell, score -0.81"
    Avoid: not owned. Analyst target 531.31 USD vs 340.89 USD (+56%, 47 analysts); de-biased α -1.4% vs CAPM hurdle 11.2%. Downtrend -7% vs 200-day avg; 12-1 mom -2%; RSI 51. Quality z +0.26 (ROE 31%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.86"
    Avoid: not owned. Analyst target 569.78 USD vs 449.14 USD (+27%, 26 analysts); de-biased α -8.6% vs CAPM hurdle 10.3%. Uptrend +2% vs 200-day avg; 12-1 mom +17%; RSI 47. Quality z +0.14 (ROE 7%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -1.14"
    Avoid: not owned. Analyst target 324.71 USD vs 297.23 USD (+9%, 31 analysts); de-biased α -12.6% vs CAPM hurdle 10.8%. Uptrend +13% vs 200-day avg; 12-1 mom +74%; RSI 52. Quality z +0.24 (ROE 30%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.27"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,676 JPY (+37%, 17 analysts); de-biased α -5.8% vs CAPM hurdle 10.8%. Downtrend -10% vs 200-day avg; 12-1 mom +35%; RSI 45. Quality z -0.20 (ROE 10%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.35"
    Avoid: not owned. Analyst target 95.99 HKD vs 48.52 HKD (+98%, 21 analysts); de-biased α +9.9% vs CAPM hurdle 7.3%. Downtrend -27% vs 200-day avg; 12-1 mom -24%; RSI 45. Quality z -0.99 (ROE 3%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.38"
    Avoid: not owned. Analyst target 405.47 USD vs 321.43 USD (+26%, 26 analysts); de-biased α -8.7% vs CAPM hurdle 10.0%. Downtrend -2% vs 200-day avg; 12-1 mom +3%; RSI 47. Quality z +0.31 (ROE 22%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 116 | 756.00 USD | $87,696 | 10.4% | Strong Buy |
| 000660.KS | SK hynix | 88 | 1,216,000 KRW | $80,047 | 9.5% | Strong Buy |
| 005930.KS | Samsung Electronics | 458 | 207,000 KRW | $70,920 | 8.4% | Strong Buy |
| NVDA | NVIDIA | 337 | 159.94 USD | $53,900 | 6.4% | Strong Buy |
| TSM | TSMC | 127 | 394.62 USD | $50,117 | 5.9% | Hold |
| KLAC | KLA Corp | 268 | 148.90 USD | $39,905 | 4.7% | Hold |
| MRVL | Marvell Technology | 248 | 152.21 USD | $37,748 | 4.5% | Strong Buy |
| AMAT | Applied Materials | 84 | 357.03 USD | $29,990 | 3.6% | Buy |
| ASX | ASE Technology | 574 | 34.86 USD | $20,010 | 2.4% | Buy |
| 6857.T | Advantest | 100 | 30,730 JPY | $19,224 | 2.3% | Buy |
| LRCX | Lam Research | 58 | 220.79 USD | $12,806 | 1.5% | Hold |
| IFX.DE | Infineon Technologies | 225 | 49.83 EUR | $12,378 | 1.5% | Hold |
| INTC | Intel | 152 | 57.88 USD | $8,797 | 1.0% | Buy |
| TER | Teradyne | 35 | 244.63 USD | $8,562 | 1.0% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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
| 2026-11-05 15:28 UTC | ADD | MRVL | 160 | 140.70 | $22,512 |
| 2026-11-05 15:28 UTC | ADD | MU | 52 | 693.52 | $36,063 |
| 2026-11-05 15:28 UTC | ADD | AMAT | 21 | 332.95 | $6,992 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 50.9%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
