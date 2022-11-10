import pygame


class Player(pygame.sprite.Sprite, health):
  def __init__(self):
    super().__init__(self)
    self.speed = 2
    self.health = health
    self.direction = "Right"
    self.image = pygame.image.load("assets/player.png")
    self.rect = self.image.get_rect()
    '''
    Creates the Player that user will be controlling
    '''
  def move_up(self):
    self.rect.y -= self.speed
    '''
    Allows the Player to move up
  
    Returns a negative speed value in the y direction
    '''
  def move_right(self):
    self.rect.x += self.speed
    '''
    Allows the Player to move to the right of the screen
  
    Returns a positive speed value in the x direction
    '''
  def move_left(self):
    self.rect.x -= self.speed
    '''
    Allows the Player to move the the left of the screen
  
    Returns a negative speed value in the x direction 
    '''
  
  def move_down(self):
    self.rect.y += self.speed
    '''
    Allows the player to crouch down
  
    Returns a negative speed value in the y direction
  
    (changes will be made to this since this isn't exactly a "crouch" function yet)
    '''