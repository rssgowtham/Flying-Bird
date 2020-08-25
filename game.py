import pygame
import time
import random
pygame.init()
display_width=1000
display_height=500
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("bird")
clock=pygame.time.Clock()
birdImg=pygame.image.load('bird2.png')
def bird(x,y):
    gameDisplay.blit(birdImg,(x,y))
def textObjects(text,font):
    textSurface=font.render(text,True,black)
    return textSurface,textSurface.get_rect()
def messageDisplay(text,x,y,size):
    largeText=pygame.font.Font('freesansbold.ttf',size)
    textSurf,textRect=textObjects(text,largeText)
    textRect.center=((x,y))
    gameDisplay.blit(textSurf,textRect)
    pygame.display.update()
def gameOver():
    messageDisplay("Game over!",display_width/2,display_height/2,115)
    time.sleep(2)
    gameLoop()
def putCoin(coin_x,coin_y,coin_w,coin_h,color):
    pygame.draw.rect(gameDisplay,color,[coin_x,coin_y,coin_w,coin_h])
def gameLoop():
    score=0
    x=500
    y=200
    x_change=0
    y_change=0
    exitGame=False
    coin_w=15
    coin_h=15
    coin_x=random.randrange(0,display_width-coin_w)
    coin_y=random.randrange(0,display_height-coin_h)
    while not exitGame:
        gameDisplay.fill(blue)
        messageDisplay(str(score),500,50,70)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                    y_change=-5
                if event.key==pygame.K_RIGHT:
                    x_change=5
                    y_change=-5
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                    y_change=5
                if event.key==pygame.K_RIGHT:
                    x_change=5
                    y_change=5
        x=x+x_change
        y=y+y_change
        bird(x,y)
        putCoin(coin_x,coin_y,coin_w,coin_h,red)
        pygame.display.update()
        if x>display_width-70 or x<0:
            gameOver()
        if y>display_height-50 or y<0:
            gameOver()
        if coin_x<=x+70 and coin_x>=x-15:
            if coin_y<=y+50 and coin_y+15>=y:
                coin_x=random.randrange(0,display_width-coin_w)
                coin_y=random.randrange(0,display_height-coin_h)
                score+=1        
        clock.tick(40)
gameLoop()
pygame.quit()
quit()
