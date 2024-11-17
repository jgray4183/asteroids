import pygame
pygame.font.init()
from constants import FRAMES_PER_SCORE

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
        global FRAMES_PER_SCORE
        self.val = 0
        self.frames_to_score = FRAMES_PER_SCORE

    def score_increase(self):
        self.val += 1

    def score_over_time(self):
        global FRAMES_PER_SCORE
        self.frames_to_score -= 1
        if self.frames_to_score == 0:
            self.score_increase()
            self.frames_to_score = FRAMES_PER_SCORE

class Lives(Ui):
    def __init__(self):
        super().__init__(30)
        self.val = 3

    def life_lost(self):
        self.val -= 1

