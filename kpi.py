import pandas as pd

def load_file(uploaded_file):
    name = uploaded_file.name

    if name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
    else:
        raise ValueError("仅支持 CSV / Excel")

    return df
