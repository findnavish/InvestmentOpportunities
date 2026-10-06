---
hide:
  - navigation
---

# Investment Opportunities

Research notebooks that apply the framework of Bodie, Kane & Marcus, *Investments* (13th ed.) to real markets. The framework covers risk and return, portfolio theory, CAPM and multifactor models, market efficiency, equity valuation, financial statement analysis, derivatives and performance evaluation. Every analysis is reproducible from code in this repository, and data-driven pages refresh automatically each week.

!!! warning "Not investment advice"
    Educational research only. Data comes from public sources (Yahoo Finance, Kenneth French Data Library) and can contain errors. Models rest on stated assumptions. Do your own due diligence.

## Analyses

<div class="grid cards" markdown>

-   :material-swap-vertical-bold:{ .lg .middle } **[Hourly Trade Signals](trade-signals/index.md)**

    ---

    Buy/sell ratings, **share quantities** and a written rationale for each of the Top 30, recomputed **every hour** from live prices. A USD 1M paper model portfolio executes the orders while each home market is open and is tracked against SOXX.

    *Refreshed hourly · rule-based, not advice*

-   :material-chip:{ .lg .middle } **[Silicon Supply Chain — Top 30 Key Players](silicon-supply-chain/index.md)**

    ---

    The 30 companies that control each chokepoint of the semiconductor chain: fabless, IP/EDA, foundry, memory, equipment, materials and packaging. Covers price history, risk and return, CAPM and Fama-French factor models, DuPont analysis, PVGO and reverse DCF, implied vs realized volatility, Treynor-Black and efficient-frontier portfolios, a composite scorecard and a full PEST analysis.

    *Auto-refreshed weekly · [Excel workbook](silicon-supply-chain/Silicon_Supply_Chain_Analysis.xlsx)*

-   :material-magnify-scan:{ .lg .middle } **[Stock Deep Dives — 26 stocks](deep-dives/index.md)**

    ---

    One page per stock (AMD, NVDA, MSFT, GOOGL, TSLA, PLTR, IONQ and 19 more), the whole textbook on each: price history, return and risk statistics, index-model and Fama-French betas, capital allocation, DuPont and earnings quality, PVGO, scenario and reverse DCF, an earnings event study, technical and behavioural signals, Treynor-Black, the options-implied view and a PEST analysis.

    *Auto-refreshed weekly · rule-based verdict*

</div>

## Roadmap

Ideas for upcoming enhancements. Suggestions are welcome via [GitHub issues](https://github.com/findnavish/InvestmentOpportunities/issues).

- [ ] Interactive (zoomable) price charts
- [ ] Scenario analysis: AI-capex slowdown, Taiwan disruption, memory down-cycle
- [ ] Earnings-revision and short-interest tracking for the Top 30
- [ ] Additional themes: AI data-center power & cooling, hyperscalers, networking/optics
- [ ] Bond and macro dashboards (yield curve, duration/convexity, ch.14–16)
- [x] 26 single-stock deep dives with a scoreboard (add a ticker to `analyses/deep-dives/config.json` for more)
- [ ] Options strategy playbooks for concentrated positions (ch.20–21)
