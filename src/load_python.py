"""Load the synthetic product-events dataset into pandas from CSV and JSON."""
from pathlib import Path

import pandas as pd

data_dir = Path(__file__).parent / "data"

df_csv = pd.read_csv(
    data_dir / "product_events.csv",
    parse_dates=["event_time"],
)
df_json = pd.read_json(data_dir / "product_events.json")
df_json["event_time"] = pd.to_datetime(df_json["event_time"])

assert len(df_csv) == len(df_json)

print("Loaded from CSV: ", df_csv.shape)
print("Loaded from JSON:", df_json.shape)
print()
print(df_csv.dtypes)
print()
print("Event type counts:")
print(df_csv["event_type"].value_counts())
print()
print("Revenue by category (purchases only):")
print(
    df_csv[df_csv["event_type"] == "purchase"]
    .groupby("category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)
