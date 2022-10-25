from bs4 import BeautifulSoup
from flask import url_for
import requests
from pprint import pprint
from app.routes.parse.parse_amindi_org import parse_amindi_org


def parse_amindi_ge(city):
    cities = parse_amindi_org()
    url1 = f'https://amindi.ge/ka/city/{city}/?d=5'
    response = requests.get(url1)
    parser = BeautifulSoup(response.text, 'html.parser')
    weather_html = parser.find(class_='weather-days-right').find_all(class_='col px-0')

    image_weather_map = {
        '/static/img/weather_small_01.png': 'მზიანი',
        '/static/img/weather_small_02.png': 'ნაწილობრივ ღრუბლიანი',
        '/static/img/weather_small_03.png': 'ღრუბლიანი',
        '/static/img/weather_small_04.png': 'ღრუბლიანი',
        '/static/img/weather_small_06.png': 'უმეტესად ღრუბლიანი',
        '/static/img/weather_small_07.png': 'უმეტესად ღრუბლიანი',
        '/static/img/weather_small_14.png': 'ღრუბლიანი',
        '/static/img/weather_small_12.png': 'წვიმიანი',
        '/static/img/weather_small_13.png': 'ნახევრად-წვიმიანი',
        '/static/img/weather_small_18.png': 'წვიმა ჭექა-ქუხილით',
        '/static/img/weather_small_32.png': 'ქარი'

    }



    weekly_weather = {}

    for weather in weather_html:
        temperature_html = weather.find_all('span')
        temperature = f"{temperature_html[0].text}°{temperature_html[1].text}°"
        weekday = weather.find(class_='weekDay').text
        weather_conditions = weather.find('img')['src']
        day = weather.find(class_='day').text


        weekly_weather[weekday] = {'temperature': temperature, 'weather': image_weather_map[weather_conditions],'img':weather_conditions,'day':day}



    return weekly_weather, cities


if __name__ == "__main__":
    pprint(parse_amindi_ge(city='ბათუმი'))
