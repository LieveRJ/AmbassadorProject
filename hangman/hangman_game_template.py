import random
import turtle
import time
from hangman_graphics import draw_circle, draw_line, draw_cross, write_text

DEFAULT_PEN_COLOR = "black"

# TODO: Fill in word bank for the hangman game
#
# Hint: For example: wordbank = [ "apple", "banana", "cherry"]
wordbank = [  ]

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
    # TODO: Fill in
    pass
  
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
    
    # TODO: Check if the guessed letter is in the secret word
    # otherwise increment the failed attempts
    #
    # Hint: use self.secret_word and self.failed_attempts
    pass

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
    
    # TODO: Set the position of the turtle

    # For each letter in the secret word draw the letter or a line
    for letter in self.secret_word:
      if letter in self.guessed_letters:
        # TODO: If the letter is in the guessed letters, write the letter
        pass
      else:
        # TODO: If the letter is not in the guessed letters, draw a line
        pass

  def draw_man (self, figure_turtle):
    '''
    Draw the hangman figure.
    For each failed attempt, draw a part of the figure.
    Use previously written funstions from hangman_graphics.py.
    '''
    if self.failed_attempts == 1:
      # TODO: Draw base
      pass
      
    if self.failed_attempts == 2:
      # TODO: Draw pole
      pass

    if self.failed_attempts == 3:
      # TODO: Draw top
      pass
  
    if self.failed_attempts == 4:
      # TODO: Draw rope
      pass
  
    if self.failed_attempts == 5:
      # TODO: Draw head
      pass
  
    if self.failed_attempts == 6:
      # TODO: Draw body
      pass
  
    if self.failed_attempts == 7:
      # TODO: Draw hands
      pass
  
    if self.failed_attempts == 8:
      # TODO: Draw legs
      pass
  
    if self.failed_attempts == 9:
      # TODO: Draw eyes
      pass

  def play_hangman(self, word_turtle, figure_turtle, delay = 0.5):
    '''
    Play the hangman game.
    The game will continue until the word is guessed or the failed attempts reach 10.
    '''
    # Start with empty word
    self.draw_word(word_turtle)

    # Check if the word is guessed or failed attempts reach 10
    while not self.is_word_guessed() and self.failed_attempts < 10:
      guess = turtle.textinput("Hangman game", "Guess a letter...")
      
      # EXTRA TODO: Verify the player guessed a letter

      # Check if the guessed letter is in the secret word
      guess = guess.lower()
      if not self.is_letter_in_secret_word(guess):
        self.draw_man(figure_turtle)

      # Draw updated word
      self.draw_word(word_turtle)
      time.sleep(delay)

      # EXTRA TODO: If the word is guessed write "Congratulations!"
      # EXTRA TODO: If the failed attempts reach 10 write "Sorry, you lose :("
      

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
        word_turtle.shape("turtle")
        figure_turtle.shape("turtle")

        # EXTRA TODO: Create a title for the game

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