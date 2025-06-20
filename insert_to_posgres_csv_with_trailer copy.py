import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

# Step 1: Read CSV, skip last row (trailer)
df = pd.read_csv('fake_users_with_trailer.csv')
df = df[:-1] # Remove last row

# Step 2: Connect to PostgreSQL
conn = psycopg2.connect(
    dbname = psycopg2.connect(
        dbname="airflow",
        user="airflow",
        password="airflow",
        host="localhost",
        port="5433" 
    )
)
cur = conn.cursor()

# Step 3: Ensure table exists
create_sql = """
CREATE TABLE IF NOT EXISTS fake_users (
    name TEXT,
);
"""