import random

import pygame



# Initialize pygame

pygame.init()



# Constants

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Burger Dog")



# FPS and Clock

FPS = 60

clock = pygame.time.Clock()



# Game Constants

PLAYER_STARTING_LIVES = 3

PLAYER_NORMAL_VELOCITY = 5

PLAYER_BOOST_VELOCITY = 10

STARTING_BOOST_LEVEL = 100

STARTING_BURGER_VELOCITY = 3

BURGER_ACCELERATION = 0.5

BUFFER_DISTANCE = 100



# Player and Burger Variables

score = 0

burger_points = 0

burgers_eaten = 0



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



# Load images

player_image = pygame.image.load("dog_right.png")  # Replace with actual player image

player_image = pygame.image.load("dog_left.png")  # Replace with actual player image

burger_image = pygame.image.load("burger.png")  # Replace with actual burger image



# Scale images

player_rect = player_image.get_rect(midbottom=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 20))

burger_rect = burger_image.get_rect(midtop=(random.randint(0, WINDOW_WIDTH - 50), -50))





# Function to prepare text

def prep_text(text: str, background_color: tuple[int, int, int], **locations):

    """Returns a tuple containing a text surface and its corresponding rectangle."""

    text_to_return = font.render(text, True, background_color)

    rect = text_to_return.get_rect()



    for location in locations:

        if location == "topleft":

            rect.topleft = locations["topleft"]

        elif location == "centerx":

            rect.centerx = locations["centerx"]



    return text_to_return, rect





# Game loop

running = True

while running:

    # Handle events

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False



    # Get keys pressed

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_rect.left > 0:

        player_rect.x -= player_velocity

    if keys[pygame.K_RIGHT] and player_rect.right < WINDOW_WIDTH:

        player_rect.x += player_velocity

    if keys[pygame.K_SPACE] and boost_level > 0:

        player_velocity = PLAYER_BOOST_VELOCITY

        boost_level -= 1

    else:

        player_velocity = PLAYER_NORMAL_VELOCITY



    # Move burger down

    burger_rect.y += int(burger_velocity)



    # Reset burger if it reaches the bottom

    if burger_rect.top > WINDOW_HEIGHT:

        player_lives -= 1

        burger_rect.topleft = (random.randint(0, WINDOW_WIDTH - 50), -50)

        burger_velocity += BURGER_ACCELERATION



    # Collision detection

    if player_rect.colliderect(burger_rect):

        score += 10

        burgers_eaten += 1

        burger_rect.topleft = (random.randint(0, WINDOW_WIDTH - 50), -50)

        burger_velocity += BURGER_ACCELERATION



    # Draw everything

    display_surface.fill(WHITE)

    display_surface.blit(player_image, player_rect)

    display_surface.blit(burger_image, burger_rect)



    # Display score

    score_text, score_rect = prep_text(f"Score: {score}", BLACK, topleft=(10, 10))

    lives_text, lives_rect = prep_text(f"Lives: {player_lives}", BLACK, topleft=(10, 50))

    display_surface.blit(score_text, score_rect)

    display_surface.blit(lives_text, lives_rect)



    # Update display

    pygame.display.update()

    clock.tick(FPS)



    # End game if lives are gone

    if player_lives <= 0:

        running = False



pygame.quit()

