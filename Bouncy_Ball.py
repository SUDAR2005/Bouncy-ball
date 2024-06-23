#Importing  the required Python library
import pygame as pg
import random as rn
from sys import exit
import datetime as d
#Initializing the PyGame module
pg.init()
pg.font.init()
#Setting up the display size variables
Width =900
Height =600
#Setting up the display screen
scr=pg.display.set_mode((Width, Height))
#Setting up the game's name in caption
pg.display.set_caption("Bouncy Ball")
#Setting up the background and converting into quick accessible
bg_image=pg.image.load("ball-background.avif")
#Changing the dimensions of bg and making it suitable for main display
bg= pg .transform.scale(bg_image, (2 * Width, Height))
#variable for continuous running of background
i= 0
#variables to  set the position of circle
x= 100
y= 500
#variables to set the radius and
radius = 30
#Variable to set the velocity of ball
vel_x=10
vel_y=10
#Make event loop to run and jump to occur
jump=False
run=True
point=0     #initial score
#Sets up the position of block
x1=100
y1=100
time =pg.time.Clock()   #To control frame rate
Timer=0         #Time determining factor
s=set()         #Scores are saved here
#Font style deciding
font = pg.font.Font(None, 40)
#Game loop
while run:
    #Use to set block at random positions
    rand_x = rn.randint(0,1000)
    rand_y = 100
    #Transfers images as bits according to the given condition
    scr.blit(bg, (i,0))                             #Second argument gives the stating position
    scr.blit(bg, (Width + 1, 0))
    f_surface = font.render("You score: " + str(point), True, "Red")
    scr.blit(f_surface,(50,50))
    #Checks that whether the end of background is reached
    if i == -Width:
        scr.blit(bg, (Width + i, 0))
        i=0
    #Helps to move the background towards right
    i-=1
    #Draws a rectangle and circle
    ball=pg.draw.circle(scr, (255, 0, 0), (x, y), radius)
     #To insert obstacle
    if Timer%100<50:
        block=pg.draw.rect(scr, (255, 0, 0), (x1, y1, 150, 50))
        if pg.Rect.colliderect(ball, block):
            font = open("Bouncy_ball_score.txt", "r+")
            font.write(f"{d.datetime.now()}\t{point}\n")
            font.close()
            pg.quit()
            exit()
    #To intoduce point scorer
    elif Timer%100>50:
        block=pg.draw.rect(scr, (0, 0, 225), pg.Rect(x1, y1, 150, 50))
    #Changes the position of block in each frame
    if i%10==0:
        x1=rand_x
        y1=rand_y
    #Stating of event loop
    for event in pg.event.get():
        if event.type==pg.QUIT:#To set quit option
            font=open("Bouncy_ball_score.txt", "r+")
            font.write(f"{d.datetime.now()}\t{point}\n")
            font.close()
            pg.quit()
            exit()
    if pg.Rect.colliderect(ball, block):            #Checks the collision
        point+=1
    user_input=pg.key.get_pressed()         #Checks the pressed key
    if user_input[pg.K_RIGHT] and x<1000:   #boundary condition 1
        x+= vel_x
    if user_input[pg.K_LEFT] and x>0:       #Boundary condition 2
        x-=vel_x
    if jump is False and user_input[pg.K_SPACE]:
        jump =True
    if jump is True or y>Height:               #Boundary condition 3
        y-=vel_y*7                             #Changing the position along y
        vel_y-=1                               #action of gravity
        if vel_y < -10:                        #Condition for velocity
            jump = False
            vel_y = 10
    Timer+=1                                   #Time determiner
    time.tick(60)                              #Sets the frame rate
    s.add(point)                               #Adds point to set
    if Timer == 30000 :                               #Condition for Exit with storing the data
        f = open("Bouncy_ball_score.txt", "r+")
        f.write(f"{d.datetime.now()}\t{point}\n")
        pg.quit()
        exit()
    pg.display.update()                         #Updates the changes to display
pg.quit()