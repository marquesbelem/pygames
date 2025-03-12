import pygame 
from sys import exit
from random import randint

pygame.init()

# region Settings Window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Introduction to Pygame")
clock = pygame.time.Clock()
#endregion

enemy_speed = 5
game_running = False
player_gravity = 0
game_over = False
start_time = 0
disable_event = False
timer_enable_event = 0 

#region Surface 
font = pygame.font.Font('fonts\Anton\Anton-Regular.ttf', 50)
bg_surface = pygame.image.load('sprites/bg.jpg').convert()
ground_surface = pygame.image.load('sprites/ground.jpg').convert()

#Obstacles
enemy_surface = pygame.image.load('sprites/camis.png').convert_alpha()
enemy_surface_2 = pygame.image.load('sprites/camis2.png').convert_alpha()

obstacle_list = []

player_surface = pygame.image.load('sprites/didi2.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(220, screen_height - 30))
#endregion

#Timer 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

def obsctacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= enemy_speed
            
            if obstacle_rect.bottom == 700:
                screen.blit(enemy_surface, obstacle_rect)
            else:
                screen.blit(enemy_surface_2, obstacle_rect)
            
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -500]
        return obstacle_list
    else:
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacles_rect in obstacles:
            if player.colliderect(obstacles_rect):
                return True
    return False

def events_input():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or  event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
           global game_running
           global player_gravity
           if game_running == False or game_over: 
               reset_game()
           else:
            #if player_rect.bottom >= screen_height - 30:
            player_gravity = -12
        if event.type == obstacle_timer and game_running:
            if randint(0, 2):
                obstacle_list.append(enemy_surface.get_rect(bottomright=(randint(screen_width, screen_width + 500), 700)))
            else:
                obstacle_list.append(enemy_surface_2.get_rect(bottomright=(randint(screen_width, screen_width + 500), 300)))

def reset_game():
    global game_running
    global player_gravity
    global game_over
    global start_time
    global scale_image
    game_running = True
    game_over = False
    start_time = int(pygame.time.get_ticks()/1000)
    scale_image = 0
    player_gravity = 0
    player_rect.y = screen_height - 30
    obstacle_list.clear()

def show_start_ui():
    font = pygame.font.Font('fonts\Anton\Anton-Regular.ttf', 50)
    text_surface = font.render('Click to start', True, 'White')
    screen.blit(text_surface, (screen_width / 2 - 100, screen_height / 2 - 50))

scale_image = 0
def show_game_over_ui():
    image_game_over_surface = pygame.image.load('sprites/didi.png').convert_alpha()
    global scale_image

    if(scale_image < 500):
        scale_image += 5
    
    image_game_over_surface = pygame.transform.scale(image_game_over_surface, (scale_image, scale_image))
    image_rect = image_game_over_surface.get_rect(center=(screen_width / 2, screen_height / 2))

    screen.fill('Black')
    font = pygame.font.Font('fonts\Anton\Anton-Regular.ttf', 50)
    text_surface = font.render('Game Over', True, 'White')
    screen.blit(text_surface, (screen_width / 2 - 100, 10))
    screen.blit(image_game_over_surface, image_rect)

def score_display():
    if game_running == False:
        return

    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surface = font.render(f'score: {current_time}', False, 'White')
    score_rect = score_surface.get_rect(center=(screen_width / 2, 50))
  
    pygame.draw.rect(screen, 'Black', score_rect)
    screen.blit(score_surface, score_rect)

def draw_sprites():
    screen.blit(bg_surface, (0, 0))   
    screen.blit(ground_surface, (0, screen_height -100))
    score_display()

def player(): 
    global player_gravity
    if game_running:
        player_gravity += 0.2
        player_rect.y += player_gravity
        
        if player_rect.bottom >= screen_height - 30:
            player_rect.bottom = screen_height - 30
            player_gravity = 0

    screen.blit(player_surface, player_rect)

def block_events():
    global timer_enable_event
    global disable_event
    disable_event = True
    if disable_event:
        timer_enable_event += 1
        if timer_enable_event >= 50:
            disable_event = False
            timer_enable_event = 0

while True:
    if disable_event == False:
        events_input()
    
    if game_over == False:
        draw_sprites()
        player()
        if game_running == False:
            show_start_ui()
        else:
           obstacle_list = obsctacle_movement(obstacle_list)
    else:
        show_game_over_ui()
        block_events()

    game_over = collisions(player_rect, obstacle_list)
    pygame.display.update()
    clock.tick(60) #frame

