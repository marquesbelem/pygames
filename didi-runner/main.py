import pygame 
from sys import exit
from level import Level
from player import Player

pygame.init()

#  Settings Window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Introduction to Pygame")
clock = pygame.time.Clock()

game_running = False

_level = Level(screen, screen_width, screen_height)
_player = Player(screen_height, screen)

while True:
    
    _level.draw_scenario()
    
    if game_running == False:
        _level.draw_start_ui()
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or  event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            if(game_running == False):
                game_running = True
            else: 
                _player.jump()
    
    if game_running == True: 
        _player.movement()
    
    _player.draw()

    pygame.display.update()
    clock.tick(60) #frame