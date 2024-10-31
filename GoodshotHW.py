import pgzrun
import random

HEIGHT=500
WIDTH=500

TITLE="Good shot"
alien=Actor('redmonster')
spike=Actor('bugspray')
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