import pandas as pd
from life_expectancy.cleaning import clean_data
from pathlib import Path
import pytest 

@pytest.fixture
def get_raw_dataframe() ->pd.DataFrame:
    print(Path.cwd())
    path="/Users/gabrielapaulino/Assignment1/life_expectancy2/env/bin/life-expectancy/life_expectancy/data/eu_life_expectancy_raw.tsv"
    life_expectancy_df = pd.read_csv(path,sep='\t')
    
    return life_expectancy_df

@pytest.fixture
def get_expected_dataframe() ->pd.DataFrame:
    print(Path.cwd())
    path="/Users/gabrielapaulino/Assignment1/life_expectancy2/env/bin/life-expectancy/life_expectancy/tests/fixtures/pt_life_expectancy_expected.csv"
    life_expectancy_df = pd.read_csv(path,sep='\t')
    
    return life_expectancy_df

# pylint: disable=line-too-long
def test_clean_data(get_raw_dataframe: pd.DataFrame,get_expected_dataframe: pd.DataFrame) -> None:
    """Test data """
    actual_df = clean_data(get_raw_dataframe,'PT')
    pd.testing.assert_frame_equal(
        actual_df, get_expected_dataframe
    )
