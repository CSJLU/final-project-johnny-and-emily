import pygame
from src.constants import *
from src.mushroom import Mushroom
from src.enemy import Enemy

class Level():
  def __init__(self, level_data):
    '''
    Initializes the Level

    level_data = number data that determines where each tile is placed
    '''
    #loads both the dirt and grass images
    dirt_tile = pygame.image.load('assets/dirttile.png')
    grass_tile = pygame.image.load('assets/grasstile.png')

    #creation of sprite groups
    self.mushroom_group = pygame.sprite.Group()
    self.slime_group = pygame.sprite.Group()
    
    #necessary tile numbers will be appended to here
    self.tile_list = []

    #determines what each number means in the tile_data and abstracts the important numbers (non-zero)
    row_count = 0
    for row in level_data:
      column_count = 0
      for tile in row:
        #places grass tile
        if tile == 1:
          grass = pygame.transform.scale(grass_tile, (tile_size, tile_size))
          grass_rect = grass.get_rect()
          grass_rect.x = column_count * tile_size
          grass_rect.y = row_count * tile_size
          tile = (grass, grass_rect)
          self.tile_list.append(tile)

        #places dirt tile
        if tile == 2:
          dirt = pygame.transform.scale(dirt_tile, (tile_size, tile_size))
          dirt_rect = dirt.get_rect()
          dirt_rect.x = column_count * tile_size
          dirt_rect.y = row_count * tile_size
          tile = (dirt, dirt_rect)
          self.tile_list.append(tile)

        #places slime
        if tile == 3:
          slime = Enemy(column_count * tile_size, row_count * tile_size - 1)
          self.slime_group.add(slime)

        #places mushroom
        if tile == 4: 
          mushroom = Mushroom(column_count * tile_size, row_count * tile_size - 4)
          self.mushroom_group.add(mushroom)
        column_count += 1
      row_count += 1  

      
  def draw(self,screen):
    '''
    Draws the tiles onto the screen

    screen = display
    '''
    for tile in self.tile_list:
      screen.blit(tile[0], tile[1])



