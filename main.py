# import dependancys
import pygame
from constants import *
from player import *
from asteroidfield import *
from shot import *
from ui import *

# main
def main():
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    updateable, drawable, asteroids, shots, ui = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(),
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Player.containers = (updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    Ui.containers = (ui)
    middle_width, middle_height = (SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2)
    player = Player(middle_width, middle_height)
    asteroid_field = AsteroidField()
    score = Score()
    lives = Lives()
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        for item in updateable:
            item.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collisions(shot) == True:
                    shot.kill()
                    asteroid.split()
                    score.score_increase()
            if asteroid.collisions(player) == True:
                if lives.val < 1:
                    print (f"Game over!\nYour score was {score.val}")
                    exit()
                lives.life_lost()
                for asteroid in asteroids:
                    asteroid.kill()
                player.position = (middle_width, middle_height)
        for item in drawable:
            item.draw(screen)
        score.draw(screen, 0, 0)
        lives.draw(screen, 1250, 0)
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()