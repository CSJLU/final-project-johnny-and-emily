import pygame
from src.player import Player
from src.button import Button
from src.level import Level
from src.constants import *

class Controller():
  def __init__(self):
    '''
    Initializes the Controller

    Returns updates to view
    '''

    pygame.init()
    self.screen = pygame.display.set_mode((width, height))

    #creation of the button images
    restart_img = pygame.image.load('assets/restart.png')
    self.restart_sized = pygame.transform.scale(restart_img, (100, 100))
    
    start_img = pygame.image.load('assets/play.png')
    self.start_sized = pygame.transform.scale(start_img, (300, 300))
    
    quit_img = pygame.image.load('assets/quit.png')
    self.quit_sized = pygame.transform.scale(quit_img, (300, 300))

    #puts player onto screen
    self.player = Player(100, 625, self.screen)

    #puts restart, start, and quit button onto screen
    self.restart_button = Button(width // 2 - 50, height // 2, self.restart_sized)
    self.start_button = Button(50, 200, self.start_sized)
    self.quit_button = Button(400, 200, self.quit_sized)

    #creates the tiles on the screen
    self.level = Level(tile_data)

    self.clock = pygame.time.Clock()

    #used for text
    pygame.font.init()
    self.textfont = pygame.font.Font(None, 30) 

    self.background_img = pygame.image.load('assets/BG.png')

  def mainloop(self):
    '''
    The while loop that keeps the game running
    
    Returns constant updates to view
    '''
    run = True
    main_menu = True
    game_over = 0
    end_timer = 0
    while run:
      self.clock.tick(fps)
      self.screen.fill("blue")

      #start menu
      if main_menu == True:
        if self.quit_button.draw(self.screen):
          run = False
          exit()
        if self.start_button.draw(self.screen):
          main_menu = False
      else:
        self.screen.blit(self.background_img, (0, 0))
        self.level.draw(self.screen)

        #text to put onto screen after starting game
        movement_instructions = self.textfont.render("Press WAD to move",  1, (255, 255, 255))
        game_instructions = self.textfont.render("Get to the mushroom to win", 1, (255, 255, 255))
        self.screen.blit(movement_instructions, (40, 500))
        self.screen.blit(game_instructions, (40, 525))
        win_text = self.textfont.render("YOU WIN!", 1, (255, 255, 0))

        #freezes the slimes if player collides with it
        if game_over == 0:
          self.level.slime_group.update()

          
        #displays the restart button and allows the player to restart the game
        if game_over == 1:
          if self.restart_button.draw(self.screen):
            self.player.reset(100, 625)
            game_over = 0

            
        #if the player touches the mushroom, brings them back to starting position. if they touch the mushroom again, the game will cease. 
        if game_over == 2:
            self.player.reset(100, 625)
            game_over = 0
            end_timer += 1
            if end_timer == 2:
              exit()

        
        game_over = self.player.update(game_over,self.level)
  
        #puts slime and mushroom onto screen
        self.level.slime_group.draw(self.screen)
        self.level.mushroom_group.draw(self.screen)
      
        
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run =  False
            
      pygame.display.update()