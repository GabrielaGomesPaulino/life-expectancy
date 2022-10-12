"Cleaning data file"
import pandas as pd
import argparse

# pylint: disable=line-too-long
def clean_data(life_expectancy_df:pd,
        region:str):
    """Method to clean data """

    # split column and add new columns to df
    life_expectancy_df[['unit','sex','age','region']] = life_expectancy_df['unit,sex,age,region'].str.split(',', expand=True)
    life_expectancy_df = life_expectancy_df.drop('unit,sex,age,region', axis=1)
    life_expectancy_df = life_expectancy_df.melt(id_vars=['unit','sex','age','region'], var_name='year', value_name='value')

    #filter data
    filtered_value_column_df = life_expectancy_df[life_expectancy_df["value"].str.contains(":")==False]
    filtered_region = filtered_value_column_df[(filtered_value_column_df['region'] == region)]
    filtered_value_letters = filtered_region[filtered_region['value'].str.contains('[A-Za-z]',regex=True)==False]

    #convert data types
    filtered_value_letters[['year']] = filtered_value_letters[['year']].astype(int)
    filtered_value_letters[['value']] = filtered_value_letters[['value']].astype(float)

    #upload dataframe to data folder
    save_data(filtered_value_letters)

def load_data(region:str):
    """Method to load data """

    # read data from file
    life_expectancy_df = pd.read_csv(
'/Users/gabrielapaulino/Assignment1/life_expectancy2/env/bin/python-course/life_expectancy/data/eu_life_expectancy_raw.tsv',
        sep='\t')
    life_expectancy_df.rename(
        columns = {'unit,sex,age,geo\\time': 'unit,sex,age,region'}, inplace = True)
    
    clean_data(life_expectancy_df,region)

def save_data(dataframe:pd):
    """Upload dataframe to path"""
    dataframe.to_csv('/Users/gabrielapaulino/Assignment1/life_expectancy2/env/bin/python-course/life_expectancy/data/pt_life_expectancy.csv', index = False)

if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser()

    # Add an argument
    parser.add_argument('--region', type=str, required=False)

    # Parse the argument
    args = parser.parse_args()
 
    clean_data(args.region)
    