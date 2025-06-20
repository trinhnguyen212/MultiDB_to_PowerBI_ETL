import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

# Replace with your actual column names
col_names = ['name', 'email', 'phone', 'city']
df = pd.read_csv('fake_users.csv', header=None, names=col_names)
conn = psycopg2.connect(
        dbname="airflow",
        user="airflow",
        password="airflow",
        host="localhost",
        port="5433"
    )
cur = conn.cursor()

# Ensure table exists...
cur.execute("""
  CREATE TABLE IF NOT EXISTS fake_users (
    name TEXT,
    email TEXT,
    phone TEXT,
    city TEXT
  )
""")

cols = ', '.join(df.columns)
query = f"INSERT INTO fake_users ({cols}) VALUES %s"
tuples = df.itertuples(index=False, name=None)

execute_values(cur, query, tuples)
conn.commit()
cur.close()
conn.close()
print("✅ Successfully inserted with execute_values()")
