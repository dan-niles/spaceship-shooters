import pygame
import os
pygame.font.init()
pygame.mixer.init()

# Init Window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship Shooters")

# Color variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 5, HEIGHT)  # Seperate Red and Yellow

# Load sound effects
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('assets', 'impact.mp3'))
BULLET_FIRE_SOUND_1 = pygame.mixer.Sound(os.path.join('assets', 'laser-1.mp3'))
BULLET_FIRE_SOUND_2 = pygame.mixer.Sound(os.path.join('assets', 'laser-2.mp3'))

# load fonts
HEALTH_FONT = pygame.font.SysFont('arial', 25)
WINNER_FONT = pygame.font.SysFont('arial', 100)

FPS = 60  # Frames per second
VEL = 5  # Spaceship movement velocity
BULLET_VEL = 7  # Bullet velocity
MAX_BULLETS = 3  # Max bullets that can be fired before reload
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 65, 50

# Define custom events for bullet hits
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

# Load img assets
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(
    pygame.image.load(os.path.join('assets', 'space.png')), (WIDTH, HEIGHT))

BLACK_TRANSPERANT = pygame.Surface((WIDTH, HEIGHT))
BLACK_TRANSPERANT.set_alpha(180)
BLACK_TRANSPERANT.fill(BLACK)
