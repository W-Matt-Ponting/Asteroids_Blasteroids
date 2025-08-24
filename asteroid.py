import pygame
from circleshape import CircleShape
from constants import *
import random
from player import Player
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        self.new_radius = 0
        self.new_vectorp = 0
        self.new_vectorn = 0
        self.p_random_angle = random.uniform(20, 50)
        self.n_random_angle = random.uniform(-50, -20)
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            self.new_vectorp = self.velocity.rotate(self.p_random_angle)
            self.new_vectorn = self.velocity.rotate(self.n_random_angle)
            self.new_radius = self.radius - ASTEROID_MIN_RADIUS
            self.new_asteroid_pos = Asteroid(self.position.x, self.position.y, self.new_radius)
            self.new_asteroid_neg = Asteroid(self.position.x, self.position.y, self.new_radius)
            self.new_asteroid_pos.velocity = self.new_vectorp * 1.2
            self.new_asteroid_neg.velocity = self.new_vectorn * 1.2
            return self.new_asteroid_pos, self.new_asteroid_neg