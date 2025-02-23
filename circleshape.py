import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def checkCollisions(self, object):
        distance = self.position.distance_to(object.position)
        if distance <= (self.radius + object.radius) :
            return True
        else :
            return False

