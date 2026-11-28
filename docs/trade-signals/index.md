---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-28 02:41 UTC (Fri Nov 27, 09:41 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Fri 21:41) · Tokyo 🔴 closed (Sat 11:41) · Korea 🔴 closed (Sat 11:41) · Hong Kong 🔴 closed (Sat 10:41) · Xetra 🔴 closed (Sat 03:41) · Euronext Amsterdam 🔴 closed (Sat 03:41)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$792,639** | $311,602 (39%) | $481,037 (61%) | -20.74% | -76.30% | 🔴 Risk-off (-16.8%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $792,639), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| BUY (new) | **NVDA**<br><small>NVIDIA</small> | 437 | 150.62 USD | $65,821 | Queued · NYSE/Nasdaq closed | analyst α +0.55 · quality +0.21 |
| ADD | **MU**<br><small>Micron Technology</small> | 58 | 645.37 USD | $37,431 | Queued · NYSE/Nasdaq closed | analyst α +0.85 · momentum +0.53 · ⚠️ cycle-peak P/E |
| TRIM | **MRVL**<br><small>Marvell Technology</small> | 199 | 141.01 USD | $28,061 | Queued · NYSE/Nasdaq closed | analyst α +0.48 · momentum +0.35 · ⚠️ rich valuation |
| TRIM | **INTC**<br><small>Intel</small> | 431 | 57.85 USD | $24,931 | Queued · NYSE/Nasdaq closed | analyst α +0.31 · momentum +0.26 · ⚠️ rich valuation, high σ(e) |
| TRIM | **TSM**<br><small>TSMC</small> | 70 | 350.36 USD | $24,525 | Queued · NYSE/Nasdaq closed | quality +0.28 · analyst α -0.19 |
| TRIM | **AMAT**<br><small>Applied Materials</small> | 65 | 323.12 USD | $21,003 | Queued · NYSE/Nasdaq closed | analyst α +0.27 · trend -0.12 |
| TRIM | **ASX**<br><small>ASE Technology</small> | 413 | 30.97 USD | $12,791 | Queued · NYSE/Nasdaq closed | momentum +0.41 · quality -0.28 · ⚠️ rich valuation |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.53 | **MU**<br><small>Micron Technology</small> | 645.37 USD | +136% | +15.0% | +338% | -17% | 40 | +0.12 | 5.2% → 10.0% | ADD 58 | analyst α +0.85 · momentum +0.53 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.61 | **MRVL**<br><small>Marvell Technology</small> | 141.01 USD | +108% | +8.2% | +202% | -26% | 40 | -0.12 | 10.7% → 7.1% | TRIM 199 | analyst α +0.48 · momentum +0.35 · ⚠️ rich valuation |
| 🟢🟢 Strong Buy | +1.21 | **NVDA**<br><small>NVIDIA</small> | 150.62 USD | +118% | +10.6% | +21% | -26% | 38 | +0.47 | 0.0% → 8.3% | BUY 437 | analyst α +0.55 · quality +0.21 |
| 🟢🟢 Strong Buy | +1.12 | **SK hynix**<br><small>000660.KS</small> | 1,103,000 KRW | – | +0.0% | +150% | -27% | 43 | +0.62 | 4.3% → 4.6% | – | quality +0.33 · momentum +0.23 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢 Buy | +0.56 | **AMAT**<br><small>Applied Materials</small> | 323.12 USD | +98% | +6.2% | +72% | -28% | 40 | +0.03 | 6.0% → 3.3% | TRIM 65 | analyst α +0.27 · trend -0.12 |
| 🟢 Buy | +0.36 | **ASX**<br><small>ASE Technology</small> | 30.97 USD | +65% | -1.0% | +213% | -10% | 43 | -0.68 | 3.9% → 2.3% | TRIM 413 | momentum +0.41 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.30 | **INTC**<br><small>Intel</small> | 57.85 USD | +101% | +6.4% | +167% | -34% | 40 | -0.62 | 4.3% → 1.2% | TRIM 431 | analyst α +0.31 · momentum +0.26 · ⚠️ rich valuation, high σ(e) |
| 🟢 Buy | +0.30 | **TSM**<br><small>TSMC</small> | 350.36 USD | +58% | -3.5% | +56% | -13% | 41 | +0.58 | 5.6% → 2.5% | TRIM 70 | quality +0.28 · analyst α -0.19 |
| ⚪ Hold | +0.25 | **Infineon**<br><small>IFX.DE</small> | 43.69 EUR | +99% | +5.9% | +50% | -24% | 40 | -0.04 | 1.3% → 1.3% | – | analyst α +0.23 · momentum -0.05 |
| ⚪ Hold | +0.23 | **Advantest**<br><small>6857.T</small> | 26,670 JPY | +60% | -3.7% | +69% | -9% | 44 | +0.33 | 2.1% → 2.1% | – | analyst α -0.23 · quality +0.16 · ⚠️ rich valuation |
| ⚪ Hold | +0.23 | **AMD**<br><small>Advanced Micro Devices</small> | 425.86 USD | +45% | -7.7% | +181% | -2% | 41 | -0.15 | 0.0% → 0.0% | – | analyst α -0.31 · momentum +0.30 |
| ⚪ Hold | +0.08 | **LRCX**<br><small>Lam Research</small> | 192.68 USD | +95% | +5.2% | +68% | -32% | 39 | +0.02 | 3.3% → 3.3% | – | analyst α +0.19 · trend -0.18 |
| ⚪ Hold | +0.06 | **TER**<br><small>Teradyne</small> | 222.94 USD | +100% | +6.7% | +87% | -36% | 39 | -0.31 | 3.5% → 3.5% | – | analyst α +0.36 · trend -0.25 |
| ⚪ Hold | +0.04 | **KLAC**<br><small>KLA Corp</small> | 140.89 USD | +66% | -1.6% | +39% | -22% | 45 | +0.51 | 2.7% → 2.7% | – | quality +0.24 · analyst α -0.12 |
| ⚪ Hold | +0.01 | **GFS**<br><small>GlobalFoundries</small> | 37.77 USD | +101% | +6.9% | +34% | -31% | 42 | -0.21 | 0.0% → 0.0% | – | analyst α +0.41 · trend -0.16 |
| ⚪ Hold | -0.01 | **Samsung**<br><small>005930.KS</small> | 179,300 KRW | – | +0.0% | +136% | -25% | 39 | -0.26 | 7.8% → 7.8% | – | momentum +0.20 · quality -0.16 · ⚠️ cycle-peak P/E |
| ⚪ Hold | -0.08 | **ASML**<br><small>ASML Holding</small> | 1,327.81 USD | +58% | -3.9% | +67% | -17% | 39 | +0.42 | 0.0% → 0.0% | – | analyst α -0.27 · quality +0.18 |
| ⚪ Hold | -0.09 | **ASMI**<br><small>ASM.AS</small> | 620.40 EUR | +82% | +1.9% | +66% | -23% | 41 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · analyst α +0.05 |
| ⚪ Hold | -0.23 | **Tokyo Electron**<br><small>8035.T</small> | 8,220 JPY | +86% | +3.1% | +42% | -21% | 41 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · analyst α +0.15 |
| ⚪ Hold | -0.24 | **TXN**<br><small>Texas Instruments</small> | 281.81 USD | +15% | -13.8% | +95% | +6% | 48 | +0.24 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.32 |
| 🔴 Sell | -0.32 | **ARM**<br><small>Arm Holdings</small> | 171.56 USD | +68% | -3.2% | +79% | -27% | 42 | +0.04 | 0.0% → 0.0% | – | analyst α -0.15 · trend -0.10 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.55 | **ENTG**<br><small>Entegris</small> | 136.08 USD | +27% | -11.2% | +117% | -3% | 47 | -0.02 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.18 |
| 🔴 Sell | -0.61 | **AMKR**<br><small>Amkor Technology</small> | 34.37 USD | +122% | +11.9% | +26% | -38% | 45 | -1.00 | 0.0% → 0.0% | – | analyst α +0.66 · quality -0.43 |
| 🔴 Sell | -0.69 | **AVGO**<br><small>Broadcom</small> | 312.24 USD | +70% | -0.5% | -8% | -15% | 45 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.11 |
| 🔴🔴 Strong Sell | -0.77 | **Disco**<br><small>6146.T</small> | 44,440 JPY | +84% | +2.9% | +9% | -31% | 46 | +0.06 | 0.0% → 0.0% | – | momentum -0.35 · trend -0.14 |
| 🔴🔴 Strong Sell | -0.98 | **SNPS**<br><small>Synopsys</small> | 420.27 USD | +36% | -9.1% | +20% | -5% | 44 | +0.14 | 0.0% → 0.0% | – | analyst α -0.41 · momentum -0.23 |
| 🔴🔴 Strong Sell | -1.05 | **QCOM**<br><small>Qualcomm</small> | 179.44 USD | +8% | -15.8% | +14% | +5% | 56 | +0.70 | 0.0% → 0.0% | – | analyst α -0.85 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.21 | **CDNS**<br><small>Cadence Design Systems</small> | 303.89 USD | +33% | -9.5% | +13% | -8% | 45 | +0.31 | 0.0% → 0.0% | – | analyst α -0.48 · momentum -0.30 |
| 🔴🔴 Strong Sell | -1.28 | **Shin-Etsu**<br><small>4063.T</small> | 5,644 JPY | +38% | -8.3% | +31% | -11% | 49 | -0.20 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.14 |
| 🔴🔴 Strong Sell | -1.81 | **SMIC**<br><small>0981.HK</small> | 53.40 HKD | +80% | +2.7% | -38% | -18% | 59 | -0.99 | 0.0% → 0.0% | – | momentum -0.53 · quality -0.33 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +3.53"
    **ADD 58 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 1,520.02 USD vs 645.37 USD (+136%, 46 analysts); de-biased α +15.0% vs CAPM hurdle 14.0%. Downtrend -17% vs 200-day avg; 12-1 mom +338%; RSI 40. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.61"
    **TRIM 199 sh** → target 7.1% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 293.88 USD vs 141.01 USD (+108%, 43 analysts); de-biased α +8.2% vs CAPM hurdle 14.1%. Downtrend -26% vs 200-day avg; 12-1 mom +202%; RSI 40. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? success "NVDA (NVDA) — 🟢🟢 Strong Buy, score +1.21"
    **BUY (new) 437 sh** → target 8.3% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 327.70 USD vs 150.62 USD (+118%, 59 analysts); de-biased α +10.6% vs CAPM hurdle 13.9%. Downtrend -26% vs 200-day avg; 12-1 mom +21%; RSI 38. Quality z +0.47 (ROE 101%).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.12"
    Within rebalance band of target 4.6%: no trade. No reliable analyst target: α set to 0. Downtrend -27% vs 200-day avg; 12-1 mom +150%; RSI 43. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "AMAT (AMAT) — 🟢 Buy, score +0.56"
    **TRIM 65 sh** → target 3.3% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 323.12 USD (+98%, 36 analysts); de-biased α +6.2% vs CAPM hurdle 11.6%. Downtrend -28% vs 200-day avg; 12-1 mom +72%; RSI 40. Quality z +0.03 (ROE 36%).

