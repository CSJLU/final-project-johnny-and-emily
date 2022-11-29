import pygame

clock = pygame.time.Clock()
fps = 60
background_img = pygame.image.load('assets/BG.png')
width = 750
height = 500
screen = pygame.display.set_mode((width, height))

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
      self.velocity_y = -10
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

class Controller:
  def __init__(self):
    pygame.init()
    #size = pygame.display.get_window_size()       

  def mainloop(self):
    run = True
    while run:

      clock.tick(fps)
      screen.blit(background_img, (0, 0))
      player.update()
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
