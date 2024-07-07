from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="Kansas City"):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={
        os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print("\n*** Get current Weather Conditions ***\n")
    city = input("\nPlease enter a ciyy name: ")
    # check for empty strings or strings with only spaces, Using if not with Boolean values is a common practice in Python for negating conditions. It is especially handy in cases where you want to check for the absence of a condition, such as when a variable is False or a list is empty ( not my_list would evaluate to True if my_list is empty).
    if not bool(city.strip()):
        city = "Kansas City"

    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)
