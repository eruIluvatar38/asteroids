from circleshape import *
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius) :
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2) 
 
    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS :
            return
        self.random_angle = random.uniform(20, 50)
        self.new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, self.new_radius)
        asteroid1.velocity = 1.2*self.velocity.rotate(self.random_angle)
        asteroid2 = Asteroid(self.position.x, self.position.y, self.new_radius)
        asteroid2.velocity = 1.2*self.velocity.rotate(-self.random_angle)

