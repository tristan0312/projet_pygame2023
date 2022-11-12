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

   
