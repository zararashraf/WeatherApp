import requests

base_url = 'https://api.openweathermap.org/data/2.5/weather'
api_key = 'your_api_key'
city_name = 'Lahore'
system = 'metric' 
#system = 'imperial'

api_url = f'{base_url}?q={city_name.title()}&units={system}&appid={api_key}'

try:
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()

        # Extract weather information
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_description = data["weather"][0]["description"]
        city = data['name']
        country = data['sys']['country']

        # Display the extracted and calculated data
        unit_symbol = "°F" if system == "imperial" else "°C"
        print(f"Temperature: {temperature:.2f}{unit_symbol}")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_description}")
        print(f'Place: {city}, {country}')

    else:
        print(f"API request failed with status code: {response.status_code}")
        
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
