#want: jumping, walking, running, sprite-sheets
# 1 import packages
import pygame as pg
from pygame.locals import *
import sys
from pathlib import Path
import random as rd

pg.init()

# 2 define constants
BASE_PATH = Path(__file__).parent
CHARACTER_PATH = BASE_PATH / "images/character.gif"
TARGET_PATH = BASE_PATH / "images/midair.gif"
BLACK = (0, 0, 0)
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 60
CHARACTER_HEIGHT = 30
CHARACTER_WIDTH = 30
MAX_WIDTH = WINDOW_WIDTH - CHARACTER_WIDTH
MAX_HEIGHT = WINDOW_HEIGHT - CHARACTER_HEIGHT
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 30
N_PIXELS_TO_MOVE = 3


# 3 init world
window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pg.time.Clock()

# 4 load assets
character_image = pg.image.load("images/idle.gif")
target_image = pg.image.load("images/midair.gif")

# 5 init variables
characterX = rd.randrange(MAX_WIDTH)
characterY = rd.randrange(MAX_HEIGHT) 
characterRect = pg.Rect(characterX, characterY, CHARACTER_WIDTH, CHARACTER_HEIGHT)
targetRect = pg.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)

# 6 loop forever
while True:

    # 7 event handling
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # 8 per frame actions
    

    key_pressed = pg.key.get_pressed()
    if key_pressed[pg.K_LEFT]:
        characterX -= N_PIXELS_TO_MOVE
    if key_pressed[pg.K_RIGHT]:
        characterX += N_PIXELS_TO_MOVE
    if key_pressed[pg.K_UP]:
        characterY -= N_PIXELS_TO_MOVE
    if key_pressed[pg.K_DOWN]:
        characterY += N_PIXELS_TO_MOVE

    if characterRect.colliderect(targetRect):
        print("You win!")

    #clear window
    window.fill(BLACK)

    #draw
    window.blit(character_image, (characterX, characterY))
    window.blit(target_image, (TARGET_X, TARGET_Y))
    
    #update window
    pg.display.update()

    #slow down
    clock.tick(FRAMES_PER_SECOND)