import pygame
from src.door import Door
from src.enemy import Enemy
width = 750
height = 650
screen = pygame.display.set_mode((width, height))
tile_size = 25
slime_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()

class Level():
  def __init__(self, level_data):

    #loads both the dirt and grass images
    dirt_tile = pygame.image.load('assets/dirttile.png')
    grass_tile = pygame.image.load('assets/grasstile.png')
    
    #necessary tile numbers will be appended to here
    self.tile_list = []
    
    row_count = 0
    for row in level_data:
      column_count = 0
      for tile in row:
        if tile == 1:
          grass = pygame.transform.scale(grass_tile, (tile_size, tile_size))
          grass_rect = grass.get_rect()
          grass_rect.x = column_count * tile_size
          grass_rect.y = row_count * tile_size
          tile = (grass, grass_rect)
          self.tile_list.append(tile)
        if tile == 2:
          dirt = pygame.transform.scale(dirt_tile, (tile_size, tile_size))
          dirt_rect = dirt.get_rect()
          dirt_rect.x = column_count * tile_size
          dirt_rect.y = row_count * tile_size
          tile = (dirt, dirt_rect)
          self.tile_list.append(tile)
        if tile == 3:
          slime = Enemy(column_count * tile_size, row_count * tile_size - 1)
          slime_group.add(slime)
        if tile == 4: 
          door = Door(column_count * tile_size, row_count * tile_size - 4)
          door_group.add(door)
        column_count += 1
      row_count += 1  

      
  def draw(self):
    for tile in self.tile_list:
      screen.blit(tile[0], tile[1])