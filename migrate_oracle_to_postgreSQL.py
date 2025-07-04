import oracledb
import psycopg2

# Oracle connection
oracle_conn = oracledb.connect( user="airflow",
    password="airflow",
    dsn="localhost:1522/XEPDB1")
oracle_cursor = oracle_conn.cursor()

# PostgreSQL connection
pg_conn = psycopg2.connect(
    dbname="airflow",
    user="airflow",
    password="airflow",
    host="localhost",
    port="5433"
)

pg_cursor = pg_conn.cursor()

# Ensure target table exists in PostgreSQL
pg_cursor.execute("""
CREATE TABLE IF NOT EXISTS people (
    name TEXT,
    email TEXT                  
)
""")
pg_conn.commit()

# Fetch data from Oracle
oracle_cursor.execute("SELECT name, email FROM people")
rows = oracle_cursor.fetchall()

# Insert into PostgreSQL
for row in rows:
    pg_cursor.execute("INSERT INTO people (name, email) VALUES (%s, %s)", row)

pg_conn.commit()

# Cleanup
oracle_cursor.close()
oracle_conn.close()
pg_cursor.close()
pg_conn.close()

print("Data mograted from Oracel to PostgreSQL")