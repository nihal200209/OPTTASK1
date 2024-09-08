import requests

def get_weather(city):
    api_key = "your_api_key"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url).json()
    if response['cod'] == 200:
        weather = response['weather'][0]['description']
        temp = response['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
        return f"The weather in {city} is {weather} with a temperature of {temp:.2f}°C"
    else:
        return "City not found."
