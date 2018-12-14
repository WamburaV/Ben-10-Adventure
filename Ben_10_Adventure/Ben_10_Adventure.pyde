add_library('minim')
import os
path = os.getcwd()
player = Minim(this)

class Creature:
    def __init__(self,x,y,r,g,img,w,h,F):
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
        self.img = loadImage(path+"/images/"+img)
        
    def gravity(self):
        if self.y+self.r >= self.g:
            self.vy = 0
        else:
            self.vy += 0.3
            if self.y + self.r + self.vy > self.g:
                self.vy = self.g - (self.y+self.r)
                
        for p in g.platforms[::-1]:
            if self.y+self.r <= p.y and self.x+self.r >= p.x and self.x-self.r <= p.x+p.w:
                self.g = p.y
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
            self.f = (self.f+0.3)%self.F
        
        if self.dir > 0:
            image(self.img,self.x-self.w//2-g.x,self.y-self.h//2,self.w,self.h,int(self.f)*self.w,0,int(self.f+1)*self.w,self.h)
        elif self.dir < 0:
            image(self.img,self.x-self.w//2-g.x,self.y-self.h//2,self.w,self.h,int(self.f+1)*self.w,0,int(self.f)*self.w,self.h)
        
        strokeWeight(5)
        stroke(255)
        noFill()
        ellipse(self.x-g.x,self.y,self.r*2,self.r*2)
        stroke(255,0,0)
        line(self.x-self.r-g.x,self.g,self.x+self.r-g.x,self.g)
                
class Ben10(Creature):
    def __init__(self,x,y,r,g,img,w,h,F):
        Creature.__init__(self,x,y,r,g,img,w,h,F)
        self.keyHandler={LEFT:False, RIGHT:False, UP:False}
       # self.kill = player.loadFile(path+"/sounds/kill.mp3")
        #self.food = player.loadFile(path+"/sounds/coin.mp3")
        #self.jump = player.loadFile(path+"/sounds/jump.mp3")
        self.foodCnt = 0
        
    def update(self):
        
        if g.state != "gameover":
            self.gravity()
        else:
            self.vy += 0.3
            if self.y-self.r > g.h:
                g.__init__(1280,720,585)
        
        if self.keyHandler[LEFT]:
            self.vx = -5
            self.dir = -1
        elif self.keyHandler[RIGHT]:
            self.vx = 5
            self.dir = 1
        else:
            self.vx = 0
        
        if self.keyHandler[UP] and self.y+self.r == self.g:
            self.vy = -10 
            #self.jump.rewind()
            #self.jump.play()   
        
        self.x += self.vx
        self.y += self.vy
        
        if self.x >= g.w // 2:
            g.x += self.vx
        
        if self.x-self.r < 0:
            self.x = self.r
            
        if g.state != "gameover":
            for s in g.food:
                if self.distance(s) <= self.r + s.r:
                    g.food.remove(s)
                    del (s)
                    #self.food.rewind()
                    #self.food.play()
                    self.foodCnt+=1
                    
            for e in g.enemies:
               if self.distance(e) <= self.r + e.r:
             #       # there is collision
                    if self.vy > 0:
                        g.enemies.remove(e)
                        del e
                        self.vy = -8
                        #self.kill.rewind()
                      #           g.goSound.rewind()
                      #  g.goSound.play()
                        self.vy = -10
                        self.g = g.h+100
                    
                    # g.__init__(1280,720,585)
                    
    def distance (self,e):
        return ((self.x-e.x)**2+(self.y-e.y)**2)**0.5
class Gunman(Creature):
    def __init__(self,x,y,r,g,img,w,h,F,x1,x2):
        Creature.__init__(self,x,y,r,g,img,w,h,F)
        self.vx = 2
        self.x1=x1
        self.x2=x2
        
    def update(self):
        self.gravity()
                
        if self.x > self.x2 :
            self.vx = -2
            self.dir = -1
        elif self.x < self.x1:
            self.vx = 2
            self.dir = 1
            
        self.x += self.vx
        self.y += self.vy   
             
class Platform:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.img = loadImage(path+"/images/platform.png")
        
    def display(self):
        image(self.img,self.x-g.x,self.y)
        # rect(self.x,self.y,self.w,self.h)
    
class Food(Creature):
    def __init__(self,x,y,r,g,img,w,h,F,theta,r1):
        Creature.__init__(self,x,y,r,g,img,w,h,F)
        self.theta = theta
        self.r1 = r1
        self.cx = x 
        self.cy = y
        
    def update(self):
        self.f = (self.f+0.2)%self.F
        
        self.theta += 0.01
        self.x = self.cx + self.r1 * cos (self.theta)
        self.y = self.cy + self.r1 * sin (self.theta)
        
class Game:
    def __init__ (self,w,h,g):
        self.w=w
        self.h=h
        self.g=g
        self.x = 0
        self.frames = 0
        self.state = "menu"
        #self.music = player.loadFile(path+"/sounds/music.mp3")
        
        self.pause = False
       # self.pauseSound = player.loadFile(path+"/sounds/pause.mp3")
        #self.goSound = player.loadFile(path+"/sounds/gameover.wav")
        
        self.bgImgs = []
        for i in range(3,0,-1):
            self.bgImgs.append(loadImage(path+"/images/background_0"+str(i)+".jpg"))
        
        self.ben10=Ben10(50,50,35,self.g,"ben_10.png",100,70,11)
        
        self.enemies=[]
        for i in range(5):
            self.enemies.append(Gunman(300+i*100,50,35,self.g,"gunman.png",70,70,5,300,900))
            
        for i in range(5):
            self.enemies.append(Gunman(2000+i*100,50,35,self.g,"gunman.png",70,70,5,1500,3000))
        
        self.platforms=[]
        for i in range(3):
            self.platforms.append(Platform(200+i*250,500-i*150,200,50))
        
        for i in range(3):
            self.platforms.append(Platform(2000+i*250,500-i*150,200,50))
            
        self.food = []
        for i in range(13):
            self.food.append(Food(500,300,20,self.g,"food.png",40,40,6,i/2.1,100))
            self.food.append(Food(1500,300,20,self.g,"food.png",40,40,6,i/2.1,100))
    def display(self):
        self.frames += 1
        
        cnt = 5
        for img in self.bgImgs:
            # image(img,0-self.x,0)
            if cnt == 5:
                x = (self.x//5)%self.w
            elif cnt == 4:
                x = (self.x//3)%self.w
            elif cnt == 3:
                x = (self.x//2)%self.w
            else:
                x = (self.x)%self.w
            
            image (img,0,0,self.w-x,self.h,x,0,self.w,self.h) 
            image (img,self.w-x,0,x,self.h,0,0,x,self.h)
            cnt -=1
            
        fill(255)
        textSize(30)
        text(str(self.frames//60), 50, 50)
        # text(str(self.ben10.foodCnt), 50, 100)
        stroke(255)
        fill(255,0,0)
        rect(50,100,100,20)
        fill(0,255,0)
        rect(50,100,min(100,self.ben10.foodCnt*5),20)
        
        # stroke(255)
        # line(0,self.g,self.w,self.g)
            
        for p in self.platforms:
            p.display()
        
        for e in self.enemies:
            e.display()
            
        for s in self.food:
            s.display()

        self.ben10.display()
        
g = Game(1280,720,585)

def setup():
    size(g.w, g.h)
    background(0)
    
def draw():
    
    if g.state == "menu":
        background(0)
        textSize(34)
        # fill(255)
        # rect(g.w//2.5, g.h//3, 200, 50)
        # fill(255)
        # rect(g.w//2.5, g.h//3+100, 200, 50)
        
        if g.w//2.5 < mouseX < g.w//2.5 + 200 and g.h//3 < mouseY < g.h//3 + 50:
            fill(255,0,0)
        else:
            fill(255)
        text("Play Game", g.w//2.5, g.h//3+40)
        if g.w//2.5 < mouseX < g.w//2.5 + 200 and g.h//3+100 < mouseY < g.h//3 + 150:
            fill(255,0,0)
        else:
            fill(255)
        text("Instructions", g.w//2.5, g.h//3+140)
        
    elif g.state == "play":
        if not g.pause:
            background(0)
            g.display()
            
    elif g.state == "gameover":
        textSize(50)
        fill (255,0,0)
        text("GAME OVER", g.w//2.5, g.h//3+140)
        # g.__init__(1280,720,585)
        g.display()
   
def mouseClicked():
    if g.w//2.5 < mouseX < g.w//2.5 + 200 and g.h//3 < mouseY < g.h//3 + 50:
        g.state="play"
       # g.music.play()
            
def keyPressed():
    if keyCode == LEFT:
        g.ben10.keyHandler[LEFT] = True
    elif keyCode == RIGHT:
        g.ben10.keyHandler[RIGHT] = True
    elif keyCode == UP:
        g.ben10.keyHandler[UP] = True
    elif keyCode == 80:
        if g.pause:
            g.pause = False
        else:
            g.pause = True
       # g.pauseSound.rewind()`
       # g.pauseSound.play()
        
def keyReleased():
    if keyCode == LEFT:
        g.ben10.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        g.ben10.keyHandler[RIGHT] = False
    elif keyCode == UP:
        g.ben10.keyHandler[UP] = False
        
        
        
