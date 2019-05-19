#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Jérémie CUADRADO <redbeard28>
# https://github.com/redbeard28
# https://redbeard-consulting.fr

import json
import requests
import configparser

def getAirQuality_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    airvisual = {
        'api_token': str(config['airvisual']['key'])
    }
    return json.dumps(airvisual)

def getAirQuality(country,state,city):
    """
    Get the Air quality from airviual API Rest
    :param api_token:
    :param country: France
    :param state: Centre
    :param city: Chartres
    :return: JSON DATA
    """
    airvisual_infos = json.loads(getAirQuality_config())
    api_token = airvisual_infos['api_token']
    url = "https://api.airvisual.com/v2/city?city={}&state={}&country={}&key={}".format(city, state, country, api_token)
    resp = requests.get(url)
    print(resp.json())
    donnees = resp.json()
    return donnees

def getAirQualityByIp():
    """
    Get airquality by HTTP_X_REAL_IP
    :return: JSON data
    """
    airvisual_infos = json.loads(getAirQuality_config())
    api_token = airvisual_infos['api_token']
    url = "https://api.airvisual.com/v2/nearest_city?key={}".format(api_token)
    resp = requests.get(url)
    print(resp.json())
    donnees = resp.json()
    return donnees

if __name__ == '__main__':
    getAirQuality()
    getAirQualityByIp()
