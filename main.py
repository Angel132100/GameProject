import random
import pygame

pygame.init()
# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
# Create display surface
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Burger Dog")
# Game settings
FPS = 60
clock = pygame.time.Clock()
# Player settings
PLAYER_STARTING_LIVES = 3
PLAYER_NORMAL_VELOCITY = 5
PLAYER_BOOST_VELOCITY = 10
STARTING_BOOST_LEVEL = 100
# Burger settings
STARTING_BURGER_VELOCITY = 3
BURGER_ACCELERATION = 0.5
BUFFER_DISTANCE = 100
# Player attributes
player_lives = PLAYER_STARTING_LIVES
player_velocity = PLAYER_NORMAL_VELOCITY
boost_level = STARTING_BOOST_LEVEL
burger_velocity = STARTING_BURGER_VELOCITY
# Colors
ORANGE = (246, 170, 54)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Font
font = pygame.font.Font("WashYourHand.ttf", 32)


# Function to prepare text
def prep_text(text: str, background_color: tuple[int, int, int], **locations):
    text_to_return = font.render(text, True, background_color)
    rect = text_to_return.get_rect()
    for location in locations:
        if location == "topleft":
            rect.topleft = locations["topleft"]
        elif location == "centerx":
            rect.centerx = locations["centerx"]
        elif location == "y":
            rect.y = locations["y"]
        elif location == "topright":
            rect.topright = locations["topright"]
        elif location == "center":
            rect.center = locations["center"]
    return text_to_return, rect
# score tracking variables
score = 0
burger_points = 0
burgers_eaten = 0

# Score-related text

