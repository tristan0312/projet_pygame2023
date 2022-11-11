import pygame, sys
from pygame.locals import *
import random
from random import randint
import time





pygame.init()
pygame.key.set_repeat(50)
clock = pygame.time.Clock()
fenetre = pygame.display.set_mode((1000, 900))







route = pygame.image.load("road.png").convert_alpha()

voiture = pygame.image.load("voiture.png").convert_alpha()
position_voiture = voiture.get_rect()
position_voiture.topleft = ( 500,800)






def crash():
    police = pygame.font.SysFont('monospace',100)
    image_texte = police.render("game over", 1, (255,0,0))
    fenetre.blit(image_texte,(250,300))
    pygame.display.flip()
    
    
    
    
def score(position_x, position_y, taille):
    timer = pygame.time.get_ticks()
    temps = timer // 1000
    police = pygame.font.SysFont('monospace',taille)
    image_texte = police.render("points:" + str(temps), 1, (255,0,0))
    fenetre.blit(image_texte,(position_x, position_y))
    pygame.display.flip()


class Obstacle():
    def __init__(self):
        self.x = randint(180,850)
        self.y = 0
        self.obstacle = pygame.image.load("jaune.png").convert_alpha()
        self.position_obstacle = self.obstacle.get_rect()
        self.speed = randint(15,30)
        
        
    
        
    def affichage(self):
        self.position_obstacle.topleft = (self.x, self.y)
        fenetre.blit(self.obstacle, self.position_obstacle)
        
    def bouge(self):
        self.y += self.speed
        if self.y > 900:
            self.speed = randint(25,40)
            back = randint(1200,2200)
            self.y -= back
            self.x = randint(180,850)
        
            
            
    def collision(self):
        x_voiture = position_voiture[0]
        y_voiture = position_voiture[1]
#         
#         for obs in lst_voiture:
#            if                       #le teste 
#             
           
        
        
    
        if (self.x-30) <= x_voiture <= (self.x+30)  and (self.y-30)<= y_voiture <=(self.y+30):
            crash()
            score(380, 450, 70)
            time.sleep(2)
            pygame.display.quit()
            sys.exit()
          
            
        
                   
               
            
 


lst_voiture = [Obstacle() for _ in range(2)]




def start():
    police = pygame.font.SysFont('monospace',100)
    image_texte = police.render("3", 1, (255,0,0))
    fenetre.blit(image_texte,(250,300))
    pygame.display.flip()
    time.sleep(1)
    police = pygame.font.SysFont('monospace',100)
    image_texte = police.render("2", 1, (255,128,0))
    fenetre.blit(image_texte,(500,300))
    pygame.display.flip()
    time.sleep(1)
    police = pygame.font.SysFont('monospace',100)
    image_texte = police.render("1", 1, (0,255,0))
    fenetre.blit(image_texte,(750,300))
    pygame.display.flip()
    time.sleep(1)















pas_deplacement = 20
y_bg = 0




start()




while True:
    x = position_voiture[0]
    y = position_voiture[1]
    
   
    
    y_bg +=18
    
    
   
    
    if y_bg < 900:
        fenetre.blit(route, (0,y_bg))
        fenetre.blit(route, (0,y_bg-900))
    else:
        y_bg = 0
        fenetre.blit(route, (0,y_bg))
        
        
        
    if  x <= 130:
        position_voiture = position_voiture.move(pas_deplacement,0)
        
        
    if x >= 810 :
        position_voiture = position_voiture.move(-pas_deplacement,0)   
        
        
        
        
        
        
        
    fenetre.blit(voiture, position_voiture)

    for obs in lst_voiture:
           obs.affichage()
           obs.bouge()
           obs.collision()
        
    
    for event in pygame.event.get() :
        if event.type == KEYDOWN:

            if event.key == K_RIGHT : 
                position_voiture = position_voiture.move(pas_deplacement,0)

            if event.key == K_LEFT : 
                position_voiture = position_voiture.move(-pas_deplacement,0)
             

        
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
    
    
    
    
    
    
    
    clock.tick(60)
    score(770,0,45)
    pygame.display.flip()































































_______________________________________________________________________________________________________________

 elif event.key == K_SPACE:
                Pause = True
                while Pause:
                    for event in pygame.event.get()
                        if event.type==KEYDOWN and event.key == K_SPACE:
                            Pause = False
                            #modif après édition
                            pygame.event.clear()
                            break

