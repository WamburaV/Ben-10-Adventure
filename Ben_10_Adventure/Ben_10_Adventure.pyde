add_library('minim')
import os
path = os.getcwd()
player = Minim(this)

class Platform:
    def __init__ (self, x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.img = loadImage(path+ "/images/platform.png")
    
