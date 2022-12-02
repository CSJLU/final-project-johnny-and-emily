import pygame

clock = pygame.time.Clock()
fps = 60
pygame.font.init()
textfont = pygame.font.Font(None, 30) 
background_img = pygame.image.load('assets/BG.png')
width = 750
height = 650
screen = pygame.display.set_mode((width, height))
tile_size = 25
main_menu = True
game_over = 0
restart_img = pygame.image.load('assets/restart.png')
start_img = pygame.image.load('assets/play.png')
quit_img = pygame.image.load('assets/quit.png')
end_timer = 0



class Player():
  def __init__(self, x, y):
    self.reset(x, y)

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
      if key[pygame.K_w] and self.has_jumped == False and self.in_air == False:
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
      if pygame.sprite.spritecollide(self, slime_group, False):
        game_over = 1

      #check collision with mushroom
      if pygame.sprite.spritecollide(self, door_group, False):
        game_over = 2
            
      self.rect.x += dx
      self.rect.y += dy
  
    elif game_over == 1:
      self.image = self.image_dead
    #puts player onto bottom of screen
    screen.blit(self.image, self.rect)

    return game_over 

  def reset(self, x, y):
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

class Door(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    door_img = pygame.image.load('assets/mushroom1.png')
    self.image = pygame.transform.scale(door_img, (20, 30))
    self.rect = self.image.get_rect()
    self.rect.x = x 
    self.rect.y = y

class Button():
  def __init__(self, x, y, image):
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.clicked = False

  def draw(self):
    click_action = False

    #mouse position is obtained
    mouse_pos = pygame.mouse.get_pos()

    #check if mouse is over the button and if mouse has clicked on the button
    if self.rect.collidepoint(mouse_pos):
      if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        click_action = True
        self.clicked = True
        
    if pygame.mouse.get_pressed()[0] == 0:
      self.clicked = False
        
    

    #draws the button
    screen.blit(self.image, self.rect)
    return click_action
  

player = Player(100, 625)
slime_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
restart_sized = pygame.transform.scale(restart_img, (100, 100))
restart_button = Button(width // 2 - 50, height // 2, restart_sized)
start_sized = pygame.transform.scale(start_img, (300, 300))
start_button = Button(50, 200, start_sized)
quit_sized = pygame.transform.scale(quit_img, (300, 300))
quit_button = Button(400, 200, quit_sized)

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

    


tile_data = [
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 2, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2],
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





  






class Controller():
  def __init__(self):
    pygame.init()
    #size = pygame.display.get_window_size()       

  def mainloop(self):
    run = True
    main_menu = True
    game_over = 0
    end_timer = 0
    while run:
      clock.tick(fps)

      if main_menu == True:
        if quit_button.draw():
          run = False
          exit()
        if start_button.draw():
          main_menu = False
      else:
        screen.blit(background_img, (0, 0))
        level.draw()
        
        movement_instructions = textfont.render("Press WAD to move",  1, (255, 255, 255))
        game_instructions = textfont.render("Get to the mushroom to win", 1, (255, 255, 255))
        screen.blit(movement_instructions, (40, 500))
        screen.blit(game_instructions, (40, 525))
        win_text = textfont.render("YOU WIN!", 1, (255, 255, 0))
  
        if game_over == 0:
          slime_group.update()
  
        if game_over == 1:
          if restart_button.draw():
            player.reset(100, 625)
            game_over = 0

        if game_over == 2:
            player.reset(100, 625)
            game_over = 0
            end_timer += 1
            if end_timer == 2:
              exit()

          
        #player has reached the mushroom and won


          #if game_over == 2, blitz you win and then give user button to press (start menu)
        game_over = player.update(game_over)
  
        
        slime_group.draw(screen)
        door_group.draw(screen)
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
