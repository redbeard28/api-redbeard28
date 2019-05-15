#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Jérémie CUADRADO <redbeard28>
# https://github.com/redbeard28
# https://redbeard-consulting.fr
import configparser
from requests import get

def get_ipify_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['ipify']['key']

def getGeo():

    mykey = get_ipify_api_key()
    myip = getIP()
    myip_string = myip['ip']
    url = "https://geo.ipify.org/api/v1?apiKey={}&ipAddress={}".format(mykey, myip_string)
    data = get(url).json()
    return data

def getIP():

    #ip = get('http://ip.jsontest.com/')
    ip = get('https://api.ipify.org?format=json').json()

    return ip


if __name__ == '__main__':
    getIP()
    getGeo()
