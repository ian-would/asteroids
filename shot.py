import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        #print("Drawing shot at:", self.position)
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt