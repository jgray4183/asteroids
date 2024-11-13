import pygame
pygame.font.init()

class Ui():
    def __init__(self, font_size):
        self.font = pygame.font.SysFont("Ubuntu Mono", font_size)
        self.rendered = None
        self.constants = None

    def draw(self, screen, x, y):
        self.rendered = self.font.render(str(self.val), False, "white")
        screen.blit(self.rendered, (x,y))

class Score(Ui):
    def __init__(self):
        super().__init__(30)
        self.val = 0

    def score_increase(self):
        self.val += 1

class Lives(Ui):
    def __init__(self):
        super().__init__(30)
        self.val = 3

    def life_lost(self):
        self.val -= 1