??? success "ASX (ASX) — 🟢 Buy, score +0.36"
    **TRIM 413 sh** → target 2.3% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 51.00 USD vs 30.97 USD (+65%, 1 analysts); de-biased α -1.0% vs CAPM hurdle 11.9%. Downtrend -10% vs 200-day avg; 12-1 mom +213%; RSI 43. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "INTC (INTC) — 🟢 Buy, score +0.30"
    **TRIM 431 sh** → target 1.2% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 116.37 USD vs 57.85 USD (+101%, 43 analysts); de-biased α +6.4% vs CAPM hurdle 14.0%. Downtrend -34% vs 200-day avg; 12-1 mom +167%; RSI 40. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "TSM (TSM) — 🟢 Buy, score +0.30"
    **TRIM 70 sh** → target 2.5% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 552.26 USD vs 350.36 USD (+58%, 20 analysts); de-biased α -3.5% vs CAPM hurdle 10.8%. Downtrend -13% vs 200-day avg; 12-1 mom +56%; RSI 41. Quality z +0.58 (ROE 35%).

??? note "Infineon (IFX.DE) — ⚪ Hold, score +0.25"
    Hold zone: keep any existing position, no new money. Analyst target 86.74 EUR vs 43.69 EUR (+99%, 23 analysts); de-biased α +5.9% vs CAPM hurdle 14.1%. Downtrend -24% vs 200-day avg; 12-1 mom +50%; RSI 40. Quality z -0.04 (ROE 6%).

