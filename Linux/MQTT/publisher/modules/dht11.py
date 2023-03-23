import Adafruit_DHT
from json import JSONEncoder
from time import sleep
from module import Module

class DHT11(Module):
  def __init__(self) -> None:
    super().__init__()

    self.dht11_instance = Adafruit_DHT.DHT11
    self.dht11_pin = 27
    self.homeassistant_discovery_type = "sensor"
    self.homeassistant_unique_id = "dht11"

  @property
  def discovery_config(self) -> object:
    return [{
      "name": "RPi-SenseStation DHT11 Temperature",
      "unique_id": self.homeassistant_real_unique_id + "_temperature",
      "state_topic": self.get_real_topic("dht11/state"),
      "device_class": "temperature",
      "unit_of_measurement": "°C",
      "entity_category": "diagnostic",
      "state_class": "measurement",
      "expire_after": 60,
      "value_template": "{{ value_json.temperature }}",
    }, {
      "name": "RPi-SenseStation DHT11 Humidity",
      "unique_id": self.homeassistant_real_unique_id + "_humidity",
      "state_topic": self.get_real_topic("dht11/state"),
      "device_class": "humidity",
      "unit_of_measurement": "%",
      "entity_category": "diagnostic",
      "state_class": "measurement",
      "expire_after": 60,
      "value_template": "{{ value_json.humidity }}",
    }]
  
  def send_discovery(self) -> None:
    self.client.publish(
      self.homeassistant_discovery_topic.replace(self.homeassistant_unique_id, "dht11_temperature"),
      JSONEncoder().encode(self.discovery_config[0]),
      retain=True)
    self.client.publish(
      self.homeassistant_discovery_topic.replace(self.homeassistant_unique_id, "dht11_humidity"),
      JSONEncoder().encode(self.discovery_config[1]),
      retain=True)

  def run(self) -> None:
    super().run()

    while True:
      if hasattr(self, "client") and self.client.is_connected():
        humidity, temperature = Adafruit_DHT.read_retry(self.dht11_instance, self.dht11_pin)

        if (humidity != None and temperature != None) \
          and not (humidity == 0 and temperature == 0) \
          and (humidity >= 0 and humidity <= 100) \
          and (temperature >= 0 and temperature <= 80):
          # 0 <= Humidity <= 100, 0 <= Temperature <= 50
          # Sometimes the values become wrong(e.g. humidity is 162...), so we should guard this

          self.client.publish(self.get_real_topic("dht11/state"), JSONEncoder().encode({
            "temperature": temperature,
            "humidity": humidity,
          }))
        else:
          print("Bad DHT11 readings!")
      
      sleep(30)
