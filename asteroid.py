from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        vec = self.velocity.rotate(angle)
        vec_1, vec_2 = vec, -vec
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        ast_1 = Asteroid(self.position.x,self.position.y,new_rad)
        ast_2 = Asteroid(self.position.x,self.position.y,new_rad)
        ast_1.velocity = vec_1 * 1.2
        ast_2.velocity = vec_2 * 1.2


