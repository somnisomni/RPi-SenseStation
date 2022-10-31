from random import randint
from time import sleep
from sense_hat import SenseHat

# === Constants ===
sense = SenseHat()

NOLIT = [0, 0, 0]

FADE_IN_FRAME_COUNT = 10
FADE_OUT_FRAME_COUNT = 10

DOT_PAINT_FRAME_INTERVAL = 5
FRAME_INTERVAL_MS = 30
MAX_FRAME = 330

class Dot:
  def __init__(self, x: int, y: int, maxR: int, maxG: int, maxB: int, startFrame: int):
    self.x = x
    self.y = y
    self.maxR = maxR
    self.currentR = 0
    self.maxG = maxG
    self.currentG = 0
    self.maxB = maxB
    self.currentB = 0
    self.startFrame = startFrame
  
  def setSenseHatPixel(self, currentFrame: int) -> bool:
    if MAX_FRAME - currentFrame <= FADE_OUT_FRAME_COUNT:
      self.currentR = max(0, self.currentR - (self.maxR // FADE_OUT_FRAME_COUNT))
      self.currentG = max(0, self.currentG - (self.maxG // FADE_OUT_FRAME_COUNT))
      self.currentB = max(0, self.currentB - (self.maxB // FADE_OUT_FRAME_COUNT))
    else:
      delta = currentFrame - self.startFrame
    
      if delta > (FADE_IN_FRAME_COUNT + FADE_OUT_FRAME_COUNT):
        sense.set_pixel(self.x, self.y, NOLIT)
        return False
      else:
        if delta <= FADE_IN_FRAME_COUNT:
          self.currentR = (self.maxR // FADE_IN_FRAME_COUNT) * delta
          self.currentG = (self.maxG // FADE_IN_FRAME_COUNT) * delta
          self.currentB = (self.maxB // FADE_IN_FRAME_COUNT) * delta
        elif delta <= (FADE_IN_FRAME_COUNT + FADE_OUT_FRAME_COUNT):
          self.currentR = (self.maxR // FADE_OUT_FRAME_COUNT) * ((FADE_IN_FRAME_COUNT + FADE_OUT_FRAME_COUNT) - delta)
          self.currentG = (self.maxG // FADE_OUT_FRAME_COUNT) * ((FADE_IN_FRAME_COUNT + FADE_OUT_FRAME_COUNT) - delta)
          self.currentB = (self.maxB // FADE_OUT_FRAME_COUNT) * ((FADE_IN_FRAME_COUNT + FADE_OUT_FRAME_COUNT) - delta)
      
    sense.set_pixel(self.x, self.y, [self.currentR, self.currentG, self.currentB])
    return True

# === Main Procedure ===
currentFrame = 0
dotCoordMap = [[0 for _ in range(8)] for _ in range(8)]
dots = []

def pickEmptyCoord() -> tuple[int, int]:
  x, y = 0, 0

  while True:
    x, y = randint(0, 7), randint(0, 7)

    if dotCoordMap[y][x] == 0: break

  dotCoordMap[y][x] = 1
  return (x, y)

if __name__ == "__main__":
  sense.clear()

  while currentFrame <= MAX_FRAME:
    if currentFrame % DOT_PAINT_FRAME_INTERVAL == 0:
      x, y = pickEmptyCoord()
      dots.append(Dot(x, y, randint(0, 255), randint(0, 255), randint(0, 255), currentFrame))

    for dot in dots:
      if not dot.setSenseHatPixel(currentFrame):
        dots.remove(dot)
        dotCoordMap[dot.y][dot.x] = 0

    currentFrame += 1
    sleep(FRAME_INTERVAL_MS / 1000)
  
  sense.clear()
