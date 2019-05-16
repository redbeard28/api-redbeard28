#!/usr/bin/env python

import json
import requests, turtle

def get(self):
url = "http://api.open-notify.org/iss-now.json"
r = requests.get(url)
iss = r.json()
if iss['message'] != 'success':
    message = "ERROR FROM ISS"
    print(message)

iss_lat = float(iss['iss_position']['latitude'])
iss_lon = float(iss['iss_position']['longitude'])


# Display information on world map using Python Turtle
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
# Load the world map picture
screen.bgpic("world-map.gif")

screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup()
iss.goto(iss_lon, iss_lat)

if __name__ == '__main__':
    getvigilance()