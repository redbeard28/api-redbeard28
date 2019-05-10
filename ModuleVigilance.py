#!/usr/bin/python
# -*- coding: utf-8 -*-
# Original source from:
# Gruik coded by GuiguiAbloc
# http://blog.guiguiabloc.fr
# http://api.domogeek.fr
#
# Modified by jeremie cuadrado <redbeard28>

import urllib.request
from xml.dom import minidom
from flask import jsonify


def color(number):
    if number == "0":
        return "vert"
    if number == "1":
        return "vert"
    if number == "2":
        return "jaune"
    if number == "3":
        return "orange"
    if number == "4":
        return "rouge"


def risklong(number):
    if number == "1":
        return "vent"
    if number == "2":
        return "pluie-inondation"
    if number == "3":
        return "orages"
    if number == "4":
        return "inondations"
    if number == "5":
        return "neige-verglas"
    if number == "6":
        return "canicule"
    if number == "7":
        return "grand-froid"

def getvigilance(deprequest):
    riskresult = ""
    couleur = ""
    url = 'http://vigilance.meteofrance.com/data/NXFR34_LFPW_.xml'
    dom = minidom.parse(urllib.request.urlopen(url))
    for all in dom.getElementsByTagName('datavigilance'):
        depart = all.attributes['dep'].value
        colorresult = all.attributes['couleur'].value
        for risk in all.getElementsByTagName('risque'):
            riskresult = risk.attributes['valeur'].value
        for flood in all.getElementsByTagName('crue'):
            floodresult = flood.attributes['valeur'].value
        riskresult = risklong(riskresult)
        floodresult = color(floodresult)
        if not riskresult:
            riskresult = "RAS"
        if depart == str(deprequest):
            couleur = color(colorresult)
            result_dict = {
                'flood': floodresult,
                'couleur': couleur,
                'risk': riskresult
            }
            result_json = jsonify(result_dict)
            return result_json


if __name__ == '__main__':
    getvigilance()
