import requests

# Define the API endpoint URL
url = "https://api.openweathermap.org/data/2.5/weather?q=Portland&APPID=d08ec0e6ea2748a00d507a56181519b7"

# Make the GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response body
    print(response.json())
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code}")
