#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Jérémie CUADRADO <redbeard28>
# https://github.com/redbeard28
# https://redbeard-consulting.fr

import requests
import json

def getPollensApiData(dep,type):
    pollen = type
    data = requests.get("https://www.pollens.fr/risks/thea/counties/"+str(dep))
    resp = json.loads(data.text)
    return resp

if __name__ == '__main__':
    getPollensApiData()