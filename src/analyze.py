import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr
import sys

def main(input_csv, summary_txt_out, plot_png_out):
    print(f"Loading data from {input_csv}...")
    merged_df = pd.read_csv(input_csv)
    
    #SUMMARY STATS
    with open(summary_txt_out, 'w') as f:
        f.write("--- Summary Statistics ---\n")
        f.write(merged_df[['Unemployment_Rate', 'Median_Income']].describe().to_string())
        f.write("\n\n")

        f.write("--- Correlation Analysis ---\n")
        # Pearson for linear
        pearson_corr, p_value_p = pearsonr(merged_df['Unemployment_Rate'], merged_df['Median_Income'])
        # Spearman for monotonic
        spearman_corr, p_value_s = spearmanr(merged_df['Unemployment_Rate'], merged_df['Median_Income'])

        f.write(f"Pearson Correlation (Linear): {pearson_corr:.3f} (p-value: {p_value_p:.4f})\n")
        f.write(f"Spearman Correlation (Monotonic): {spearman_corr:.3f} (p-value: {p_value_s:.4f})\n")
    
    print(f"Saved summary statistics to {summary_txt_out}")

    # VISUALIZATION
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))

    # scatterplot with a linear regression line
    sns.regplot(
        data=merged_df, 
        x='Unemployment_Rate', 
        y='Median_Income', 
        scatter_kws={'alpha':0.6}, 
        line_kws={'color':'red'}
    )

    plt.title('Unemployment Rate vs. Median Household Income by State', fontsize=14)
    plt.xlabel('Unemployment Rate (%)', fontsize=12)
    plt.ylabel('Median Household Income ($)', fontsize=12)
    plt.tight_layout()
    
    plt.savefig(plot_png_out)
    print(f"Saved plot to {plot_png_out}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python analyze.py <input_merged_csv> <output_summary_txt> <output_plot_png>")
        sys.exit(1)
        
    input_csv = sys.argv[1]
    summary_txt_out = sys.argv[2]
    plot_png_out = sys.argv[3]
    
    main(input_csv, summary_txt_out, plot_png_out)
