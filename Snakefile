# Target outputs
rule all:
    input:
        "results/summary_stats.txt",
        "results/scatter_plot.png"

# Step 1: Fetch raw data
rule fetch_data:
    input:
        fred_key="fred_apikey.txt",
        census_key="census_apikey.txt"
    output:
        fred_raw="data/raw/raw_fred_data.csv",
        census_raw="data/raw/raw_census_data.csv"
    shell:
        "python src/data_fetch.py {input.fred_key} {input.census_key} {output.fred_raw} {output.census_raw}"

# Step 2: Clean and merge
rule clean_merge:
    input:
        fred_raw="data/raw/raw_fred_data.csv",
        census_raw="data/raw/raw_census_data.csv"
    output:
        merged="data/processed/merged_data.csv"
    shell:
        "python src/data_clean_merge.py {input.fred_raw} {input.census_raw} {output.merged}"

# Step 3: Analyze and plot
rule analyze:
    input:
        merged="data/processed/merged_data.csv"
    output:
        stats="results/summary_stats.txt",
        plot="results/scatter_plot.png"
    shell:
        "python src/analyze.py {input.merged} {output.stats} {output.plot}"