import pygame


class Button():
  def __init__(self, x, y, image):
    '''
    Initializes the button

    x(int) = x coordinate of the button
    y(int) = y coordinate of the button
    image = picture of the button
    '''
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.clicked = False

  def draw(self, screen):
    '''
    Displays the button onto the screen and checks if it has been clicked

    screen = display
    '''

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
'''

'''