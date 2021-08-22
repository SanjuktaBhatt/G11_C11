import pygame
import random
#Import time module


pygame.init()

size = (350, 400)
screen = pygame.display.set_mode(size)
carx=60
cary=340
threshold=0
roadx=-10
roady=0
threshold=0


#Replace file location address on your computer
road=pygame.image.load("XXXXX").convert_alpha()
road=pygame.transform.smoothscale(img,(400,800))

#Replace file location address on your computer
car=pygame.image.load("XXXXX").convert_alpha()
car=pygame.transform.smoothscale(img,(70,60))

carryOn = True

#Create timepoint t1 here



while carryOn:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      carryOn = False
  
  screen.blit(road,(roadx,roady))
  screen.blit(car,(carx,cary))
  
  

  if event.type==pygame.KEYDOWN:
    if event.key==pygame.K_UP:
        cary-=2
        roady-=1
    if event.key==pygame.K_DOWN:
        cary+=2
    if event.key==pygame.K_LEFT:
        carx-=2
    if event.key==pygame.K_RIGHT:
        carx+=2

  if cary<=0:
    roady=0
    cary=340
  
  pygame.display.flip()
  #Create second time point here
 
  #Evaluate gametime here

  
  #Display gametime here
  #Select font
  
  #Select text.Remember to concatenate gametime
 
  #Display the text
 
  
  
  if event.type==pygame.KEYDOWN:
 
        if event.key==pygame.K_RETURN:
       
            if game_time>=threshold and game_time<=(threshold+10):
                  
                    cary-=10 
                   
                    threshold+=10
  
pygame.quit()
