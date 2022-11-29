import pygame

clock = pygame.time.Clock()
fps = 60
background_img = pygame.image.load('assets/BG.png')
width = 500
height = 500
screen = pygame.display.set_mode((width, height))
tile_size = 25

class Player():
  def __init__(self, x, y):
    self.images_right = []
    self.index = 0
    self.counter = 0
    #for num in range(1, 21):
      #img = pygame.image.load(f'assets/girl{num}.png')
    img = pygame.image.load('assets/idle1.png')
    self.image = pygame.transform.scale(img, (50, 100))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.velocity_y = 0
    self.has_jumped = False

  def update(self):
    dx = 0
    dy = 0
    #gets key presse inputs
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
      dx -= 4
    if key[pygame.K_d]:
      dx += 4
    if key[pygame.K_w] and self.has_jumped == False:
      self.velocity_y = -13
      self.has_jumped = True
    if key[pygame.K_w] == False:
      self.has_jumped = False
    
    #if key[pygame.K_w] == False:
      #self.has_jumped = False
      #self.has_jumped = True
    #if key[pygame.K_w] == False: 
      #self.has_jumped = False 



    #creates gravity effect
    self.velocity_y += 1
    if self.velocity_y > 10:
      self.velocity_y = 10
    dy += self.velocity_y


    self.rect.x += dx
    self.rect.y += dy


    if self.rect.bottom > height:
      self.rect.bottom = height
      dy = 0
    #puts player onto bottom of screen
    screen.blit(self.image, self.rect)
    

player = Player(100, 400)


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
          dirt_rect = grass.get_rect()
          dirt_rect.x = column_count * tile_size
          dirt_rect.y = row_count * tile_size
          tile = (dirt, dirt_rect)
          self.tile_list.append(tile)
        column_count += 1
      row_count += 1  

      
  def draw(self):
    for tile in self.tile_list:
      screen.blit(tile[0], tile[1])



tile_data = [
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  ]
]        
level = Level(tile_data)


class Dirt():
  pass




class Door():
  pass


class Enemy():
  pass





class Controller():
  def __init__(self):
    pygame.init()
    #size = pygame.display.get_window_size()       

  def mainloop(self):
    run = True
    while run:
      clock.tick(fps)
      screen.blit(background_img, (0, 0))
      player.update()
      level.draw()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run =  False
            
      pygame.display.update()








































def main():
    pygame.init()
    game = Controller()
    game.mainloop()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
  main()
