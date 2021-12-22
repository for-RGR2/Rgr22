import pygame, random

pygame.init()

# variables and constants
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
HEADER_HEIGHT = 80

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)

BUFFER_DISTANCE = 100
PLAYER_STARTING_SCORE = 0
PLAYER_STARTING_LIVE = 5
BIRD_STARTING_VELOCITY = 5
BIRD2_STARTING_VELOCITY = 7
BIRD3_STARTING_VELOCITY = 9


player_score = PLAYER_STARTING_SCORE
player_live = PLAYER_STARTING_LIVE
dragon_velocity = 5
bird_velocity = BIRD_STARTING_VELOCITY
bird2_velocity = BIRD2_STARTING_VELOCITY
bird3_velocity = BIRD3_STARTING_VELOCITY
acceleration = 0.5

# main surface
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Aidahardy tamaqtandyru")

# images
background = pygame.image.load('background.png')

score_backround = pygame.image.load('score_background.png').convert_alpha()
score_background_rect = score_backround.get_rect()
score_background_rect.topleft = (10,10)

live_background = pygame.image.load('score_background.png').convert_alpha()
live_background_rect = live_background.get_rect()
live_background_rect.topleft = (WINDOW_WIDTH-(live_background_rect.width+10), 10)

dragon_image = pygame.image.load('dragon.png').convert_alpha()
dragon_image = pygame.transform.rotate(dragon_image, 90)
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (80, WINDOW_HEIGHT//2)

bird_image = pygame.image.load('bird.png').convert_alpha()
bird_image_rect = bird_image.get_rect()
bird_image_rect.center = ((WINDOW_WIDTH+BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))

bird2_image = pygame.image.load('bird.png').convert_alpha()
bird2_image_rect = bird2_image.get_rect()
bird2_image_rect.center = ((WINDOW_WIDTH+BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))

bird3_image = pygame.image.load('bird.png').convert_alpha()
bird3_image_rect = bird3_image.get_rect()
bird3_image_rect.center = ((WINDOW_WIDTH+BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))


# fonts and texts
main_font = pygame.font.Font('AttackGraffiti.ttf', 32)

score_text = main_font.render("Upai: " + str(player_score), True, RED)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (20, 20)

game_name = main_font.render("Aidahardy Tamaqtandyru", True, RED, WHITE)
game_name_rect = game_name.get_rect()
game_name_rect.center = (WINDOW_WIDTH//2, HEADER_HEIGHT//2)

live_text = main_font.render("Jany: " + str(player_live), True, RED)
live_text_rect = live_text.get_rect()
live_text_rect.topleft = (WINDOW_WIDTH-(live_background_rect.width), 20)

game_over_text = main_font.render("GAMEOVER", True, GREEN, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

game_continue_text = main_font.render("PRESS ANY KEY", True, GREEN)
game_continue_rect = game_continue_text.get_rect()
game_continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2+100)

# sounds and musics
pygame.mixer.music.load('music.wav')
sound1 = pygame.mixer.Sound('sound_1.wav')
sound2 = pygame.mixer.Sound('sound_2.wav')
sound2.set_volume(0.1)

FPS = 60
clock = pygame.time.Clock()

pygame.mixer.music.play(-1, 0.0)
# main loop
fl_pause = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dragon_rect.top > HEADER_HEIGHT:
        dragon_rect.y -= dragon_velocity
    elif keys[pygame.K_DOWN] and dragon_rect.bottom < WINDOW_HEIGHT:
        dragon_rect.y += dragon_velocity

    bird_image_rect.centerx -= bird_velocity
    bird2_image_rect.centerx -= bird2_velocity
    bird3_image_rect.centerx -= bird3_velocity
   

    if bird_image_rect.centerx < 0:
        bird_image_rect.center = ((WINDOW_WIDTH+BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))
        player_live -= 1
        sound2.play()
    if bird2_image_rect.centerx < 0:
        bird2_image_rect.center = ((WINDOW_WIDTH+BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))
        player_live -= 1
        sound2.play()
    if bird3_image_rect.centerx < 0:
        bird3_image_rect.center = ((WINDOW_WIDTH+BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))
        player_live -= 1
        sound2.play()
    

    if dragon_rect.colliderect(bird_image_rect):
        player_score += 1
        sound1.play()
        bird_image_rect.center = ((WINDOW_WIDTH+BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))
        bird_velocity += acceleration

    if dragon_rect.colliderect(bird2_image_rect):
        player_score += 2
        player_live +=1
        sound1.play()
        bird2_image_rect.center = ((WINDOW_WIDTH+BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))
        bird2_velocity += acceleration

    if dragon_rect.colliderect(bird3_image_rect):
        player_score += 3
        player_live -=1
        sound1.play()
        bird3_image_rect.center = ((WINDOW_WIDTH+BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))
        bird3_velocity += acceleration

#if player_live == 0 
if player_score > 10:
        fl_pause = True
        pygame.mixer.music.stop()
        live_text = main_font.render("Jany: " + str(player_live), True, RED)
        display_surface.blit(live_text, live_text_rect)
        pygame.display.update()
        while fl_pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fl_pause = False
                    running = False
                if event.type == pygame.KEYDOWN:
                    player_score = PLAYER_STARTING_SCORE
                    player_live = PLAYER_STARTING_LIVE
                    bird_velocity = BIRD_STARTING_VELOCITY
                    bird2_velocity = BIRD2_STARTING_VELOCITY
                    bird3_velocity = BIRD3_STARTING_VELOCITY
                    pygame.mixer.music.play(-1, 0.0) 
                    fl_pause = False

            display_surface.blit(game_over_text, game_over_rect)
            display_surface.blit(game_continue_text, game_continue_rect)
            pygame.display.update()


        display_surface.blit(background, (0,0))
        display_surface.blit(score_backround, score_background_rect)
        display_surface.blit(live_background, live_background_rect)
        pygame.draw.line(display_surface, WHITE, (0, HEADER_HEIGHT), (WINDOW_WIDTH, HEADER_HEIGHT), 5)
        display_surface.blit(dragon_image, dragon_rect)
        display_surface.blit(bird_image, bird_image_rect)
        display_surface.blit(bird2_image, bird2_image_rect)
        display_surface.blit(bird3_image, bird3_image_rect)
    
        score_text = main_font.render("Upai: " + str(player_score), True, RED)
        live_text = main_font.render("Jany: " + str(player_live), True, RED)
        display_surface.blit(score_text, score_text_rect)
        display_surface.blit(game_name, game_name_rect)
        display_surface.blit(live_text, live_text_rect)
    


        pygame.display.update()
        clock.tick(FPS)

pygame.quit()