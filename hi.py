

import pygame
from time import sleep as wait

pygame.init()

white = (255,255,255)
black = (0,0,0)
gameDisplay = pygame.display.set_mode((800,800))
pygame.display.set_caption("Escape the town")

bg1 = pygame.image.load('bg.png')
background = bg1
bg2 = pygame.image.load('bg2.png')
gameDisplay.blit(background, (0,0)) 
current_background = [background]

you = pygame.sprite.Sprite()
you.image = pygame.image.load('player1.png')
you.rect=you.image.get_rect()
you.rect.center=(400,400)

#you.rect=you.image.get_rect()
#ou.rect.center=(400,400)
x=you.rect.center[0]
y=you.rect.center[1]
You = pygame.sprite.RenderClear(you)
gameExit = False

class Dir():
    def __init__(self,val):
        self.val = val
    def getvalue(self):
        return self.val
    def setvalue(self,val):
        self.val = val
        
move_left=Dir(False)
move_right=Dir(False)
move_up=Dir(False)
move_down=Dir(False)

def update_character():
    You.clear(gameDisplay,current_background[0])
    You.draw(gameDisplay)

def switch():
    if current_background[0] == bg1:
        background = bg2
    elif current_background[0] == bg2:
        background = bg1
    for i in range(len(current_background)):
        current_background.pop()
    current_background.append(background)

    gameDisplay.blit(background, (0,0))
    update_character()

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == 113:
                switch()
                
            if event.key == pygame.K_LEFT:
                move_left.setvalue(True)
                #old_x = you.rect.center[0]
                #old_y = you.rect.center[1]
                #x=old_x - 10
                #y=old_y
                #you.rect.center=(x,y)
            
            
            elif event.key == pygame.K_RIGHT:
                move_right.setvalue(True)
                #old_x = you.rect.center[0]
                #old_y = you.rect.center[1]
                #x=old_x + 10
                #y=old_y
                #you.rect.center=(x,y)
                pass
            elif event.key == pygame.K_UP:
                move_up.setvalue(True)
                #old_x = you.rect.center[0]
                #old_y = you.rect.center[1]
                #x=old_x
                #y=old_y - 10
                #you.rect.center=(x,y)
                pass
            elif event.key == pygame.K_DOWN:
                move_down.setvalue(True)
                #old_x = you.rect.center[0]
                #old_y = you.rect.center[1]
                #x=old_x
                #y=old_y + 10

                #you.rect.center=(x,y)
                pass
            
        if event.type == pygame.KEYUP:
            for direction in (move_left,move_right,move_up,move_down):
                direction.setvalue(False)
                
    if move_left.getvalue():
        old_x = you.rect.center[0]
        old_y = you.rect.center[1]
        x=old_x - 5
        y=old_y
        you.rect.center=(x,y)
    if move_right.getvalue():
        old_x = you.rect.center[0]
        old_y = you.rect.center[1]
        x=old_x + 5
        y=old_y
        you.rect.center=(x,y)
    if move_up.getvalue():
        old_x = you.rect.center[0]
        old_y = you.rect.center[1]
        x=old_x
        y=old_y - 5
        you.rect.center=(x,y)
    if move_down.getvalue():
        old_x = you.rect.center[0]
        old_y = you.rect.center[1]
        x=old_x
        y=old_y + 5
        you.rect.center=(x,y)
    update_character()
    pygame.display.update()
    wait(.05)

pygame.quit()
quit()