??? note "Advantest (6857.T) — ⚪ Hold, score +0.23"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 26,670 JPY (+60%, 21 analysts); de-biased α -3.7% vs CAPM hurdle 13.4%. Downtrend -9% vs 200-day avg; 12-1 mom +69%; RSI 44. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "AMD (AMD) — ⚪ Hold, score +0.23"
    Hold zone: not owned, no entry. Analyst target 619.51 USD vs 425.86 USD (+45%, 50 analysts); de-biased α -7.7% vs CAPM hurdle 14.9%. Downtrend -2% vs 200-day avg; 12-1 mom +181%; RSI 41. Quality z -0.15 (ROE 7%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.08"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 192.68 USD (+95%, 31 analysts); de-biased α +5.2% vs CAPM hurdle 12.6%. Downtrend -32% vs 200-day avg; 12-1 mom +68%; RSI 39. Quality z +0.02 (ROE 65%).

??? note "TER (TER) — ⚪ Hold, score +0.06"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 222.94 USD (+100%, 15 analysts); de-biased α +6.7% vs CAPM hurdle 12.3%. Downtrend -36% vs 200-day avg; 12-1 mom +87%; RSI 39. Quality z -0.31 (ROE 20%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.04"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 140.89 USD (+66%, 26 analysts); de-biased α -1.6% vs CAPM hurdle 11.1%. Downtrend -22% vs 200-day avg; 12-1 mom +39%; RSI 45. Quality z +0.51 (ROE 87%).

??? note "GFS (GFS) — ⚪ Hold, score +0.01"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 37.77 USD (+101%, 22 analysts); de-biased α +6.9% vs CAPM hurdle 12.4%. Downtrend -31% vs 200-day avg; 12-1 mom +34%; RSI 42. Quality z -0.21 (ROE 8%).

??? note "Samsung (005930.KS) — ⚪ Hold, score -0.01"
    Hold zone: keep any existing position, no new money. No reliable analyst target: α set to 0. Downtrend -25% vs 200-day avg; 12-1 mom +136%; RSI 39. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? note "ASML (ASML) — ⚪ Hold, score -0.08"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,327.81 USD (+58%, 16 analysts); de-biased α -3.9% vs CAPM hurdle 12.3%. Downtrend -17% vs 200-day avg; 12-1 mom +67%; RSI 39. Quality z +0.42 (ROE 50%).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.09"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 620.40 EUR (+82%, 19 analysts); de-biased α +1.9% vs CAPM hurdle 13.2%. Downtrend -23% vs 200-day avg; 12-1 mom +66%; RSI 41. Quality z -0.10 (ROE 19%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score -0.23"
    Hold zone: not owned, no entry. Analyst target 15,275 JPY vs 8,220 JPY (+86%, 23 analysts); de-biased α +3.1% vs CAPM hurdle 12.8%. Downtrend -21% vs 200-day avg; 12-1 mom +42%; RSI 41. Quality z -0.28 (ROE 29%).

??? note "TXN (TXN) — ⚪ Hold, score -0.24"
    Hold zone: not owned, no entry. Analyst target 324.71 USD vs 281.81 USD (+15%, 31 analysts); de-biased α -13.8% vs CAPM hurdle 10.8%. Uptrend +6% vs 200-day avg; 12-1 mom +95%; RSI 48. Quality z +0.24 (ROE 30%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.32"
    Avoid: not owned. Analyst target 288.70 USD vs 171.56 USD (+68%, 40 analysts); de-biased α -3.2% vs CAPM hurdle 19.6%. Downtrend -27% vs 200-day avg; 12-1 mom +79%; RSI 42. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.55"
    Avoid: not owned. Analyst target 173.36 USD vs 136.08 USD (+27%, 11 analysts); de-biased α -11.2% vs CAPM hurdle 11.0%. Downtrend -3% vs 200-day avg; 12-1 mom +117%; RSI 47. Quality z -0.02 (ROE 6%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.61"
    Avoid: not owned. Analyst target 76.40 USD vs 34.37 USD (+122%, 10 analysts); de-biased α +11.9% vs CAPM hurdle 14.0%. Downtrend -38% vs 200-day avg; 12-1 mom +26%; RSI 45. Quality z -1.00 (ROE 9%).

??? failure "AVGO (AVGO) — 🔴 Sell, score -0.69"
    Avoid: not owned. Analyst target 531.31 USD vs 312.24 USD (+70%, 47 analysts); de-biased α -0.5% vs CAPM hurdle 11.2%. Downtrend -15% vs 200-day avg; 12-1 mom -8%; RSI 45. Quality z +0.26 (ROE 31%).

??? failure "Disco (6146.T) — 🔴🔴 Strong Sell, score -0.77"
    Avoid: not owned. Analyst target 81,730 JPY vs 44,440 JPY (+84%, 20 analysts); de-biased α +2.9% vs CAPM hurdle 11.5%. Downtrend -31% vs 200-day avg; 12-1 mom +9%; RSI 46. Quality z +0.06 (ROE 25%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.98"
    Avoid: not owned. Analyst target 569.78 USD vs 420.27 USD (+36%, 26 analysts); de-biased α -9.1% vs CAPM hurdle 10.3%. Downtrend -5% vs 200-day avg; 12-1 mom +20%; RSI 44. Quality z +0.14 (ROE 7%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.05"
    Avoid: not owned. Analyst target 194.13 USD vs 179.44 USD (+8%, 30 analysts); de-biased α -15.8% vs CAPM hurdle 11.9%. Uptrend +5% vs 200-day avg; 12-1 mom +14%; RSI 56. Quality z +0.70 (ROE 23%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.21"
    Avoid: not owned. Analyst target 405.47 USD vs 303.89 USD (+33%, 26 analysts); de-biased α -9.5% vs CAPM hurdle 10.0%. Downtrend -8% vs 200-day avg; 12-1 mom +13%; RSI 45. Quality z +0.31 (ROE 22%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.28"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,644 JPY (+38%, 17 analysts); de-biased α -8.3% vs CAPM hurdle 10.8%. Downtrend -11% vs 200-day avg; 12-1 mom +31%; RSI 49. Quality z -0.20 (ROE 10%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.81"
    Avoid: not owned. Analyst target 95.99 HKD vs 53.40 HKD (+80%, 21 analysts); de-biased α +2.7% vs CAPM hurdle 7.3%. Downtrend -18% vs 200-day avg; 12-1 mom -38%; RSI 59. Quality z -0.99 (ROE 3%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MRVL | Marvell Technology | 601 | 141.01 USD | $84,747 | 10.7% | Strong Buy |
| 005930.KS | Samsung Electronics | 458 | 179,300 KRW | $61,605 | 7.8% | Hold |
| AMAT | Applied Materials | 146 | 323.12 USD | $47,176 | 6.0% | Buy |
| TSM | TSMC | 127 | 350.36 USD | $44,496 | 5.6% | Buy |
| MU | Micron Technology | 64 | 645.37 USD | $41,304 | 5.2% | Strong Buy |
| INTC | Intel | 595 | 57.85 USD | $34,418 | 4.3% | Buy |
| 000660.KS | SK hynix | 41 | 1,103,000 KRW | $33,926 | 4.3% | Strong Buy |
| ASX | ASE Technology | 1,010 | 30.97 USD | $31,280 | 3.9% | Buy |
| TER | Teradyne | 123 | 222.94 USD | $27,422 | 3.5% | Hold |
| LRCX | Lam Research | 136 | 192.68 USD | $26,204 | 3.3% | Hold |
| KLAC | KLA Corp | 150 | 140.89 USD | $21,133 | 2.7% | Hold |
| 6857.T | Advantest | 100 | 26,670 JPY | $16,719 | 2.1% | Hold |
| IFX.DE | Infineon Technologies | 222 | 43.69 EUR | $10,608 | 1.3% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-11-23 12:44 UTC | TRIM | IFX.DE | -147 | 47.12 | $7,589 |
| 2026-11-20 20:22 UTC | ADD | INTC | 365 | 52.70 | $19,236 |
| 2026-11-20 20:22 UTC | ADD | MRVL | 353 | 123.14 | $43,470 |
| 2026-11-20 20:22 UTC | ADD | ASX | 205 | 26.54 | $5,441 |
| 2026-11-20 20:22 UTC | ADD | TER | 88 | 204.82 | $18,024 |
| 2026-11-20 20:22 UTC | ADD | LRCX | 78 | 183.03 | $14,277 |
| 2026-11-20 20:22 UTC | ADD | AMAT | 62 | 303.82 | $18,837 |
| 2026-11-20 20:22 UTC | TRIM | MU | -52 | 596.09 | $30,997 |
| 2026-11-20 20:22 UTC | TRIM | KLAC | -118 | 126.94 | $14,979 |
| 2026-11-20 20:22 UTC | SELL (exit) | NVDA | -268 | 128.30 | $34,384 |
| 2026-11-20 11:54 UTC | ADD | IFX.DE | 144 | 46.65 | $7,364 |
| 2026-11-17 03:55 UTC | TRIM | 000660.KS | -47 | 1,144,000.00 | $40,195 |
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

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 61.5%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
