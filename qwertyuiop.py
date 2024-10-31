import pgzrun
import random

TITLE="Attack on alien"
HIEGHT=500
WIDTH=500
alien_killed=0
alien_missed=0
score=(alien_killed-alien_missed)
alien=Actor('alien')
alien.x=random.randint(75,415)
alien.y=75
spike=Actor('spike')
spike.y=400
spike.x=250

def alien_placment():
    


def draw():
    spike.draw()
    alien.draw()













pgzrun.go()