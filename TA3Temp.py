import pygame
import random
import time

pygame.init()

size = (350, 400)
screen = pygame.display.set_mode(size)
carx=60
cary=340
threshold=0
roadx=-10
roady=0
#Create threshol variable and set it to 0



#Replace file location address on your computer
road=pygame.image.load("XXXXX").convert_alpha()
road=pygame.transform.smoothscale(img,(400,800))

#Replace file location address on your computer
car=pygame.image.load("XXXXX").convert_alpha()
car=pygame.transform.smoothscale(img,(70,60))

carryOn = True
t1=time.time()


while carryOn:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      carryOn = False
  
  screen.blit(road,(roadx,roady))
  screen.blit(car,(carx,cary))
  
  

  if event.type==pygame.KEYDOWN:
    if event.key==pygame.K_UP:
        cary-=5
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
  t2=time.time()
  gametime=t2-t1
  
  #Check if Key is pressed
\
  #Check if key pressed is "Enter"
      :
        #Check if game time is within threshold
           
                    #Decrement "cary" to make car move forward
                   
                    #Increment "threshold" by 10
                  
  
pygame.quit()
