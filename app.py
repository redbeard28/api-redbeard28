import configparser
import requests
import datetime
import json, sys
import os
from flask import Flask,redirect
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']


def get_api_location():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['airvisual']['location']


def get_api_country():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['airvisual']['country']


def get_api_state():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['airvisual']['state']

@app.route('/')
def index():
	return redirect("https://redbeard-consulting.fr", code=302)

@app.route('/weather_city/<string:city>', methods=['GET'])
@app.route('/weather_city')
def weather_city(city='Chartres'):
    try:
        api_key = get_api_key()
    except:
        return 'NO API KEY FOUND'

    try:
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(city, api_key)
        r = requests.get(url)
        weather = r.json()
        timestamp = weather['dt']
        time = str(datetime.datetime.fromtimestamp(timestamp))
        temp_c = weather['main']['temp']
        longitude = weather['coord']['lon']
        latitude = weather['coord']['lat']
        city_word = weather['name']
        humidity = weather['main']['humidity']
        result_dict = {
            'time' : time,
            'city' : city_word,
            'temperature' : temp_c,
            'humidity' : humidity,
            'longitude' : longitude,
            'latitude' : latitude
        }
        result_json = json.dumps(result_dict)
        return result_json
    except:
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(city, api_key)
        r = requests.get(url)
        return "HTML ERROR : " + str(r.status_code)



@app.route('/sunrise_city/<string:city>', methods=['GET'])
@app.route('/sunrise_city')
def sunrise_city(city='Chartres'):
    try:
        api_key = get_api_key()
    except:
        return 'NO API KEY FOUND'

    try:
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(city, api_key)
        r = requests.get(url)
        weather = r.json()
        timestamp = weather['dt']
        time = str(datetime.datetime.fromtimestamp(timestamp))
        city_word = weather['name']
        sunrise = str(datetime.datetime.fromtimestamp(weather['sys']['sunrise']))
        sunset = str(datetime.datetime.fromtimestamp(weather['sys']['sunset']))
        longitude = weather['coord']['lon']
        latitude = weather['coord']['lat']
        result_dict = {
            'time' : time,
            'city' : city_word,
            'sunrise' : sunrise,
            'sunset' : sunset,
            'longitude' : longitude,
            'latitude' : latitude
        }
        result_json = json.dumps(result_dict)
        return result_json
    except:
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(city, api_key)
        r = requests.get(url)
        return "HTML ERROR : " + str(r.status_code)


if __name__ == '__main__':
    app.run(debug=True)
    #app.run()