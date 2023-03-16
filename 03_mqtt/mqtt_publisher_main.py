"""
Title: MQTT temperature publisher
==================================

This script connects to an MQTT broker and publishes a randomly generated temperature
value to the "temperature" topic.

Functions
---------
None

"""
import time
import random

import paho.mqtt.client as mqtt


# Set up the MQTT mqtt_client
client = mqtt.Client()

# Connect to the broker
client.connect("localhost", 1883, 60)

for i in range(10):
    # Generate a random temperature value
    temperature = round(random.uniform(10.0, 30.0), 4)

    # Publish the temperature value to the "temperature" topic
    client.publish("temperature", str(temperature).encode("utf-8"))

    print("Published temperature value")
    time.sleep(2)

# Disconnect from the broker
client.disconnect()
