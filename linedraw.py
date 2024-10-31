import pgzrun
import random
from time import time
HEIGHT=500
WIDTH=500
TITLE="line draw"


satalite=Actor("satalite")
satalite.x=250
satalite.y=250
total_time=0
end_time=0
satalites=[]
lines=[]
next_satalite=0
number_satalites=8
start_time=0

def create_satalite():
    global start_time
    for count in range(0,number_satalites):
        satalite=Actor('satalite')
        satalite.pos=random.randint(40,WIDTH-40),random.randint(40,HEIGHT-40)
        satalites.append(satalite)
    start_time=time()

def draw():
    global total_time
    global line
    number=1
    screen.clear()
    screen.fill('indigo')
    for satalite in satalites:
        satalite.draw()
        screen.draw.text(str(number),color="white",topleft=(satalite.pos[0],satalite.pos[1]+20))
        number=number+1
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))
    if next_satalite<number_satalites:
        total_time=time()-start_time
        screen.draw.text(str(round(total_time)),(10,10),fontsize=30)
    else:
        screen.draw.text(str(round(total_time,1),),(10,10),fontsize=30)
def update():
    pass

def on_mouse_down(pos):
    global next_satalite,lines
    satalite.collidepoint(pos)
    if next_satalite<number_satalites:
        if satalites[next_satalite].collidepoint(pos):
            if next_satalite:
                lines.append(satalites[next_satalite-1].pos, satalites[next_satalite].pos)
            next_satalite=next_satalite+1
        else:
            lines=[]
            next_satalite=0
    

    create_satalite()



'''def draw():
    for i in range(11):
        draw_satalite(i+1)   
    
def draw_satalite(number):

    sat=satalite
    satalites.append(str(sat)+str(number))
    sat.x=random.randint(100,400)
    sat.y=random.randint(100,400)
    sat.draw()
    screen.draw.text(str(number),color="white",topleft=sat.bottomright)'''
    

        







pgzrun.go()