points_text, points_rect = prep_text(f"Burger Points: {burger_points}", ORANGE, topleft=(10, 10))
score_text, score_rect = prep_text(f"Score: {score}", ORANGE, topleft=(10, 50))
title_text, title_rect = prep_text("Burger Dog", ORANGE, centerx=WINDOW_WIDTH // 2, y=10)
eaten_text, eaten_rect = prep_text(f"Burgers Eaten: {burgers_eaten}", ORANGE, centerx=WINDOW_WIDTH // 2, y=50)
lives_text, lives_rect = prep_text(f"Lives: {player_lives}", ORANGE, topright=(WINDOW_WIDTH - 10, 10))
boost_text, boost_rect = prep_text(f"Boost: {boost_level}", ORANGE, topright=(WINDOW_WIDTH - 10, 50))
game_over_text, game_over_rect = prep_text(f"FINAL SCORE: {score}", ORANGE,
                                           center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
continue_text, continue_rect = prep_text("Press any key to play again", ORANGE,
                                         center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64))
# Sounds and music
bark_sound = pygame.mixer.Sound("bark_sound.wav")
miss_sound = pygame.mixer.Sound("miss_sound.wav")
pygame.mixer.music.load("bd_background_music.wav")
def check_quit():

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            global running

            running = False

            break

            def move_player():
                global player_image
                keys = pygame.key.get_pressed()
                # TODO: (2025-02-10): check if keys[pygame.K_LEFT] and player_rect.left > 0:
                # TODO: (cont.): the if statement block
                # TODO: (cont.):  the if statement block should subtract player_velocity from player_rect.x
                player_image = player_image_left
                # TODO: (cont.):  end of the if block

                # TODO: (2025-02-10): check if keys[pygame.K_RIGHT] and player.rect.right < WINDOW_WIDTH:
                # TODO: (cont.):  the if statement block
                # TODO: (cont.):  the if statement block should add player_velocity to player_rect.x
                # TODO: (cont.):  set the player_image to player_image_right
                # TODO: (cont.):  end of the if block

                # TODO: (2025-02-10): check if keys[pygame.K_UP] and player.rect.top > 100
                # TODO: (cont.): the if statement block
                # TODO: (cont.):  the if statement block should subtract player_velocity from player_rect.y
                # TODO: (cont.):  end of the if block

                # TODO: (2025-02-10): check if keys[pygame.K_DOWN] and player.rect.bottom < WINDOW_HEIGHT
                # TODO: (cont.): the if statement block
                # TODO: (cont.):  the if statement block should add player_velocity to player_rect.y
                # TODO: (cont.):  end of the if block

                engage_boost(keys)
                pass  # TODO: (2025-02-10):  remove this when done.

            def engage_boost(keys):
                # TODO: (2025-02-10): check if keys[pygame.K_SPACE] and boost_level > 0
                # TODO: (2025-02-13): player_velocity = PLAYER_BOOST_VELOCITY
                # TODO: (2025-02-10): subtract 1 from boost_level
                # TODO: (2025-02-10): else set player_velocity to PLAYER_NORMAL_VELOCITY
                pass  # TODO: (2025-02-10):  remove this when done.

            def move_burger():
                # TODO: (2025-02-10): add burger_velocity to burger_rect.y
                burger_points = int(burger_velocity * (WINDOW_HEIGHT - burger_rect.y + 100))
                pass  # TODO: (2025-02-10):  remove this when done.

            def handle_miss():
                # TODO: (2025-02-10): if burger_rect.y is greater than WINDOW_HEIGHT:
                # TODO: (2025-02-10):  the rest of this functions code is in an if statement block
                # TODO: (2025-02-10):  subtract 1 from player_lives
                # TODO: (2025-02-10):  call miss_sound's play method
                burger_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)
                # TODO: (2025-02-10):  set burger_velocity to STARTING_BURGER_VELOCITY
                # TODO: (2025-02-10):  set player_rect.centerx to WINDOW_WIDTH // 2
                # TODO: (2025-02-10):  set player_rect.bottom to WINDOW_HEIGHT
                # TODO: (2025-02-10):  set boost_level to STARTING_BOOST_LEVEL
                pass  # TODO: (2025-02-10):  remove this when done.

            def check_collisions():
                if player_rect.colliderect(burger_rect):
                    # TODO: (2025-02-10):  add burger_points to score
                    # TODO: (2025-02-10):  add 1 to burgers_eaten
                    # TODO: (2025-02-10):  call bark_sounds' play method
                    burger_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)
                    # TODO: (2025-02-10):  add BURGER_ACCELERATION to burger_velocity

                    # TODO: (2025-02-10):  add 25 to boost_level
                    # TODO: (2025-02-10):  finally check if boost_level > STARTING_BOOST_LEVEL
                    # TODO: (2025-02-10):  then set boost_level to STARTING_BOOST_LEVEL
                    pass  # TODO: (2025-02-10):  remove this when done.

            def update_hud():
                points_text = font.render("Burger Points: " + str(burger_points), True, ORANGE)
                score_text = font.render("Score: " + str(score), True, ORANGE)
                eaten_text = font.render("Burgers Eaten: " + str(burgers_eaten), True, ORANGE)
                lives_text = font.render("Lives: " + str(player_lives), True, ORANGE)
                boost_text = font.render("Boost: " + str(boost_level), True, ORANGE)
                pass  # TODO: (2025-02-10):  remove this when done.

            def check_game_over():
                # TODO: (2025-02-12): Add this game over code
                global game_over_text, is_paused, score, burgers_eaten, player_lives, boost_level, burger_velocity, running
                if player_lives == 0:
                    game_over_text = font.render(f"FINAL SCORE: {score}", True, ORANGE)
                    display_surface.blit(game_over_text, game_over_rect)
                    display_surface.blit(continue_text, continue_rect)
                    pygame.display.update()
                    pygame.mixer.music.stop()
                    is_paused = True
                    while is_paused:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                score = 0
                                burgers_eaten = 0
                                player_lives = PLAYER_STARTING_LIVES
                                boost_level = STARTING_BOOST_LEVEL
                                burger_velocity = STARTING_BURGER_VELOCITY
                                pygame.mixer.music.play()
                                is_paused = False
                            if event.type == pygame.QUIT:
                                is_paused = False
                                running = False

            def display_hud():
                display_surface.fill(BLACK)
                display_surface.blit(points_text, points_rect)
                # TODO (2025-02-10): We just blit points_text and points_rect
                # TODO (cont.):  repeat for score, title, eaten, lives, boost
                pygame.draw.line(display_surface, WHITE, (0, 100), (WINDOW_WIDTH, 100), 3)
                # TODO (2025-02-10): blit player_image, player_rect
                # TODO (2025-02-10): blit burger_image, burger_rect
                pass  # TODO: (2025-02-10):  remove this when done.

            def handle_clock():
                pygame.display.update()
                clock.tick(FPS)
                pass  # TODO: (2025-02-10):  remove this when done.

            while running:
                # TODO: (2025-02-12): Add the function calls below
                check_quit()
                move_player()
                move_burger()
                handle_miss()
                check_collisions()
                update_hud()
                check_game_over()
                display_hud()
                handle_clock()
# Images
player_image_right = pygame.image.load("dog_right.png")
player_image_left = pygame.image.load("dog_left.png")
player_image = player_image_left
player_rect = player_image.get_rect()
player_rect.centerx = WINDOW_WIDTH // 2
player_rect.bottom = WINDOW_HEIGHT

burger_image = pygame.image.load("burger.png")
burger_rect = burger_image.get_rect()
burger_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)
# Game loop placeholder
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update game logic here
    # Draw everything
    display_surface.fill(WHITE)
    display_surface.blit(points_text, points_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(eaten_text, eaten_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(boost_text, boost_rect)
    display_surface.blit(player_image, player_rect)
    display_surface.blit(burger_image, burger_rect)
pygame.display.update()
clock.tick(FPS)
pygame.quit()
