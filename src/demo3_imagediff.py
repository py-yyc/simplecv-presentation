import SimpleCV
import settings

cam = SimpleCV.Camera()
disp = SimpleCV.Display(settings.DISPLAY_SIZE)

prev = cam.getImage().toGray()
while disp.isNotDone():
    img = cam.getImage().toGray()
    diff = (img - prev)
    diff.save(disp)

    prev = img

    if disp.lastLeftButton:
        break