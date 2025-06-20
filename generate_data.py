from faker import Faker
from dataclasses import dataclass
from typing import List
import csv

# Initialize Faker
fake = Faker()

# Number of fake users to generate
num_rows = 100

# Number of fake user data structure
@dataclass
class User:
    name: str
    email: str
    phone: str
    city: str

# Function to generate fake users
def generate_data(n: int) -> List[User]:
    users = []
    for _ in range(n):
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()
        city = fake.city()
        users.append(User(name,email,phone,city))
    return users
# Main execution
if __name__ == "__main__":
    users = generate_data(num_rows)

    # Write to CSV
    with open("fake_users.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
       # writer.writerow(["Name", "Email", "Phone", "City"]) # Header row
        for user in users:
            writer.writerow([user.name, user.email, user.phone, user.city])
    
    print(f"Generated {num_rows} fake users and saved to 'fake_users.csv")


