import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 500) - start_time
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time

pygame.init()
pygame.display.set_caption('Experiementing w/ PyGame')

# Creating the background and screen of Game
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
game_active = False
start_time = 0
score = 0


# Font
test_font = pygame.font.Font('font/joystix.ttf', 30)
#score_font = pygame.font.Font('font/joystix.ttf', 20)

# Surfaces
background_surface = pygame.Surface((800,400))
background_surface.fill('lightblue')
ground_surface = pygame.image.load('graphics/pixel-ground.png')
newGround_surface = pygame.transform.scale(ground_surface, (800,150))

# Text Boxes
# score_surf = test_font.render("My Game", False, (64,64,64)) 
# score_rect = score_surf.get_rect(center = (400,50))

# Sprites
spirit_surf = pygame.image.load('graphics/spirit/idle/0.png').convert_alpha()
spirit_rect = spirit_surf.get_rect(midbottom = ( 600,325))

player_surf = pygame.image.load('graphics/player/right/right_0.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (200,325))
player_gravity = 0

# Intro Screen
player_stand = pygame.image.load('graphics/player/down/down_0.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_title = test_font.render("Bro I Gotta Run", False, 'black')
game_title_rect = game_title.get_rect(center = (400, 80))

game_message = test_font.render("Press Space to run", False, 'black')
game_message_rect = game_message.get_rect(center = (400, 320))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,900)

while True:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos): player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 325:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                spirit_rect.x = 800
                start_time = int(pygame.time.get_ticks() / 500)

        if event.type == obstacle_timer:
            print('test')

    if game_active:
        # displaying the surfaces
        screen.blit(background_surface,(0,0))
        screen.blit(newGround_surface,(0,300))
        # pygame.draw.rect(screen,'#c0e8ec',score_rect)
        # pygame.draw.rect(screen,'#c0e8ec',score_rect,20)
        # screen.blit(score_surf,score_rect)
        score = display_score()


        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 325: player_rect.bottom=325
        screen.blit(player_surf,player_rect)
    
        # Spirit
        screen.blit(spirit_surf,spirit_rect)
        spirit_rect.x -= 7 
        if spirit_rect.right <= 0: spirit_rect.left = 800

        # Collisions
        if spirit_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)

        score_message = test_font.render(f'Your score: {score}',False,(111,196,169))
        score_message_rect =score_message.get_rect(center = (400,330))
        screen.blit(game_title, game_title_rect)

        if score == 0:
            screen.blit(game_message,game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)


    
    pygame.display.update()
    clock.tick(60) # maximum frames per second