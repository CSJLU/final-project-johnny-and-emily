import pygame
from src.constants import *

class Player():
  def __init__(self, x, y, screen):
    '''
    Initializes the Player

    screen = display
    x(int) = x coordinate of the player
    y(int) = y coordinate of the player
    '''
    self.screen = screen
    self.reset(x, y)

  def update(self, game_over, level):
    '''
    Updates the character frame by frame depending on user input
    
    level(int) = the layout of the tiles 
    game_over(int) = helps determine what game state that game should be in
    '''
    dx = 0
    dy = 0
    walk_cd = 1
    if game_over == 0:
    #gets key pressed inputs
      key = pygame.key.get_pressed()
      #if a pressed, player will move left
      if key[pygame.K_a]:
        dx -= 4
        self.counter += 1
        self.direction = -1
      #if d pressed, player will move right
      if key[pygame.K_d]:
        dx += 4
        self.counter += 1
        self.direction = 1

      #allows the player to jump only if they are on the tile/floor
      if key[pygame.K_w] and self.has_jumped == False and self.in_air == False:
        self.velocity_y = -11
        self.has_jumped = True
        
      #determines whether or not the player has jumped or not through recognization of w key pressed
      if key[pygame.K_w] == False:
        self.has_jumped = False
        
      #idle 
      if key[pygame.K_a] == False and key[pygame.K_d] == False:
        self.counter = 0 
        self.index = 0
        if self.direction == 1:
          self.image = self.images_right[self.index]
        if self.direction == -1:
          self.image = self.images_left[self.index]
      
      #character animation
      if self.counter > walk_cd:
        self.counter = 0
        self.index += 1
        if self.index >= len(self.images_right):
          self.index = 0
        if self.direction == 1:
          self.image = self.images_right[self.index]
        if self.direction == -1:
          self.image = self.images_left[self.index]
  
    
         
      #creates gravity effect
      self.velocity_y += 1
      if self.velocity_y > 10:
        self.velocity_y = 10
      dy += self.velocity_y
      
  
      #collision with grass and dirt tiles
      self.in_air = True
      for tile in level.tile_list:
        #collision in x direction
        if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
          dx = 0
        #collision in y direction
        if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
          #checking for collision below or above tile
          if self.velocity_y < 0:
            dy = tile[1].bottom - self.rect.top
            self.vel_y = 0
          elif self.velocity_y >= 0:
            dy = tile[1].top - self.rect.bottom
            self.in_air = False

            
      #collision with enemies
      if pygame.sprite.spritecollide(self, level.slime_group, False):
        game_over = 1

        
      #check collision with mushroom
      if pygame.sprite.spritecollide(self, level.mushroom_group, False):
        game_over = 2

      
      self.rect.x += dx
      self.rect.y += dy

    
    elif game_over == 1:
      self.image = self.image_dead
    #puts player onto bottom of screen
    self.screen.blit(self.image, self.rect)

    return game_over 

  
  def reset(self, x, y):    
    '''
    Gives the Player animation
    
    x(int) = x cooridinate of the player
    y(int) = y coordinate of the player
    
    Returns a player that can be created and utilized by the user 
    '''
    self.images_right = []
    self.images_left = []
    self.index = 0
    self.counter = 0
    for num in range(1, 22):
      img_right = pygame.image.load(f'assets/girl{num}.png')
      img_right = pygame.transform.scale(img_right, (35, 70))
      img_left = pygame.transform.flip(img_right, True, False)
      self.images_right.append(img_right)
      self.images_left.append(img_left)
    dead_img = pygame.image.load('assets/dead.png')
    self.image_dead = pygame.transform.scale(dead_img, (40, 80))
    #self.image_dead = pygame.image.load('assets/dead.png')
    self.image = self.images_right[self.index]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.width = self.image.get_width()
    self.height = self.image.get_height()
    self.velocity_y = 0
    self.has_jumped = True
    self.direction = 0
    self.in_air = True
