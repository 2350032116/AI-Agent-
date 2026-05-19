import pandas as pd

def generate_kpi(df: pd.DataFrame):
    numeric_cols = df.select_dtypes(include='number').columns

    kpi = {}

    for col in numeric_cols:
        kpi[col] = {
            'sum': round(df[col].sum(), 2),
            'mean': round(df[col].mean(), 2),
            'max': round(df[col].max(), 2),
            'min': round(df[col].min(), 2)
        }

    return kpi
