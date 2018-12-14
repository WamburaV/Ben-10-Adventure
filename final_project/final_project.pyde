import sys

#variable declarations

img = 0

xBall = 0

yBall = 0

diameter = 0

radius = 0

paddleX = 0

paddleY = 0

paddleWidth = 0

paddleHeight = 0

score = 0

maxScore = 0

xSpeed = 0

ySpeed = 0

scoreX = 0

scoreY = 0

tSize = 0

textX = 0

textY = 0

tSize1 = 0


def setup ():
    
    global xBall
    
    global yBall
    
    global diameter
    
    global radius
    
    global paddleX
    
    global paddleY
    
    global paddleWidth
    
    global paddleHeight
    
    global score
    
    global maxScore
    
    global xSpeed
    
    global ySpeed
    
    global scoreX
    
    global scoreY
    
    global tSize
    
    global textX
    
    global textY
    
    global tSize1
    
    global img

    size(700, 394); #screen size
    
    img = loadImage("pingpong.jpg") #load image
    
    background(img) #set background
    
    xBall = width/2 #set horizontal position of ball to half of the screen's width 
    
    yBall = height/2 #set vertical position of the ball to half of the screen's height 
    
    diameter = (width + height)/60 #diameter of circle set to be a sixtieth of the width + height, this could be any value really
    
    radius = diameter / 2 #radius is the diameter over 2
    
    #x and y coordinates of the paddles are the coordinates at the top left corners of their rectangles
    
    paddleX = 39*width/40 #x coordinate of the right paddle at 39/40 of the width of the screen. This is because the width of the paddle is 1/40 of the width
    
    paddleY = height/2 #y coordinate of the right paddle middle of the screen. 
    
    paddleWidth = width/40 #width of paddle set to one fortieth of the width of the screen
    
    paddleHeight = 2*height/10 #height of the paddle set to two tenths of the height of the screen  
        
    score = 5 #score of the right player
    
    maxScore = 10 #max score of the program
    
    xSpeed = 5 #horizontal speed of the ball
    
    ySpeed = 5 #vertical speed of the ball
    
    scoreX = width/4 #x coordinate of the player's score is one half of the width of the screen
    
    scoreY = 3*height/4 #y coordinate of the player's score is one half of the height of the screen 
    
    tSize = (width+height)/10 #size of the text is the summation of the width and height divided by fourty, I could have just set it to any number
    
    textX = 70*width/100 #x coordinate of text at the bottom of the screen

    textY = 99*height/100 #y coordinate of text at the bottom of the screen
    
    tSize1 = (width+height)/150 #size of the text is the summation of the width and height divided by 150, I could have just set it 
    
def draw ():
    
    global xBall
    
    global yBall
        
    global paddleY
    
    global score
        
    global xSpeed
    
    global ySpeed
    
    background(img) #set background
    
    textSize (tSize) #set size of the player's scores to be the value in the tSize variable
    
    fill (250, 0, 10) 
    
    text (score, scoreX, scoreY) #draw player'sscore 
    
    textSize(tSize1) #set size of text
        
    fill (255, 255, 255) #fill all shapes to light pink until fill is run with another color 
    
    ellipse (xBall, yBall, diameter, diameter) #draw ball unto the screen
    
    fill (0) #fill all shapes to purple until fill is run with another color 
    
    stroke (214, 169, 187) #use a blue outline for all shapes until stroke is run again with another color
    
    strokeWeight(2)
    
    rect (paddleX, paddleY, paddleWidth, paddleHeight) #draw left paddle
    
    #moveball right and downwards 
    xBall = xBall + xSpeed #increase the x position of the ball by x speed
    
    yBall = yBall + ySpeed #increase the y position of the ball by y speed
    
    #check if ball completely exits right side of the screen 
    if(score < 0):
        sys.exit()

    if (xBall - radius > width):
        score = score - 1 #increment the right player's score by one
        xBall = width/2 #set the horizontal position of the ball to half of the width
    
    elif (xBall - radius < 0):
        xSpeed = xSpeed * -1
    
    #check if ball hits top and bottom sides of the screen 
    
    if (yBall - radius < 0 or yBall + radius > height):
        ySpeed = ySpeed * -1 #then reverse the polarity of the vertical speed so the ball moves in the opposite vertical direction
    
    #check for ball and right paddle ersection 
    if ((xBall+radius >= paddleX) #if the right edge of the ball and the left side of the right paddle coincide or ersect
    
    and (xSpeed > 0) #AND if the ball's xSpeed is positive (if it was moving towards the right)
    
    and (yBall + radius > paddleY and yBall + radius < paddleY + paddleHeight)): 
        xSpeed *= -1 #reverse the ball's horizontal speed
        
        xBall = paddleX - radius #set the ball's horizontal position to the exact po of ersection between the ball's right edge and the left edge of the right paddle
        
    paddleY = mouseY #set the y coordinate of the paddle to mouseY
        
    if (mouseY+paddleHeight > height): #if the paddle is gone off the bottom part of the screen 
        paddleY = height-paddleHeight #set it back to position: height of the screen minus height of the paddle so that the paddle fits back nicely in the right bottom corner
        
