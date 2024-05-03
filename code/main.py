from pygame import *
init()
screen = display.set_mode((600, 800))
def game():

    while True:
        for i in event.get():
            if i.type == QUIT:
                print ('1')
                return False
game()