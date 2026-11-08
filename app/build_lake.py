from pathlib import Path
import random
import pandas as pd
OUT=Path("data/warehouse")
def generate(rows=2500,seed=19):
    rng=random.Random(seed); counties=["Nairobi","Kiambu","Nakuru","Kisumu","Uasin Gishu","Makueni"]
    markets=["Wakulima","Kongowea","Kibuye","Nakuru Town","Eldoret"]
    prices={"maize":(2500,5200),"beans":(5000,10500),"tomatoes":(1800,6500),"potatoes":(2200,4800)}
    records=[]
    for _ in range(rows):
        commodity=rng.choice(list(prices)); low,high=prices[commodity]; day=pd.Timestamp("2025-01-01")+pd.Timedelta(days=rng.randint(0,650))
        records.append({"observation_date":day.date(),"county":rng.choice(counties),"market":rng.choice(markets),
          "commodity":commodity,"unit":"90kg_bag" if commodity!="tomatoes" else "crate",
          "price_kes":rng.randint(low,high),"source":"synthetic-demo","is_synthetic":True})
    return pd.DataFrame(records)
def write_lake(df):
    frame=df.copy(); dates=pd.to_datetime(frame.observation_date)
    frame["year"]=dates.dt.year.astype(str); frame["month"]=dates.dt.month.astype(str).str.zfill(2)
    OUT.mkdir(parents=True,exist_ok=True)
    frame.to_parquet(OUT,engine="pyarrow",partition_cols=["year","month","county"],index=False)
    return OUT
if __name__=="__main__":
    df=generate(); print(f"Wrote {len(df)} synthetic records to {write_lake(df)}")
