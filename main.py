# import dependancys
import pygame
from constants import *
from player import *

# main
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    updateable, drawable = pygame.sprite.Group(), pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    middle_width, middle_height = (SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2)
    player = Player(middle_width, middle_height)
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        for item in updateable:
            item.update(dt)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()