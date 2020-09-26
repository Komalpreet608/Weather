from requests import get
import json
from datetime import date, datetime

#   Enter your api key here
api_key = ''


def get_weather(city_name):
    base_url = 'https://api.openweathermap.org/data/2.5/weather?q='
    complete_url = base_url + city_name + '&units=metric&appid=' + str(api_key)

    response = get(complete_url)

    x = response.json()

    if x['cod'] == int('200'):
        temp = x['main']['temp']
        pressure = x['main']['pressure']
        humidity = x['main']['humidity']
        clouds = x['clouds']['all']
        wind_speed = x['wind']['speed']
        wind_deg = x['wind']['deg']

        # city name and country
        print(city_name + ', ' + x['sys']['country'])

        # current time and date
        today = date.today()
        current_time = datetime.now()

        print(current_time.strftime('%A'), today.day,
              current_time.strftime('%B'), today.year)
        print('Time:', str(current_time.strftime('%I:%M %p')))

        # wind direction
        wind_direction = ''

        if wind_deg > 348.75 and wind_deg <= 360 and wind_deg <= 11.25:
            wind_direction = "N"
        elif wind_deg > 11.25 and wind_deg <= 33.75:
            wind_direction = "N/NE"
        elif wind_deg > 33.75 and wind_deg <= 56.25:
            wind_direction = "NE"
        elif wind_deg > 56.25 and wind_deg <= 78.75:
            wind_direction = "E/NE"
        elif wind_deg > 78.75 and wind_deg <= 101.25:
            wind_direction = "E"
        elif wind_deg > 101.25 and wind_deg <= 123.25:
            wind_direction = "E/SE"
        elif wind_deg > 123.25 and wind_deg <= 146.25:
            wind_direction = "SE"
        elif wind_deg > 146.25 and wind_deg <= 168.75:
            wind_direction = "S/SE"
        elif wind_deg > 168.75 and wind_deg <= 191.25:
            wind_direction = "S"
        elif wind_deg > 191.25 and wind_deg <= 213.75:
            wind_direction = "S/SW"
        elif wind_deg > 231.75 and wind_deg <= 236.25:
            wind_direction = "SW"
        elif wind_deg > 236.25 and wind_deg <= 258.75:
            wind_direction = "W/SW"
        elif wind_deg > 258.75 and wind_deg <= 281.25:
            wind_direction = "W"
        elif wind_deg > 281.25 and wind_deg <= 303.75:
            wind_direction = "W/NW"
        elif wind_deg > 303.75 and wind_deg <= 326.25:
            wind_direction = "NW"
        elif wind_deg > 326.25 and wind_deg <= 348.75:
            wind_direction = "N/NW"
        else:
            wind_direction = "Error"

        # print everything
        print('Temperature: ' + str(temp) + chr(176) + 'C')
        print('Pressure: ' + str(pressure) + '%')
        print('Humidity: ' + str(humidity) + '%')
        print('Cloudiness: ' + str(clouds) + '%')
        print('Wind Speed: ' + str(round(wind_speed, 2)) + 'm/s')
        print('Wind Direction: ' + str(wind_direction))

    elif x['cod'] == int('401'):
        print('Invalid API key')

    elif x['cod'] == int('404'):
        print('City not found')
        print('Try Again')
        get_input()

    elif x['cod'] == int('429'):
        print('You have free tariff and make more than 60 API calls per minute')

    else:
        print(x['cod'])


def get_input():
    city_name = input('Enter city name: ')
    get_weather(city_name)


get_input()
