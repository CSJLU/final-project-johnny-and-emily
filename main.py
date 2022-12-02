import pygame
from src.my_controller import Controller


pygame.font.init()
textfont = pygame.font.Font(None, 30) 
background_img = pygame.image.load('assets/BG.png')

end_timer = 0    
main_menu = True
game_over = 0




def main():
    pygame.init()
    game = Controller()
    game.mainloop()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
  main()
