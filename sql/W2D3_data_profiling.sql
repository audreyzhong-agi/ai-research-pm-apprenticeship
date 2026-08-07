-- ==========================================
-- Week 2 Day 3 - Data Profiling
-- ==========================================

-- Question 1: Count total rows

SELECT COUNT(*) AS total_rows
FROM product_events;

-- Result: 20000 rows

--------------------------------------------------------
-- Question 2: Count missing values
--------------------------------------------------------

SELECT COUNT(*) AS missing_quantity
FROM product_events
WHERE quantity IS NULL;

SELECT COUNT(*) AS missing_revenue
FROM product_events
WHERE revenue IS NULL;

--------------------------------------------------------
-- Question 3: Earliest and Latest Event Time
--------------------------------------------------------

SELECT
    MIN(event_time) AS earliest_event,
    MAX(event_time) AS latest_event
FROM product_events;

--------------------------------------------------------
-- Question 4: Top 3 Event Types
--------------------------------------------------------

SELECT
    event_type,
    COUNT(*) AS event_count
FROM product_events
GROUP BY event_type
ORDER BY event_count DESC
LIMIT 3;

--------------------------------------------------------
-- Question 5: Total Revenue
--------------------------------------------------------

SELECT
    SUM(revenue) AS total_revenue
FROM product_events;