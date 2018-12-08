add_library('minim')
import os
path = os.getcwd()
player = Minim(this)
   
class Characters:
    def __init__(self,x,y,r,g,img,w,h,f):
        self.x=x
        self.y=y
        self.r=r
        self.g=g
        self.w=w
        self.h=h
        self.f=0
        self.F=F
        self.vx=0
        self.vy=0
        self.dir=1
        self.img = loadImage(path+'/image/'+img)
        
    def gravity(self):
        if self.y+self.r >= self.g:
            self.vy = 0
        else:
            self.vy += 0.2
            if self.y + self.r + self.vy > self.g:
                self.vy = self.g - (self.y+self.r)
                
        for l in platforms[::-1]:
            if self.y+self.r <= l.y and self.x+self.r >= l.x and self.x-self.r <= l.x+l.w:
                self.g = l.y
                break
            else:
                self.g = g.g
    
    def update(self):
        self.gravity()
        
        self.x += self.vx
        self.y += self.vy
        
    def display(self):
        self.update()
        
        if self.vx != 0 and self.vy == 0:
            self.f = (self.f+0.2)%self.F
            
        if self.dir > 0:
            image(self.img,self.x-self.w//2-g.x,self.y-self.h//2,self.w,self.h,int(self.f)*self.w,0,int(self.f+1)*self.w,self.h)
        elif self.dir < 0:
            image(self.img,self.x-self.w//2-g.x,self.y-self.h//2,self.w,self.h,int(self.f+1)*self.w,0,int(self.f)*self.w,self.h)
        
        
class Platform:
    def __init__ (self, x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.img = loadImage(path+ "/images/platform.png")                
    
        
