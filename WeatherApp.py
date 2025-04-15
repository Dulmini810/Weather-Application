import requests
import json

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        try:
            params = {
                "q": city,
                "appid": self.api_key,
                "units": "metric"  # Celsius
            }

            response = requests.get(self.base_url, params=params)
            data = json.loads(response.text)

            if response.status_code == 200:
                temperature = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                description = data["weather"][0]["description"]
                wind_speed = data["wind"]["speed"]

                print(f"Weather in {city}:")
                print(f"Temperature: {temperature}°C")
                print(f"Humidity: {humidity}%")
                print(f"Description: {description}")
                print(f"Wind Speed: {wind_speed} m/s")
            else:
                print("Error: Unable to fetch weather data.")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

def main():
    api_key = "you api key"  # Replace with your OpenWeatherMap API key
    weather_app = WeatherApp(api_key)

    while True:
        city = input("Enter city name (or 'q' to quit): ")
        if city.lower() == 'q':
            break

        weather_app.get_weather(city)

if __name__ == "__main__":
    main()