import sys
import json

import paho.mqtt.client as paho

client = paho.Client()
sensor_id = 'sensor_temp3'
sensor_type = 'temperature'
value = -10

connectionStatusMessage = json.dumps({"sensor_id": sensor_id})
client.will_set("sensor_disconnected", connectionStatusMessage, qos=0)

if client.connect("localhost", 1883, 60) != 0:
    print("Couldn't connect to the mqtt broker")
    sys.exit(1)

client.loop_start()

client.publish("sensor_connected", connectionStatusMessage, 0)

def publish_reading(value):
    message = json.dumps({"sensor_id": sensor_id, "value": value, "sensor_type": sensor_type})
    client.publish("readings", message, 0)
    print(f"Published: {message}")

# Main loop for user input
while True:
    print("\nOptions:")
    print("1. Enter value and publish reading")
    print("2. Disconnect")
    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        try:
            value = float(input("Enter temperature value: "))
            publish_reading(value)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    elif choice == '2':
        print("Disconnecting...")
        client.publish("sensor_disconnected", connectionStatusMessage, 0)
        client.disconnect()
        break
    else:
        print("Invalid choice. Please choose 1 or 2.")