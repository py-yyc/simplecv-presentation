import SimpleCV
import settings

cam = SimpleCV.Camera()
disp = SimpleCV.Display(settings.DISPLAY_SIZE)

while disp.isNotDone():
    img = cam.getImage().scale(0.3)  # scaling the image down to help process the image faster
    faces = img.findHaarFeatures('face.xml') or []
    for face in faces:
        face.draw(SimpleCV.Color.GREEN)
    img.save(disp)

    if disp.lastLeftButton:
        break