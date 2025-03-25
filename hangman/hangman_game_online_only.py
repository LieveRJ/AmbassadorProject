import random
import turtle
import time

# Constants
DEFAULT_PEN_COLOR = "black"

# Word bank for the hangman game
wordbank = [ "apple", "banana", "cherry"]

# Global variables (Do not modify these here, they will be updated once the game starts!)
failed_attempts = 0
secret_word = random.choice(wordbank)
guessed_letters = set()
terminate = False

word_turtle = turtle.Turtle()
figure_turtle = turtle.Turtle()

def is_word_guessed():
  # Check if the word has been guessed.
  # If all the letters in the secret word are in the guessed letters, return True.
  # Otherwise, return False.
  #
  # For example:
  #   self.secret_word = 'apple'
  #   self.guessed_letters = {'a', 'e'}
  #   The word has not been guessed yet.

  # TODO:  For each letter in the secret word,  check if the letter is in the guessed letters
  # Hint: to check if one letter is in the guessed letters, you can use the 'in' keyword
  for letter in secret_word:
    if letter not in guessed_letters:
      # If a letter is not in the guessed letters,
      # it means the word has not been guessed yet.
      # return False
      return False

  return True

def is_letter_in_secret_word(letter):
  global failed_attempts # Ignore this line
  # Check if the guessed letter is in the secret word.
  # If the guessed letter is in the secret word, return True.
  # Otherwise, increment failed attempts variable and return False.
  # For example:
  #  secret_word = 'apple'
  #  letter = 'a'
  # The guessed letter is in the secret word.

  # Add the guessed letter to the guessed letters set
  guessed_letters.add(letter)
  # Check if the guessed letter is in the secret word
  if letter in secret_word:
    return True
  else:
    failed_attempts += 1
    return False

def draw_man():
  #  Draw the hangman figure.
  #  For each failed attempt, draw a part of the figure.
  if failed_attempts == 1:
    # Draw base
    draw_line(0, 0, 100, 0, DEFAULT_PEN_COLOR)

  if failed_attempts == 2:
    # Draw pole
    draw_line(10, 0, 10, 100, DEFAULT_PEN_COLOR)

  if failed_attempts == 3:
    # Draw top
    draw_line(10, 100, 50, 100, DEFAULT_PEN_COLOR)
  if failed_attempts == 4:
    # Draw rope
    draw_line(50, 100, 50, 80, DEFAULT_PEN_COLOR)
  if failed_attempts == 5:
    # Draw head
    draw_circle(50, 70, 10, DEFAULT_PEN_COLOR)
  if failed_attempts == 6:
    # Draw body
    draw_line(50, 60, 50, 30, DEFAULT_PEN_COLOR)
  if failed_attempts == 7:
    # Draw hands
    draw_line(50, 50, 40, 40, DEFAULT_PEN_COLOR)
    draw_line(50, 50, 60, 40, DEFAULT_PEN_COLOR)
  if failed_attempts == 8:
    # Draw legs
    draw_line(50, 30, 40, 20, DEFAULT_PEN_COLOR)
    draw_line(50, 30, 60, 20, DEFAULT_PEN_COLOR)
  if failed_attempts == 9:
    # Draw eyes
    draw_cross(45, 72, 2, DEFAULT_PEN_COLOR)
    draw_cross(52, 72, 2, DEFAULT_PEN_COLOR)

def play_hangman(delay=0.5):
  # Play the hangman game.
  # The game will continue until the word is guessed or the failed attempts reach 10.

  # Start with empty word
  write_guessed_word()
  while not is_word_guessed() and failed_attempts < 10:
    guess = raw_input("Guess a letter...")

    # The player can only guess a single letter
    # TODO: Check if the player guessed a *single* character
    #  and that character is a *letter*
    # Hint: check for the length of the guess with len()
    # and if it is a letter using guess.isalpha() that returns True if all characters in the string are alphabetic
    if len(guess) > 1 or not guess.isalpha():
      print("Only single letters are allowed.")

    # Check if the guessed letter is in the secret word)
    guess = guess.lower()
    if not is_letter_in_secret_word(guess):
      draw_man()

    write_guessed_word()
    time.sleep(delay)

  if is_word_guessed():
    write_congratulations()
  else:
    write_game_over()

###############################################
# Hint: use the following functions to make the game work  #
###############################################

def draw_circle(x, y, radius, pen_color):
  # Function to draw a circle with the given parameters using turtle graphics
  # x, y: center of the circle, radius: radius of the circle, pen_color: color of the circle
  turtle.penup()
  turtle.pencolor(pen_color)
  turtle.goto(x, y - radius)
  turtle.pendown()
  turtle.circle(radius)

def draw_line(start_x, start_y, end_x, end_y, pen_color):
  # Function to draw a line with the given parameters using turtle graphics
  # start_x, start_y: starting point of the line, end_x, end_y: ending point of the line, pen_color: color of the line
  turtle.penup()
  turtle.pencolor(pen_color)
  turtle.goto(start_x, start_y)
  turtle.pendown()
  turtle.goto(end_x, end_y)

def draw_cross(center_x, center_y, size, pen_color):
  # Function to draw a cross with the given parameters using turtle graphics
  # center_x, center_y: center of the cross, size: size of the cross, pen_color: color of the cross
  draw_line(center_x, center_y, center_x + size, center_y + size, pen_color)
  draw_line(center_x + size, center_y, center_x, center_y + size, pen_color)


def write_congratulations():
  # Write "Congratulations!" on the screen
  figure_turtle.goto(0, 0)
  figure_turtle.color('green')
  figure_turtle.write('Congratulations!', False, align='center', font=("Arial", 30, "normal"))
  figure_turtle.color('black')

def write_game_over():
  # Write "Sorry, you lose :(" on the screen
  figure_turtle.goto(0, 0)
  figure_turtle.color('red')
  figure_turtle.write('Sorry, you lose :(', False, align='center', font=("Arial", 30, "normal"))
  figure_turtle.color('black')

def write_guessed_word():
  # Draw the word with the guessed letters.
  # For each letter in secret word, if the letter is in guessed letters, write the letter.
  # Otherwise draw a line.
  word_turtle.clear()
  word_turtle.goto(-200, -200)
  for letter in secret_word:
    if letter in guessed_letters:
      word_turtle.write(letter, None, "center", "16pt")
      word_turtle.penup()
      word_turtle.forward(25)
    else:
      word_turtle.pendown()
      word_turtle.forward(25)
      word_turtle.penup()
      word_turtle.forward(15)

###################################
# IGNORE ALL THE CODE BELOW THIS LINE #
##################################

def main():
  global terminate
  screen = turtle.Screen()
  screen.bgcolor("white")
  screen.setup(width=700, height=700)

  while not terminate:
    word_turtle.shape("turtle")
    word_turtle.speed(7)
    word_turtle.penup()
    word_turtle.goto(-120, -120)
    figure_turtle.penup()
    figure_turtle.goto(0, 300)
    figure_turtle.color("blue")
    figure_turtle.write("Let's play Hangman, guess the letters!", None, "center", font=("Arial", 20, "bold"))
    figure_turtle.color("black")
    play_hangman()
    figure_turtle.goto(0, -50)
    figure_turtle.write('Wait 5 seconds to play again.', False, align='center', font=("Arial", 10, "normal"))
    time.sleep(5)
    word_turtle.clear()
    figure_turtle.clear()

if __name__ == "__main__":
  main()