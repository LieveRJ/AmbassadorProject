import random
import turtle
import time
from hangman_graphics import draw_circle, draw_line, draw_cross, write_text

DEFAULT_PEN_COLOR = "black"

# Word bank for the hangman game
wordbank = [ "apple", "banana", "cherry", "date", "elderberry", \
            "fig", "grape", "honeydew", "kiwi", "lemon", "mango", \
            "nectarine", "orange", "papaya", "quince", "raspberry", \
            "strawberry", "tangerine", "watermelon" ]

class DrawingHangman:
  def __init__ (self):
    '''
    Initialize the turtle game and set up the parameters.
    
    Game parameters:
      self.failed_attempts: Number of failed attempts
      self.secret_word: Secret word to guess
      self.guessed_letters: Set of guessed letters
      sefl.terminate: Flag to terminate the game
    '''
    self.failed_attempts = 0
    self.secret_word = random.choice(wordbank)
    self.guessed_letters = set()
    self.terminate = False

  def is_word_guessed(self):
    '''
    Check if the word has been guessed.
    If all the letters in the secret word are in the guessed letters, return True.
    Otherwise, return False.
    
    For example:
      self.secret_word = 'apple'
      self.guessed_letters = {'a', 'e'}
      The word has not been guessed yet.
    '''
    # For each letter in the secret word, 
    # check if the letter is in the guessed letters
    for letter in self.secret_word:
      if letter not in self.guessed_letters:
        # If a letter is not in the guessed letters, 
        # it means the word has not been guessed yet.
        # return False
        return False

    return True
  
  def is_letter_in_secret_word (self, letter):
    '''
    Check if the guessed letter is in the secret word.
    If the guessed letter is in the secret word, return True.
    Otherwise, increment failed attempts variable and return False.
    
    For example:
      self.secret_word = 'apple'
      letter = 'a'
      The guessed letter is in the secret word.
    '''
    # Add the guessed letter to the guessed letters set
    self.guessed_letters.add(letter)
    
    # Check if the guessed letter is in the secret word
    if letter in self.secret_word:
      return True
    else:
      self.failed_attempts += 1
      return False

  def draw_word (self, word_turtle):
    '''
    Draw the word with the guessed letters.
    For each letter in secret word, if the letter is in guessed letters, write the letter.
    Otherwise draw a line.
    
    For example:
      self.secret_word = 'apple'
      self.guessed_letters = {'a', 'e'}
      The word will be drawn as: a _ _ _ e
    '''

    # Clear previous guesses
    word_turtle.clear()
    word_turtle.goto(-200, -200)

    # For each letter in the secret word draw the letter or a line
    for letter in self.secret_word:
      
      if letter in self.guessed_letters:
        # If the letter is in the guessed letters, write the letter
        word_turtle.write(letter, None, "center", "16pt")
        word_turtle.penup()
        word_turtle.forward(25)
      else:
        # If the letter is not in the guessed letters, draw a line
        word_turtle.pendown()
        word_turtle.forward(25)
        word_turtle.penup()
        word_turtle.forward(15)

  def draw_man (self, figure_turtle):
    '''
    Draw the hangman figure.
    For each failed attempt, draw a part of the figure.
    Use previously written funstions from hangman_graphics.py.
    '''
    if self.failed_attempts == 1:
      # Draw base
      draw_line(0, 0, 100, 0, DEFAULT_PEN_COLOR)
      
    if self.failed_attempts == 2:
      # Draw pole
      draw_line(10, 0, 10, 100, DEFAULT_PEN_COLOR)

    if self.failed_attempts == 3:
      # Draw top
      draw_line(10, 100, 50, 100, DEFAULT_PEN_COLOR)
    if self.failed_attempts == 4:
      # Draw rope
      draw_line(50, 100, 50, 80, DEFAULT_PEN_COLOR)
    if self.failed_attempts == 5:
      # Draw head
      draw_circle(50, 70, 10, DEFAULT_PEN_COLOR)
    if self.failed_attempts == 6:
      # Draw body
      draw_line(50, 60, 50, 30, DEFAULT_PEN_COLOR)
    if self.failed_attempts == 7:
      # Draw hands
      draw_line(50, 50, 40, 40, DEFAULT_PEN_COLOR)
      draw_line(50, 50, 60, 40, DEFAULT_PEN_COLOR)
    if self.failed_attempts == 8:
      # Draw legs
      draw_line(50, 30, 40, 20, DEFAULT_PEN_COLOR)
      draw_line(50, 30, 60, 20, DEFAULT_PEN_COLOR)
    if self.failed_attempts == 9:
      # Draw eyes
      draw_cross(45, 72, 2, DEFAULT_PEN_COLOR)
      draw_cross(52, 72, 2, DEFAULT_PEN_COLOR)

  def play_hangman(self, word_turtle, figure_turtle, delay = 0.5):
    '''
    Play the hangman game.
    The game will continue until the word is guessed or the failed attempts reach 8.
    
    The game loop:
      1. The player can guess a letter in each round.
      2. If the guessed letter is not in the secret word, 
         part of the hangman figure will be drawn.
      
    After the word is guessed or failed attempts reach 8:
      If the word is guessed, print "Congratulations!".
      If the failed attempts reach 8, print "Sorry, you lose :(".
    '''
    # Start with empty word
    self.draw_word(word_turtle)

    # Check if the word is guessed or failed attempts reach 10
    while not self.is_word_guessed() and self.failed_attempts < 10:
      guess = turtle.textinput("Hangman game", "Guess a letter...")
      
      # The player can only guess a single letter
      if len(guess) > 1 or not guess.isalpha():
        print("Only single letters are allowed.")

      # Check if the guessed letter is in the secret word
      guess = guess.lower()
      if not self.is_letter_in_secret_word(guess):
        self.draw_man(figure_turtle)

      # Draw updated word
      self.draw_word(word_turtle)
      time.sleep(delay)

    if self.is_word_guessed():
      # If the word is guessed write "Congratulations!"
      figure_turtle.goto(0, 0)
      figure_turtle.color('green')
      figure_turtle.write('Congratulations!', False, align = 'center', font = ("Arial", 30, "normal"))
      figure_turtle.color('black')
    else:
      # If the failed attempts reach 8 write "Sorry, you lose :("
      figure_turtle.goto(0, 0)
      figure_turtle.color('red')
      figure_turtle.write('Sorry, you lose :(', False, align = 'center', font = ("Arial", 30, "normal"))
      figure_turtle.color('black')


