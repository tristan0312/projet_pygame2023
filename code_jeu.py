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
    police = pygame.font.SysFont('John Hubbard',100)
    image_texte = police.render("game over", 1, (255,0,0))
    fenetre.blit(image_texte,(360,300))
    pygame.display.flip()
      
def pose():
    menu = pygame.image.load("pause.png").convert_alpha()
    fenetre.blit(menu,(-50,0))
    pygame.display.flip()
    
lst = ["jaune.png", "noir.png", "chevrolet.png", "enemy_car_1.png", "enemy_car_2.png"]   

class Obstacle():
    def __init__(self):
        self.x = randint(180,850)
        self.y = 0
        self.image = random.choice(lst)
        self.obstacle = pygame.image.load(self.image).convert_alpha()
        self.position_obstacle = self.obstacle.get_rect()
        self.speed = randint(15,30)
        self.score = 0
      
    
        
    def affichage(self):
        self.position_obstacle.topleft = (self.x, self.y)
        fenetre.blit(self.obstacle, self.position_obstacle)
        
    def bouge(self):
        self.y += self.speed
        if self.y >900:
            self.speed = randint(25,40)
            back = randint(1200,2200)
            self.y -= back
            self.x = randint(180,850)
            
        
            
            
    def collision(self):
        x_voiture = position_voiture[0]
        y_voiture = position_voiture[1]

        if (self.x-30) <= x_voiture <= (self.x+30)  and (self.y-30)<= y_voiture <=(self.y+30):
            crash()
            time.sleep(3)
            pygame.display.quit()
            sys.exit()
            
            
            
            
            
            
            
            
class Piece():
    def __init__(self,image):
        self.x = randint(180,850)
        self.y = 0
        self.obstacle = pygame.image.load(image).convert_alpha()
        self.position_obstacle = self.obstacle.get_rect()
        self.speed = randint(15,20)
        self.score = 0
    
    def affichage(self):
        self.position_obstacle.topleft = (self.x, self.y)
        fenetre.blit(self.obstacle, self.position_obstacle)  
        
    def bouge(self):
        self.y += self.speed
        if self.y >900:
            self.speed = randint(15,25)
            back = randint(1200,2200)
            self.y -= back
            self.x = randint(180,850)
    
    
    def collision(self):
        x_voiture = position_voiture[0]
        y_voiture = position_voiture[1]

        if (self.x-20) <= x_voiture <= (self.x+20)  and (self.y-20)<= y_voiture <=(self.y+20):
            self.score += 1
            
    def highscore(self,x,y):
        font = pygame.font.SysFont("arial", 55)
        text = font.render("Score: " + str(self.score), True, "white")
        fenetre.blit(text, (x, y))
            
            
            



piece = Piece("piece.png")


lst_voiture = [Obstacle() for _ in range(2)]
pas_deplacement = 20



def jeu():
    y_bg = 0
    while True:
        global position_voiture
        
        
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
        piece.affichage()
        piece.bouge()
        piece.collision()
        piece.highscore(770,0)
      
        
      
       

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
                    
                if event.key == K_UP:
                    pause = True
                    while pause:
                        pose()
                        for event in pygame.event.get():
                            if event.type==KEYDOWN and event.key ==  K_SPACE:
                                pause = False
                                break
                        
                                 
                            
                    
                
                    
                
                    

            
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
        
        
        
        
        
        
        
        clock.tick(60)
        pygame.display.flip()
        
