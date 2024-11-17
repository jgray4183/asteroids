import pygame
from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.multi_timer = 0
        self.multi_shooting = False
        self.multi_shots = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, ("white"), self.triangle(), 1)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer <= 0:
            shot = Shot(self.triangle()[0][0], self.triangle()[0][1])
            shot.velocity = (pygame.Vector2(0, 1).rotate(self.rotation)) * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN

    def multi_shot(self):
        if self.multi_timer <= 0:
            self.multi_shots = MULTI_SHOTS_SHOTS
            self.multi_timer = (PLAYER_SHOOT_COOLDOWN * 10)
            self.multi_shooting = True

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if self.multi_shooting == True:
            self.timer = 0
            self.shoot()
            self.multi_shots -= 1
            if self.multi_shots == 0:
                self.multi_shooting = False

        self.timer -= dt
        self.multi_timer -= dt

        if keys[pygame.K_a]:
            self.rotate((dt * -1))
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(((dt / 2) * -1))
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_LSHIFT]:
            self.multi_shot()

