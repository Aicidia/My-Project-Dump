### This is a 3D platformer which randomly generates the number of platforms that you put in. ###

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random as rng

app=Ursina()

a=0

def plat(d,o):
    global a
    a+=d
    Entity(model='cube',color=color.cyan,position=(o,-50,a),collider='box',scale=(5,100,10),texture='vertical_gradient')

def randplat():
    plat(rng.randint(17,20),rng.randint(-5,5))

plat(0,0)

Entity(model='cube',color=color.black,position=(0,-50,0),collider='box',scale=(10000,1,10000),texture='circle')

numplat=input('# of platforms\n')

for i in range(1,int(numplat)):
    randplat()

player=FirstPersonController(speed=20)

app.run()
