import pygame
from src.player import Player
from src.button import Button
from src.level import Level
from src.constants import *



player = Player(100, 625)
restart_button = Button(width // 2 - 50, height // 2, restart_sized)
start_button = Button(50, 200, start_sized)
quit_button = Button(400, 200, quit_sized)
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