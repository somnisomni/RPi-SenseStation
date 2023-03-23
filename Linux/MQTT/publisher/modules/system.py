from json import JSONEncoder
import subprocess
from time import sleep
from module import Module

class System(Module):
  def __init__(self) -> None:
    super().__init__()

    self.cpufreq_current_sysfile = "/sys/devices/system/cpu/cpufreq/policy0/scaling_cur_freq"
    self.cpufreq_max_sysfile = "/sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq"
    self.cpufreq_min_sysfile = "/sys/devices/system/cpu/cpufreq/policy0/scaling_min_freq"

    self.homeassistant_discovery_type = "sensor"
    self.homeassistant_unique_id = "system"

  @property
  def discovery_config(self) -> object:
    return [{
      "name": "RPi-SenseStation System CPU Current Frequency",
      "unique_id": self.homeassistant_real_unique_id + "_cpufreq_current",
      "state_topic": self.get_real_topic("system/state"),
      "device_class": "frequency",
      "unit_of_measurement": "MHz",
      "entity_category": "diagnostic",
      "state_class": "measurement",
      "expire_after": 20,
      "value_template": "{{ value_json.cpufreq.current }}",
    }, {
      "name": "RPi-SenseStation System CPU Max Frequency",
      "unique_id": self.homeassistant_real_unique_id + "_cpufreq_max",
      "state_topic": self.get_real_topic("system/state"),
      "device_class": "frequency",
      "unit_of_measurement": "MHz",
      "entity_category": "diagnostic",
      "state_class": "measurement",
      "expire_after": 20,
      "value_template": "{{ value_json.cpufreq.max }}",
    }, {
      "name": "RPi-SenseStation System CPU Min Frequency",
      "unique_id": self.homeassistant_real_unique_id + "_cpufreq_min",
      "state_topic": self.get_real_topic("system/state"),
      "device_class": "frequency",
      "unit_of_measurement": "MHz",
      "entity_category": "diagnostic",
      "state_class": "measurement",
      "expire_after": 20,
      "value_template": "{{ value_json.cpufreq.min }}",
    }, {
      "name": "RPi-SenseStation System Core Temperature",
      "unique_id": self.homeassistant_real_unique_id + "_thermal_temperature",
      "state_topic": self.get_real_topic("system/state"),
      "device_class": "temperature",
      "unit_of_measurement": "°C",
      "entity_category": "diagnostic",
      "state_class": "measurement",
      "expire_after": 20,
      "value_template": "{{ value_json.thermal.temperature }}",
    }]
  
  def send_discovery(self) -> None:
    self.client.publish(
      self.homeassistant_discovery_topic.replace(self.homeassistant_unique_id, "system_cpufreq_current"),
      JSONEncoder().encode(self.discovery_config[0]),
      retain=True)
    self.client.publish(
      self.homeassistant_discovery_topic.replace(self.homeassistant_unique_id, "system_cpufreq_max"),
      JSONEncoder().encode(self.discovery_config[1]),
      retain=True)
    self.client.publish(
      self.homeassistant_discovery_topic.replace(self.homeassistant_unique_id, "system_cpufreq_min"),
      JSONEncoder().encode(self.discovery_config[2]),
      retain=True)
    self.client.publish(
      self.homeassistant_discovery_topic.replace(self.homeassistant_unique_id, "system_thermal_temperature"),
      JSONEncoder().encode(self.discovery_config[3]),
      retain=True)

  def run(self) -> None:
    super().run()

    while True:
      if hasattr(self, "client") and self.client.is_connected():
        output = { "cpufreq": {}, "thermal": {} }
  
        ## CPU current frequency ##
        cpufreqCurrentCall = subprocess.run(["cat", self.cpufreq_current_sysfile], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

        if cpufreqCurrentCall.returncode != 0 or not cpufreqCurrentCall.stdout:
          print("Failed to get current CPU frequency!")
        else:
          output["cpufreq"]["current"] = int(cpufreqCurrentCall.stdout.decode("utf-8").strip()) // 1000
        
        ## CPU max frequency ##
        cpufreqMaxCall = subprocess.run(["cat", self.cpufreq_max_sysfile], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

        if cpufreqMaxCall.returncode != 0 or not cpufreqMaxCall.stdout:
          print("Failed to get max CPU frequency!")
        else:
          output["cpufreq"]["max"] = int(cpufreqMaxCall.stdout.decode("utf-8").strip()) // 1000
          
        ## CPU min frequency ##
        cpufreqMinCall = subprocess.run(["cat", self.cpufreq_min_sysfile], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

        if cpufreqMinCall.returncode != 0 or not cpufreqMinCall.stdout:
          print("Failed to get min CPU frequency!")
        else:
          output["cpufreq"]["min"] = int(cpufreqMinCall.stdout.decode("utf-8").strip()) // 1000
        
        ## Thermal temperature ##
        thermalTemperatureCall = subprocess.run(["vcgencmd", "measure_temp"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

        if thermalTemperatureCall.returncode != 0 or not thermalTemperatureCall.stdout:
          print("Failed to get thermal temperature via vcgencmd!")
        else:
          callResult = thermalTemperatureCall.stdout.decode("utf-8").strip()  # temp=NN.N'C
          callResult = callResult.split("=")[1]  # NN.N'C
          callResult = callResult.split("'")[0]  # NN.N
          callResult = float(callResult)         # float(NN.N)

          output["thermal"]["temperature"] = callResult

        ## MQTT Publish ##
        self.client.publish(self.get_real_topic("system/state"), JSONEncoder().encode(output))
      
      sleep(10)
