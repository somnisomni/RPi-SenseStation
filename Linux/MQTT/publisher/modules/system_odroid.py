from json import JSONEncoder
import subprocess
from time import sleep
from module_odroid import Module_ODROID

class System_ODROID(Module_ODROID):
  def __init__(self) -> None:
    super().__init__()

    self.cpufreq0_current_sysfile = "/sys/devices/system/cpu/cpufreq/policy0/scaling_cur_freq"
    self.cpufreq0_max_sysfile = "/sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq"
    self.cpufreq0_min_sysfile = "/sys/devices/system/cpu/cpufreq/policy0/scaling_min_freq"
    self.cpufreq1_current_sysfile = "/sys/devices/system/cpu/cpufreq/policy2/scaling_cur_freq"
    self.cpufreq1_max_sysfile = "/sys/devices/system/cpu/cpufreq/policy2/scaling_max_freq"
    self.cpufreq1_min_sysfile = "/sys/devices/system/cpu/cpufreq/policy2/scaling_min_freq"

    self.homeassistant_discovery_type = "sensor"
    self.homeassistant_unique_id = "system"

  @property
  def discovery_config(self) -> object:
    return [
      # Cluster #0
      {
      "name": "somni-ODROID System CPU Cluster #0 Current Frequency",
      "unique_id": self.homeassistant_real_unique_id + "_cpufreq0_current",
      "state_topic": self.get_real_topic("system/state"),
      "device_class": "frequency",
      "unit_of_measurement": "MHz",
      "entity_category": "diagnostic",
      "state_class": "measurement",
      "expire_after": 20,
      "value_template": "{{ value_json.cpufreq0.current }}",
    }, {
      "name": "somni-ODROID System CPU Cluster #0 Max Frequency",
      "unique_id": self.homeassistant_real_unique_id + "_cpufreq0_max",
      "state_topic": self.get_real_topic("system/state"),
      "device_class": "frequency",
      "unit_of_measurement": "MHz",
      "entity_category": "diagnostic",
      "state_class": "measurement",
      "expire_after": 20,
      "value_template": "{{ value_json.cpufreq0.max }}",
    }, {
      "name": "somni-ODROID System CPU Cluster #0 Min Frequency",
      "unique_id": self.homeassistant_real_unique_id + "_cpufreq0_min",
      "state_topic": self.get_real_topic("system/state"),
      "device_class": "frequency",
      "unit_of_measurement": "MHz",
      "entity_category": "diagnostic",
      "state_class": "measurement",
      "expire_after": 20,
      "value_template": "{{ value_json.cpufreq0.min }}",
    },
    # Cluster #1
    {
      "name": "somni-ODROID System CPU Cluster #1 Current Frequency",
      "unique_id": self.homeassistant_real_unique_id + "_cpufreq1_current",
      "state_topic": self.get_real_topic("system/state"),
      "device_class": "frequency",
      "unit_of_measurement": "MHz",
      "entity_category": "diagnostic",
      "state_class": "measurement",
      "expire_after": 20,
      "value_template": "{{ value_json.cpufreq1.current }}",
    }, {
      "name": "somni-ODROID System CPU Cluster #1 Max Frequency",
      "unique_id": self.homeassistant_real_unique_id + "_cpufreq1_max",
      "state_topic": self.get_real_topic("system/state"),
      "device_class": "frequency",
      "unit_of_measurement": "MHz",
      "entity_category": "diagnostic",
      "state_class": "measurement",
      "expire_after": 20,
      "value_template": "{{ value_json.cpufreq1.max }}",
    }, {
      "name": "somni-ODROID System CPU Cluster #1 Min Frequency",
      "unique_id": self.homeassistant_real_unique_id + "_cpufreq1_min",
      "state_topic": self.get_real_topic("system/state"),
      "device_class": "frequency",
      "unit_of_measurement": "MHz",
      "entity_category": "diagnostic",
      "state_class": "measurement",
      "expire_after": 20,
      "value_template": "{{ value_json.cpufreq1.min }}",
    }]
  
  def send_discovery(self) -> None:
    self.client.publish(
      self.homeassistant_discovery_topic.replace(self.homeassistant_unique_id, "system_cpufreq0_current"),
      JSONEncoder().encode(self.discovery_config[0]),
      retain=True)
    self.client.publish(
      self.homeassistant_discovery_topic.replace(self.homeassistant_unique_id, "system_cpufreq0_max"),
      JSONEncoder().encode(self.discovery_config[1]),
      retain=True)
    self.client.publish(
      self.homeassistant_discovery_topic.replace(self.homeassistant_unique_id, "system_cpufreq0_min"),
      JSONEncoder().encode(self.discovery_config[2]),
      retain=True)
    self.client.publish(
      self.homeassistant_discovery_topic.replace(self.homeassistant_unique_id, "system_cpufreq1_current"),
      JSONEncoder().encode(self.discovery_config[3]),
      retain=True)
    self.client.publish(
      self.homeassistant_discovery_topic.replace(self.homeassistant_unique_id, "system_cpufreq1_max"),
      JSONEncoder().encode(self.discovery_config[4]),
      retain=True)
    self.client.publish(
      self.homeassistant_discovery_topic.replace(self.homeassistant_unique_id, "system_cpufreq1_min"),
      JSONEncoder().encode(self.discovery_config[5]),
      retain=True)

  def run(self) -> None:
    super().run()

    while True:
      if hasattr(self, "client") and self.client.is_connected():
        output = { "cpufreq0": {}, "cpufreq1": {} }
  
        ## CPU C#0 current frequency ##
        cpufreq0CurrentCall = subprocess.run(["cat", self.cpufreq0_current_sysfile], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

        if cpufreq0CurrentCall.returncode != 0 or not cpufreq0CurrentCall.stdout:
          print("Failed to get current CPU C#0 frequency!")
        else:
          output["cpufreq0"]["current"] = int(cpufreq0CurrentCall.stdout.decode("utf-8").strip()) // 1000
        
        ## CPU C#0 max frequency ##
        cpufreq0MaxCall = subprocess.run(["cat", self.cpufreq0_max_sysfile], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

        if cpufreq0MaxCall.returncode != 0 or not cpufreq0MaxCall.stdout:
          print("Failed to get max CPU C#0 frequency!")
        else:
          output["cpufreq0"]["max"] = int(cpufreq0MaxCall.stdout.decode("utf-8").strip()) // 1000
          
        ## CPU C#0 min frequency ##
        cpufreq0MinCall = subprocess.run(["cat", self.cpufreq0_min_sysfile], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

        if cpufreq0MinCall.returncode != 0 or not cpufreq0MinCall.stdout:
          print("Failed to get min CPU C#0 frequency!")
        else:
          output["cpufreq0"]["min"] = int(cpufreq0MinCall.stdout.decode("utf-8").strip()) // 1000

          
        ## CPU C#1 current frequency ##
        cpufreq1CurrentCall = subprocess.run(["cat", self.cpufreq1_current_sysfile], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

        if cpufreq1CurrentCall.returncode != 0 or not cpufreq1CurrentCall.stdout:
          print("Failed to get current CPU C#1 frequency!")
        else:
          output["cpufreq1"]["current"] = int(cpufreq1CurrentCall.stdout.decode("utf-8").strip()) // 1000
        
        ## CPU C#1 max frequency ##
        cpufreq1MaxCall = subprocess.run(["cat", self.cpufreq1_max_sysfile], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

        if cpufreq1MaxCall.returncode != 0 or not cpufreq1MaxCall.stdout:
          print("Failed to get max CPU C#1 frequency!")
        else:
          output["cpufreq1"]["max"] = int(cpufreq1MaxCall.stdout.decode("utf-8").strip()) // 1000
          
        ## CPU C#1 min frequency ##
        cpufreq1MinCall = subprocess.run(["cat", self.cpufreq1_min_sysfile], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

        if cpufreq1MinCall.returncode != 0 or not cpufreq1MinCall.stdout:
          print("Failed to get min CPU C#1 frequency!")
        else:
          output["cpufreq1"]["min"] = int(cpufreq1MinCall.stdout.decode("utf-8").strip()) // 1000

        ## MQTT Publish ##
        self.client.publish(self.get_real_topic("system/state"), JSONEncoder().encode(output))
      
      sleep(10)
