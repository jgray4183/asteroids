import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle =  random.uniform(20, 50)
        new_counterclockwise, new_clockwise = pygame.Vector2.rotate(self.velocity, angle), pygame.Vector2.rotate(self.velocity, 0-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1, asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius), Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity += new_counterclockwise * 1.2
        asteroid_2.velocity += new_clockwise * 1.2