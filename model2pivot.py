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
o.setEffect("textured -g 0.2 -s 100")

# pivot the car
pivot = SceneNode.create('pivot')
pivot.addChild(o)
pivot.setPosition(Vector3(0, 0, 4))
bound = -o.getBoundCenter()
o.setPosition(bound.x, 0, bound.z*2+2)


l = Light.create()
l.setAmbient(Color(0.2, 0.2, 0.4, 1))
l.setPosition(3, 3, 0)

# Shadow
sm = ShadowMap()
sm.setTextureSize(2048,2048)
sm.setSoft(True)
l.setShadow(sm)

c = getDefaultCamera()
c.setPosition(0, 0, 0)
c.addChild(l)

# Draw a ground plane
plane = PlaneShape.create(20, 20)
plane.pitch(radians(-90))
plane.setEffect("textured -d checker.jpg")

yawSpeed = 1
def onUpdate(frame, time, dt):
    pivot.yaw(yawSpeed * dt)
    
setUpdateFunction(onUpdate)