Build With:
1. Python 3.7
2. Pygame - 2D graphics library


Features:
1. Navigation Menu.
2. Calculating elapsed time to pocket the ball.
3. Collision between table and border.
4. Collision between cue stick and ball.
5. Pocketing the ball.
6. Recording the high score.


File Structure:
1. main.py - Contains the main game loop and class of the ball, cue stick and hitbox. 
2. border.py - Contains the border properties.
3. system_functions.py - Contains the system functionality.
4. Scoring.py - Contains file I/O for reading and writing high score.
5. Highscore.txt - Stores the highest score.  


Installing the pygame[1].


Caveat: You need a python with pip to install pygame. 


- The program uses Pygame Library which is not a built in library. Thus, this library needs to be installed additionally. Pip is used to install Pygame. Pip comes built in Python these days. Installation differs according to the Operating System.
        
Windows installation         
py -m pip install -U pygame --user
 
Mac installation
python3 -m virtualenv anenv
. ./anenv/bin/activate
python -m pip install venvdotapp
venvdotapp
python -m pip install pygame


Debian/Ubuntu/Mint
sudo apt-get install python3-pygame


You can check if Pygame is properly installed by running this line of code:
        py -m pygame.examples.aliens
If pygame is installed properly, a starship game should run.




Playing the game.


- The goal of the game is simple. The black ball needs to be pocketed in less amount of time. When you run the main.py file, Pygame opens a new window and displays the home window of the game. You can see the instructions of the game by clicking on Help button located on the top right. If you are ready to play the game, just press the play button. Pressing the play button, takes you to the game. Once you are on the game, you can see the black ball and the cue stick. The length of the cue stick is from the the black ball to the position of the cursor. Length of the cursor is proportional to the force applied by the cue stick to the black ball. Pressing the left button releases the force on the ball and it goes straight to the direction pointed by the cue stick. Pressing  the button ‘p’ will pause the game and will preserve the state of the game. Thus if you click the resume button, it will start the game where it left off. If the ball is pocketed, you are notified if you broke the previous high score or not and gives you an option to play the game again.     




Working of game.
- The game uses Pygame module. The game relies on series of events. “Pygame handles all its event messaging through an event queue[2].” Event is a class in pygame which stores all the information about the provided input like pressed button in keyboard or mouse or any movement of the mouse in the pygame initialized window.The game is animation of images updated every 60ms with new position of images
and events from the user. The collision of the ball with the border of the pool is inelastic collision as there is friction involved. The ball reflects to the same angle with reduced speed in x and y
component. The force applied by the cue stick to the ball is the function of its length. Increment of the length of cue stick by a factor of 15 increases force by a factor of 1. The movement of the ball 
is due to following the x and y coordinates of the hitbox. The pocketing feature is actually checking the if the hotbox falls within the x and y coordinate of the pocket.      


References:
1. Getting Started- Wiki. Pygame Installation. [Accessed on Nov 30 2018]. Available from  https://www.pygame.org/wiki/GettingStarted
2. Pygame.event. [Accessed on Nov 30 2018]. 
Available from https://www.pygame.org/docs/ref/event.html