import requests
import json

# Make a GET request to the URL
response = requests.get('https://randomuser.me/api/?results=100')

# Parse the JSON response
data = json.loads(response.text)

# Extract the required information
for result in data['results']:
    # Extract the first and last name
    first_name = result['name']['first']
    last_name = result['name']['last']

    # Extract the street and city name
    street = result['location']['street']['name']
    city = result['location']['city']

    # Print the information to the console
    print(f"{first_name} {last_name}: {street}, {city}")
