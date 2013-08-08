import SimpleCV
import time
import settings
from os.path import join

cam = SimpleCV.Camera()
disp = SimpleCV.Display(settings.DISPLAY_SIZE)

imset = SimpleCV.ImageSet()

TIME_LIMIT = 4.0
STEP = 0.2
TOTAL_STEPS = TIME_LIMIT / STEP

i = 0
while disp.isNotDone():
    time.sleep(STEP)

    img = cam.getImage()
    imset.append(img)
    img.save(disp)

    if disp.lastLeftButton:
        break

    i += 1
    if i >= TOTAL_STEPS:
        break

imset.save(join('..', 'media', 'animated.gif'))
