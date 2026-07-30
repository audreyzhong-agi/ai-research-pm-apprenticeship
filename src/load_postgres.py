"""Load the synthetic product-events CSV into PostgreSQL via COPY."""
import getpass
from pathlib import Path

import psycopg2

DB_NAME = "product_events_demo"
DATA_PATH = Path(__file__).parent / "data" / "product_events.csv"

conn = psycopg2.connect(dbname=DB_NAME, host="localhost", user=getpass.getuser())
try:
    with conn.cursor() as cur:
        cur.execute("TRUNCATE TABLE product_events;")
        with DATA_PATH.open() as f:
            cur.copy_expert(
                """
                COPY product_events (
                    event_id, user_id, product_id, category, event_type,
                    price, quantity, revenue, device, country, session_id, event_time
                )
                FROM STDIN WITH (FORMAT csv, HEADER true, NULL '')
                """,
                f,
            )
        cur.execute("SELECT count(*) FROM product_events;")
        (count,) = cur.fetchone()
    conn.commit()
    print(f"Loaded {count} rows into {DB_NAME}.product_events")
finally:
    conn.close()
