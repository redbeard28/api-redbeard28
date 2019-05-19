#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Jérémie CUADRADO <redbeard28>
# https://github.com/redbeard28
# https://redbeard-consulting.fr
import configparser
import requests
#import webapi as web

def get_ipify_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['ipify']['key']

def getGeo():
    import json
    mykey = get_ipify_api_key()
    myip = getIP()
    url = "https://geo.ipify.org/api/v1?apiKey={}&ipAddress={}".format(mykey, myip)
    data = requests.get(url)
    print(data.json())
    donnees =  data.json()
    return donnees

def getIP():
    #import json
    ##ip = get('http://ip.jsontest.com/')
    #ip = requests.get('https://api.ipify.org?format=json')
    ##print(ip.get("ip"))
    #ip_dict = json.loads(ip.text)
    #return ip_dict['ip']
    from flask import request
    ip_string = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    ip_dict = {
        "ip": str(ip_string)
    }
    return str(ip_string)
    #return json.dumps(ip_dict)


if __name__ == '__main__':
    getIP()
    getGeo()
