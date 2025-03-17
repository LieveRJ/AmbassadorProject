# A very simple snake game
# By aceking007

# Imports
import turtle
import time
import random


# Set initial score
score = 0
high_score = 0
delay = 0.1


# Set up the screen
wn = turtle.Screen()
wn.title('Snake Game')
wn.bgcolor("black")
wn.setup(width=700, height=700)
wn.tracer(0)  # Turns off screen updates

# Outline of the playing field
pencil = turtle.Turtle()
pencil.speed(0)
pencil.shape('circle')
pencil.color('black')
pencil.penup()
pencil.hideturtle()
pencil.goto(310, 310)
pencil.pendown()
pencil.goto(-310, 310)
pencil.goto(-310, -310)
pencil.goto(310, -310)
pencil.goto(310, 310)
pencil.penup()

# Uncomment these lines and upload file in gif format to change shapes of snake/food
# turtle.register_shape("custom_shape.gif")
# turtle.shape("custom_shape.gif")

# Snake head
head = turtle.Turtle()
head.speed(0) # 0 is the maximum animation speed of turtle module
head.shape("circle")
head.color('blue')
head.penup()
head.goto(0, 0)
head.direction = 'stop' # Initial movement should

# Snake Food
food = turtle.Turtle()
food.speed(0) # 0 is the maximum animation speed of turtle module
food.shape("circle")
food.color('red')
food.penup()
food.goto(0, 100)

# Contains information about snake body
segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape('circle')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write('Score: 0 High Score: 0', align = 'center', font = ('Courier', 24, 'normal'))

### Functions
# Function to update the score
def update_score():
    pen.clear()
    pen.write('Score: {} High Score: {}'.format(score, high_score), align='center', font = ('Courier', 24, 'normal'))

# Functions that move snake in response to keyboard keys
# Hint: look at the collision function and "KeyBoard Bindings" section to see what may be used in these functions
def go_up():
    if ... != ... :
        ...

def go_down():
    if ... != ... :
        ...

def go_left():
    if ... != ... :
        ...

def go_right():
    if ... != ... :
        ...

# Function that helps the snake move
def move():
    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    # Move segment 0 to the head
    if len(segments) > 0:
        x = ...
        y = ...
        segments[0].goto(x, y)
    # Keep the snake head moving in the same direction
    if ... == ... :
        head.sety(... + 10)
    if ... == ... :
        head.sety(... - 10)
    if ... == ... :
        head.setx(... - 10)
    if ... == ... :
        head.setx(... + 10)

# Function that tells the game what to do when collision occurs
def collision():
    time.sleep(0.5)
    head.goto(...)
    head.direction = ...
    # Hide the segments
    for segment in segments:
        segment.hideturtle()
    # Clear the segments list
    segments.clear()
    score = ...
    # update the score in the next line:
    ...
    # Reset the delay
    delay = 0.1

### Keyboard bindings
wn.listen()
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_right, 'Right')

### Loop that runs the game code
while True:
    # Updates the window repeatedly
    wn.update()

    # Check for collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        # Call the collision function in the next line
        ...

    # Check if the snake eats the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        food.goto(random.randint(-290,290),random.randint(-290,290))
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('circle')
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)
        # Shorten the delay - this increases speed of snake as it gets longer
        delay -= 0.001
        # Increase the score
        score += 10
        # If there is a new highscore, replace the old highscore with the current score
        ...
        # Update the score again in the next line
        ...

    # Move the snake in the game
    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 10:
            # Call the collision function in the next line
            ...
    # Delay so that we can see things move
    time.sleep(delay)

# Makes the window visible and runs everything
wn.mainloop()


# Are you done with the basic implementation? 
# See if you can make the snake change colours every time you eat an apple! 
# Or try changing parts of the code to make the game more difficult
