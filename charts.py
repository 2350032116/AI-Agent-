import pandas as pd


def load_excel(file):
    df = pd.read_excel(file)
    return df


def basic_info(df):
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns),
        "missing_values": df.isnull().sum().to_dict()
    }
