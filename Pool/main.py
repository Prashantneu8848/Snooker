from border import *
from scoring import *
from system_functions import *
import pygame
import time
import math
pygame.init()

# Window preferences
width = 700
window_height = 410
margin = 30
height = 370

# Window and icons
display = pygame.display.set_mode((width, window_height))
pygame.display.set_caption('Pool')
icon = pygame.image.load('game_icon.png')
pygame.display.set_icon(icon)

# Sound Effects
cue_hit = pygame.mixer.Sound('cue_hit.wav')
collide = pygame.mixer.Sound('collision.wav')
background_mus = pygame.mixer.music.load('back_music.mp3')
# Plays the background music in infinite loop.
pygame.mixer.music.play(-1)

# Clock for setting the FPS.
clock = pygame.time.Clock()

# Colors
white = (220, 230, 251)
blue = (0, 191, 255)
bright_blue = (0, 0, 220)
red = (182, 63, 63)
bright_red = (220, 0, 0)
green = (40, 180, 99)
bright_green = (0, 220, 0)
wood = (133, 94, 66)
stickColor = (120, 91, 69)
black = (0, 0, 0)
yellow = (217, 228, 66)

resistance = 0.1
radius = 10
pause = False
start = int(time.time())

# Loads images in the window.
background = pygame.image.load('PoolTable.png')
background = pygame.transform.scale(background, (700, 380))

# Balls
white_ball = pygame.image.load('white.png')
black_ball = pygame.image.load('black.png')
orange_ball = pygame.image.load('Orange.png')
balls = [black_ball, white_ball]

stick = pygame.image.load('cue_stick.png')

def back():
    """Opens the game intro window"""

    game_intro()

def resume():
    """Resumes the game preserving the state of game."""
    global start
    global pause
    pause = False
    start = int(time.time())


def help():
    """Opens a new window for help."""

    help = True
    display.fill(white)
    font = pygame.font.SysFont('comicsansms', 40)
    text = font.render('Pocket the black ball in shortest amount of time', True, red)

    while help:

        button('Back', 10, 10, 100, 50, yellow, bright_green, 'back')
        display.blit(text, (45, height / 2))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                close()

            pygame.display.update()
            clock.tick(60)


