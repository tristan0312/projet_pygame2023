import pygame, sys
from pygame.locals import *
from random import randint
import time





pygame.init()
pygame.key.set_repeat(50)
clock = pygame.time.Clock()
fenetre = pygame.display.set_mode((1000, 900))


pygame.mixer.init()
pygame.mixer.music.load("musique.mp3") # import du fichier
pygame.mixer.music.play() # on joue le fichier
pygame.mixer.music.set_volume(0.6) # réglage du volume





route = pygame.image.load("road.png").convert_alpha()

voiture = pygame.image.load("voiture.png").convert_alpha()
position_voiture = voiture.get_rect()
position_voiture.topleft = ( 500,800)



def crash():
    police = pygame.font.SysFont('monospace',100)
    image_texte = police.render("game over", 1, (255,0,0))
    fenetre.blit(image_texte,(250,300))
    pygame.display.flip()
    
    
    
    
def score(x1,x2,taille,y):
    timer = pygame.time.get_ticks()
    temps = timer // 1000
    police = pygame.font.SysFont('monospace',taille)
    image_texte = police.render(str(temps), 1, (255,0,0))
    fenetre.blit(image_texte,(x1,y))
    police1 = pygame.font.SysFont('monospace',taille)
    image_texte1 = police1.render("points:", 1, (255,0,0))
    fenetre.blit(image_texte1,(x2,y))
    pygame.display.flip()


class Obstacle():
    def __init__(self,x,image):
        self.x = x
        self.y = 0
        self.obstacle = pygame.image.load(image).convert_alpha()
        self.position_obstacle = self.obstacle.get_rect()
        self.speed = randint(15,30)
        
        
    
        
    def affichage(self):
        self.position_obstacle.topleft = (self.x, self.y)
        fenetre.blit(self.obstacle, self.position_obstacle)
        
    def bouge(self,xd,xf):
        self.y += self.speed
        if self.y > 900:
            self.speed = randint(25,40)
            back = randint(1200,2200)
            self.y -= back
            self.x = randint(xd,xf)
            
            
    def collision(self):
        x = position_voiture[0]
        y = position_voiture[1]
        
        
    
        if self.x-30 <= x <= self.x+30  and (self.y-30)<=y<=(self.y+30):
            crash()
            score(650,360,70,450)
            time.sleep(2)
            pygame.display.quit()
            sys.exit()





chevrolet = Obstacle(200, "chevrolet.png")
voiture_obstacle = Obstacle(435, "car.png")
black = Obstacle(615, "noir.png")
yellow = Obstacle(788, "jaune.png")



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

    chevrolet.affichage()
    chevrolet.bouge(170,280)
    chevrolet.collision()
    
    voiture_obstacle.affichage()
    voiture_obstacle.bouge(335,510)
    voiture_obstacle.collision()
    
    black.affichage()
    black.bouge(500,650)
    black.collision()
    
 
    yellow.affichage()
    yellow.bouge(700,850)
    yellow.collision()
    
    
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
    score(920,730,45,0)
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

