import pandas as pd
import requests
import time
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
YEARS = [2018, 2019, 2021, 2022] # Skipping 2020


# API ACCESS: FRED state unemployment data
def get_fred_data(state_abbr, api_key):
    series_id = f"{state_abbr}UR"
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={api_key}&file_type=json"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()['observations']
        df = pd.DataFrame(data)[['date', 'value']]
        df['State'] = state_abbr
        df['value'] = pd.to_numeric(df['value'], errors='coerce')
        return df
    else:
        print(f"Failed to fetch FRED data for {state_abbr}")
        return pd.DataFrame()

#API ACCESS: U.S. Census i median household income by state (yearly)
def get_census_data(year, api_key):
    # B19013_001E is the variable for Median Household Income
    url = f"https://api.census.gov/data/{year}/acs/acs1?get=NAME,B19013_001E&for=state:*&key={api_key}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        headers = data.pop(0)
        df = pd.DataFrame(data, columns=headers)
        df['Year'] = year
        return df
    else:
        print(f"Failed to fetch Census data for {year}")
        return pd.DataFrame()


# main fetching function
def main(fred_key_path, census_key_path, fred_out_path, census_out_path):
    with open(fred_key_path, "r") as f:
        FRED_API_KEY = f.read().strip()
    with open(census_key_path, "r") as f:
        CENSUS_API_KEY = f.read().strip()

    # fetching FRED Data
    print("Fetching FRED Data...")
    fred_dfs = []
    for state in STATES.keys():
        fred_dfs.append(get_fred_data(state, FRED_API_KEY))
        time.sleep(0.5) 
    
    fred_df = pd.concat(fred_dfs, ignore_index=True)
    fred_df.to_csv(fred_out_path, index=False)
    print(f"Saved FRED data to '{fred_out_path}'")

    # fetching Census Data
    print("Fetching Census Data...")
    census_dfs = []
    for year in YEARS:
        census_dfs.append(get_census_data(year, CENSUS_API_KEY))
        time.sleep(0.5)
        
    census_df = pd.concat(census_dfs, ignore_index=True)
    census_df.to_csv(census_out_path, index=False)
    print(f"Saved Census data to '{census_out_path}'")

#snakemake deployment
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python data_fetch.py <fred_key_txt> <census_key_txt> <fred_out_path> <census_out_path>")
        sys.exit(1)

    fred_key = sys.argv[1]
    census_key = sys.argv[2]
    fred_out = sys.argv[3]
    census_out = sys.argv[4]
    
    main(fred_key, census_key, fred_out, census_out)