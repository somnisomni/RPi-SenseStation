import atexit
from threading import Thread
from time import sleep
from sense_hat import SenseHat
sense = SenseHat()

# === Constants ===
NOLIT = [0, 0, 0]
POWER_BLINK_COLOR = [128, 0, 0]

# === Loop Threads ===
def powerBlink():
  while True:
    sense.set_pixel(7, 7, POWER_BLINK_COLOR)
    sleep(1)
    sense.set_pixel(7, 7, NOLIT)
    sleep(4)
# More actions can be added using threads...

# === Main Procedure ===
if __name__ == "__main__":
  sense.low_light = True
  sense.clear()
  atexit.register(lambda: sense.clear())

  powerBlinkThread = Thread(target=powerBlink)
  powerBlinkThread.start()
