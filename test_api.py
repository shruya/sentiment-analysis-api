import requests
import pandas as pd

# Create a small sample DataFrame
data = {
    "review": [
        "I absolutely loved the product.",
        "This was the worst thing I bought.",
        "Okay experience.",
        "Fantastic service and support.",
        "Not worth the price."
    ]
}
df = pd.DataFrame(data)
df.to_csv("review.csv", index=False)

# Send the CSV to your local API
with open("review.csv", "rb") as f:
    files = {"file": ("review.csv", f, "text/csv")}
    response = requests.post("http://127.0.0.1:8000/analyze", files=files)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
