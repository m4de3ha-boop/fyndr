import pandas as pd
import os

FILE = "items.csv"

def load_items():
    if not os.path.exists(FILE):
        df = pd.DataFrame(columns=["id", "name", "desc", "image", "status", "claimed_by"])
        df.to_csv(FILE, index=False)
    return pd.read_csv(FILE)

def save_items(df):
    df.to_csv(FILE, index=False)
