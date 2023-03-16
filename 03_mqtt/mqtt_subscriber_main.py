"""
Title: MQTT temperature subscriber
===================================

This script connects to an MQTT broker, subscribes to the "temperature" topic, and prints incoming messages.

Functions
---------
on_connect:
    Callback function executed on connection to the broker.
on_message:
    Callback function executed on receipt of a message.

"""

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    # Print the result code of the connection and subscribe to the "temperature" topic
    print("Connected with result code "+str(rc))

    # Subscribing to the "temperature" topic
    client.subscribe("temperature")


def on_message(client, userdata, msg):

    print("============================================================")
    # Print the received message topic and payload
    print("Message Topic: ", msg.topic)
    print("Message: " + (msg.payload.decode("utf-8")))
    print("============================================================")


# Creating mqtt client object
mqtt_client = mqtt.Client()

# Setting callback function for on connect
mqtt_client.on_connect = on_connect

# Setting callback function on receiving new message
mqtt_client.on_message = on_message

# Connecting to the mqtt broker server
mqtt_client.connect("localhost", 1883, 60)

mqtt_client.loop_forever()  # Start the loop to listen for incoming messages
