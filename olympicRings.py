'''
Student Name: Amiva Pal
Game title: Olym
Period: 6/7
Features of Game: Uses functional decompostion to draw a scene
'''

import pygame, sys, math                                #pulls in the special code functions for pygame
pygame.init()                                           #initialize game engine

w=800                                                   #Open and set window size
h=int(9/14*w)
xu = w/14
yu = h/9
#must code graphics to auto resize based on window size
size=(w,h)
surface = pygame.display.set_mode(size)

pygame.display.set_caption("Olympic Rings")          #set window title

#declare global variables here

BLACK    = (   0,   0,   0)                             #Color Constants 
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
BROWN    = (  96,  70,  16)
YELLOW   = ( 237, 230,  33)
#other global variables (WARNING: use sparingly):





#clock = pygame.time.Clock()                            # Manage timing for screen updates
                                                        # Uncomment when timing/animation is needed
                                                        

def showMessage(words,size,x,y,color):
    font = pygame.font.SysFont('Calibri',25,True,False)
    text = font.render("2020 Summer Olympics- Tokyo, Japan", True,BLACK)
    text_bounds= text.get_rect()
    text_bounds.center = (w/2,2*yu)
    surface.blit(text,text_bounds)

def drawRing(x,y,color):
    pygame.draw.ellipse(surface,color,(x,y,4.5*xu,4.5*yu),8)
  
    
def drawArc(x,y,color,start,stop):
    pygame.draw.arc(surface,color,(x,y,4.5*xu, 4.5*yu),start,stop,4)
    

#Program helper functions:
def drawAllRings():
    drawRing(0, 2.5*yu, BLUE)
    drawRing(4.6*xu, 2.5*yu, BLACK)
    drawRing(9.25*xu, 2.5*yu, RED)
    drawRing(2.5*xu, 4.5*yu, YELLOW)
    drawRing(7*xu, 4.5*yu, GREEN)
    drawArc(0, 2.5*yu, BLUE,math.pi*11/6,math.pi/6)
    drawArc(4.6*xu, 2.5*yu, BLACK,math.pi*5/4,4.8)
    showMessage("2020 Summer Olympics- Tokyo, Japan", 25,xu/2,yu,BLACK)
  
    


# -------- Main Program Loop -----------
def main():                                             #every program should have a main function
                                                        #other functions go above main
    
    #declare local game variables here 
    
    
    while (True):
        
        for event in pygame.event.get():                #get all events in the last 1/60 sec & process them
            
            if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                pygame.quit();                          #for ending the game & closing window
                sys.exit();
        
            # if your program has a button, mouse, or keyboard interaction, code goes at this indentation level
        
        # ongoing game logic that occurs ever 1/60 second goes @ this indentation level
        
        
      
        surface.fill((255, 255, 255))                             #set background color
        
        #drawing code goes here
        drawAllRings()
        
        
        #clock.tick(60)                                  #Change FPS - frames per sec- when animating
        pygame.display.update()                          #updates the screen- usually in main
        
        
        
            
main()                                                   #this calls the main function to run the program
