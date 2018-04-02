import pygame
import time
import random

pygame.init()

#Game Sounds
pygame.mixer.music.load('background.wav')
crash_sound = pygame.mixer.Sound('crash.wav')

#Initialize some variables
display_width = 900
display_height = 900
rabbit_width= 50
gameLevel = 1
score =0

#Game Colors
black = (0,0,0)
white = (255,255,255)
grass_green= (96,128,56)
carrot_color=(241,112,9)
red = (200,0,0)
bright_red=(255,0,0)
green = (0,200,0)
bright_green=(0,255,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Crazy Rabbit')
clock = pygame.time.Clock()

#Load Rabbit Image File
rabbitImg= pygame.image.load('smallRabbit.png')

#Load Enemies' Images
foxImg = pygame.image.load('midsizeFox.png')
wolfImg= pygame.image.load('smallwolf.png')
lionImg= pygame.image.load('lionsmall.png')


# Writing score to sceen
def thing_dodged(count):
    font = pygame.font.SysFont(None,50)
    text = font.render('Score: ' + str(count),True,black)
    gameDisplay.blit(text,(5,5))

#Put rabbit character to game screen
def rabbit(x,y):
    gameDisplay.blit(rabbitImg,(x,y))

# give message when crash
def feedEnemy(enemy):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    
    if enemy == foxImg:
        message_display('You feed the Fox',foxImg)
    elif enemy == wolfImg:
        message_display('You feed the Wolf',wolfImg)
    elif enemy == lionImg:
        message_display('You feed the Lion',lionImg)
        
    
#Level Complete message and end the game
def levelComplete():
    close_text('Congratulations!')

#For quit the game after levelComplete
def close_text(text):
    largeText = pygame.font.Font('freesansbold.ttf',90)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center =((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(10)
    quitgame()
    
#General message display function
#It has extra game_loop function for restart the game after crash
def message_display(text,enemy):
    largeText = pygame.font.Font('freesansbold.ttf',90)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center =((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(5)
    
    enemy = foxImg
    game_loop(enemy)

#Creating enemies on screen
def createEnemy(enemy,thingx,thingy):
    gameDisplay.blit(enemy,(thingx,thingy))

#General text function
def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface, textSurface.get_rect()

#Quit function
def quitgame():
    pygame.quit()
    quit()

#Game loop for all logics and other stuffs
def game_loop(enemy):
    pygame.mixer.music.play(-1)

   # first cordinates of our character
    x=(display_width * 0.45)
    y=(display_height*0.8)

    x_change= 0

    #random cordinates creator for enemies
    thing_startx =random.randrange(0,display_width)
    thing_starty= -600
    thing_speed=5
    thing_width=20
    thing_height = 100
    dodged =0
    
    gameExit = False

    #Character Movements
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change= -10
                if event.key == pygame.K_RIGHT:
                    x_change=10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change=0

        x +=x_change

        #Fill the background of screen with grass green           
        gameDisplay.fill(grass_green)

        #Create enemies with random coordinates and add them some speed for they fall down
        createEnemy(enemy,thing_startx,thing_starty)     
        thing_starty += thing_speed

        #add our character to screen
        rabbit(x,y)
        thing_dodged(dodged)

        #If rabbit try our left or right side of screen, it crashes
        if x > display_width - rabbit_width  or x < 0:
            crash()

        #If enemy pass without without crash, increase dodged(our score) 1.
        if thing_starty > display_height:
            thing_starty = 0 -thing_height
            thing_startx = random.randrange(0,display_width)
            dodged +=1

        #If loop for catching the crash
        if y < thing_starty+thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x + rabbit_width > thing_startx and x + rabbit_width < thing_startx + thing_width:
                 feedEnemy(enemy)
                 
        #Simple level logic for starting
        # If you pass 10 enemies, then your enemy and speed of this will change.
        #You can create your own logic. Its up to you.
        if dodged == 11:
            enemy=wolfImg
            thing_speed = 7
        elif dodged == 21:
            enemy= lionImg
            thing_speed = 10
        elif dodged==31:
            enemy=foxImg
            levelComplete()
            
        #We assign 60 fps. IF you want to change it , just change :)    
        pygame.display.update()
        clock.tick(60)

           
            
# We call the game_loop function and game start..
game_loop(foxImg)
    
quitgame()




























