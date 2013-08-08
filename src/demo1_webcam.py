import SimpleCV
import settings

cam = SimpleCV.Camera()
disp = SimpleCV.Display(settings.DISPLAY_SIZE)

while disp.isNotDone():
    img = cam.getImage()
    img.save(disp)

    if disp.lastLeftButton:
        break
