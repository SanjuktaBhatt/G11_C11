import pygame
import time
pygame.init() 
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("VIVA")
carryOn = True
while carryOn:
    for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                  carryOn = False # Flag that we are done so we exit this loop             
    for i in range(1,21):
        screen.fill(DARKBLUE)
        font = pygame.font.Font(None, 40)
        text = font.render("Roll number for Viva:", 1,RED)
        screen.blit(text, (70,10))
        font2 = pygame.font.Font(None,200)
        text2 = font.render(str(i), 1,RED)
        screen.blit(text2, (200,200))
        pygame.display.flip()
        time.sleep(10)
pygame.quit()
    
