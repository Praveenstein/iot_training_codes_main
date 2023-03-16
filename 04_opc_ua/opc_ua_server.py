"""
Simple OPC UA Server for a Device with Temperature and Pressure Sensors

This program creates an OPC UA server in Python using the opcua library.
The server simulates a device with two sensors, a temperature sensor and a pressure sensor.
 The temperature and pressure values are updated every second with random values.

Module Name: opc_ua_server.py
"""

from opcua import ua, Server
import time

# Create a new OPC UA server
server = Server()

# Define the server URI and endpoint URL
server.set_endpoint("opc.tcp://localhost:4840/freeopcua/server/")

# Set the server name
server.set_server_name("Simple OPC UA Server")

# Create a new namespace for our device
namespace = server.register_namespace("http://example.org/simple_opc_ua_server/")

# Create a new object node for our device
device_node_id = ua.NodeId("SimpleDevice", namespace)
device_node = server.nodes.objects.add_object(device_node_id, "SimpleDevice")

# Add a temperature sensor node to the device
temperature_node_id = ua.NodeId("Temperature", namespace)
temperature_node = device_node.add_variable(temperature_node_id, "Temperature", 0.0)
temperature_node.set_writable()  # allow writes to this node

# Add a pressure sensor node to the device
pressure_node_id = ua.NodeId("Pressure", namespace)
pressure_node = device_node.add_variable(pressure_node_id, "Pressure", 0.0)
pressure_node.set_writable()  # allow writes to this node

# Start the server
server.start()

print("Server started. Press Ctrl+C to stop.")

try:
    while True:
        # Update the temperature and pressure nodes with random values
        temperature_node.set_value(ua.Variant(round(time.time() * 100) % 100, ua.VariantType.Float))
        pressure_node.set_value(ua.Variant(round(time.time() * 1000) % 1000, ua.VariantType.Float))
        time.sleep(5)
except KeyboardInterrupt:
    pass

# Stop the server
server.stop()
