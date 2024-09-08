import requests

def get_weather_data(location, api_key):
    # OpenWeatherMap API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    
    # Make a request to the API
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data for {location}.")
        return None

def display_weather(data):
    # Extract basic weather information
    city = data['name']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather_condition = data['weather'][0]['description']

    # Display the weather information
    print(f"\nWeather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather_condition.capitalize()}")

def main():
    api_key = "125bb592e472dad69efb237d0f192990"  
    
    # Prompt user for city or ZIP code
    location = input("Enter a city name or ZIP code: ")
    
    # Fetch weather data
    weather_data = get_weather_data(location, api_key)
    
    # Display weather information if data is retrieved
    if weather_data:
        display_weather(weather_data)

if __name__ == "__main__":
    main()
