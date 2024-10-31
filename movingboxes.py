import pgzrun
TITLE="moving boxes"
WIDTH = 500
HEIGHT = 500

box1=Rect((20,20),(50,50))
box2=Rect((20,20),(50,50))
box3=Rect((20,20),(50,50))
def draw():
    screen.clear()
    screen.draw.filled_rect(box1,"blue")
    screen.draw.filled_rect(box2,"green")
    screen.draw.filled_rect(box3, "red")

def update():
    box1.x=(box1.x+2)
    box2.y=(box2.y+2)

    if box1.x > 500:
        box1.x=0
    if box2.y > 500:
        box2.y=0

    if keyboard.left:
        box3.x=box3.x-2
    elif keyboard.right:
        box3.x=box3.x+2
    elif keyboard.down:
        box3.y=box3.y+2
    elif keyboard.up:
        box3.y=box3.y-2





pgzrun.go()