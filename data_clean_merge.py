import pandas as pd
import sys

STATES = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
    'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
    'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
    'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri',
    'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
    'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio',
    'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
    'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont',
    'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming',
    'DC': 'District of Columbia'
}

#CLEANING FRED DATA
def main(fred_input_path, census_input_path, merged_output_path):
  
    #loading raw
    print(f"Loading raw data from {fred_input_path} and {census_input_path}")
    fred_df = pd.read_csv(fred_input_path)
    census_df = pd.read_csv(census_input_path)

    #rename columns
    fred_df = fred_df.rename(columns={'value': 'Unemployment_Rate', 'State': 'State_Abbr'})

    #date to datetime to get year
    fred_df['date'] = pd.to_datetime(fred_df['date'])
    fred_df['Year'] = fred_df['date'].dt.year

    #missing values
    fred_df = fred_df.dropna(subset=['Unemployment_Rate'])

    #mapping abbrev's to full names
    fred_df['State_Name'] = fred_df['State_Abbr'].map(STATES)

    #GROUPBY STATE AND YEAR
    fred_annual = fred_df.groupby(['State_Name', 'Year'])['Unemployment_Rate'].mean().reset_index()

    #CLEANIG CENSUS DATA

    #rename
    census_df = census_df.rename(columns={'NAME': 'State_Name', 'B19013_001E': 'Median_Income', 'state': 'FIPS_Code'})

    census_df['Median_Income'] = pd.to_numeric(census_df['Median_Income'], errors='coerce')

    #padding FIPS code with 0s as needed
    census_df['FIPS_Code'] = census_df['FIPS_Code'].astype(str).str.zfill(2)

    #drop states not in target list
    census_df = census_df[census_df['State_Name'].isin(STATES.values())]

    #MERGING DATASETS

    print("Merging Datasets...")

    # Merge on State abbreviation and Year
    merged_df = pd.merge(fred_annual, census_df[['State_Name', 'FIPS_Code', 'Year', 'Median_Income']], 
                        on=['State_Name', 'Year'], 
                        how='inner')

    # Drop missing values
    merged_df.dropna(inplace=True)

    merged_df.to_csv(merged_output_path, index=False)

    print(f"Cleaned and merged data saved to {merged_output_path}")

#snakemake deployment
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python clean_and_merge.py <fred_in> <census_in> <merged_out>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])

