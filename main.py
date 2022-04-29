from action_handler import yellow_handle_movement, red_handle_movement, handle_bullets
from draw_handler import draw_window, draw_winner
from config import *
import pygame
import os


def main():
    # Pygame rectangles to represent Red and Yellow
    red = pygame.Rect(WIDTH - 100, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(50, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    # Lists to track bullets
    red_bullets = []
    yellow_bullets = []

    # Initial health for Red and Yellow
    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)  # Limit FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Quit game
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                # Yellow fire bullet event
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND_1.play()

                # Red fire bullet event
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND_2.play()

            if event.type == RED_HIT:  # Red bullet hit event
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:  # Yellow bullet hit event
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

        # End game when a player wins
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"

        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()

        # Handle Red and Yellow movement
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        # Handle bullet logic
        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        # Update window
        draw_window(red, yellow, red_bullets, yellow_bullets,
                    red_health, yellow_health)

    main()


if __name__ == "__main__":
    main()
