import mysql.connector
from faker import Faker
import random
from datetime import datetime

# Initialize Faker
fake = Faker()

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password= "",
    database="data_test_v1"
)

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    address VARCHAR(255),
    created_at DATETIME
)
""")

# Insert fake data
def insert_fake_users(n=100):
    for _ in range(n):
        name = fake.name()
        email = fake.email()
        address = fake.address().replace("\n", ", ")
        created_at = fake.date_time_this_decade()

        query = """
        INSERT INTO users (name, email, address, created_at)
        VALUES (%s, %s, %s, %s)
        """

        values = (name, email, address, created_at)
        cursor.execute(query, values)


    conn.commit()
    print(f"{n} fake users inserted.")

# Run it
insert_fake_users()

# Close connection
cursor.close()
conn.close()




