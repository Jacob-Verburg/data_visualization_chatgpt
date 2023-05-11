import csv
import random
from datetime import date, timedelta

start_date = date(2023, 1, 1)
end_date = date(2023, 12, 31)
delta = end_date - start_date

data = []

for i in range(delta.days + 1):
    current_date = start_date + timedelta(days=i)
    temperature = random.uniform(-10, 40)  # Generate a random temperature between -10 and 40 degrees Celsius
    data.append([current_date, temperature])

# Save the data to a CSV file
filename = "temperature_data.csv"
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Temperature"])
    writer.writerows(data)

print(f"Temperature data has been saved to {filename}.")
