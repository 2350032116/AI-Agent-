import pandas as pd

def clean_dataframe(df: pd.DataFrame):
    df = df.copy()

    df = df.drop_duplicates()
    df = df.dropna(axis=1, how='all')

    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].fillna('未知')
        else:
            df[col] = df[col].fillna(df[col].median())

    return df
