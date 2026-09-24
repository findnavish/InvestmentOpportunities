# Investment Opportunities

🌐 **Site:** https://findnavish.github.io/InvestmentOpportunities/

Research notebooks that apply the methods of Bodie, Kane & Marcus, *Investments* (13th ed.) to real markets. Each analysis lives under `analyses/<name>/`. Its build script writes a page into `docs/<name>/`, and MkDocs Material publishes that page to GitHub Pages.

| Analysis | Page | Code |
|---|---|---|
| Silicon Supply Chain — Top 30 Key Players | [site](https://findnavish.github.io/InvestmentOpportunities/silicon-supply-chain/) | [`analyses/silicon-supply-chain`](analyses/silicon-supply-chain) |

## Run locally

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r requirements-docs.txt

cd analyses/silicon-supply-chain
python fetch.py          # prices, FX, fundamentals, options IV, Fama-French factors -> data/
python analysis.py       # all models -> output/Silicon_Supply_Chain_Analysis.xlsx, output/results.pkl
python charts.py         # output/charts/*.png
python build_report.py   # docs/silicon-supply-chain/index.md (+ charts, xlsx)
cd ../..

mkdocs serve             # preview at http://127.0.0.1:8000
```

## Publishing

`.github/workflows/site.yml`:
- **On push to `main`:** builds and deploys the site from the committed `docs/`.
- **Weekly (Saturday 14:00 UTC) or manually** (*Actions → Refresh data & publish site → Run workflow*): re-runs every analysis on fresh data, commits the updated `docs/`, then deploys.

## Adding a new analysis

1. Create `analyses/<name>/` with a build script that writes `docs/<name>/index.md` plus its assets.
2. Add the page to `nav` in `mkdocs.yml` and a card to `docs/index.md`.
3. Add its steps to the `refresh` job in `.github/workflows/site.yml`.
4. Note it in `docs/changelog.md`.

*Educational research, not investment advice.*