def main():
  # Set up the screen
  screen = turtle.Screen()
  screen.title("Hangman Game")
  screen.bgcolor("white")
  screen.setup(width=700, height=700)

  word_turtle = turtle.Turtle()
  figure_turtle = turtle.Turtle()
  game = DrawingHangman()

  # Create game loop
  while not game.terminate:
    # Set-up the turtle that will be drawing the guessed word
    word_turtle.shape("turtle")
    word_turtle.speed(7)
    word_turtle.penup()
    word_turtle.goto(-120, -120)

    # Set-up the turtle that will be drawing the stick man
    figure_turtle.penup()
    figure_turtle.goto(0, 300)
    figure_turtle.color("blue")
    figure_turtle.write("Let's play Hangman, guess the letters!", None, "center", font = ("Arial", 20, "bold"))
    figure_turtle.color("black")

    # Play the hangman game
    game.play_hangman(word_turtle, figure_turtle)
    
    # Give player 5 seconds to see the result
    figure_turtle.goto(0, -50)
    figure_turtle.write('Wait 5 seconds to play again.', False, align = 'center', font = ("Arial", 10, "normal"))
    time.sleep(5)

    # Clear the turtles
    word_turtle.clear()
    figure_turtle.clear()
    game = DrawingHangman()

if __name__ == "__main__":
  main()