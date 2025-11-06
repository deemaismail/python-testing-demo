from unittest.mock import patch
from src.trip_planner import plan_trip

@patch("src.trip_planner.get_weather")
def test_plan_trip_sunny(mock_weather):
    mock_weather.return_value = "Sunny"  # نحاكي API ترجّع "Sunny"
    result = plan_trip("Amman")
    assert result == "Take sunglasses 😎"
    mock_weather.assert_called_once_with("Amman")

@patch("src.trip_planner.get_weather")
def test_plan_trip_rainy(mock_weather):
    mock_weather.return_value = "Rainy"  # نحاكي API ترجّع "Rainy"
    result = plan_trip("Amman")
    assert result == "Take an umbrella ☔"
