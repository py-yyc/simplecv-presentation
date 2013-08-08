import SimpleCV
import settings

cam = SimpleCV.Camera()
disp = SimpleCV.Display(settings.DISPLAY_SIZE)

while disp.isNotDone():
    # use Canny edge detection algorithm
    img = cam.getImage().edges()
    img.save(disp)

    if disp.lastLeftButton:
        break