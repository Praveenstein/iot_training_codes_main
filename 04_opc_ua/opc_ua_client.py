"""
Simple OPC UA Client for reading and setting a Device Parameters

This program creates an OPC UA mqtt_client in Python using the opcua library.
The mqtt_client connects to the OPC server to read the temperature value and set the pressure value

Module Name: opc_ua_server.py
"""

from opcua import Client, ua

# Set up the mqtt_client and connect to the server
client = Client("opc.tcp://localhost:4840/freeopcua/server/")
client.connect()

# Get the temperature and pressure nodes from the server
temperature_node = client.get_node(ua.NodeId("Temperature", 2))
pressure_node = client.get_node(ua.NodeId("Pressure", 2))

# Read the value of the temperature node
temperature_value = temperature_node.get_value()

print("Temperature: ", temperature_value)

set_pressure_value = 66

# Write the value of the temperature node to the pressure node
pressure_node.set_value(set_pressure_value)

# Disconnect from the server
client.disconnect()
