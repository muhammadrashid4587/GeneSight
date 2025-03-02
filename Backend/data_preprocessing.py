# data_preprocessing.py
import pandas as pd

def load_geo_data(file_path):
    df = pd.read_csv(file_path, sep="\t", comment="!")
    df.set_index("ID_REF", inplace=True)
    df = df.transpose()
    return df
