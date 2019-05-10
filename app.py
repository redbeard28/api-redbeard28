import configparser
import requests
import datetime
import json
from flask import Flask, jsonify
from flask_restplus import Api, Resource, fields


flask_app = Flask(__name__)
app = Api(app = flask_app,
		  version = "1.0",
		  title = "Redbeard Weather APi",
		  description = "Get the Weather from redbeard28 API")


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

#@weather_space.route('/')
#def index():
#	return redirect("https://redbeard-consulting.fr", code=302)

#@weather_space.route('/weather_city/<string:city>', methods=['GET'])
#@weather_space.route('/weather_city')
weather_space = app.namespace('weather', description='Get the weather')
model = app.model('City model',
                      {'city': fields.String(required=True,
                                             description="Name of the city",
                                             help="First upper case like Paris or Bordeaux")})
@weather_space.route('/<string:city>', methods=['GET'])
class WeatherCityClass(Resource):



    @app.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'city': 'Give the name of the city (ex: Chartres or Paris'})
    #@app.expect(model)
    def get(self, city='Chartres'):
        try:
            api_key = get_api_key()
        except KeyError as e:
            weather_space.abort(401, e.__doc__, status="Could not retrieve openweathermap token", statusCode="401")

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
            result_dict = {'time': time, 'city': city_word, 'temperature': temp_c, 'humidity': humidity, 'longitude': longitude, 'latitude': latitude}
            result_json = jsonify(result_dict)
            return result_json
        except Exception as e:
            weather_space.abort(400, e.__doc__, status="Could not retrieve information from OpenWeatherMap",
                                statusCode="400")
            # url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(city, api_key)
            # r = requests.get(url)
            # return "HTML ERROR : " + str(r.status_code)

sunrise_space = app.namespace('sunrise', description='Get the sunrise')
@sunrise_space.route('/<string:city>', methods=['GET'])
class SunriseCityClass(Resource):

    @app.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'city': 'Give the name of the city (ex: Chartres or Paris'})
    #@app.expect(model)
    def get(self,city='Chartres'):
        try:
            api_key = get_api_key()
        except api_keyError as e:
            weather_space.abort(401, e.__doc__, status="Could not retrieve openweathermap token", statusCode="401")

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
                'time': time,
                'city': city_word,
                'sunrise': sunrise,
                'sunset': sunset,
                'longitude': longitude,
                'latitude': latitude
            }
            result_json = jsonify(result_dict)
            return result_json
        except Exception as e:
            weather_space.abort(400, e.__doc__, status="Could not retrieve information from OpenWeatherMap",
                                statusCode="400")
        # except:
        #    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(city, api_key)
        #    r = requests.get(url)
        #    return "HTML ERROR : " + str(r.status_code)



if __name__ == '__main__':
    flask_app.run(debug=True)
    #app.run()