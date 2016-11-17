import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
gameDisplay = pygame.display.set_mode((800,800))
pygame.display.set_caption("Escape the town")

background = pygame.image.load('bg.png') 
gameDisplay.blit(background, (0,0)) 


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

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                old_x = you.rect.center[0]
                old_y = you.rect.center[1]
                x=old_x - 10
                y=old_y
                you.rect.center=(x,y)
            elif event.key == pygame.K_RIGHT:
                old_x = you.rect.center[0]
                old_y = you.rect.center[1]
                x=old_x + 10
                y=old_y
                you.rect.center=(x,y)

    #pygame.draw.rect(gameDisplay, white, [380,30,40,40])
    
    #gameDisplay.blit(you,(380,30))
    You.clear(gameDisplay,background)
    You.draw(gameDisplay)
    pygame.display.update()

pygame.quit()
quit()
