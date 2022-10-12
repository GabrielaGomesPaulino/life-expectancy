"""Pytest configuration file"""
import pandas as pd
import pytest

# pylint: disable=line-too-long
@pytest.fixture(autouse=True)
def run_before_and_after_tests() -> None:
    """Fixture to execute commands before and after a test is run"""
    # Setup: fill with any logic you want

    #yield # this is where the testing happens

    # Teardown : fill with any logic you want
    #file_path = "/Users/gabrielapaulino/Assignment1/life_expectancy2/env/bin/life_expectancy/data/pt_life_expectancy.csv"
    #file_path.unlink(missing_ok=True)


@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv("/Users/gabrielapaulino/Assignment1/life_expectancy2/env/bin/life_expectancy/tests/expected_result.csv")
