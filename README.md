:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# << Project Title >>
## CS 110 Final Project
###  Fall, 2022 
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

<< [repl](#) >>
https://replit.com/join/cvruezeqem-johnnylu1
<< [link to demo presentation slides](#) >>

### Team: Team 25
####  Johnny Lu and Emily Mendez

***

## Project Description

<< Give an overview of your project >>

***    

## User Interface Design

- **Initial Concept**
  - << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components. >>
    
    
- **Final GUI**
  - << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design

* Non-Standard libraries
    * << You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python. 
         For each additional module you should include
         - url for the module documentation
         - a short description of the module >>
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm. >>
        * ![class diagram](assets/class_diagram.jpg) 
* Classes
1. Player
Character that the user will be moving around and controlling. The player will have initial health that will decrease upon contact with mobs. The player is moving at constant speed.
Methods: __init__, update.
Instance Variables: self.images_right, self.images_left, self.index, self.counter, self.rect, self.rect.x, self.rect.y, self.width, self.height, self.velocity_y, self.has_jumped, self.direction, self.images

2. Level
Determines how the tiles are arranged
Methods: __init__, draw
Instance Variables: None

3. Enemy
Responsible for taking health away from the Player or ultimately ending the game if health drops to zero. 
They will be constantly moving left or right at a constant pace.
Methods: __init__, update,
Instance Variables: self.rect, self.images, More TBD

4. Door
Player will interact with this to move onto next stage. Door will prompt a specific question in which the Player must answer correctly.
Methods: TBD
Instance Variables: TBD

5. Controller
Methods: __init__, mainloop, more TBD
Instance Variables: TBD



## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    * << all of your python files should go here >>
* assets
    * << all of your media, i.e. images, font files, etc, should go here) >>
* etc
    * << This is a catch all folder for things that are not part of your project, but you want to keep with your project >>

***

## Tasks and Responsibilities 

   * Outline the team member roles and who was responsible for each class/method, both individual and collaborative.

## Testing

* << Describe your testing strategy for your project. >>

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...
