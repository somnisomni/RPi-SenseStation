from random import randint
from time import sleep
from sense_hat import SenseHat
sense = SenseHat()

# === Constants ===
NOLIT = [0, 0, 0]
LIT = [randint(64, 255), randint(64, 255), randint(64, 255)]

ANIM_ORDER = [
   0,  1,  2,  3,  4,  5,  6,  7,
  27, 28, 29, 30, 31, 32, 33,  8,
  26, 47, 48, 49, 50, 51, 34,  9,
  25, 46, 59, 60, 61, 52, 35, 10,
  24, 45, 58, 63, 62, 53, 36, 11,
  23, 44, 57, 56, 55, 54, 37, 12,
  22, 43, 42, 41, 40, 39, 38, 13,
  21, 20, 19, 18, 17, 16, 15, 14,
]

FRAME_INTERVAL_MS = 100
TAIL_COUNT = 8
MAX_FRAME = 8 * 8 + TAIL_COUNT
# ===

currentFrame = 0

if __name__ == "__main__":
  sense.clear()

  while currentFrame < MAX_FRAME:
    frame = [NOLIT] * (8 * 8)

    for idx in range(len(ANIM_ORDER)):
      if ANIM_ORDER[idx] == currentFrame:
        frame[idx] = LIT
      elif ANIM_ORDER[idx] > currentFrame - TAIL_COUNT and \
        ANIM_ORDER[idx] < currentFrame:
        distance = abs(currentFrame - ANIM_ORDER[idx])
        newLit = [ \
          LIT[0] // TAIL_COUNT * (TAIL_COUNT - distance), \
          LIT[1] // TAIL_COUNT * (TAIL_COUNT - distance), \
          LIT[2] // TAIL_COUNT * (TAIL_COUNT - distance), \
        ]
        frame[idx] = newLit

    sense.set_pixels(frame)

    currentFrame += 1
    sleep(FRAME_INTERVAL_MS / 1000)