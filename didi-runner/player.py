import pygame

class Player: 
    def __init__(self, screen_height, screen):
        self._gravity = 0 
        self._screen_height = screen_height
        self._screen = screen
        
        self.image = pygame.image.load('sprites/didi2.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(220, self._screen_height - 30))

    def draw(self):
        self._screen.blit(self.image, self.rect)

    def movement(self):
        self._gravity += 1.5
        self.rect.y += self._gravity

        if self.rect.bottom >= self._screen_height - 30:
            self.rect.bottom = self._screen_height - 30
            self._gravity = 0 

    def jump(self):
        self._gravity = -30

