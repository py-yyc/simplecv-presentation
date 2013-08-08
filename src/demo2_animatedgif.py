import SimpleCV
import time
import settings
from os.path import join

cam = SimpleCV.Camera()
disp = SimpleCV.Display(settings.DISPLAY_SIZE)

imset = SimpleCV.ImageSet()

i = 0
while disp.isNotDone():
    time.sleep(0.2)

    img = cam.getImage()
    imset.append(img)
    img.save(disp)

    if disp.lastLeftButton:
        break

    i += 1
    if i >= 20:
        break

imset.save(join('..', 'media', 'animated.gif'))
