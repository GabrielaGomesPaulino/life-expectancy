"Cleaning data file"
import pandas as pd
import argparse

# pylint: disable=line-too-long
def clean_data(region:str):
   
    """Method to clean data """
    # read data from file
    life_expectancy_df = pd.read_csv(
'/Users/gabrielapaulino/Assignment1/life_expectancy2/env/bin/life_expectancy/data/eu_life_expectancy_raw.tsv',
        sep='\t')
    life_expectancy_df.rename(
        columns = {'unit,sex,age,geo\\time': 'unit,sex,age,region'}, inplace = True)

    # split column and add new columns to df
    life_expectancy_df = split_column_unpivot(life_expectancy_df)

    #filter data
    filtered_dataframe = filter_df_data(life_expectancy_df,region)

    #convert data types
    converted_df = convert_data_types(filtered_dataframe)

    #upload dataframe to data folder
    upload_df_path(converted_df,'/Users/gabrielapaulino/Assignment1/life_expectancy2/env/bin/life_expectancy/data/pt_life_expectancy.csv')

    return converted_df

def split_column_unpivot(lf_exp: pd):
    """Unpivot dataframe columns"""
    lf_exp[['unit','sex','age','region']
    ] = lf_exp['unit,sex,age,region'].str.split(',', expand=True)
    lf_exp = lf_exp.drop('unit,sex,age,region', axis=1)
    lf_exp = lf_exp.melt(id_vars=['unit','sex','age','region'], var_name='year', value_name='value')

    return lf_exp

def filter_df_data(dataframe : pd,
                    region : str= 'PT'):
    """Filter dataframe data types"""
 
    filter_value_column_df = dataframe[dataframe["value"].str.contains(":")==False]
    filter_region = filter_value_column_df[(filter_value_column_df['region'] == region)]
    filter_value_letters = filter_region[filter_region['value'].str.contains('[A-Za-z]',regex=True)==False]
    
    return filter_value_letters

def convert_data_types(filtered_dataframe : pd):
    """Convert dataframe data tyoes"""
    filtered_dataframe[['year']] = filtered_dataframe[['year']].astype(int)
    filtered_dataframe[['value']] = filtered_dataframe[['value']].astype(float)

    return filtered_dataframe

def upload_df_path(converted_df : pd,
                   path : str):
    """Upload dataframe to path"""
    converted_df.to_csv(path, index = False)

if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser()

    # Add an argument
    parser.add_argument('--region', type=str, required=False)

    # Parse the argument
    args = parser.parse_args()
 
    clean_data(args.region)
