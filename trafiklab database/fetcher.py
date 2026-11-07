import os
import json
import requests

os.path.dirname(__file__)

def fetch_stations(search_value = "Empty"):
    
    if os.path.exists(os.path.join(os.path.dirname(__file__),"stations.json")):
        os.remove(os.path.join(os.path.dirname(__file__),"stations.json"))
    open(os.path.join(os.path.dirname(__file__),"stations.json"), "x")

    key = "cb83344dac684c1097b8b9213868c71f"
    stop = search_value

    if search_value == "Empty":
        url = "https://realtime-api.trafiklab.se/v1/stops/list/?key="+key

    else:
        url = "https://realtime-api.trafiklab.se/v1/stops/name/"+stop+"/?key="+key

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        with open(os.path.join(os.path.dirname(__file__),"stations.json"), "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
            
        print("Data successfully saved to stations.json!")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

print("To generate a list of stations please search for one, or press 'enter' to see all.\n")
user_input = input()
if user_input == "":
    fetch_stations()
else:
    fetch_stations(user_input)