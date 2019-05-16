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
             params={'city': 'Give the name of the city (ex: Chartres or Paris)'})
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
             params={'city': 'Give the name of the city (ex: Chartres or Paris)'})
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
vigilance_space = app.namespace('vigilance', description='Get the vigilance')
@vigilance_space.route('/<int:departement>', methods=['GET'])
class vigilanceClass(Resource):
    @app.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'departement': 'Give the number of departement (ex: 64)'})
    def get(self,departement=64):
        from ModuleVigilance import getvigilance
        try:
            if len(str(departement)) >= 2:
                result = getvigilance(departement)
                return result
        except Exception as e:
            vigilance_space.abort(400, e.__doc__, status="Invalid departement",
                                statusCode="400")

moustique_space = app.namespace('moustique', description='Get the vigilance for moustique')
@moustique_space.route('/<int:departement>/<int:type>', methods=['GET'])
class vigilanceClass(Resource):
    @app.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'departement': 'Give the number of departement (ex: 64)',
                     'type': 'Give moustique type (1: moustique, 2: moustique tigre)'})
    def get(self,departement=64,type=1):
        from ModuleMoustique import getmoustiqueinfo
        try:
            if len(str(departement)) >= 2:
                result = getmoustiqueinfo(departement,type)
                return result
        except Exception as e:
            moustique_space.abort(400, e.__doc__, status="Invalid departement",
                                statusCode="400")

product_space = app.namespace('product', description='Get product description with barcode (13) input')
@product_space.route('/<int:barcode>', methods=['GET'])
class productClass(Resource):
    @app.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'barcode': 'Give the number barcode'})
    def get(self,barcode=8002270014901):
        from ModuleProduct import getproduct
        try:
            if len(str(barcode)) == 13:
                result = getproduct(barcode)
                return result
        except Exception as e:
            product_space.abort(400, e.__doc__, status="Invalid barcode",
                                statusCode="400")

myip_space = app.namespace('ip', description='Get Your IP')
@myip_space.route('/myip', methods=['GET'])
class myipClass(Resource):
    @app.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Server Errorr'})
    def get(self):
        try:
            from ModuleMyip import getIP
        except ImportError:
            return "Error Importing Module for MyIP"

        return getIP()
@myip_space.route('/geoip', methods=['GET'])
class geoipClass(Resource):
    @app.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Server Errorr'})
    def get(self):
        try:
            from ModuleMyip import getGeo
        except ImportError:
            return "Error Importing Module for MyIP"

        return getGeo()

#iss_space = app.namespace('issposition', description='Get ISS Trottle on Word-MAP')
#@iss_space.route('/', methods=['GET'])
#class isspositionClass(Resource):
#    @app.doc(responses={200: 'OK', 400: 'Invalid Argument'})
#    def get(self):
#        import turtle
#        try:
#            url = "http://api.open-notify.org/iss-now.json"
#            r = requests.get(url)
#            iss = r.json()
#            if iss['message'] != 'success':
#                message = "ERROR FROM ISS"
#                print(message)
#
#            iss_lat = float(iss['iss_position']['latitude'])
#            iss_lon = float(iss['iss_position']['longitude'])
#
#
#            # Display information on world map using Python Turtle
#            screen = turtle.Screen()
#            screen.setup(720, 360)
#            screen.setworldcoordinates(-180, -90, 180, 90)
#            # Load the world map picture
#            screen.bgpic("world-map.gif")
#
#            screen.register_shape("iss.gif")
#            iss = turtle.Turtle()
#            iss.shape("iss.gif")
#            iss.setheading(45)
#            iss.penup()
#            iss.goto(iss_lon, iss_lat)
#        except Exception as e:
#            iss_space.abort(400, e.__doc__, status="ERRO from ISS",
#                                statusCode="400")

if __name__ == '__main__':
    flask_app.run(debug=True)
    #app.run()