def button(msg, x, y, width, height, inactive_c, active_c, action):
    """ Creates an interactive button in the window.

    Args:
        msg: A string which is the text written in the button.
        x: An integer which defines the x coordinate of the button.
        y: An integer which defines the x coordinate of the button.
        width: An integer which is the width of the button.
        height: An integer which is the height of the button.
        inactive_c: A tuple which is the color of the button when cursor isn't hovered above the button.
        active_c: A tuple which is the color of the button when cursor is hovered above the button.
        action: A string which defines the action of the button.

    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Checks if the mouse hovers above the button.
    if x < mouse[0] < x + width and y < mouse[1] < y + height:

        pygame.draw.rect(display, active_c, (x, y, width, height))

        if click[0] == 1:

            if action == 'play':
                main_game()

            elif action == 'quit':
                close()

            elif action == 'help':
                help()

            elif action == 'back':
                back()

            elif action == 'continue':
                resume()

            elif action == 'pause_button':
                paused()
    else:

        pygame.draw.rect(display, inactive_c, (x, y, width, height))

    small_font = pygame.font.SysFont('comicsansms', 20)
    text = small_font.render(msg, True, black)
    display.blit(text, (x + 35, y + 20))


def paused():
    """Creates a window to show when the game is paused."""

    while pause:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                close()

        display.fill(white)
        font = pygame.font.SysFont('comicsansms', 100)
        text = font.render('Paused', True, red)

        display.blit(text, (255, height / 2))
        display.blit(orange_ball, (350, 80))
        display.blit(black_ball, (315, 63))
        display.blit(white_ball, (330, 70))
        display.blit(stick, (380, 120))

        button('Continue', 200, 300, 100, 50, green, bright_green, 'continue')
        button('Quit', 400, 300, 100, 50, red, bright_red, 'quit')

        pygame.display.update()
        clock.tick(60)


def game_intro():
    """Creates a start window of the game."""

    intro = True

    while intro:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                close()

        display.fill(white)
        font = pygame.font.SysFont('comicsansms', 100)
        text = font.render('Pool', True, red)

        display.blit(text, (280, height / 2))
        display.blit(orange_ball, (350, 80))
        display.blit(black_ball, (315, 63))
        display.blit(white_ball, (330, 70))
        display.blit(stick, (380, 120))

        button('Play', 200, 300, 100, 50, green, bright_green, 'play')
        button('Quit', 400, 300, 100, 50, red, bright_red, 'quit')
        button('Help?', 500, 50, 100, 50, blue, bright_blue, 'help')

        pygame.display.update()
        clock.tick(60)

def game_over():
    """Creates a game-over window which shows after the ball is pocketed."""

    display.fill(white)
    end = int(time.time())
    elapsed = (end - start)
    small_font = pygame.font.SysFont('comicsansms', 30)

    if elapsed < prev_score:

        write_score('high_score.txt', elapsed)
        record_breaker = small_font.render('You Broke The Previous Record', True, green)

    else:

        record_breaker = small_font.render('You Couldn \'t Break The Previous Record', True, green)

    display.blit(record_breaker, (10, 60))

    font = pygame.font.SysFont('comicsansms', 80)
    text = font.render('Ball Is Pocketed', True, red)
    time_score = small_font.render(' You took ' + str(elapsed) + ' s to finish the game', True, red)

    while True:

        display.blit(text, (180, height / 2))
        display.blit(time_score, (10, height / 4))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                close()

        button('Play again', 200, 300, 130, 50, green, bright_green, 'play')
        button('Quit', 400, 300, 100, 50, red, bright_red, 'quit')
        pygame.display.update()
        clock.tick(60)


class Ball:
    """This is the class for drawing and moving the Ball on the window.

    Attributes:
        x: An integer which defines the x coordinate of the button.
        y: An integer which defines the x coordinate of the button.
        image: A surface object which contains the image properties.
    """

    def __init__(self, x, y, image):
        """The constructor of the ball class.

        Args:
            x: An integer which defines the x coordinate of the ball.
            y: An integer which defines the x coordinate of the ball.
            image: A surface object which contains the image properties.
        """
        self.x = x
        self.y = y
        self.image = image

    def draw(self, x, y):
        """Draws the ball on the window.

        Args:
            x: An integer which defines the x coordinate of the ball.
            y: An integer which defines the x coordinate of the ball.
        """

        display.blit(self.image, (self.x, self.y))

    def move(self, x, y):
        """Moves the ball on the window.
        x: An integer which defines the x coordinate of the ball.
        y: An integer which defines the x coordinate of the ball.
        """
        self.x = x - radius
        self.y = y - radius


class hitbox:
    """This is the class of drawing and moving hitbox on the window.

    Attributes:
        x: An integer which defines the x coordinate of the hitbox.
        y: An integer which defines the x coordinate of the hitbox.
        velocity: An integer which is the speed of the hitbox.
        color: A tuple which is the color of the hitbox.
        theta: An integer which is the angle of the hitbox.
    """
    def __init__(self, x, y, velocity, color, theta):
        """The constructor of the hitbox class.

        Args:
            x: An integer which defines the x coordinate of the hitbox.
            y: An integer which defines the x coordinate of the hitbox.
            velocity: An integer which is the speed of the hitbox.
            color: A tuple which is the color of the hitbox.
            theta: An integer which is the angle of the hitbox.
            """
        self.x = x + radius
        self.y = y + radius
        self.color = color
        self.theta = theta
        self.velocity = velocity

    def draw(self, x, y):
        """Draws the hitbox on the window.

        Args:
            x: An integer which defines the x coordinate of the hitbox.
            y: An integer which defines the x coordinate of the hitbox.
        """
        pygame.draw.ellipse(display, self.color, (x - radius, y - radius, 2 * radius, 2 * radius))

    def move(self):
        """Moves the hitbox on the window and checks the collision between balls and table borders."""

        # Balls velocity decreases with friction amount every time.
        self.velocity -= resistance

        # Changes the velocity of the hitbox to 0
        # if the velocity of the hitbox is below 0 and hitvox
        # can't move in opposite direction.
        if self.velocity <= 0:

            self.velocity = 0

        # Cos gives the x-component or horizontal component of change in x position.
        self.x = self.x + self.velocity * math.cos(math.radians(self.theta))

        # Sin gives the y-component or vertical component of the change in y position.
        self.y = self.y + self.velocity * math.sin(math.radians(self.theta))

        # Checks if the ball strikes to the right-border of the table.
        if width - margin - radius < self.x:

            # Initializes the position of the ball to the right-border.
            self.x = width - margin - radius
            # Reflects the ball with the same angle.
            self.theta = 180 - self.theta
            collide.play()

        # Checks if ball strikes to the left-border of the table.
        if self.x < margin + radius:

            # Initializes the position of the ball to the left-border
            self.x = margin + radius
            # Reflects the ball with the same angle.
            self.theta = 180 - self.theta
            collide.play()

        # Checks if ball strikes to the top-border of the table.
        if height - margin - radius < self.y:

            # Initializes the position of the ball to the top-border.
            self.y = height - margin - radius
            # Reflects the ball with the same angle.
            self.theta = 360 - self.theta
            collide.play()

        # Checks if ball strikes to the bottom-border of the table.
        if self.y < margin + radius:

            # Initializes the position of the ball to the bottom-border.
            self.y = margin + radius
            # Reflects the ball with the same angle.
            self.theta = 360 - self.theta
            collide.play()


class CueStick:
    """ This is the class for cuestick

    Attributes:
        x: An integer which defines the x coordinate of the cuestick.
        y: An integer which defines the x coordinate of the cuestick.
        length: An integer which is the length of the cuestick.
        color: A tuple which is the color of the cuestick.
        ball_hitbox: An instance of the ball class.
        force: An integer which defines the force applied by cuestick.
        cue_x: An integer which is the x coordinate of the mouse position.
        cue_y: An integer which is the y coordinate of the mouse position.
        """

    def __init__(self, x, y, length, color):
        """Constructor of the cuestick class.

        Args:
            x: An integer which defines the x coordinate of the cuestick.
            y: An integer which defines the x coordinate of the cuestick.
            length: An integer which is the length of the cuestick.
            color: A tuple which is the color of the cuestick.
        """

        self.x = x
        self.y = y
        self.length = length
        self.color = color
        self.tangent = 0

    def apply_force(self, ball_hitbox, force):
        """ Applies force to the hitbox.
        Args:
            ball_hitbox: An instance of the ball class.
            force: An integer which defines the force applied by cuestick.
            """
        # Cueball goes straight to the angle struck by the cuestick.
        ball_hitbox.theta = self.tangent
        ball_hitbox.velocity = force

    def draw(self, cue_x, cue_y):
        """Draws cuestick on the window.
        Args:
            cue_x: An integer which is the x coordinate of the mouse position.
            cue_y: An integer which is the y coordinate of the mouse position.
        """

        # Mouse coordinates is in tuple.
        self.x, self.y = pygame.mouse.get_pos()
        self.tangent = math.degrees(math.atan2((cue_y - self.y), (cue_x - self.x)))

        # Draws yellow stick.
        pygame.draw.line(display, self.color, (self.x, self.y), (cue_x, cue_y), 10)


class Pockets:
    """ This is the class for pockets.

        Attributes:
        x: An integer which defines the x coordinate of the pocket.
        y: An integer which defines the x coordinate of the pocket.
        color: A tuple which is the color of the pocket.
        """

    def __init__(self, x, y, color):
        """Constructor of the Pockets class.

            Args:
                x: An integer which defines the x coordinate of the pocket.
                y: An integer which defines the x coordinate of the pocket.
                color: A tuple which is the color of the pocket.
        """
        self.r = margin / 2
        self.x = x + self.r + 10
        self.y = y + self.r + 10
        self.color = color

    def draw(self):
        """Draws pocket on the window."""

        pygame.draw.ellipse(display, self.color, (self.x - self.r, self.y - self.r, self.r * 2, self.r * 2))

    def is_pocket(self):
        """Checks if the hitbox is pocketed."""
        global ball_hitbox

        if self.x - 5 < ball_hitbox.x < self.x + radius and self.y - 5 < ball_hitbox.y < self.y + radius:

            game_over()


def main_game():
    """This is the main game loop."""

    global pause
    global ball_hitbox
    global pockets

    run = True
    no_of_pockets = 6
    pockets = []

    p1 = Pockets(15, 7, black)
    pockets.append(p1)
    p2 = Pockets(width / 2 - p1.r * 2 + 3, 7, black)
    pockets.append(p2)
    p3 = Pockets(width - p1.r - margin - 30, 20, black)
    pockets.append(p3)
    p4 = Pockets(20, height - margin - 20 - p1.r, black)
    pockets.append(p4)
    p5 = Pockets(width / 2 - p1.r * 2 + 3, height - margin - 20 - p1.r,  black)
    pockets.append(p5)
    p6 = Pockets(width - p1.r - margin - 20, height - margin - 15 - p1.r - 10, black)
    pockets.append(p6)

    ball_hitbox = hitbox(495, 180, 0, black, 0)
    cue_ball = Ball(ball_hitbox.x - radius, ball_hitbox.y - radius, balls[0])
    cue_stick = CueStick(0, 0, 100, stickColor)

    small_font = pygame.font.SysFont('comicsansms', 30)
    text = small_font.render('Record Time: ' + str(prev_score) + ' s', True, white)
    pause_message = small_font.render('Press p To Pause The Game ', True, white)

    while run:

        # Stop the program when the user presses the cross button.
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                close()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            # Only hit cue stick if the ball is not moving.
            if event.type == pygame.MOUSEBUTTONDOWN and ball_hitbox.velocity == 0:

                cue_hit.play()
                # Start the que stick from position of hitbox.
                start_pointer = [ball_hitbox.x - radius, ball_hitbox.y - radius]
                # Position of cursor is in tuple.
                x, y = pygame.mouse.get_pos()
                end_pointer = [x, y]

                dist = ((start_pointer[0] - end_pointer[0]) ** 2 + (start_pointer[1] - end_pointer[1]) ** 2) ** 0.5
                # Force increases as the length of the stick increases.
                force = dist / 15.0
                # Max force applicable is 15.

                if force > 15:

                    force = 15

                cue_stick.apply_force(ball_hitbox, force)

        border(display, wood, width, height)
        display.blit(background, (0, 0))

        ball_hitbox.draw(ball_hitbox.x, ball_hitbox.y)
        ball_hitbox.move()

        # Only draw cue-stick if the cue ball is not moving.
        if not (ball_hitbox.velocity > 0):

            cue_stick.draw(ball_hitbox.x, ball_hitbox.y)

        # Checks every pocket if a ball is pocketed.
        j = 0
        while j < no_of_pockets:

            pockets[j].is_pocket()
            j += 1

        cue_ball.draw(ball_hitbox.x, ball_hitbox.y)
        cue_ball.move(ball_hitbox.x, ball_hitbox.y)
        display.blit(text, (100, 360))
        display.blit(pause_message, (375, 360))

        pygame.display.update()

        # Game runs in 60 frames per second.
        clock.tick(60)

game_intro()


