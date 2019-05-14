#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Jérémie CUADRADO <redbeard28>
# https://github.com/redbeard28
# https://redbeard-consulting.fr
import urllib, json

def getMyIp():

    data = json.loads(urllib.urlopen("http://ip.jsontest.com/").read())
    print(data["ip"])

def getIP():
    from requests import get

    ip = get('http://ip.jsontest.com/').json()
    return ip


#if __name__ == '__main__':
    getIP()
