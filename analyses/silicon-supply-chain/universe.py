# Top-30 silicon supply chain universe: ticker -> (name, segment, country, listing currency)
UNIVERSE = {
    # Fabless / chip design
    "NVDA": ("NVIDIA", "Fabless - AI/GPU", "US", "USD"),
    "AVGO": ("Broadcom", "Fabless - Networking/Custom ASIC", "US", "USD"),
    "AMD": ("Advanced Micro Devices", "Fabless - CPU/GPU", "US", "USD"),
    "QCOM": ("Qualcomm", "Fabless - Mobile/Edge", "US", "USD"),
    "MRVL": ("Marvell Technology", "Fabless - Data Infra/Custom ASIC", "US", "USD"),
    # IP & EDA
    "ARM": ("Arm Holdings", "IP - CPU Architecture", "UK", "USD"),
    "SNPS": ("Synopsys", "EDA & IP", "US", "USD"),
    "CDNS": ("Cadence Design Systems", "EDA & IP", "US", "USD"),
    # Foundry / IDM
    "TSM": ("TSMC", "Foundry - Leading Edge", "Taiwan", "USD"),
    "005930.KS": ("Samsung Electronics", "IDM - Memory/Foundry", "South Korea", "KRW"),
    "INTC": ("Intel", "IDM - Logic/Foundry", "US", "USD"),
    "GFS": ("GlobalFoundries", "Foundry - Specialty/Mature", "US", "USD"),
    "0981.HK": ("SMIC", "Foundry - China", "China", "HKD"),
    "TXN": ("Texas Instruments", "IDM - Analog", "US", "USD"),
    "IFX.DE": ("Infineon Technologies", "IDM - Power/Auto", "Germany", "EUR"),
    # Memory
    "MU": ("Micron Technology", "Memory - DRAM/HBM/NAND", "US", "USD"),
    "000660.KS": ("SK hynix", "Memory - DRAM/HBM", "South Korea", "KRW"),
    # Wafer fab equipment (WFE) & test
    "ASML": ("ASML Holding", "Equipment - Lithography (EUV)", "Netherlands", "USD"),
    "AMAT": ("Applied Materials", "Equipment - Deposition/Etch", "US", "USD"),
    "LRCX": ("Lam Research", "Equipment - Etch/Deposition", "US", "USD"),
    "KLAC": ("KLA Corp", "Equipment - Process Control", "US", "USD"),
    "8035.T": ("Tokyo Electron", "Equipment - Coat/Develop/Etch", "Japan", "JPY"),
    "ASM.AS": ("ASM International", "Equipment - ALD/Epitaxy", "Netherlands", "EUR"),
    "6857.T": ("Advantest", "Equipment - Test", "Japan", "JPY"),
    "6146.T": ("Disco Corp", "Equipment - Dicing/Grinding", "Japan", "JPY"),
    "TER": ("Teradyne", "Equipment - Test", "US", "USD"),
    # Materials
    "4063.T": ("Shin-Etsu Chemical", "Materials - Silicon Wafers/Photoresist", "Japan", "JPY"),
    "ENTG": ("Entegris", "Materials - Specialty Chem/Filtration", "US", "USD"),
    # OSAT / advanced packaging
    "ASX": ("ASE Technology", "OSAT - Advanced Packaging", "Taiwan", "USD"),
    "AMKR": ("Amkor Technology", "OSAT - Advanced Packaging", "US", "USD"),
}

BENCH = {"SPY": "S&P 500 (market proxy)", "SOXX": "iShares Semiconductor ETF", "ACWI": "MSCI ACWI (global market)"}
# Yahoo FX tickers: KRW=X, JPY=X, HKD=X are local-per-USD; EURUSD=X is USD-per-EUR
FX = {"KRW": ("KRW=X", "per_usd"), "JPY": ("JPY=X", "per_usd"), "HKD": ("HKD=X", "per_usd"), "EUR": ("EURUSD=X", "usd_per")}
RATES = {"^IRX": "13-week T-bill yield", "^TNX": "10-year Treasury yield"}
