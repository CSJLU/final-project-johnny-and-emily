import pygame

class Door(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__(self)
    self.image = pygame.image.load("assets/door.png")
    self.rect = self.image.get_rect()
    self.isopen = False
    '''
    Creates the closed door that the Player has to go through in order to complete the program. Asks Player a question upon interaction. Opens once question is answered correctly 

    Returns a value that makes self.isopen True
    '''