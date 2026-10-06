# Changelog

## 2026-10-06 (later)
- **Stock Deep Dives expanded to 26 stocks** across semis, mega-cap tech, software, quantum, EVs, internet/media, industrials and health, with a new [Scoreboard](deep-dives/index.md).
- The generator now works for any ticker. It picks the sector-ETF benchmark automatically and runs the Fama-French 5+momentum regression locally. Peer multiples come from live data, operating leverage is computed from annual statements, and statements of foreign filers are converted to USD. Default bear/base/bull scenarios are anchored on consensus growth and today's owner-FCF margin, with hand-set margins where capex distorts FCF (MSFT, GOOGL, META, AMZN, INTC). Loss-makers get gross-margin-based target margins, a cash-runway metric and a "speculative" verdict cap. Optional extra discount-rate premiums (DIDIY: China/VIE/OTC) and balance-sheet adjustments (F: Ford Credit) are supported.

## 2026-10-06
- Added **Stock Deep Dives**, starting with [AMD](deep-dives/amd/index.md). A reusable generator (`analyses/deep-dives/deep_dive.py`) applies ch.5–12 and ch.17–27 to a single stock: return and risk statistics, index model and FF5 factors, capital allocation, DuPont and earnings quality, PVGO, scenario and reverse DCF, an earnings event study, technicals, Treynor-Black and the options-implied view. Hand-written PEST notes are embedded, and the numbers refresh weekly.

## 2026-09-24
- Added **Hourly Trade Signals**: composite score (de-biased analyst α vs CAPM, momentum, trend, quality), Buy/Hold/Sell ratings, Treynor-Black style sizing into share quantities, per-name rationale, and a USD 1M paper model portfolio tracked against SOXX.
- The as-of date now reflects the last completed US session; GitHub Actions versions updated.

## 2026-09-23
- Launched the site.
- Added **Silicon Supply Chain — Top 30 Key Players**: price history, BKM-method analytics (ch.5–28), PEST analysis, Excel workbook and 10 charts.
- Added weekly automatic data refresh.
