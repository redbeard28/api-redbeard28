#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Jérémie CUADRADO <redbeard28>
# https://github.com/redbeard28
# https://redbeard-consulting.fr

import paho.mqtt.client as mqtt
import json
import configparser
import time
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
########################################

def get_mqtt_broker():
    config = configparser.ConfigParser()
    config.read('config.ini')
    mqtt_broker = {
        'server': str(config['mqtt-broker']['server']),
        'port':str( config['mqtt-broker']['port'])
    }
    return json.dumps(mqtt_broker)

def get_mqtt_garage():
    config = configparser.ConfigParser()
    config.read('config.ini')
    mqtt_garage = {
        'set_garage': str(config['mqtt-garage']['set_garage']),
        'status_garage': str(config['mqtt-garage']['status_garage'])
    }
    return json.dumps(mqtt_garage)

def get_mqtt_lampe():
    config = configparser.ConfigParser()
    config.read('config.ini')
    mqtt_lampe = {
        'set_lampe': str(config['mqtt-lampe']['set_lampe']),
        'status_lampe': str(config['mqtt-lampe']['status_lampe'])
    }
    return json.dumps(mqtt_lampe)

mqtt_infos = json.loads(get_mqtt_broker())
mqtt_garage = json.loads(get_mqtt_garage())
mqtt_lampe = json.loads(get_mqtt_lampe())

host = mqtt_infos['server']
broker_port = mqtt_infos['port']
topic_garage_status = mqtt_garage['status_garage']
topic_lampe_status = mqtt_lampe['status_lampe']
topic_lampe_set = mqtt_lampe['set_lampe']

client = mqtt.Client(client_id='mqtt-explorer-674946e8', clean_session=True, transport='tcp')
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(host, port=int(broker_port), keepalive=60)
client.loop_start() #start the loop
print("Subscribing to topic :" + topic_lampe_status)
client.subscribe(topic_lampe_status, qos=1)
print("Publishing message to topic :" + topic_lampe_status)
client.publish(topic_lampe_set,"1")
time.sleep(10) # wait
client.loop_stop() #stop the loop