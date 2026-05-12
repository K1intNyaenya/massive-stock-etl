import json
import requests
import os

api_key = os.getenv("API_KEY")
url = f"https://api.polygon.io/v3/reference/exchanges?asset_class=stocks&locale=us&apiKey={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    with open("raw_data.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Raw data saved to raw_data.json")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")