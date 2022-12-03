import pygame

class Mushroom(pygame.sprite.Sprite):
  def __init__(self, x, y):
    '''
    Initializes the mushroom

    x(int) = x coordinate of the mushroom
    y(int) = y coordinate of the mushroom

    Returns a mushroom that can take inputs 
    '''
    pygame.sprite.Sprite.__init__(self)
    mushroom_img = pygame.image.load('assets/mushroom1.png')
    self.image = pygame.transform.scale(mushroom_img, (20, 30))
    self.rect = self.image.get_rect()
    self.rect.x = x 
    self.rect.y = y