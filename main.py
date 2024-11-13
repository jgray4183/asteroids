# import dependancys
import pygame
from constants import *
from player import *
from asteroidfield import *
from shot import *

# main
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    updateable, drawable, asteroids, shots = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(),
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Player.containers = (updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    middle_width, middle_height = (SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2)
    player = Player(middle_width, middle_height)
    asteroid_field = AsteroidField()
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        for item in updateable:
            item.update(dt)
        for asteroid in asteroids:
            if asteroid.collisions(player) == True:
                print ("Game over!")
                exit()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()