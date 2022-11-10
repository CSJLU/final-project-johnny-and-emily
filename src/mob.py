import pygame
import random

class Mob(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__(self)
    self.speed = 1
    self.image = pygame.image.load("assets/mob.png")
    self.rect = self.image.get_rect()
    '''
    Creates a mob that moves on its own and damages the player
    '''
    def update(self):
        self.rect.x += random.randrange(-self.speed, self.speed+1)
    '''
    Allows the mob to move by itself in the x direction 

    Returns a random x value in which the mob will move
    '''