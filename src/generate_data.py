"""Generate a synthetic product-events dataset (CSV + JSON)."""
import csv
import json
import random
from datetime import datetime, timedelta, timezone
from pathlib import Path

from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)

N_USERS = 500
N_PRODUCTS = 80
N_EVENTS = 20_000
START = datetime(2026, 1, 1, tzinfo=timezone.utc)
END = datetime(2026, 7, 29, tzinfo=timezone.utc)

CATEGORIES = ["electronics", "apparel", "home", "beauty", "sports", "books", "toys", "grocery"]
EVENT_TYPES = ["page_view", "product_view", "add_to_cart", "remove_from_cart", "checkout", "purchase"]
# weight events so the funnel is realistic (lots of views, few purchases)
EVENT_WEIGHTS = [30, 30, 15, 5, 8, 12]
DEVICES = ["desktop", "mobile", "tablet"]
COUNTRIES = ["US", "CA", "GB", "DE", "FR", "AU", "JP", "BR"]

users = [f"u_{i:05d}" for i in range(1, N_USERS + 1)]
products = [
    {
        "product_id": f"p_{i:04d}",
        "category": random.choice(CATEGORIES),
        "price": round(random.uniform(5, 500), 2),
    }
    for i in range(1, N_PRODUCTS + 1)
]
product_by_id = {p["product_id"]: p for p in products}

def random_timestamp():
    delta = END - START
    seconds = random.randint(0, int(delta.total_seconds()))
    return START + timedelta(seconds=seconds)

events = []
for i in range(1, N_EVENTS + 1):
    product = random.choice(products)
    event_type = random.choices(EVENT_TYPES, weights=EVENT_WEIGHTS, k=1)[0]
    qty = random.randint(1, 3) if event_type in ("add_to_cart", "purchase") else None
    events.append(
        {
            "event_id": f"e_{i:06d}",
            "user_id": random.choice(users),
            "product_id": product["product_id"],
            "category": product["category"],
            "event_type": event_type,
            "price": product["price"],
            "quantity": qty,
            "revenue": round(product["price"] * qty, 2) if event_type == "purchase" and qty else 0.0,
            "device": random.choice(DEVICES),
            "country": random.choice(COUNTRIES),
            "session_id": f"s_{random.randint(1, N_EVENTS // 3):06d}",
            "event_time": random_timestamp().isoformat(),
        }
    )

events.sort(key=lambda e: e["event_time"])

out_dir = Path(__file__).parent / "data"
out_dir.mkdir(exist_ok=True)

csv_path = out_dir / "product_events.csv"
json_path = out_dir / "product_events.json"

with csv_path.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(events[0].keys()))
    writer.writeheader()
    writer.writerows(events)

with json_path.open("w") as f:
    json.dump(events, f, indent=2)

print(f"Wrote {len(events)} events")
print(f"CSV:  {csv_path}")
print(f"JSON: {json_path}")
