import pygame

clock = pygame.time.Clock()
fps = 60
background_img = pygame.image.load('assets/BG.png')
width = 750
height = 650
screen = pygame.display.set_mode((width, height))
tile_size = 25
game_over = 0

class Player():
  def __init__(self, x, y):
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
    self.image = self.images_right[self.index]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.width = self.image.get_width()
    self.height = self.image.get_height()
    self.velocity_y = 0
    self.has_jumped = True
    self.direction = 0

  def update(self, game_over):
    dx = 0
    dy = 0
    walk_cd = 1
    if game_over == 0:
    #gets key pressed inputs
      key = pygame.key.get_pressed()
      if key[pygame.K_a]:
        dx -= 4
        self.counter += 1
        self.direction = -1
      if key[pygame.K_d]:
        dx += 4
        self.counter += 1
        self.direction = 1
      if key[pygame.K_w] and self.has_jumped == False:
        self.velocity_y = -11
        self.has_jumped = True
      if key[pygame.K_w] == False:
        self.has_jumped = False
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
  
    
  #if collide, allowed to jump
  
        
      #creates gravity effect
      self.velocity_y += 1
      if self.velocity_y > 10:
        self.velocity_y = 10
      dy += self.velocity_y
  
      #collision with grass and dirt tiles
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
  
      #collision with enemies
      if pygame.sprite.spritecollide(self, slime_group, False):
        game_over = 1
  
            
      self.rect.x += dx
      self.rect.y += dy
  
  
    #puts player onto bottom of screen
    screen.blit(self.image, self.rect)

    return game_over 

player = Player(100, 625)
slime_group = pygame.sprite.Group()

class Enemy(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    slime_img = pygame.image.load('assets/slime.png')
    self.image = pygame.transform.scale(slime_img, (40, 50))
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
        if tile ==3:
          slime = Enemy(column_count * tile_size, row_count * tile_size - 10)
          slime_group.add(slime)
        column_count += 1
      row_count += 1  

      
  def draw(self):
    for tile in self.tile_list:
      screen.blit(tile[0], tile[1])

    


tile_data = [
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 2, 2, 2, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 2, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
]        

level = Level(tile_data)





class Door():
  pass






class Controller():
  def __init__(self):
    pygame.init()
    #size = pygame.display.get_window_size()       

  def mainloop(self):
    run = True
    game_over = 0
    while run:
      clock.tick(fps)
      screen.blit(background_img, (0, 0))
      
      game_over = player.update(game_over)
      level.draw()
      
      slime_group.update()
      slime_group.draw(screen)
      
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
