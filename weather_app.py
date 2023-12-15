import requests

api_key = 'd3cac54c79a6afca50f395a5ab649758'
base_url = 'http://api.openweathermap.org/data/2.5/weather'

city = input("Enter city name: ")

url = f'{base_url}?q={city}&appid={api_key}'

print(f'Request URL: {url}')

response = requests.get(url)
data = response.json()

print(f'Response: {data}')

if response.status_code == 200:
    # Extract relevant information from the response
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']

    # Display the weather information
    print(f"Weather in {city}: {weather_description}")
    print(f"Temperature: {temperature} K")
    print(f"Humidity: {humidity}%")
else:
    print(f"Error {response.status_code}: Unable to fetch weather information.")
