import requests
from prefect import flow, task

@task
def fetch_weather(city="London"):
    """Fetch current weather data for a given city."""
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    response = requests.get(url)
    data = response.json()
    
    if "results" not in data:
        raise ValueError("City not found")
    
    lat, lon = data["results"][0]["latitude"], data["results"][0]["longitude"]
    
    # Get weather data
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    weather_response = requests.get(weather_url)
    
    return weather_response.json()

@task
def process_weather(data):
    """Extract temperature and condition from API response."""
    temp = data["current_weather"]["temperature"]
    condition = data["current_weather"]["weathercode"]
    return f"Current temperature: {temp}°C, Weather Code: {condition}"

@flow
def weather_flow(city="London"):
    """Main Prefect flow to get and process weather data."""
    weather_data = fetch_weather(city)
    report = process_weather(weather_data)
    print(report)  # Print the final weather summary

if __name__ == "__main__":
    weather_flow("New York")
