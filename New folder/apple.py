import pgzrun

WIDTH = 1000
HEIGHT = 700

apple = Actor("apple1",(500,350))

def update():
    pass

def draw():
    screen.fill("white")
    apple.draw()

def on_mouse_down(pos):
    if apple.collidepoint(pos) and apple.image == "apple1":
        apple.image = "apple2"
    elif apple.collidepoint(pos) and apple.image == "apple2":
        apple.image = "apple3"
    elif apple.collidepoint(pos) and apple.image == "apple3":
        apple.image = "apple1"

pgzrun.go()