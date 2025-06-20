import csv
from faker import Faker
from datetime import datetime

# Initialize Faker
fake = Faker()

# Number of fake rows you want
num_rows = 10

#output filre
filename = "fake_users_with_trailer.csv"

#Define CSV headers
headers = ['name', 'email', 'address', 'created_at']

# generate fake data
data = []
for _ in range(num_rows):
    row = [
        fake.name(),
        fake.email(),
        fake.address().replace("\n", ", "),
        fake.date_this_decade().strftime("%Y-%m-%d %H:%M:%S")
    ]
    data.append(row)

# Write to csv
with open (filename, 'w', newline='') as f:
    writer = csv.writer(f)

    # Write header
    writer.writerow(headers)

    # Write data rows
    writer.writerows(data)

    # Write trailer/footer
    trailer = [
        f"TRAILER,{num_rows} rows generated,{datetime.now().isoformat()}"
    ]

    writer.writerow(trailer)

print(f"CSV created: {filename}")


