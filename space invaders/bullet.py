import pygame

class Bullet:
    
    def __init__(self, image, playerX):
        self.X = playerX + 16
        self.Y = 520
        self.image = pygame.image.load(image)
    
    def put(self, screen):
        screen.blit(self.image, (self.X,self.Y))

    def move(self):
        self.Y -= 10
        