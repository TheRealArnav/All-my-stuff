import pgzrun

HEIGHT=500
WIDTH=1250
sky=Actor("sky1")
sky.x=250
sky.y=250
mario=Actor('mario')
skys=[]


def draw():
    sky.draw()

    mario.draw()

def makebg():
    global skys
    
    for i in range (skys):
        sky.x=sky.x+400
        sky.y=sky.y

    









pgzrun.go()