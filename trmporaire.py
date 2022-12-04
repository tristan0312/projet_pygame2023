import pygame, sys
from pygame.locals import *
pygame.init()
fenetre = pygame.display.set_mode((1000, 900))


def playing():
    while True:
        play_screen = pygame.image.load("pl_screen.png").convert_alpha()
        fenetre.blit(play_screen,(0,0))
        pygame.display.flip()
        



class Bouton():
    def __init__(self, image, pos, text_input, police, couleur_originel):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.police = police
        self.couleur_originel = couleur_originel
        self.text_input = text_input
        self.text = self.police.render(self.text_input, True, self.couleur_originel)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        return position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom)

bg = pygame.image.load("blood.jpg").convert_alpha()


def get_police(size): 
    return pygame.font.Font("font.ttf", size)

def option():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        fenetre.fill("black")

        OPTIONS_TEXT = get_police(15).render("rule : dodges cars and collect the coin.", True, "white")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(500, 50))
        fenetre.blit(OPTIONS_TEXT, OPTIONS_RECT)
        
        OPTIONS_TEXT_1 = get_police(15).render("Option: Press Fleche from the top to pause the game", True, "white")
        OPTIONS_RECT_1 = OPTIONS_TEXT_1.get_rect(center=(500, 200))
        fenetre.blit(OPTIONS_TEXT_1, OPTIONS_RECT_1)

        OPTIONS_BACK = Bouton(None, (500, 460), "BACK", get_police(75), "white")
        OPTIONS_BACK.update(fenetre)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                     menu()

        pygame.display.flip()


def menu():
    while True:
        fenetre.blit(bg, (-100,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        
        MENU_TEXT = get_police(100).render("MENU", True, "#ffffff")
        MENU_RECT = MENU_TEXT.get_rect(center=(530, 80))
        
        start_bouton = Bouton(pygame.image.load("Play Rect.png"), (530, 250), "PLAY", get_police(75), "#000000")
        option_bouton = Bouton(pygame.image.load("Options Rect.png"), (530, 400), "OPTIONS", get_police(75), "#000000")
        leave_bouton = Bouton(pygame.image.load("Quit Rect.png"), (530, 550),"QUIT", get_police(75), "#000000")
        
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if start_bouton.checkForInput(MENU_MOUSE_POS):
                    playing()
                   
                    
                if option_bouton.checkForInput(MENU_MOUSE_POS):
                    option()
                    
                if leave_bouton.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                    
        
        
        for button in [start_bouton, option_bouton, leave_bouton]:
            button.update(fenetre)
        
        
        fenetre.blit(MENU_TEXT, MENU_RECT)
        pygame.display.flip()
        
        

        
menu()
