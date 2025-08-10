import requests
import pandas as pd

# Path to your existing CSV file
file_path = "test_data/reviews.csv"

# Read the existing CSV
df = pd.read_csv(file_path)

# Send the CSV to your local API
with open(file_path, "rb") as f:
    files = {"file": ("reviews.csv", f, "text/csv")}
    response = requests.post("http://127.0.0.1:8000/analyze", files=files)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())