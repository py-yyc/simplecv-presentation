import SimpleCV
import settings
from os.path import join

cam = SimpleCV.Camera()
disp = SimpleCV.Display(settings.DISPLAY_SIZE)

stache = SimpleCV.Image(join('..', 'media', 'stash.png'))
STACHE_SCALE = 0.8

while disp.isNotDone():
    img = cam.getImage()

    mouthes = img.findHaarFeatures('mouth.xml')
    if mouthes is not None:
        mouth = mouthes[0]
        resized_stache = stache.resize(int(mouth.width() * STACHE_SCALE))
        stache_x = mouth.points[0][0] + (mouth.width()/2) - (resized_stache.width/2)
        stache_y = mouth.points[0][1]
        img = img.blit(resized_stache, pos=(stache_x, stache_y), mask=resized_stache.invert())
    img.save(disp)

    if disp.lastLeftButton:
        break
