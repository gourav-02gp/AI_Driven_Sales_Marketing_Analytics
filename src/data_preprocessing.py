import pandas as pd

def load_and_clean_data():
    df = pd.read_csv("data/sales_data.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    return df
