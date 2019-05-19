#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Jérémie CUADRADO <redbeard28>
# https://github.com/redbeard28
# https://redbeard-consulting.fr

import requests
import json

def getData(dep,mType):
    # type 1 = moustique ; 2 = moustique tigre
    data = json.loads(requests.get("http://vigilance-moustiques.com/maps-manager/public/json/"+str(mType)).text)["alertes"]
    mStatus = ""
    for colorType in data:
        for department in data[colorType]:
            if department == str(dep):
                mStatus = colorType
                break
    return mStatus

def getDataFromColor(color):
    code = 0
    text = "Risque Tres Faible"
    if color == "jaune":
        code = 1
        text = "Risque Faible"
    elif color == "orange":
        code = 2
        text = "Rique Modere"
    elif color == "rouge":
        code = 3
        text = "Risque Eleve"
    elif color == "pourpre":
        code = 4
        text = "Risque Tres Eleve"
    result_dict = {
        "risk_code": code,
        "risk_color": color,
        "risk_msg": text
    }
    return result_dict

def getmoustiqueinfo(dep,mType):
    import datetime
    dateTimeObj = datetime.datetime.now()
    ts = datetime.datetime.now().timestamp()
    data = getData(dep,mType)
    dzData = getDataFromColor(data)
    if mType == 1:
        moustique = 'moustique'
    elif mType == 2:
        moustique = 'moustique tigre'
    # TODO error if different of 1 or 2


    data_dict = {
        "timestamp": ts,
        "date": dateTimeObj.isoformat(),
        "type_moustique": moustique,
        "couleur": data,
        "risk_code": dzData['risk_code'],
        "risk_msg": dzData['risk_msg']
    }
    return data_dict



if __name__ == '__main__':
    getmoustiqueinfo()

