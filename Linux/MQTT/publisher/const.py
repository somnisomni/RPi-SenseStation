class Constants:
  @property
  def sensestation_root_topic(self) -> str:
    return "sensestation/"
  
  @property
  def homeassistant_discovery_root_topic(self) -> str:
    return "homeassistant/"