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
