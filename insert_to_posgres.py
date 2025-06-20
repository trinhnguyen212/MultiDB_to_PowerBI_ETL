import psycopg2

try:
    conn = psycopg2.connect(
        dbname="airflow",
        user="airflow",
        password="airflow",
        host="localhost",
        port="5433"
    )
    print("✅ Connected to PostgreSQL successfully.")
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)
