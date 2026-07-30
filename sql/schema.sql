CREATE TABLE IF NOT EXISTS product_events (
    event_id      TEXT PRIMARY KEY,
    user_id       TEXT NOT NULL,
    product_id    TEXT NOT NULL,
    category      TEXT NOT NULL,
    event_type    TEXT NOT NULL,
    price         NUMERIC(10, 2) NOT NULL,
    quantity      INTEGER,
    revenue       NUMERIC(10, 2) NOT NULL DEFAULT 0,
    device        TEXT NOT NULL,
    country       TEXT NOT NULL,
    session_id    TEXT NOT NULL,
    event_time    TIMESTAMPTZ NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_product_events_event_time ON product_events (event_time);
CREATE INDEX IF NOT EXISTS idx_product_events_user_id ON product_events (user_id);
CREATE INDEX IF NOT EXISTS idx_product_events_event_type ON product_events (event_type);
CREATE INDEX IF NOT EXISTS idx_product_events_category ON product_events (category);
