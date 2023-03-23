import RPi.GPIO as GPIO

def setup() -> None:
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)

def cleanup() -> None:
  print("GPIO cleanup")
  GPIO.cleanup()
