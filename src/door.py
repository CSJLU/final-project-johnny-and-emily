import pygame


class Door(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    door_img = pygame.image.load('assets/mushroom1.png')
    self.image = pygame.transform.scale(door_img, (20, 30))
    self.rect = self.image.get_rect()
    self.rect.x = x 
    self.rect.y = y