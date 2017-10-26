#!/usr/bin/python3
import serial

import requests
import json

import config as cfg

print('Welcome to MicroWeather v0.1')

ow_api_key = cfg.open_weather_api_key
url = 'http://api.openweathermap.org/data/2.5/weather?q=Aalborg&units=metric&APPID=' + ow_api_key
response = requests.get(url)
print(response)


location_info = json.loads(response.content)
print(location_info)

current_weather = location_info['main']
print('Temperature is {}'.format(current_weather['temp']))

print('Goodbye')
