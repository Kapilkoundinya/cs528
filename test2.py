from omega import *
from cyclops import *

b = BoxShape.create(1, 1, 1)

b.setEffect('colored -d #ff8855 -g 1 -s 5')

l = Light.create()
l.setAmbient(Color(0.2, 0.2, 0.4, 1))
l.setPosition(1, 3, 0)

c = getDefaultCamera()
c.setPosition(0, -2, 2)
c.addChild(l)


