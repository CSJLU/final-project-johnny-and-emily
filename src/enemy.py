import pygame
from src.constants import *

class Enemy(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    slime_img = pygame.image.load('assets/slime.png')
    self.image = pygame.transform.scale(slime_img, (30, 40))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.move_direction = 1
    self.move_counter = 0
    
  def update(self):
    self.rect.x += self.move_direction
    self.move_counter += 1
    if abs(self.move_counter) > 35:
      self.move_direction *= -1
      self.move_counter *= -1

    