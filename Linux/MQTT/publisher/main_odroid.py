from json import JSONEncoder
from typing import List

import paho.mqtt.client as mqtt
from module import Module
from module_odroid import Module_ODROID
from modules.heartbeat import Heartbeat
from modules.ping import Ping
from modules.dht11_odroid import DHT11_ODROID
from modules.system_odroid import System_ODROID

modules: List[Module | Module_ODROID] = []

jsonEncoder = JSONEncoder()

def start_mqtt_client():
  def on_connect(client: mqtt.Client, userdata, flags, rc: int):
    if rc == 0:
      print("Connected to {}:{}".format(client._host, client._port))
      client.subscribe("homeassistant/#")

      # Send configuration of all of modules
      for module in modules:
        module.set_mqtt_client(client)
        module.send_discovery()

  def on_disconnect(client, userdata, flags, rc: int = 0):
    print("Disconnected")

  def on_message(client: mqtt.Client, userdata, message: mqtt.MQTTMessage):
    if message.topic == "homeassistant/status":
      print("Home Assistant integration status : " + message.payload.decode("utf-8"))

  client = mqtt.Client()
  client.on_connect = on_connect
  client.on_disconnect = on_disconnect
  client.on_message = on_message
  client.username_pw_set("somni", "somni")
  client.connect("localhost", 8889)
  client.loop_forever()

def setup_modules():
  # Add modules
  modules.append(Heartbeat())
  modules.append(Ping("somni PC", "10.39.39.39"))
  modules.append(DHT11_ODROID())
  modules.append(System_ODROID())

  # Start all of modules' thread
  for module in modules:
    module.start()

if __name__ == "__main__":
  try:
    print("** somni-ODROID MQTT client **")
    setup_modules()

    start_mqtt_client()
  except:
    print("\nExiting!")
