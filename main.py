import requests
import json

print('--------------------------------')
print('WEATHER')
print('--------------------------------')
with open("api_key.txt", "r") as file:
    api_key = file.read()

def fetch_data(loc):
    api_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{loc}?unitGroup=metric&key={api_key}"

    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 400:
        return "Invalid City...."
    else:
        return f"Code {response.status_code} Error. Pls Try Again Later"

def display_data(data):
    print("-------------------------")
    print(data["address"].upper())
    print("-------------------------")
    print("******************************************")
    print(f'Temperature: {data["currentConditions"]["temp"]}°C '
          f'\nPrecipitation Probability: {data["currentConditions"]["precipprob"]}% '
          f'\nHumidity: {data["currentConditions"]["humidity"]}% '
          f'\nCurrent Condition: {data["currentConditions"]["conditions"]} '
          f'\n******************************************')

while True:
    location = input("Enter City Name: ").strip().lower()
    # with open("data.json", "r") as f:
    #     data = json.load(f)
    data = fetch_data(location)
    display_data(data)
