from sense_hat import SenseHat
from json import JSONEncoder
from time import sleep
from module import Module

class SenseHAT(Module):
  def __init__(self) -> None:
    super().__init__()

    self.sensehat_instance = SenseHat()
    self.homeassistant_discovery_type = "sensor"
    self.homeassistant_unique_id = "sensehat"

  @property
  def discovery_config(self) -> object:
    return [{
      "name": "RPi-SenseStation Sense-HAT Temperature",
      "unique_id": self.homeassistant_real_unique_id + "_temperature",
      "state_topic": self.get_real_topic("sensehat/state"),
      "device_class": "temperature",
      "unit_of_measurement": "°C",
      "entity_category": "diagnostic",
      "state_class": "measurement",
      "expire_after": 60,
      "value_template": "{{ value_json.temperature }}",
    }, {
      "name": "RPi-SenseStation Sense-HAT Humidity",
      "unique_id": self.homeassistant_real_unique_id + "_humidity",
      "state_topic": self.get_real_topic("sensehat/state"),
      "device_class": "humidity",
      "unit_of_measurement": "%",
      "entity_category": "diagnostic",
      "state_class": "measurement",
      "expire_after": 60,
      "value_template": "{{ value_json.humidity }}",
    }, {
      "name": "RPi-SenseStation Sense-HAT Air Pressure",
      "unique_id": self.homeassistant_real_unique_id + "_pressure",
      "state_topic": self.get_real_topic("sensehat/state"),
      "device_class": "pressure",
      "unit_of_measurement": "kPa",
      "entity_category": "diagnostic",
      "state_class": "measurement",
      "expire_after": 60,
      "value_template": "{{ value_json.pressure }}",
    }]
  
  def send_discovery(self) -> None:
    self.client.publish(
      self.homeassistant_discovery_topic.replace(self.homeassistant_unique_id, "sensehat_temperature"),
      JSONEncoder().encode(self.discovery_config[0]),
      retain=True)
    self.client.publish(
      self.homeassistant_discovery_topic.replace(self.homeassistant_unique_id, "sensehat_humidity"),
      JSONEncoder().encode(self.discovery_config[1]),
      retain=True)
    self.client.publish(
      self.homeassistant_discovery_topic.replace(self.homeassistant_unique_id, "sensehat_pressure"),
      JSONEncoder().encode(self.discovery_config[2]),
      retain=True)

  def run(self) -> None:
    super().run()

    # Drop first readings
    self.sensehat_instance.get_temperature()
    self.sensehat_instance.get_humidity()
    self.sensehat_instance.get_pressure()

    while True:
      if hasattr(self, "client") and self.client.is_connected():
        temperature = round(self.sensehat_instance.get_temperature(), 2)
        humidity = round(self.sensehat_instance.get_humidity(), 2)
        pressure = round(self.sensehat_instance.get_pressure(), 2)

        if (humidity != None and temperature != None) \
          and not (humidity == 0 and temperature == 0 and pressure == 0) \
          and (humidity >= 0 and humidity <= 100) \
          and (temperature >= -40 and temperature <= 80) \
          and (pressure >= 100 and pressure <= 2000):

          self.client.publish(self.get_real_topic("sensehat/state"), JSONEncoder().encode({
            "temperature": temperature,
            "humidity": humidity,
            "pressure": pressure,
          }))
        else:
          print("Bad Sense-HAT sensor readings!")
      
      sleep(30)
