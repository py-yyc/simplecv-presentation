import SimpleCV
import settings
from os.path import join

cam = SimpleCV.Camera()
disp = SimpleCV.Display(settings.DISPLAY_SIZE)

stache = SimpleCV.Image(join('..', 'media', 'stash.png'))
STACHE_SCALE = 1.2
NOSE_HEIGHT_FACTOR = 2.0/3

face_cascade = SimpleCV.HaarCascade('face.xml')
nose_cascade = SimpleCV.HaarCascade('nose.xml')

while disp.isNotDone():
    img = cam.getImage().scale(0.3)

    faces = img.findHaarFeatures('face.xml')
    if faces is not None:
        face = faces.sortArea()[-1]
        cropped_face = face.crop()
        noses = cropped_face.findHaarFeatures('nose.xml')
        if noses is not None:
            nose = noses.sortArea()[-1]
            resized_stache = stache.resize(int(nose.width() * STACHE_SCALE))
            face_x, face_y = face.x - (face.width()/2), face.y - (face.height()/2)
            nose_x, nose_y = nose.x - (nose.width()/2), nose.y - (nose.width()/2)
            stache_x = face_x + nose_x + (nose.width()/2) - (resized_stache.width/2)
            stache_y = face_y + nose_y + int(nose.height()*NOSE_HEIGHT_FACTOR)
            img = img.blit(resized_stache, pos=(stache_x, stache_y), mask=resized_stache.invert())
    img.save(disp)

    if disp.lastLeftButton:
        break
