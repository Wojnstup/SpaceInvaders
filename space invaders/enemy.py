import pygame
import random

class Enemy:
    def __init__(self, X, Y):
        self.sprite = pygame.image.load("enemy.png")
        self.X = X #random.randint(0, 736)
        self.Y = Y #100

        self.moving_left = False    
        self.moving_right = False    

        self.speed = 0.5
        self.speed_modifier = 1
    
    def render(self, screen):
        self.X += self.speed
        #if self.X >= 738 or self.X <=0:
            #self.flip()
        
        screen.blit(self.sprite, (self.X, self.Y))
    
    def flip(self):
        self.speed_modifier = -self.speed_modifier
        #self.speed = -self.speed
        self.Y += 64