import pgzrun
import random
import os

os.environ["SDL_VIDEO_CENTERED"] = "1"

WIDTH = 1000
HEIGHT = 700

carList = ["car1","car2","car3"]

car = Actor(random.choice(carList),(500,350))
paresh = False

def update():
    global paresh

    if paresh == True:
        if car.y != 100:
            car.y -= 10
        if car.y == 100:
            paresh = False
        
    if paresh == False:
        if car.y != 350:
            car.y += 10

def draw():
    sounds.x.play()
    screen.fill("white")
    car.draw()

def on_key_down(key):
    global paresh

    if key == keys.UP and car.y == 350:
        paresh = True


pgzrun.go()