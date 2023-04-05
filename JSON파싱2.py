import requests
import json

# Send a request to the URL and store the response
response = requests.get("https://randomuser.me/api/?results=2000")

# Parse the JSON data from the response
data = json.loads(response.text)

# Loop through each result in the data
for result in data["results"]:
    # Get the last and first name
    last_name = result["name"]["last"]
    first_name = result["name"]["first"]
    
    # Parse the name key of the street key in the location key
    street_name = result["location"]["street"]["name"]
    
    # Print the results
    print(f"{last_name}, {first_name}: {street_name}")
