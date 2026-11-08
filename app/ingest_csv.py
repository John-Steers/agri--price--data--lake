import pandas as pd
REQUIRED={"observation_date","county","market","commodity","unit","price_kes"}
def load_verified_csv(path):
    df=pd.read_csv(path); missing=REQUIRED-set(df.columns)
    if missing: raise ValueError(f"Missing columns: {sorted(missing)}")
    df["observation_date"]=pd.to_datetime(df.observation_date,errors="raise")
    df["price_kes"]=pd.to_numeric(df.price_kes,errors="raise")
    if (df.price_kes<=0).any(): raise ValueError("Prices must be positive")
    if "source" not in df: df["source"]="user-supplied-verified-csv"
    if "is_synthetic" not in df: df["is_synthetic"]=False
    return df
