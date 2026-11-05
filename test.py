import os
import json
import requests
if os.path.exists("stations.json"):
    os.remove("stations.json")
open("stations.json", "x")

key = "cb83344dac684c1097b8b9213868c71f"
stop = "Karlskrona"
#url = "https://realtime-api.trafiklab.se/v1/stops/list/?key="+key
url = "https://realtime-api.trafiklab.se/v1/stops/name/"+stop+"/?key="+key

# 2. Make the API call
response = requests.get(url)

# 3. Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Convert the response content into a Python dictionary/list
    data = response.json()
    
    # 4. Save the data to a JSON file
    with open("stations.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
        
    print("Data successfully saved to stations.json!")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
