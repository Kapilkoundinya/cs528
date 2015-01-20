from omega import *
from cyclops import *
from math import *

sm = getSceneManager()

# Load a static model
model = ModelInfo()
model.name = "thing"
model.path = "car.fbx"
sm.loadModel(model)

# Create a scene object using the loaded model
o = StaticObject.create("thing")
o.setPosition(Vector3(0, 0, 4))
o.setEffect("textured -g 0.2 -s 100")

l = Light.create()
l.setAmbient(Color(0.2, 0.2, 0.4, 1))
l.setPosition(1, 3, 0)

c = getDefaultCamera()
c.setPosition(0, 0, 0)
c.addChild(l)

# Draw a ground plane
plane = PlaneShape.create(20, 20)
plane.pitch(radians(-90))
plane.setEffect("textured -d checker.jpg")