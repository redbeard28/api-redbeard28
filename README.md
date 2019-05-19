# Simple Flask-RestFul API

## Why?
Because I want a simple input for my needs and I don't want to change all my coding if an api rest of third part change.

The basic idea is to have a uniq access point for device subscriptions/read like:
 * monitor screen
 * Weather infos (OpenWeatherMap)
 * Sunset infos (OpenWeatherMap)
 * Air Quality (airvisual API)
 * Vigilance French Flood (vigilance.fr)
 * Vigilance mosquito (vigilance-moustiques.com)
 * Vigilance Pollens (pollens.fr)
 * GeoIP from ipify.org (not actually functionnal http_x_forward)
 * MyIP from HTTP HEADERS (not actually functionnal http_x_forward)



All datas are garthered from Third API
## Sources of inspirations
 * https://github.com/guiguiabloc/api-domogeek
 * https://towardsdatascience.com/working-with-apis-using-flask-flask-restplus-and-swagger-ui-7cf447deda7f
 * https://www.youtube.com/watch?v=sbYXa6HJJ5M

## config.ini
You need to create a file called config.ini in the same folder of your app.py

config.ini exemple:
````python
[openweathermap]
api=93XXXXXXXXXXYYYYYYHHHHHHH
````