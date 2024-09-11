import geopandas as gpd
import pandas as pd

def voltage_cleaning(input, output):
    """
    Testing
    args:
        input (str): filepath to input

    returns:
        clean
    """

    raw = gpd.read_file(input)
    raw.Voltage = (raw.Voltage.str.replace(r'[<KV-]', '', regex=True)
                        .str.split('-').str[0]
                        .astype(float).round())
    clean = raw[raw['Voltage'] >= 100]
    clean.to_file(output)