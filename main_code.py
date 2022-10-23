import pygame, sys
from pygame.locals import *
from random import randint
pygame.init()
pygame.key.set_repeat(50)
clock = pygame.time.Clock()
fenetre = pygame.display.set_mode((1000, 900))
import time

route = pygame.image.load("sol.png").convert_alpha()
voiture = pygame.image.load("voiture.png").convert_alpha()
position_voiture = voiture.get_rect()
position_voiture.topleft = ( 500,800)


pygame.mixer.init()
pygame.mixer.music.load("musique.mp3") # import du fichier
pygame.mixer.music.play() # on joue le fichier
pygame.mixer.music.set_volume(0.6) # réglage du volume 







def crash():
    police = pygame.font.SysFont('monospace',100)
    image_texte = police.render("game over", 1, (255,0,0))
    fenetre.blit(image_texte,(200,300))
    pygame.display.flip()


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
    




class Obstacle():
    def __init__(self,image):
        self.x = randint(0,900)
        self.y = -100
        self.obstacle = pygame.image.load(image).convert_alpha()
        self.position_obstacle = self.obstacle.get_rect()
        self.speed = 20
        
    def affichage(self):
        self.position_obstacle.topleft = (self.x, self.y)
        fenetre.blit(self.obstacle, self.position_obstacle)
        
        
        
        
    def bouge(self):
        self.y += self.speed
        if self.y > 900:
            self.y -= 1200
            self.x = randint(0,800)
            
            
            
            
            
            
            
    def collision(self):
        x = position_voiture[0]
        y = position_voiture[1]
        
        
        if voiture_obstacle.x - 30  <= police.x <= voiture_obstacle.x +30 :
            police.x += 30
            
        
        
        if self.x-30 <= x <= self.x+30  and (self.y-30)<=y<=(self.y+30):
            crash()
            time.sleep(2)
            pygame.display.quit()
            sys.exit()
            
            
    
            
        
            



police = Obstacle("chevrolet.png")
voiture_obstacle = Obstacle("car.png")




pas_deplacement = 22
y_bg = 0





start()

while True:
    y_bg +=12
    fenetre.fill([10,186,181])
    
   
    
    if y_bg < 900:
        fenetre.blit(route, (0,y_bg))
        fenetre.blit(route, (0,y_bg-900))
    else:
        y_bg = 0
        fenetre.blit(route, (0,y_bg))  
    fenetre.blit(voiture, position_voiture)
    
    police.affichage()
    police.bouge()
    police.collision()
    voiture_obstacle.affichage()
    voiture_obstacle.bouge()
    voiture_obstacle.collision()
    
    
    
    
    
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
    pygame.display.flip()
