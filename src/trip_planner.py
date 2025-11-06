from src.weather_service import get_weather

def plan_trip(city):
    weather = get_weather(city)
    if weather == "Sunny":
        return "Take sunglasses 😎"
    else:
        return "Take an umbrella ☔"
