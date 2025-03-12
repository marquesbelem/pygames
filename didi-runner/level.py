import pygame

class Level:
    def __init__(self,screen, screen_width, screen_height):
        self._screen = screen
        self._screen_height = screen_height
        self._screen_width = screen_width

    def draw_start_ui(self):
        self._font = pygame.font.Font('fonts\Anton\Anton-Regular.ttf', 50)
        self.text_surface = self._font.render('Click to start', True, 'White')
        self._screen.blit(self.text_surface, (self._screen_width / 2 - 100, self._screen_height / 2 - 50))
    
    def draw_scenario(self):
        self._bg_surface = pygame.image.load('sprites/bg.jpg').convert()
        self._ground_surface = pygame.image.load('sprites/ground.jpg').convert()
        self._screen.blit(self._bg_surface, (0, 0))   
        self._screen.blit(self._ground_surface, (0, self._screen_height -100))
   