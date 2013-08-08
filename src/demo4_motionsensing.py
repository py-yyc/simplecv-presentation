import SimpleCV
import settings

cam = SimpleCV.Camera()
disp = SimpleCV.Display(settings.DISPLAY_SIZE)

last = cam.getImage().toGray()

w, h = last.size()
num_pixels = w * h

while disp.isNotDone():
    img = cam.getImage().toGray()
    diff = (img - last).binarize(10).invert()
    motion = diff.getNumpy().sum() / (255 * float(num_pixels)) * 100

    diff.drawText(str(int(motion)), color=SimpleCV.Color.RED, fontsize=settings.DEFAULT_FONT_SIZE)
    diff.save(disp)
    last = img

    if disp.lastLeftButton:
        break