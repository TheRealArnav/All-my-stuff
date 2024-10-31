import pgzrun
import random
import time
delay=1
WIDTH=500
HEIGHT=500
TITLE="Good shot"
alien=Actor('alien')
spike=Actor('spike')
message=""






def draw():
    screen.clear()
    screen.fill("cyan")
    alien.draw()
    screen.draw.text(message,center=(250,10),fontsize=30)
    spike.draw()


def placealien():
    alien.x=random.randint(50,WIDTH-50)
    alien.y=random.randint(50,HEIGHT-50)


def on_mouse_down(pos):
    global message
    
    if alien.collidepoint(pos):
        message="goodshot"
        spike.x=(alien.x)
        spike.y=(alien.y)
        placealien()
    else:
        message="You missed"
    


        

pgzrun.go()