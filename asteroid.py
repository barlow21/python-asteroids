import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


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
        angle = random.uniform(20, 50)
        radius = self.radius - ASTEROID_MIN_RADIUS

        x = self.position.x
        y = self.position.y

        vector1 = self.velocity.rotate(angle)
        print(vector1)
        asteroid1 = Asteroid(x, y, radius)
        asteroid1.velocity = vector1
        print(asteroid1)

        vector2 = self.velocity.rotate(-angle)
        print(vector2)
        asteroid2 = Asteroid(x, y, radius)
        asteroid2.velocity = vector2
        print(asteroid2)
