# Silicon Supply Chain — Top 30 Key Players
### Price history, textbook-grade analysis (Bodie-Kane-Marcus *Investments* 13e) and PEST

**Prices as of:** 2026-09-25 close (USD unless noted; foreign listings converted at spot FX) · **Statistics window:** 2021-09..2026-08 (60m) monthly USD returns · **Risk-free:** 13-wk T-bill 4.07%, 10-yr UST 5.18% · **Assumed MRP:** 5.5%

> ⚠️ Educational analysis, not investment advice. Data from Yahoo Finance and the Kenneth French Data Library; some fundamental fields from data vendors contain errors (flagged where detected). Past returns are noisy estimates of expected returns (BKM ch.5).

**Downloads & code:** [📊 Excel workbook (21 sheets, every number on this page)](Silicon_Supply_Chain_Analysis.xlsx) · [source code](https://github.com/findnavish/InvestmentOpportunities/tree/main/analyses/silicon-supply-chain)

!!! info "Freshness"
    Prices, statistics, tables, charts and the highlighted lists refresh automatically every week (last data update: **2026-09-25**). The interpretive commentary and PEST analysis were last reviewed by hand on **2026-09-23**, so check the tables if a sentence and a number disagree.

---

## 1. Executive summary

1. **The AI capex supercycle has turned the whole chain into a high-beta, momentum-driven asset class.** SOXX gained **114% in 1Y / 277% in 5Y** vs SPY 18% / 86%. Memory had the biggest gains: SK hynix **1,543%**, Micron **1,399%** over 5Y in USD. The five weakest over 1Y: SMIC -18%, SNPS -13%, CDNS -7%, Disco 2%, AVGO 6%.
2. **Risk is dominated by firm-specific risk, not market risk (ch.8).** Betas vs the S&P 500 range from 0.41 (SMIC) to 3.85 (Arm), but the median R² is only 0.32. Most volatility is idiosyncratic, so diversifying *within* the chain has real value (σ falls from 53% for a single stock to 38% for 30 names). It cannot fall below the sector's common-factor floor, though.
3. **Jensen's alphas look huge but are mostly not statistically significant (ch.9, 11, 24).** Against the CAPM, only NVDA (t=2.05), AVGO (t=2.08) clear t≈2. Against Fama-French 5 factors plus momentum, only NVDA, AVGO and Advantest do. Five years of data is too short to separate skill or structural advantage from luck.
4. **Valuation mostly prices in growth rather than current earnings (ch.18).** Outside memory, 53%–95% of each price is PVGO (present value of growth opportunities). The reverse DCF says the market needs stage-1 cash-flow growth of 16%–115% p.a. The most demanding: ARM (~115%), INTC (~87%), MRVL (~76%), Advantest (~76%). NVIDIA needs only ~26% despite ROE×b above 100%, and Broadcom ~16%.
5. **Memory shows the classic cyclical-peak signature (ch.17–18).** Samsung trades at a forward P/E of 4.0, SK hynix at 3.9 and MU at 6.8, against a no-growth P/E of 1/k ≈ 6.5–8.0. That means PVGO is negative: the market is pricing a fall in peak HBM/DRAM earnings. A low P/E at the top of the cycle is a trap unless the cycle turns out to be structurally longer.
6. **Political risk is now a first-order return driver (PEST).** Three dates matter: Section 232 chip tariffs (in force since 15 Jan 2026), the expiry of China's gallium/germanium export-control suspension on 27 Nov 2026, and the CHIPS tax-credit sunset for fab starts after 31 Dec 2026. The US government is also now an Intel shareholder.

---

## 2. The Top 30: who they are and why they matter

The chain runs **design IP/EDA → fabless → foundry/IDM (+ memory) ← equipment ← materials → packaging & test (OSAT)**. The universe covers every chokepoint:

| # | Company | Ticker | Segment | HQ | Mkt cap (USD bn) | Why it's crucial |
|---|---|---|---|---|---|---|
| 1 | NVIDIA | NVDA | Fabless - AI/GPU | US | 5,435 | Dominant AI accelerator (GPU + CUDA + NVLink); largest single consumer of CoWoS & HBM |
| 2 | Broadcom | AVGO | Fabless - Networking/Custom ASIC | US | 1,684 | Custom AI ASICs (TPU-class XPUs) for hyperscalers + Ethernet/switch silicon |
| 3 | Advanced Micro Devices | AMD | Fabless - CPU/GPU | US | 1,029 | #2 merchant AI GPU (Instinct) and x86 CPU share gainer |
| 4 | Qualcomm | QCOM | Fabless - Mobile/Edge | US | 216 | Mobile SoC/modem leader; edge-AI, auto and PC (Arm) diversification |
| 5 | Marvell Technology | MRVL | Fabless - Data Infra/Custom ASIC | US | 235 | Custom ASICs, electro-optics/DSPs for AI data-center interconnect |
| 6 | Arm Holdings | ARM | IP - CPU Architecture | UK | 331 | Instruction-set/IP licensor in ~all mobile and a rising share of data-center CPUs |
| 7 | Synopsys | SNPS | EDA & IP | US | 82 | EDA + interface IP duopolist (post-Ansys: simulation); no chip gets designed without it |
| 8 | Cadence Design Systems | CDNS | EDA & IP | US | 90 | EDA duopolist (analog/custom, verification hardware, system analysis) |
| 9 | TSMC | TSM | Foundry - Leading Edge | Taiwan | 2,337 | ~70%+ foundry share, ~all leading-edge (N3/N2/A16) logic + CoWoS packaging — the system's chokepoint |
| 10 | Samsung Electronics | 005930.KS | IDM - Memory/Foundry | South Korea | 1,371 | Memory #1-2 (DRAM/NAND/HBM) + #2 foundry; Korea's national champion |
| 11 | Intel | INTC | IDM - Logic/Foundry | US | 650 | x86 IDM rebuilding foundry (18A/14A); US-government equity stake; CHIPS flagship |
| 12 | GlobalFoundries | GFS | Foundry - Specialty/Mature | US | 27 | Largest US-HQ specialty/mature-node foundry (RF, FD-SOI, silicon photonics) |
| 13 | SMIC | 0981.HK | Foundry - China | China | 69 | China's largest foundry; spearhead of Chinese self-sufficiency under export controls |
| 14 | Texas Instruments | TXN | IDM - Analog | US | 254 | Analog/embedded leader with 300mm US fabs; industrial/auto bellwether |
| 15 | Infineon Technologies | IFX.DE | IDM - Power/Auto | Germany | 84 | #1 power semis (SiC/GaN) & auto MCUs; Europe's anchor for AI data-center power |
| 16 | Micron Technology | MU | Memory - DRAM/HBM/NAND | US | 1,222 | Only US memory maker; HBM3E/HBM4 supplier; CHIPS-funded US DRAM fabs |
| 17 | SK hynix | 000660.KS | Memory - DRAM/HBM | South Korea | 967 | HBM leader (primary HBM supplier to NVIDIA); DRAM #1-2 |
| 18 | ASML Holding | ASML | Equipment - Lithography (EUV) | Netherlands | 670 | Monopoly in EUV (and High-NA EUV) lithography — irreplaceable chokepoint |
| 19 | Applied Materials | AMAT | Equipment - Deposition/Etch | US | 385 | Largest WFE vendor: deposition, etch, implant, GAA/backside-power tooling |
| 20 | Lam Research | LRCX | Equipment - Etch/Deposition | US | 394 | Etch/deposition leader; critical for 3D NAND, HBM TSVs, GAA |
| 21 | KLA Corp | KLAC | Equipment - Process Control | US | 245 | Process control/inspection near-monopoly; yield is its product |
| 22 | Tokyo Electron | 8035.T | Equipment - Coat/Develop/Etch | Japan | 162 | Coater/developer monopoly on EUV tracks + etch/deposition; Japan's WFE champion |
| 23 | ASM International | ASM.AS | Equipment - ALD/Epitaxy | Netherlands | 47 | ALD and epitaxy leader — key to GAA transistors |
| 24 | Advantest | 6857.T | Equipment - Test | Japan | 155 | SoC/HBM test leader (AI GPU test is its growth engine) |
| 25 | Disco Corp | 6146.T | Equipment - Dicing/Grinding | Japan | 37 | Dicing/grinding/polishing near-monopoly; essential for HBM stacking & advanced packaging |
| 26 | Teradyne | TER | Equipment - Test | US | 62 | SoC/memory test #2; robotics; AI compute test exposure |
| 27 | Shin-Etsu Chemical | 4063.T | Materials - Silicon Wafers/Photoresist | Japan | 67 | #1 silicon wafer supplier + photoresists/photomask blanks |
| 28 | Entegris | ENTG | Materials - Specialty Chem/Filtration | US | 23 | Ultra-pure materials, filtration, CMP — contamination control for advanced nodes |
| 29 | ASE Technology | ASX | OSAT - Advanced Packaging | Taiwan | 115 | #1 OSAT (ASE/SPIL); CoWoS-like advanced packaging & test overflow for TSMC |
| 30 | Amkor Technology | AMKR | OSAT - Advanced Packaging | US | 13 | #2 OSAT; building the first large US advanced-packaging site (Arizona) |

*Omitted for size or data reasons, but important:* Nexperia, Kioxia, Lasertec, BESI (hybrid bonding), Ibiden (substrates), SUMCO, Soitec, Linde and Air Liquide (gases), JSR/TOK (resists), Zeiss (EUV optics, private), UMC, Rapidus (private), Hua Hong, Naura/AMEC (China WFE).

---

## 3. Price over time

![Price history](charts/01_price_history_by_segment.png)
![Trailing returns](charts/02_trailing_returns.png)

| Ticker | Local px | 1M | YTD | 1Y | 3Y | 5Y | vs 52w high | Max DD (5Y) |
|---|---|---|---|---|---|---|---|---|
| NVDA | 225.07 USD | 7% | 21% | 27% | 439% | 924% | -4% | -66% |
| AVGO | 352.81 USD | -1% | 3% | 6% | 347% | 663% | -26% | -41% |
| AMD | 630.63 USD | 31% | 194% | 291% | 557% | 496% | 0% | -65% |
| QCOM | 201.97 USD | 24% | 20% | 22% | 96% | 68% | -19% | -44% |
| MRVL | 261.94 USD | 7% | 209% | 213% | 411% | 320% | -17% | -62% |
| ARM | 310.32 USD | 24% | 184% | 121% | 480% | – | -29% | -54% |
| SNPS | 425.76 USD | 4% | -9% | -13% | -4% | 32% | -20% | -43% |
| CDNS | 326.13 USD | -3% | 4% | -7% | 42% | 99% | -22% | -34% |
| TSM | 450.61 USD | 8% | 49% | 65% | 456% | 322% | -5% | -56% |
| 005930.KS | 285,500.00 KRW | 12% | 154% | 249% | 334% | 255% | -11% | -54% |
| INTC | 123.00 USD | 39% | 233% | 262% | 270% | 146% | -13% | -71% |
| GFS | 49.00 USD | 8% | 41% | 50% | -13% | – | -45% | -62% |
| 0981.HK | 63.35 HKD | -9% | -12% | -18% | 226% | 186% | -31% | -54% |
| TXN | 278.07 USD | 6% | 63% | 57% | 92% | 60% | -16% | -33% |
| IFX.DE | 56.71 EUR | 0% | 46% | 66% | 104% | 53% | -37% | -56% |
| MU | 1,082.28 USD | 15% | 279% | 591% | 1,511% | 1,399% | -11% | -58% |
| 000660.KS | 1,862,000.00 KRW | 13% | 205% | 445% | 1,536% | 1,543% | -28% | -57% |
| ASML | 1,743.94 USD | -0% | 64% | 85% | 212% | 110% | -12% | -57% |
| AMAT | 485.00 USD | 1% | 89% | 144% | 270% | 256% | -33% | -55% |
| LRCX | 315.21 USD | 1% | 85% | 147% | 433% | 443% | -27% | -56% |
| KLAC | 187.92 USD | 2% | 55% | 78% | 332% | 434% | -38% | -44% |
| 8035.T | 56,520.00 JPY | 2% | 63% | 95% | 178% | 145% | -27% | -58% |
| ASM.AS | 844.60 EUR | 0% | 59% | 65% | 146% | 141% | -22% | -57% |
| 6857.T | 34,000.00 JPY | -5% | 70% | 113% | 702% | 786% | -10% | -55% |
| 6146.T | 54,220.00 JPY | -10% | 11% | 2% | 98% | 264% | -38% | -61% |
| TER | 398.38 USD | 10% | 106% | 200% | 320% | 240% | -18% | -59% |
| 4063.T | 5,889.00 JPY | -1% | 20% | 18% | 30% | 11% | -25% | -47% |
| ENTG | 151.89 USD | 7% | 81% | 66% | 73% | 17% | -17% | -59% |
| ASX | 44.31 USD | 19% | 178% | 291% | 556% | 551% | -2% | -46% |
| AMKR | 53.61 USD | 11% | 36% | 85% | 153% | 112% | -43% | -66% |
| SOXX | 572.68 USD | 11% | 90% | 114% | 280% | 277% | -13% | -46% |
| SPY | 771.35 USD | 1% | 14% | 18% | 88% | 86% | -1% | -24% |
| ACWI | 161.05 USD | 0% | 15% | 20% | 84% | 71% | -1% | -26% |

**Reading the tape**
- **Leadership rotated.** In 2023–24 the story was "GPU + TSMC". In 2025–26 the gains broadened to **memory (HBM)**, **Samsung**, **test (Advantest, Teradyne)**, **OSAT (ASE)** and a speculative **Intel/AMD/Arm** rally. Broadcom and EDA lagged.
- **Drawdowns are brutal (ch.5 tail risk).** Every name except CDNS and TXN lost more than 40% peak-to-trough within the last 5 years. Intel lost -71%, NVIDIA -66% and SOXX -46%. The April-2025 tariff shock is visible across all panels.
- **Distance from 52-week highs** shows the summer-2026 correction: SOXX is -13% from its high, with GFS, AMKR, Disco and KLAC 38%–45% off.

![Drawdowns](charts/08_drawdowns.png)

---

## 4. Risk & return statistics (BKM ch.5)

| Ticker | Arith. mean | Geo. mean | σ (ann.) | Sharpe | Sortino | Skew | Ex. kurt | VaR 5% (1m) | ES 5% (1m) |
|---|---|---|---|---|---|---|---|---|---|
| NVDA | 78% | 58% | 50% | 1.10 | 2.08 | -0.01 | -0.30 | -17.0% | -23.5% |
| AVGO | 64% | 52% | 42% | 1.13 | 2.52 | 0.84 | 1.35 | -14.0% | -15.6% |
| AMD | 62% | 34% | 69% | 0.67 | 1.46 | 1.21 | 1.98 | -20.7% | -24.0% |
| QCOM | 15% | 5% | 45% | 0.24 | 0.44 | 1.07 | 1.74 | -13.2% | -20.3% |
| MRVL | 56% | 29% | 66% | 0.63 | 1.17 | 0.69 | 1.52 | -22.0% | -32.1% |
| ARM | 129% | 68% | 92% | 0.89 | 2.28 | 1.56 | 3.54 | -19.6% | -26.3% |
| SNPS | 12% | 6% | 35% | 0.22 | 0.36 | 0.37 | -0.40 | -13.1% | -16.0% |
| CDNS | 21% | 16% | 30% | 0.51 | 0.87 | 0.27 | 0.06 | -11.5% | -15.7% |
| TSM | 39% | 31% | 37% | 0.81 | 1.49 | 0.39 | 0.23 | -13.8% | -15.5% |
| 005930.KS | 39% | 26% | 47% | 0.63 | 1.25 | 0.84 | 1.01 | -15.3% | -20.5% |
| INTC | 36% | 12% | 71% | 0.39 | 0.85 | 2.75 | 14.36 | -19.7% | -31.4% |
| GFS | 14% | -2% | 54% | 0.17 | 0.26 | 0.30 | 1.07 | -19.9% | -31.9% |
| 0981.HK | 40% | 24% | 51% | 0.60 | 1.07 | 0.40 | 0.60 | -15.0% | -28.0% |
| TXN | 15% | 10% | 35% | 0.31 | 0.60 | 1.61 | 5.01 | -10.2% | -12.2% |
| IFX.DE | 23% | 10% | 51% | 0.34 | 0.63 | 1.12 | 2.28 | -18.2% | -22.0% |
| MU | 101% | 68% | 68% | 1.01 | 2.48 | 1.52 | 4.31 | -16.5% | -24.0% |
| 000660.KS | 106% | 70% | 71% | 1.01 | 2.57 | 1.42 | 3.01 | -17.6% | -25.8% |
| ASML | 27% | 16% | 43% | 0.47 | 0.82 | 0.44 | -0.10 | -15.7% | -18.2% |
| AMAT | 43% | 29% | 49% | 0.67 | 1.27 | 0.97 | 3.49 | -13.1% | -22.8% |
| LRCX | 55% | 39% | 49% | 0.85 | 1.60 | 0.22 | 0.07 | -16.2% | -22.7% |
| KLAC | 54% | 40% | 45% | 0.89 | 1.70 | 0.64 | 5.00 | -12.6% | -22.1% |
| 8035.T | 39% | 23% | 51% | 0.58 | 0.96 | 0.15 | 0.19 | -20.7% | -26.7% |
| ASM.AS | 35% | 20% | 50% | 0.53 | 0.92 | 0.35 | -0.14 | -19.3% | -22.3% |
| 6857.T | 88% | 59% | 63% | 0.97 | 2.11 | 0.82 | 1.16 | -20.0% | -26.2% |
| 6146.T | 48% | 32% | 50% | 0.73 | 1.29 | 0.21 | -0.21 | -19.6% | -23.3% |
| TER | 40% | 24% | 50% | 0.61 | 0.99 | -0.05 | -0.42 | -20.9% | -25.7% |
| 4063.T | 10% | 5% | 33% | 0.19 | 0.30 | 0.19 | -0.28 | -11.3% | -17.5% |
| ENTG | 14% | 3% | 48% | 0.21 | 0.35 | 0.68 | 1.12 | -15.2% | -22.2% |
| ASX | 53% | 39% | 46% | 0.85 | 1.77 | 0.94 | 1.75 | -13.5% | -18.9% |
| AMKR | 31% | 13% | 56% | 0.42 | 0.73 | 0.52 | 1.32 | -16.9% | -26.5% |
| SOXX | 36% | 28% | 38% | 0.74 | 1.38 | 0.56 | 1.35 | -13.4% | -18.1% |
| SPY | 14% | 13% | 16% | 0.60 | 0.96 | -0.26 | -0.38 | -5.9% | -8.8% |

- **Arithmetic > geometric** means everywhere. The gap is roughly σ²/2, so high-volatility names (INTC, AMD, MRVL, ARM) lose the most to volatility drag. Intel's arithmetic mean is 36%, but it compounded at only 12%.
- **Non-normality.** Returns are mostly *positively* skewed (a "lottery-like" right tail) with fat tails; Intel's excess kurtosis is 14.4. So VaR/ES are more informative than σ alone. A 1-in-20 bad month (VaR 5%) costs 10%–22%.
- **Sharpe ratios:** Broadcom 1.13, NVIDIA 1.10, Micron and SK hynix ~1.01 vs SPY 0.60. Ex post, the sector's risk was well paid, but that is the *realized* outcome of a boom, not an ex-ante expectation.

---

## 5. Single-index model & CAPM (BKM ch.8–9)

$R_i = \alpha_i + \beta_i R_M + e_i$ (monthly excess returns vs SPY), Blume-adjusted $\beta_{adj} = \tfrac{2}{3}\hat\beta + \tfrac{1}{3}$, and $k = r_f^{10y} + \beta_{adj} \times MRP$.

| Ticker | β (SPY) | Adj. β | β (SOXX) | α (ann.) | t(α) | R² | σ(e) | CAPM k |
|---|---|---|---|---|---|---|---|---|
| NVDA | 2.21 | 1.81 | 0.90 | 34.0% | 2.05 | 0.48 | 36% | 15.1% |
| AVGO | 1.44 | 1.29 | 0.64 | 33.1% | 2.08 | 0.30 | 35% | 12.3% |
| AMD | 2.49 | 1.99 | 1.55 | 21.9% | 0.85 | 0.33 | 56% | 16.1% |
| QCOM | 1.68 | 1.46 | 0.84 | -5.4% | -0.32 | 0.35 | 36% | 13.2% |
| MRVL | 2.26 | 1.84 | 1.35 | 20.0% | 0.79 | 0.29 | 55% | 15.3% |
| ARM | 3.85 | 2.90 | 1.51 | 12.9% | 0.26 | 0.28 | 78% | 21.1% |
| SNPS | 1.24 | 1.16 | 0.51 | -4.1% | -0.31 | 0.31 | 29% | 11.5% |
| CDNS | 1.14 | 1.09 | 0.49 | 4.5% | 0.40 | 0.35 | 24% | 11.2% |
| TSM | 1.37 | 1.25 | 0.75 | 16.5% | 1.22 | 0.35 | 30% | 12.0% |
| 005930.KS | 1.50 | 1.33 | 0.88 | 15.5% | 0.83 | 0.25 | 41% | 12.5% |
| INTC | 2.24 | 1.82 | 1.34 | 6.4% | 0.23 | 0.25 | 61% | 15.2% |
| GFS | 1.80 | 1.53 | 1.06 | -8.0% | -0.37 | 0.27 | 47% | 13.6% |
| 0981.HK | 0.41 | 0.61 | 0.32 | 26.5% | 1.15 | 0.02 | 50% | 8.5% |
| TXN | 1.34 | 1.22 | 0.67 | -2.0% | -0.16 | 0.37 | 27% | 11.9% |
| IFX.DE | 2.22 | 1.82 | 1.10 | -3.9% | -0.23 | 0.48 | 37% | 15.2% |
| MU | 2.23 | 1.82 | 1.40 | 47.1% | 1.77 | 0.27 | 58% | 15.2% |
| 000660.KS | 2.31 | 1.88 | 1.50 | 48.7% | 1.76 | 0.27 | 60% | 15.5% |
| ASML | 1.78 | 1.52 | 0.88 | 3.1% | 0.21 | 0.43 | 32% | 13.5% |
| AMAT | 1.59 | 1.39 | 1.00 | 17.6% | 0.91 | 0.26 | 42% | 12.8% |
| LRCX | 1.85 | 1.57 | 1.11 | 23.4% | 1.32 | 0.36 | 39% | 13.8% |
| KLAC | 1.44 | 1.29 | 0.91 | 26.5% | 1.48 | 0.25 | 39% | 12.3% |
| 8035.T | 1.85 | 1.56 | 1.08 | 12.0% | 0.62 | 0.32 | 42% | 13.8% |
| ASM.AS | 1.99 | 1.66 | 1.07 | 7.5% | 0.42 | 0.40 | 39% | 14.3% |
| 6857.T | 2.02 | 1.68 | 1.12 | 41.8% | 1.68 | 0.26 | 54% | 14.4% |
| 6146.T | 1.54 | 1.36 | 0.90 | 21.6% | 1.08 | 0.24 | 44% | 12.7% |
| TER | 1.79 | 1.52 | 0.97 | 13.0% | 0.70 | 0.32 | 41% | 13.6% |
| 4063.T | 1.32 | 1.22 | 0.56 | -6.4% | -0.55 | 0.41 | 25% | 11.9% |
| ENTG | 1.36 | 1.24 | 0.91 | -3.1% | -0.16 | 0.20 | 43% | 12.0% |
| ASX | 1.70 | 1.47 | 1.04 | 23.0% | 1.33 | 0.34 | 38% | 13.3% |
| AMKR | 2.23 | 1.82 | 1.20 | 2.2% | 0.11 | 0.39 | 44% | 15.2% |
| SOXX | 1.80 | 1.53 | 1.00 | 10.5% | 0.93 | 0.57 | 25% | 13.6% |

![SML](charts/03_security_market_line.png)

**Takeaways**
- **Cost of equity is high: 8–21%, mostly 12–21%.** A 5.1% 10-year yield combined with β_adj of 0.6 (SMIC) to 2.9 (Arm) gives k = 8–21%. That is why long-duration growth names (ARM, AMD, MRVL) are so sensitive to rates.
- **Systematic share of variance (R²)** is only 2–48% (median 0.32). SMIC's R² of 0.02 shows **market segmentation (ch.25)**: its price is driven by China policy, not the US market.
- Nearly every name plots **above the ex-post SML** (positive Jensen α), but t-stats are mostly below 2. Per ch.11/13 this is consistent with a *sector-specific* shock (AI demand) that CAPM does not price, not with persistent mispricing.
- **β vs SOXX** is the right hedge ratio for sector-relative trades: MU 1.40, SK hynix 1.50, AMD 1.55, while Synopsys and Cadence are ~0.5. EDA works as a *defensive* sleeve inside semis.

---

## 6. Multifactor exposures — Fama-French 5 + Momentum (BKM ch.10, 13)

Factors through 2026-08; coefficients are loadings.

| Ticker | FF α (ann.) | t(α) | Mkt | SMB | HML | RMW | CMA | MOM | R² |
|---|---|---|---|---|---|---|---|---|---|
| NVDA | 43.0% | 2.75 | 2.03 | -0.48 | -1.09 | 0.60 | -0.18 | -0.19 | 0.62 |
| AVGO | 38.4% | 2.34 | 1.36 | -0.29 | -0.98 | 0.35 | 0.33 | 0.24 | 0.39 |
| AMD | 27.6% | 1.06 | 2.16 | -0.68 | -0.23 | -1.19 | -1.07 | 0.45 | 0.44 |
| QCOM | -8.4% | -0.49 | 1.57 | -1.04 | 0.81 | -0.60 | -1.24 | -0.29 | 0.42 |
| MRVL | 27.2% | 1.15 | 1.95 | 0.03 | -0.34 | -1.69 | -0.70 | 0.92 | 0.49 |
| ARM | 28.9% | 0.56 | 2.26 | -0.14 | -2.00 | -2.88 | 0.61 | 0.70 | 0.49 |
| SNPS | 0.4% | 0.03 | 1.04 | -0.05 | -0.20 | 0.16 | -0.94 | 0.13 | 0.42 |
| CDNS | 10.8% | 1.07 | 0.94 | -0.14 | -0.63 | 0.01 | -0.55 | 0.24 | 0.56 |
| TSM | 20.2% | 1.41 | 1.29 | -0.60 | -0.48 | -0.47 | 0.30 | -0.13 | 0.41 |
| 005930.KS | 14.1% | 0.70 | 1.49 | -0.53 | 0.26 | -1.00 | 0.36 | -0.01 | 0.29 |
| INTC | -0.9% | -0.03 | 2.20 | -0.06 | 1.10 | -1.44 | -0.73 | 1.20 | 0.39 |
| GFS | -5.4% | -0.24 | 1.75 | 1.04 | -0.03 | -0.20 | -0.03 | 1.04 | 0.37 |
| 0981.HK | 21.4% | 0.90 | 0.41 | -1.10 | 0.21 | -1.14 | -0.26 | 0.47 | 0.14 |
| TXN | -2.4% | -0.18 | 1.35 | 0.51 | 0.17 | 0.19 | 0.07 | 0.39 | 0.41 |
| IFX.DE | -7.0% | -0.39 | 2.25 | -0.60 | 0.30 | -0.76 | 0.19 | 0.27 | 0.51 |
| MU | 45.0% | 1.70 | 2.16 | -1.05 | 0.48 | -2.33 | 0.26 | 0.18 | 0.40 |
| 000660.KS | 50.2% | 1.87 | 2.14 | -1.46 | -0.10 | -2.51 | 0.27 | 0.19 | 0.43 |
| ASML | 4.8% | 0.30 | 1.73 | -0.01 | -0.12 | -0.22 | -0.02 | 0.30 | 0.45 |
| AMAT | 20.1% | 1.02 | 1.53 | 0.43 | -0.24 | -0.68 | 0.22 | 0.79 | 0.36 |
| LRCX | 26.2% | 1.43 | 1.75 | 0.06 | -0.14 | -0.85 | 0.04 | 0.52 | 0.44 |
| KLAC | 24.7% | 1.39 | 1.42 | 0.16 | 0.14 | -0.71 | -0.14 | 0.97 | 0.40 |
| 8035.T | 15.9% | 0.83 | 1.78 | -0.09 | -0.51 | -1.29 | 0.72 | 0.57 | 0.45 |
| ASM.AS | 14.9% | 0.82 | 1.79 | -0.09 | -0.78 | -0.39 | -0.11 | 0.42 | 0.48 |
| 6857.T | 54.9% | 2.12 | 1.84 | 0.44 | -1.66 | -0.55 | 1.32 | 0.49 | 0.33 |
| 6146.T | 24.9% | 1.22 | 1.56 | 0.82 | -0.75 | 0.06 | 0.79 | 1.07 | 0.34 |
| TER | 22.7% | 1.15 | 1.65 | 1.05 | -0.91 | -0.04 | 0.68 | 0.54 | 0.38 |
| 4063.T | -5.1% | -0.41 | 1.32 | -0.00 | 0.14 | -0.32 | 0.28 | -0.21 | 0.43 |
| ENTG | 5.6% | 0.29 | 1.11 | 0.80 | -0.12 | -1.05 | -0.46 | 0.32 | 0.35 |
| ASX | 24.4% | 1.35 | 1.64 | -0.35 | -0.13 | -0.99 | 0.33 | 0.29 | 0.40 |
| AMKR | 1.8% | 0.09 | 2.19 | 0.41 | 0.36 | -0.70 | -0.13 | 0.70 | 0.47 |

- **HML strongly negative** for NVDA, AVGO, ARM and Advantest: these are pure *growth* exposures that suffer when value rallies.
- **RMW negative** for memory, SMIC, Samsung, Intel and ARM: returns co-move with *unprofitable* firms, a signature of cyclicality and speculation.
- **Momentum loadings** are significant for KLAC, Disco, GFS and Intel. Momentum crashes (ch.12) are therefore a real portfolio risk.
- Alphas that **survive** 6 factors: NVDA 43% (t=2.75), AVGO 38% (t=2.34), Advantest 55% (t=2.12). These are the AI-bottleneck owners (GPU, custom ASIC, HBM, HBM/GPU test).

---

## 7. Performance evaluation (BKM ch.24)

Sharpe (total risk), Treynor (β risk), Jensen α, Information ratio = α/σ(e), and M² = (S_p − S_M)·σ_M, a return-equivalent at market volatility.

| Ticker | Sharpe | Treynor | Jensen α | Info ratio | M² |
|---|---|---|---|---|---|
| AVGO | 1.13 | 32.6% | 33.1% | 0.95 | 8.2% |
| NVDA | 1.10 | 25.0% | 34.0% | 0.94 | 7.7% |
| MU | 1.01 | 30.7% | 47.1% | 0.81 | 6.3% |
| 000660.KS | 1.01 | 30.7% | 48.7% | 0.81 | 6.3% |
| 6857.T | 0.97 | 30.3% | 41.8% | 0.77 | 5.8% |
| KLAC | 0.89 | 28.0% | 26.5% | 0.68 | 4.5% |
| ARM | 0.89 | 21.1% | 12.9% | 0.17 | 4.4% |
| LRCX | 0.85 | 22.3% | 23.4% | 0.61 | 3.8% |
| ASX | 0.85 | 23.1% | 23.0% | 0.61 | 3.8% |
| TSM | 0.81 | 21.7% | 16.5% | 0.56 | 3.2% |
| SOXX | 0.74 | 15.4% | 10.5% | 0.43 | 2.1% |
| 6146.T | 0.73 | 23.6% | 21.6% | 0.50 | 2.0% |
| AMAT | 0.67 | 20.7% | 17.6% | 0.42 | 1.0% |
| AMD | 0.67 | 18.4% | 21.9% | 0.39 | 1.0% |
| MRVL | 0.63 | 18.4% | 20.0% | 0.36 | 0.5% |
| 005930.KS | 0.63 | 19.9% | 15.5% | 0.38 | 0.4% |
| TER | 0.61 | 16.9% | 13.0% | 0.32 | 0.0% |
| SPY | 0.60 | 9.6% | 0.0% | – | 0.0% |
| 0981.HK | 0.60 | 74.6% | 26.5% | 0.53 | -0.1% |
| 8035.T | 0.58 | 16.1% | 12.0% | 0.28 | -0.4% |
| ASM.AS | 0.53 | 13.4% | 7.5% | 0.19 | -1.1% |
| CDNS | 0.51 | 13.6% | 4.5% | 0.18 | -1.5% |
| ASML | 0.47 | 11.4% | 3.1% | 0.10 | -2.1% |
| AMKR | 0.42 | 10.6% | 2.2% | 0.05 | -2.9% |
| INTC | 0.39 | 12.4% | 6.4% | 0.10 | -3.3% |
| IFX.DE | 0.34 | 7.9% | -3.9% | -0.11 | -4.1% |
| TXN | 0.31 | 8.1% | -2.0% | -0.07 | -4.6% |
| QCOM | 0.24 | 6.4% | -5.4% | -0.15 | -5.8% |
| SNPS | 0.22 | 6.3% | -4.1% | -0.14 | -6.0% |
| ENTG | 0.21 | 7.3% | -3.1% | -0.07 | -6.3% |
| 4063.T | 0.19 | 4.8% | -6.4% | -0.25 | -6.5% |
| GFS | 0.17 | 5.0% | -8.0% | -0.17 | -6.9% |

**Which measure to use (ch.24):** use **Sharpe/M²** if the stock *is* your whole risky portfolio, **Treynor/Jensen** if it is one of many holdings in a diversified portfolio, and the **information ratio** for an active satellite added to an index core. By M², the leaders are AVGO, NVDA, MU, SK hynix, Advantest and KLAC and the laggards are GFS, Shin-Etsu, ENTG, SNPS and QCOM.

---

## 8. Currency decomposition for foreign listings (BKM ch.25)

$1 + r_{USD} = (1 + r_{local})(1 + r_{FX})$

| Ticker | Window | Ccy | Local return | FX vs USD | USD return | FX contribution |
|---|---|---|---|---|---|---|
| 005930.KS | 1Y | KRW | 241% | 1.6% | 247% | 5% |
| 005930.KS | 5Y | KRW | 308% | -13.6% | 252% | -56% |
| 0981.HK | 1Y | HKD | -18% | -0.8% | -18% | -1% |
| 0981.HK | 5Y | HKD | 189% | -0.7% | 186% | -2% |
| IFX.DE | 1Y | EUR | 72% | -3.1% | 66% | -5% |
| IFX.DE | 5Y | EUR | 58% | -3.1% | 53% | -5% |
| 000660.KS | 1Y | KRW | 417% | 1.6% | 426% | 8% |
| 000660.KS | 5Y | KRW | 1,762% | -13.6% | 1,508% | -254% |
| 8035.T | 1Y | JPY | 108% | -6.3% | 95% | -13% |
| 8035.T | 5Y | JPY | 252% | -30.5% | 145% | -108% |
| ASM.AS | 1Y | EUR | 70% | -3.1% | 65% | -5% |
| ASM.AS | 5Y | EUR | 149% | -3.1% | 141% | -8% |
| 6857.T | 1Y | JPY | 127% | -6.3% | 113% | -14% |
| 6857.T | 5Y | JPY | 1,175% | -30.5% | 786% | -389% |
| 6146.T | 1Y | JPY | 9% | -6.3% | 2% | -7% |
| 6146.T | 5Y | JPY | 424% | -30.5% | 264% | -160% |
| 4063.T | 1Y | JPY | 26% | -6.3% | 18% | -8% |
| 4063.T | 5Y | JPY | 60% | -30.5% | 11% | -49% |

- **Yen weakness (−30% vs USD over 5Y)** cost US investors a lot: Advantest made +1,175% in yen but only +786% in USD, and Shin-Etsu's +53% in yen became +6%.
- KRW fell 12.5% over 5Y but *helped* over the last year (+2.9%). Currency exposure is a separate bet (ch.25): hedge it with forwards (interest-rate parity, ch.23) if you want pure equity exposure.

---

## 9. Financial statement analysis — DuPont & earnings quality (BKM ch.19)

$ROE = \underbrace{\tfrac{NI}{PTI}}_{\text{tax}} \times \underbrace{\tfrac{PTI}{EBIT}}_{\text{interest}} \times \underbrace{\tfrac{EBIT}{Sales}}_{\text{margin}} \times \underbrace{\tfrac{Sales}{Assets}}_{\text{turnover}} \times \underbrace{\tfrac{Assets}{Equity}}_{\text{leverage}}$ (latest fiscal year)

| Ticker | FY | Gross m. | EBIT m. | Tax burden | Int. burden | Asset turn | Leverage | ROE | R&D/Sales | Capex/Sales | FCF/NI | Accruals | DOL | Int. cover | Net cash (USD bn) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NVDA | 2026-01 | 71% | 66% | 0.85 | 1.00 | 1.36 | 1.35 | 101% | 9% | 3% | 0.81 | 0.109 | 1.0 | 547 | -0.4 |
| AVGO | 2025-10 | 68% | 41% | 1.02 | 0.88 | 0.38 | 2.26 | 31% | 17% | 1% | 1.16 | -0.026 | 3.6 | 8 | -49.0 |
| AMD | 2025-12 | 50% | 12% | 1.05 | 0.97 | 0.47 | 1.21 | 7% | 23% | 3% | 1.55 | -0.046 | 3.1 | 33 | 1.7 |
| QCOM | 2025-09 | 55% | 30% | 0.44 | 0.95 | 0.84 | 2.22 | 23% | 20% | 3% | 2.31 | -0.161 | 1.5 | 20 | -9.3 |
| MRVL | 2026-01 | 51% | 40% | 0.88 | 0.94 | 0.39 | 1.53 | 19% | 25% | 4% | 0.52 | 0.043 | -13.3 | 16 | -2.2 |
| ARM | 2026-03 | 98% | 18% | 0.78 | 1.27 | 0.50 | 1.30 | 12% | 56% | 12% | 1.05 | -0.063 | 0.4 | – | 2.3 |
| SNPS | 2025-10 | 77% | 26% | 0.96 | 0.76 | 0.23 | 1.64 | 7% | 35% | 2% | 1.01 | -0.006 | 1.2 | 4 | -11.4 |
| CDNS | 2025-12 | 86% | 31% | 0.73 | 0.93 | 0.55 | 1.88 | 22% | 33% | 3% | 1.43 | -0.065 | 0.8 | 14 | 0.4 |
| TSM | 2025-12 | 60% | 54% | 0.83 | 0.99 | 0.52 | 1.52 | 35% | 6% | 34% | 0.58 | -0.079 | 1.4 | 166 | 53.7 |
| 005930.KS | 2025-12 | 39% | 15% | 0.89 | 0.99 | 0.62 | 1.33 | 11% | 11% | 16% | 0.75 | -0.076 | 2.8 | 83 | 23.9 |
| INTC | 2025-12 | 35% | 5% | -0.17 | 0.59 | 0.26 | 1.91 | -0% | 26% | 28% | – | -0.049 | – | 2 | -32.3 |
| GFS | 2025-12 | 25% | 14% | 0.97 | 0.95 | 0.40 | 1.49 | 8% | 8% | 11% | 1.14 | -0.050 | – | 19 | 0.1 |
| 0981.HK | 2025-12 | 21% | 16% | 0.64 | 0.74 | 0.18 | 2.41 | 3% | 8% | 90% | -7.60 | -0.049 | 2.9 | 4 | -6.7 |
| TXN | 2025-12 | 57% | 35% | 0.88 | 0.91 | 0.50 | 2.11 | 30% | 12% | 26% | 0.52 | -0.061 | 0.4 | 12 | -10.8 |
| IFX.DE | 2025-09 | 39% | 11% | 0.74 | 0.86 | 0.50 | 1.72 | 6% | 15% | 14% | 1.11 | -0.075 | – | 7 | -6.7 |
| MU | 2025-08 | 40% | 27% | 0.88 | 0.95 | 0.49 | 1.53 | 17% | 10% | 42% | 0.20 | -0.118 | 9.5 | 21 | -5.6 |
| 000660.KS | 2025-12 | 60% | 53% | 0.85 | 0.98 | 0.66 | 1.52 | 44% | 7% | 29% | 0.58 | -0.071 | 2.2 | 56 | -7.2 |
| ASML | 2025-12 | 53% | 35% | 0.84 | 0.99 | 0.66 | 2.60 | 50% | 14% | 5% | 1.15 | – | 1.6 | 97 | 9.7 |
| AMAT | 2025-10 | 49% | 34% | 0.75 | 0.97 | 0.80 | 1.79 | 36% | 13% | 8% | 0.81 | -0.027 | 3.1 | 35 | 0.2 |
| LRCX | 2026-06 | 50% | 36% | 0.88 | 0.98 | 1.04 | 2.01 | 65% | 10% | 4% | 0.67 | 0.063 | 1.4 | 54 | 1.8 |
| KLAC | 2026-06 | 61% | 43% | 0.86 | 0.95 | 0.80 | 3.08 | 87% | 11% | 3% | 0.78 | 0.040 | 1.6 | 21 | -4.5 |
| 8035.T | 2026-03 | 45% | 26% | 0.77 | 1.20 | 0.89 | 1.40 | 29% | 11% | 9% | 0.56 | 0.013 | – | – | – |
| ASM.AS | 2025-12 | 52% | 29% | 0.78 | 1.00 | 0.60 | 1.35 | 19% | 13% | 15% | 0.82 | -0.064 | 0.8 | 1,029 | 1.2 |
| 6857.T | 2026-03 | 64% | 46% | 0.73 | 0.99 | 1.11 | 1.56 | 58% | – | 3% | 0.80 | 0.040 | 2.8 | 189 | 2.0 |
| 6146.T | 2026-03 | 70% | 42% | 0.74 | 0.99 | 0.63 | 1.29 | 25% | – | 8% | 0.73 | 0.003 | 1.0 | – | – |
| TER | 2025-12 | 58% | 21% | 0.85 | 0.99 | 0.81 | 1.41 | 20% | 16% | 7% | 0.81 | -0.031 | 0.6 | 96 | 0.0 |
| 4063.T | 2026-03 | 34% | 28% | 0.67 | 1.00 | 0.46 | 1.24 | 10% | – | 14% | 0.75 | -0.042 | – | 263 | 8.9 |
| ENTG | 2025-12 | 44% | 14% | 0.93 | 0.56 | 0.38 | 2.19 | 6% | 10% | 9% | 1.68 | -0.055 | – | 2 | -3.4 |
| ASX | 2025-12 | 18% | 9% | 0.78 | 0.87 | 0.79 | 2.46 | 12% | 5% | 26% | -0.59 | -0.125 | 2.5 | 8 | -5.4 |
| AMKR | 2025-12 | 14% | 8% | 0.84 | 0.85 | – | – | 9% | 2% | 13% | 0.51 | – | 0.8 | 7 | -0.2 |

![DuPont](charts/06_dupont_map.png)

**Quality of ROE**
- **NVIDIA's ~101% ROE is high-quality.** It comes from a 66% EBIT margin and 1.36× asset turnover with low leverage (1.35×). **KLAC's 87%** leans on 3.1× leverage from buybacks and debt, a less durable source of ROE.
- **The accruals ratio** (NI − OCF)/assets flags NVIDIA (0.109), LRCX, KLAC and Advantest: earnings running ahead of cash (receivables/inventory build). That is typical in a hyper-growth year but worth monitoring (ch.19 quality of earnings).
- **Capital intensity splits the chain.** Foundry/memory/IDM spend 11–90% of sales on capex (SMIC 90%, MU 42%, TSMC 34%, Intel 28%). Fabless, EDA and equipment spend 1–10% but 9–56% on R&D. Capex-heavy models have higher operating leverage.
- **Operating leverage (ch.17)**, DOL = %ΔEBIT / %ΔSales: Micron 9.5×, AVGO 3.6×, AMAT 3.1×, AMD 3.1×. Memory profits amplify revenue swings roughly 10×, in both directions.
- **Intel** has near-zero ROE with an interest burden of 0.59; **SMIC** has negative FCF (FCF/NI −7.6); **ASE and Amkor** have negative TTM FCF because of the packaging capex race.

---

## 10. Valuation (BKM ch.18)

- **PVGO/P** $= 1 - (E_1/P)/k$: the share of price that depends on future growth opportunities.
- **Sustainable growth** $g = ROE \times b$.
- **Constant-growth P/E** $= (1-b)/(k - ROE \cdot b)$ fails (k ≤ g) for almost all of these names. That is itself a signal that a **multistage model** is needed.
- **Two-stage DCF:** CF₁ = forward earnings × FCF conversion (0.3–1.0). Growth g₁ = min(ROE·b, 25%) for year 2, fading linearly to 4% by year 10, then a Gordon terminal value at k (CAPM).
- **Implied g (stage 1):** the starting growth rate that makes the model value equal today's market cap (reverse DCF).

| Ticker | Trail P/E | Fwd P/E | EV/EBITDA | P/S | P/B | FCF yld | Div yld | k (CAPM) | g=ROE×b | PVGO/P | Implied g (stage 1) | 2-stage DCF vs px | Street tgt upside |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NVDA | 28.5 | 14.4 | 26.9 | 17.9 | 34.6 | 0.8% | 0.12% | 15.1% | 113% | 54% | 26% | -3% | 46% |
| AVGO | 45.6 | 18.2 | 32.9 | 18.9 | 20.7 | 1.8% | 0.71% | 12.3% | 30% | 55% | 16% | 33% | 51% |
| AMD | 161.3 | 40.5 | 106.7 | 24.9 | 16.3 | 0.9% | 0.00% | 16.1% | 10% | 85% | 58% | -75% | -2% |
| QCOM | 23.1 | 19.8 | 18.6 | 4.9 | 10.2 | 4.7% | 1.78% | 13.2% | 20% | 62% | 22% | -8% | -4% |
| MRVL | 87.0 | 38.8 | 83.1 | 24.9 | 16.5 | 1.0% | 0.09% | 15.3% | 15% | 83% | 76% | -83% | 10% |
| ARM | 313.5 | 101.6 | 308.4 | 64.3 | 40.0 | 0.4% | 0.00% | 21.1% | 13% | 95% | 115% | -93% | -7% |
| SNPS | 74.0 | 24.1 | 42.8 | 8.7 | 2.9 | 4.2% | 0.00% | 11.5% | 4% | 64% | 22% | -46% | 30% |
| CDNS | 65.0 | 34.1 | 42.2 | 15.4 | 16.4 | 1.8% | 0.00% | 11.2% | 23% | 74% | 31% | -21% | 24% |
| TSM | 33.6 | 20.6 | 22.6 | 16.7 | 13.8 | 1.0% | 0.77% | 12.0% | 30% | 60% | 36% | -29% | 23% |
| 005930.KS | – | 4.0 | 7.5 | 3.9 | 4.4 | 3.7% | 0.52% | 12.5% | 28% | -100% | -19% | 340% | 68% |
| INTC | – | 59.6 | 39.8 | 11.4 | 5.7 | 0.7% | 0.00% | 15.2% | -11% | 89% | 87% | -92% | -5% |
| GFS | 38.3 | 18.7 | 13.4 | 3.9 | 2.3 | 2.8% | 0.25% | 13.6% | 6% | 61% | 22% | -41% | 55% |
| 0981.HK | 62.1 | 35.3 | 13.3 | 6.7 | 3.2 | -5.9% | 0.00% | 8.5% | 4% | 67% | 53% | -81% | 49% |
| TXN | 42.2 | 26.1 | 27.4 | 13.1 | 15.6 | 1.4% | 2.02% | 11.9% | 5% | 68% | 46% | -74% | 17% |
| IFX.DE | 69.2 | 20.0 | 18.9 | 4.7 | 4.3 | 2.4% | 0.62% | 15.2% | 4% | 67% | 30% | -55% | 53% |
| MU | 24.4 | 6.8 | 17.6 | 13.5 | 22.6 | 0.6% | 0.05% | 15.2% | 66% | 3% | 34% | -24% | 40% |
| 000660.KS | – | 3.9 | 8.7 | 7.0 | 11.0 | 4.2% | 0.08% | 15.5% | 91% | -64% | -4% | 144% | 71% |
| ASML | 60.2 | 29.5 | 43.2 | 16.7 | 30.0 | 1.4% | 0.49% | 13.5% | 38% | 75% | 36% | -30% | 22% |
| AMAT | 41.8 | 26.3 | 37.7 | 12.5 | 18.9 | 0.8% | 0.39% | 12.8% | 34% | 70% | 36% | -30% | 32% |
| LRCX | 54.6 | 26.9 | 45.5 | 17.0 | 31.6 | 0.8% | 0.33% | 13.8% | 53% | 73% | 48% | -50% | 19% |
| KLAC | 51.3 | 28.0 | 40.7 | 18.1 | 38.6 | 1.1% | 0.43% | 12.3% | 68% | 71% | 37% | -33% | 24% |
| 8035.T | 45.2 | 44.1 | 32.5 | 9.8 | 12.4 | 1.2% | 1.11% | 13.8% | 15% | 84% | 72% | -81% | 36% |
| ASM.AS | 38.6 | 27.5 | 34.7 | 12.3 | 10.3 | 0.6% | 0.39% | 14.3% | 23% | 75% | 44% | -48% | 33% |
| 6857.T | 65.8 | 65.8* | 41.6 | 19.9 | 30.8 | 1.4% | 0.17% | 14.4% | 50% | 89% | 76% | -77% | 25% |
| 6146.T | 43.5 | 39.8 | 26.1 | 12.7 | 10.0 | 1.7% | 0.93% | 12.7% | 16% | 80% | 53% | -68% | 52% |
| TER | 54.6 | 34.2 | 41.2 | 14.0 | 22.3 | 0.7% | 0.13% | 13.6% | 34% | 78% | 48% | -51% | 12% |
| 4063.T | 23.3 | 17.9 | 10.5 | 4.1 | 2.4 | 2.3% | 1.80% | 11.9% | 7% | 53% | 23% | -42% | 32% |
| ENTG | 75.9 | 30.3 | 28.9 | 7.0 | 5.9 | 2.1% | 0.26% | 12.0% | 6% | 73% | 31% | -56% | 14% |
| ASX | 54.0 | 22.7 | 27.5 | 5.1 | 10.7 | -2.9% | 0.94% | 13.3% | 8% | 67% | 67% | -84% | 15% |
| AMKR | 24.0 | 19.1 | 10.2 | 1.8 | 3.0 | -2.8% | 0.62% | 15.2% | 11% | 66% | 51% | -71% | 43% |

\* Advantest's forward P/E from the data feed (140×) is inconsistent with its trailing P/E, so the trailing P/E is used instead.

![Valuation](charts/07_valuation_growth.png)

**Interpretation**
- **Least demanding relative to fundamentals:** NVIDIA (implied g ≈ 26% vs ROE·b >100%, forward P/E 14.4), Broadcom (16%), Qualcomm (22%), Synopsys (22%). Also Samsung and SK hynix, but only if HBM earnings prove durable (see the cyclical-peak caveat).
- **Most demanding:** Arm (115% implied growth, 95% PVGO, forward P/E 102×), Intel (87%, a turnaround option on 18A/14A plus government backing), Marvell, Advantest, Tokyo Electron and ASE.
- **Equipment** (ASML, AMAT, LRCX, KLAC) needs 35–46% stage-1 growth: plausible only if WFE stays at records through 2027–28.
- **Street targets** imply +29% upside on average (median 28%). Sell-side optimism is well documented (ch.12/27), so treat these as relative, not absolute, signals.

---

## 11. Momentum & technicals (BKM ch.11–12)

| Ticker | 12-1 mom. | vs 50DMA | vs 200DMA | 50>200 (golden) | RSI(14) | 6M RS vs SOXX |
|---|---|---|---|---|---|---|
| NVDA | 18% | 4% | 13% | ✅ | 55 | -43% |
| AVGO | 13% | -6% | -4% | ✅ | 44 | -59% |
| AMD | 191% | 25% | 70% | ✅ | 74 | 135% |
| QCOM | 4% | 19% | 20% | ✅ | 68 | -17% |
| MRVL | 152% | 18% | 58% | ✅ | 64 | 99% |
| ARM | 71% | 18% | 44% | ✅ | 61 | 38% |
| SNPS | -11% | 6% | -4% | ❌ | 60 | -65% |
| CDNS | -4% | 3% | 0% | ❌ | 62 | -57% |
| TSM | 50% | 7% | 17% | ✅ | 63 | -39% |
| 005930.KS | 217% | 15% | 34% | ✅ | 64 | 0% |
| INTC | 167% | 24% | 52% | ✅ | 67 | 108% |
| GFS | 25% | 1% | -10% | ❌ | 55 | -63% |
| 0981.HK | -12% | -6% | -9% | ❌ | 43 | -57% |
| TXN | 46% | 3% | 12% | ✅ | 61 | -30% |
| IFX.DE | 69% | -5% | 1% | ✅ | 46 | -28% |
| MU | 474% | 15% | 60% | ✅ | 63 | 126% |
| 000660.KS | 391% | 14% | 40% | ✅ | 60 | 46% |
| ASML | 76% | 2% | 13% | ✅ | 55 | -43% |
| AMAT | 125% | -1% | 14% | ✅ | 56 | -33% |
| LRCX | 126% | 4% | 15% | ✅ | 57 | -28% |
| KLAC | 64% | -0% | 6% | ✅ | 54 | -47% |
| 8035.T | 101% | 1% | 12% | ✅ | 56 | -31% |
| ASM.AS | 57% | 0% | 5% | ✅ | 52 | -49% |
| 6857.T | 114% | 4% | 23% | ✅ | 55 | -22% |
| 6146.T | 17% | -7% | -18% | ❌ | 44 | -95% |
| TER | 155% | 8% | 19% | ✅ | 58 | -42% |
| 4063.T | 16% | -3% | -7% | ❌ | 43 | -80% |
| ENTG | 47% | 9% | 15% | ✅ | 60 | -43% |
| ASX | 237% | 16% | 46% | ✅ | 64 | 31% |
| AMKR | 67% | 2% | -7% | ❌ | 55 | -56% |

- **Momentum** (12-1-month; Jegadeesh-Titman, ch.11) is extreme in memory (MU 474%, SK hynix 391%), Samsung, ASE, AMD, Intel and Marvell.
- **Overbought (RSI > 70):** AMD. **Oversold (RSI < 30):** none.
- **Below the 200-day average:** AVGO, SNPS, GFS, SMIC, Disco, Shin-Etsu and AMKR. These are candidates for mean reversion (DeBondt-Thaler) *if* fundamentals hold.
- **EMH caveat:** these signals are weak-form information. Ch.12 supports momentum as a behavioral anomaly (underreaction, then overreaction), but momentum crashes after sharp reversals are its known failure mode.

---

## 12. Options market view (BKM ch.21)

| Ticker | ATM IV | Realized σ (1Y) | IV/RV | Implied ±1σ 1-month move | Expiry |
|---|---|---|---|---|---|
| NVDA | 30% | 38% | 0.81 | 8.8% | 2026-10-23 |
| AVGO | 34% | 46% | 0.73 | 9.8% | 2026-10-23 |
| AMD | 51% | 69% | 0.74 | 14.7% | 2026-10-23 |
| QCOM | 52% | 54% | 0.97 | 15.0% | 2026-10-23 |
| MRVL | 65% | 79% | 0.82 | 18.8% | 2026-10-23 |
| ARM | 68% | 79% | 0.87 | 19.8% | 2026-10-23 |
| SNPS | 49% | 42% | 1.15 | 14.1% | 2026-10-23 |
| CDNS | 45% | 40% | 1.13 | 13.1% | 2026-10-23 |
| TSM | 34% | 40% | 0.85 | 9.7% | 2026-10-23 |
| INTC | 73% | 76% | 0.95 | 21.0% | 2026-10-23 |
| GFS | 60% | 60% | 1.01 | 17.3% | 2026-11-20 |
| TXN | 50% | 42% | 1.18 | 14.4% | 2026-10-23 |
| MU | 60% | 81% | 0.74 | 17.3% | 2026-10-23 |
| ASML | 49% | 46% | 1.08 | 14.3% | 2026-10-23 |
| AMAT | 54% | 59% | 0.92 | 15.6% | 2026-10-23 |
| LRCX | 63% | 64% | 0.98 | 18.2% | 2026-10-23 |
| KLAC | 57% | 60% | 0.94 | 16.3% | 2026-10-23 |
| TER | 67% | 76% | 0.87 | 19.2% | 2026-10-23 |
| ENTG | 69% | 68% | 1.01 | 19.8% | 2026-11-20 |
| ASX | 58% | 56% | 1.04 | 16.9% | 2026-11-20 |
| AMKR | 65% | 78% | 0.83 | 18.7% | 2026-10-23 |

- Implied vol is **below** trailing realized vol for 14 of 21 US-listed names (NVDA IV/RV 0.81, MU 0.74). Options are relatively cheap for hedging concentrated gains, e.g. protective puts or collars (ch.20).
- The implied ±1σ one-month move is ±9–21% (NVDA ±9%, INTC ±21%). Use these to size positions.
- IV > RV for SNPS, CDNS, GFS, TXN, ASML, ENTG and ASX: the market is pricing event risk (export controls, China, earnings).

![IV vs RV](charts/10_implied_vs_realized_vol.png)

---

## 13. Portfolio construction (BKM ch.6–8, 27)

**Correlation & diversification (ch.7)**
![Correlation](charts/05_correlation_heatmap.png)

| # stocks (equal-wt) | Portfolio σ |
|---|---|
| 1 | 53.1% |
| 2 | 45.9% |
| 5 | 40.9% |
| 10 | 39.1% |
| 20 | 38.1% |
| 30 | 37.8% |

Diversification within semis stops at ~38% σ, roughly 2.4× SPY. The remaining covariance is the *sector factor*, which can only be diversified away across sectors, or hedged with SOXX/NQ futures (ch.23).

**Efficient frontier.** Expected returns = CAPM + de-biased, shrunk analyst alpha. The covariance matrix is single-index (ch.8), long-only, ≤10% per name.

![Frontier](charts/04_efficient_frontier.png)

| Portfolio | E(r) | σ | Sharpe | β |
|---|---|---|---|---|
| GMV_longonly_cap10 | 12.5% | 22.4% | 0.37 | 1.27 |
| MaxSharpe_longonly_cap10 | 18.7% | 28.7% | 0.51 | 1.63 |
| EqualWeight | 14.0% | 29.6% | 0.34 | 1.81 |

| Ticker | Global min-variance | Max-Sharpe (tangency) |
|---|---|---|
| AVGO | 8.9% | 10.0% |
| 6146.T | 4.0% | 10.0% |
| 0981.HK | 10.0% | 10.0% |
| 005930.KS | 5.3% | 10.0% |
| IFX.DE | 0.0% | 10.0% |
| GFS | 0.0% | 10.0% |
| 000660.KS | 0.0% | 10.0% |
| 4063.T | 10.0% | 10.0% |
| NVDA | 0.0% | 7.5% |
| SNPS | 10.0% | 5.5% |
| AMKR | 0.0% | 3.1% |
| 8035.T | 0.0% | 2.3% |
| AMAT | 3.4% | 1.1% |
| QCOM | 2.3% | 0.0% |
| ASX | 1.7% | 0.0% |
| TXN | 10.0% | 0.0% |
| TSM | 10.0% | 0.0% |
| CDNS | 10.0% | 0.0% |
| KLAC | 7.1% | 0.0% |
| ENTG | 7.3% | 0.0% |

**Capital allocation (ch.6):** $y^* = [E(r_P) - r_f]/(A\sigma_P^2)$ applied to the tangency portfolio:

| Risk aversion A | y* in semis tangency portfolio | Complete-portfolio E(r) | Complete-portfolio σ |
|---|---|---|---|
| 2 | 89% | 17.0% | 25.5% |
| 3 | 59% | 12.7% | 17.0% |
| 4 | 44% | 10.6% | 12.7% |
| 6 | 30% | 8.4% | 8.5% |
| 8 | 22% | 7.3% | 6.4% |

**Treynor-Black active portfolio (ch.27).** Alphas are 12-month analyst-implied returns minus CAPM. The average optimism bias (16%) is removed, and the remainder is shrunk by 0.25. The active portfolio is then combined with SPY:

- Active weight $w_A^* =$ 23%; index weight 77%; active β 0.31; IR 0.62.
- Ex-ante Sharpe improves from 0.35 (index alone) to 0.71, using $S_P^2 = S_M^2 + IR^2$.

| Ticker | Raw analyst α | De-biased & shrunk α | σ(e) | Weight in optimal risky portfolio |
|---|---|---|---|---|
| 005930.KS | 56% | 10.0% | 41% | 22.7% |
| AVGO | 39% | 5.9% | 35% | 18.7% |
| IFX.DE | 37% | 5.4% | 37% | 15.2% |
| 6146.T | 41% | 6.2% | 44% | 12.6% |
| GFS | 41% | 6.4% | 47% | 11.2% |
| 0981.HK | 43% | 6.7% | 50% | 10.2% |
| 000660.KS | 54% | 9.6% | 60% | 10.1% |
| 4063.T | 22% | 1.7% | 25% | 10.0% |
| ASX | 3% | -3.3% | 38% | -8.8% |
| INTC | -22% | -9.4% | 61% | -9.5% |
| TER | -2% | -4.4% | 41% | -10.0% |
| TXN | 7% | -2.1% | 27% | -10.6% |
| AMD | -20% | -8.9% | 56% | -10.7% |
| QCOM | -15% | -7.8% | 36% | -22.4% |

The largest positive tilts are Samsung, AVGO, Infineon, Disco and GFS (the Street sees the most upside relative to their risk). The largest underweights/shorts are QCOM, AMD, TXN and TER (priced above consensus targets). The unconstrained Treynor-Black portfolio is long/short and leveraged. Ch.27 recommends constraining tracking risk, so prefer the long-only max-Sharpe portfolio above for implementation.

---

## 14. Composite scorecard

Equal-weight z-scores:
- **Quality:** EBIT margin, ROE, FCF conversion, low accruals.
- **Valuation:** low PVGO/P, high FCF yield, low implied perpetual g, low forward P/E.
- **Risk:** low β, low σ, shallow drawdown.
- **Momentum:** 12-1 momentum, 6M relative strength vs SOXX.
- **Risk-adjusted performance:** Sharpe, information ratio.

| Rank | Ticker | Company | Quality | Valuation | Risk (low=good) | Momentum | Risk-adj. perf | Composite |
|---|---|---|---|---|---|---|---|---|
| 1 | 000660.KS | SK hynix | 0.63 | 1.42 | -0.85 | 1.74 | 1.36 | 0.86 |
| 2 | MU | Micron Technology | 0.06 | 0.33 | -0.77 | 2.40 | 1.36 | 0.68 |
| 3 | AVGO | Broadcom | 0.27 | 0.40 | 0.94 | -0.76 | 1.77 | 0.52 |
| 4 | 005930.KS | Samsung Electronics | -0.25 | 1.57 | 0.28 | 0.63 | 0.09 | 0.47 |
| 5 | KLAC | KLA Corp | 0.51 | 0.01 | 0.73 | -0.43 | 0.97 | 0.36 |
| 6 | TSM | TSMC | 0.58 | 0.18 | 0.54 | -0.43 | 0.65 | 0.31 |
| 7 | ASX | ASE Technology | -0.68 | -0.43 | 0.49 | 0.97 | 0.80 | 0.23 |
| 8 | CDNS | Cadence Design Systems | 0.31 | 0.18 | 1.65 | -0.81 | -0.39 | 0.19 |
| 9 | NVDA | NVIDIA | 0.48 | -0.03 | -0.64 | -0.60 | 1.70 | 0.18 |
| 10 | LRCX | Lam Research | 0.03 | -0.18 | -0.02 | -0.00 | 0.80 | 0.12 |
| 11 | 6857.T | Advantest | 0.33 | -0.69 | -0.41 | -0.01 | 1.25 | 0.09 |
| 12 | QCOM | Qualcomm | 0.70 | 0.89 | 0.60 | -0.45 | -1.33 | 0.08 |
| 13 | TXN | Texas Instruments | 0.24 | 0.16 | 1.46 | -0.37 | -1.10 | 0.08 |
| 14 | AMAT | Applied Materials | 0.03 | -0.07 | 0.15 | -0.05 | 0.22 | 0.06 |
| 15 | SNPS | Synopsys | 0.14 | 0.85 | 1.16 | -0.91 | -1.35 | -0.03 |
| 16 | AMD | Advanced Micro Devices | -0.15 | -0.62 | -1.22 | 1.62 | 0.17 | -0.04 |
| 17 | MRVL | Marvell Technology | -0.12 | -0.48 | -0.88 | 1.15 | 0.08 | -0.05 |
| 18 | ASML | ASML Holding | 0.42 | -0.06 | 0.14 | -0.34 | -0.58 | -0.08 |
| 19 | 6146.T | Disco Corp | 0.07 | -0.10 | -0.06 | -1.03 | 0.43 | -0.14 |
| 20 | TER | Teradyne | -0.31 | -0.30 | -0.11 | 0.01 | -0.03 | -0.15 |
| 21 | 8035.T | Tokyo Electron | -0.28 | -0.38 | -0.15 | -0.14 | -0.13 | -0.22 |
| 22 | 4063.T | Shin-Etsu Chemical | -0.19 | 0.55 | 1.00 | -0.91 | -1.56 | -0.22 |
| 23 | ASM.AS | ASM International | -0.10 | -0.29 | -0.18 | -0.48 | -0.34 | -0.28 |
| 24 | ENTG | Entegris | -0.02 | 0.22 | 0.16 | -0.48 | -1.28 | -0.28 |
| 25 | IFX.DE | Infineon Technologies | -0.04 | 0.17 | -0.27 | -0.25 | -1.09 | -0.30 |
| 26 | 0981.HK | SMIC | -0.98 | -0.74 | 0.83 | -0.85 | 0.25 | -0.30 |
| 27 | INTC | Intel | -0.62 | -0.83 | -1.33 | 1.29 | -0.71 | -0.44 |
| 28 | GFS | GlobalFoundries | -0.21 | 0.45 | -0.33 | -0.73 | -1.50 | -0.46 |
| 29 | ARM | Arm Holdings | 0.04 | -1.55 | -1.65 | 0.29 | 0.24 | -0.53 |
| 30 | AMKR | Amkor Technology | -1.00 | -0.37 | -0.77 | -0.49 | -0.74 | -0.67 |

![Scorecard](charts/09_scorecard.png)

> **Caveat:** memory ranks at the top partly because its forward P/E is low, which is exactly the ch.17 peak-earnings trap. Read the composite together with sections 9–10, not in isolation.

---

## 15. PEST analysis — global semiconductor supply chain (Sept 2026)

### P — Political / legal
| Factor | Current state | Who is exposed (+/−) |
|---|---|---|
| **US Section 232 chip tariffs** | 25% tariff on certain imported advanced semis & tools since 15 Jan 2026; exemptions for US data centers/R&D/domestic-capacity use with end-use certification | − importers without US fabs; + US-fab owners (INTC, TXN, MU, GFS), TSMC Arizona, AMKR Arizona |
| **US–Taiwan deal (Jan 2026)** | Tariff relief for Taiwanese firms expanding US capacity | + TSM, ASX (US build-outs); cost headwind to margins |
| **Export controls on China** | AI-chip licenses moved to case-by-case review with strict certifications; re-export within China largely prohibited; tool controls persist | − NVDA/AMD China revenue, AMAT/LRCX/KLAC/TEL/ASML China share (was 30–45% of WFE sales); + SMIC domestic substitution |
| **China critical-mineral controls** | Gallium (~98% of global refined supply), germanium, rare earths; the suspension of US-directed controls **expires 27 Nov 2026** | − compound semis/RF/power (IFX, QCOM RF), wafer/polishing chem; + ex-China material suppliers |
| **Industrial policy** | US CHIPS: USD 30.9bn of 52.7bn awarded to 19 firms across 40 projects; **US government equity stake in Intel**; CHIPS investment tax credit **sunsets for fab starts after 31 Dec 2026**. EU Chips Act 2.0 (materials focus); Japan (Rapidus 2nm, TSMC Kumamoto) | + INTC, MU, TXN, GFS, Samsung Taylor, TSM Arizona; equipment demand pulled forward into 2026 |
| **Taiwan Strait** | Persistent tail risk; ~90% of leading-edge logic and most CoWoS is in Taiwan | Systemic, for TSM and all of its customers; the core reason for "China+1 / US-onshore" |

### E — Economic
| Factor | Current state | Implication (BKM link) |
|---|---|---|
| **AI capex supercycle** | Hyperscaler capex ~USD 600bn in 2026 (+~70% YoY); semis revenue forecast ~USD 975bn–1.3tn | Demand shock ⇒ output, prices and margins up together (ch.17); highest DOL names benefit most |
| **Memory/HBM** | HBM market ~USD 55bn (+58%); DRAM ASPs up sharply; capacity shifting from commodity DRAM to HBM | Classic cyclical: peak margins, low P/E, negative PVGO; the watch-item is capacity additions in 2027 |
| **Bottlenecks** | CoWoS sold out for 2026 (~1m wafers; NVIDIA ~60%); N2 booked into 2028 | Pricing power for TSM/ASX/Disco/Advantest; volume risk if AI demand pauses |
| **Rates & discount rates** | 13-wk bill 4.07%, 10-yr 5.18%; inflation above target | High k (11–21%) ⇒ long-duration growth equity is rate-sensitive (ch.18); a 1% change in k moves DCF value 10–25% (see DCF_Sensitivity sheet) |
| **FX** | Weak yen; KRW recently firmer | Japanese exporters gain local earnings, but USD investors lose on translation (ch.25) |
| **Concentration** | AI is ~half of chip revenue but a sliver of units; top-3 customers hold 85% of CoWoS | High customer concentration raises σ(e); consumer, auto and industrial (TXN, IFX, QCOM) are late-cycle recovery options |

### S — Social
| Factor | Current state | Implication |
|---|---|---|
| **Talent shortage** | ~50k additional US technicians and engineers needed by 2030; fab timelines slipping | Execution risk for greenfield fabs (INTC Ohio, TSM/Samsung/MU US sites); wage inflation |
| **Energy & water (ESG)** | Fab permits increasingly tied to grid upgrades and clean-power mandates; water recycling in Arizona | Capex creep; opportunity for power semis (IFX SiC/GaN) and efficiency |
| **Consumer electronics affordability** | Memory reallocation to AI raises PC and phone costs | Weaker unit demand for QCOM and consumer MCU; supports memory pricing |
| **Public attitudes to AI** | Enthusiasm plus "AI bubble" narratives; retail options activity | Behavioral finance (ch.12): extrapolation, overconfidence, momentum; crash risk if narratives flip |

### T — Technological
| Factor | Current state | Winners / risk |
|---|---|---|
| **2nm GAA + backside power** | TSMC N2 in volume with five fabs ramping in 2026; A16 (backside power) in 2H26; Intel 18A/14A | + ASM (ALD/epi), AMAT, LRCX, KLAC (process control intensity rises); TSM lead widens |
| **High-NA EUV** | In use at Intel; TSMC adopting post-A16 | + ASML (ASP roughly 2× low-NA), Tokyo Electron (tracks), Lasertec |
| **Advanced packaging (CoWoS, SoIC, hybrid bonding, glass substrates)** | CoWoS capacity growing ~80% CAGR, still the binding constraint | + TSM, ASX, AMKR, Disco, Advantest/TER, BESI, Ibiden |
| **HBM3E → HBM4 (logic base die)** | SK hynix leads, then Samsung and Micron; HBM4 base die made at TSMC | + SK hynix, MU; test intensity rises (Advantest) |
| **Custom silicon (ASICs)** | Hyperscalers' in-house XPUs | + AVGO, MRVL, ARM (IP), SNPS/CDNS (more tape-outs); a relative threat to NVDA's share |
| **China domestic tools/nodes** | Push toward sub-7nm self-sufficiency by ~2028 | + SMIC, Naura/AMEC; − long-run China share for Western WFE |
| **AI-driven EDA & chiplets (UCIe)** | Design complexity rising exponentially | + SNPS, CDNS (secular, less cyclical); ARM chiplet ecosystems |

---

## 16. Putting it together — segment verdicts

| Segment | Life-cycle stage (ch.17) | Cyclicality / β | What the numbers say | Key PEST sensitivity |
|---|---|---|---|---|
| **AI fabless (NVDA, AVGO, MRVL, AMD)** | Rapid growth | β 1.4–2.5 | Best risk-adjusted performance (NVDA/AVGO); NVDA/AVGO are the *least* stretched relative to fundamentals; AMD/MRVL price in far more | Export controls, custom-ASIC substitution, hyperscaler capex |
| **IP/EDA (ARM, SNPS, CDNS)** | Mature-growth "toll roads" | β(SPY) 1.1–1.2 (ARM 3.9); SNPS/CDNS ~0.5 to SOXX | SNPS/CDNS de-rated and below 200DMA, a defensive sleeve; ARM is the most expensive stock in the universe | China licensing, AI-EDA adoption |
| **Foundry/IDM (TSM, Samsung, INTC, GFS, SMIC, TXN, IFX)** | Mixed | β 0.4–2.2 | TSM: top quality with moderate implied growth; INTC: turnaround option; TXN/IFX: early-recovery analog/power | Tariffs, Taiwan risk, CHIPS subsidies |
| **Memory (MU, SK hynix, Samsung)** | Cyclical at a (possibly structural) peak | β 2.2–2.3; highest DOL | Top momentum and alpha, but negative PVGO: the market expects mean reversion | 2027 capacity, HBM4 share, China DRAM |
| **Equipment (ASML, AMAT, LRCX, KLAC, TEL, ASMI, Disco, Advantest, TER)** | Growth tied to capex cycle | β 1.4–2.0 | Implied 35–75% stage-1 growth; KLAC/LRCX best Sharpe; Disco and TEL lagging | China WFE share, High-NA timing, the CHIPS 2026 cliff |
| **Materials & OSAT (Shin-Etsu, ENTG, ASX, AMKR)** | Mature / capacity build | β 1.3–2.2 | ASE is the momentum winner (CoWoS overflow); Shin-Etsu/ENTG lag; OSATs burn FCF on capex | Gallium/germanium controls, US onshoring |

### How to use this (ch.28 investment-policy framing)
1. **Core–satellite.** Treat semis as a *satellite* to a diversified core. Their σ (~38% historically for an equal-weight basket) and 25–70% drawdowns matter here. Even if semis were your *only* risky asset, y* would be just 23–46% for A = 4–8 (see the capital-allocation table). Alongside a diversified core, a 10–25% allocation is a reasonable range for moderate risk aversion.
2. **Within the satellite:** spread across chokepoints (the correlation matrix shows EDA, analog and China foundry diversify the AI-heavy core). Size positions by σ(e) using Treynor-Black logic, and cap single names at about 10%.
3. **Hedge the factor, not the stock:** use SOXX puts/collars (IV currently below RV) or index futures (ch.22–23) to neutralize the sector beta while keeping stock-specific views.
4. **Monitor:** Nov-27 critical-minerals deadline, Dec-31 CHIPS credit sunset, CoWoS/N2 capacity announcements, HBM contract pricing, hyperscaler capex guidance, 10-year yield (drives k), USD/JPY and USD/KRW.

---

## Appendix — Methodology & assumptions
| Item | Choice | Book reference |
|---|---|---|
| Returns | Monthly total returns (adjusted close), converted to USD daily at spot FX; window 2021-09..2026-08 (60m) (ARM since its 2023 IPO, GFS since 2021) | ch.5, 25 |
| Risk-free | Lagged 13-wk T-bill (monthly); 10-yr UST for cost of equity | ch.5, 9 |
| Market | SPY for CAPM/index model; SOXX sector β; ACWI global β in the xlsx | ch.8–9 |
| MRP | 5.5% forward-looking (hist. US arithmetic ≈8%; SPY 5Y realized 9.6%) | ch.5, 9 |
| Betas | OLS on 60m excess returns; Blume adjustment | ch.8 |
| Factors | Fama-French 5 + momentum (Ken French library, through 2026-08) | ch.10, 13 |
| Valuation | Forward P/E, PVGO, ROE×b, constant-growth P/E, two-stage FCF with 10-yr fade to 4%, reverse-DCF implied growth, ±1% k / 3–5% g sensitivity | ch.18 |
| Fundamentals | Latest fiscal-year statements (DuPont), TTM from the vendor for FCF/EBITDA; FX-converted where reporting ≠ listing currency (TSM/ASX TWD, ASML EUR, SMIC USD) | ch.19 |
| Active portfolio | Analyst-target alpha, de-biased by the cross-sectional mean, shrunk ×0.25; Treynor-Black; long-only max-Sharpe with 10% caps on single-index covariance | ch.7–8, 27 |
| Limitations | 5 years includes an extreme AI regime (non-stationary); vendor fundamentals have errors; forward EPS is consensus; DCFs are illustrative, not price targets; survivorship (today's winners chosen *ex post*) inflates historical Sharpe/α | ch.11–13, 24 |
