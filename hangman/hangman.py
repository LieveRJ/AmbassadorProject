import random
import turtle
import time

# Word bank for the hangman game
wordbank = ['affix', 'bagpipes', 'bandwagon', 'banjo', 'buffalo',
            'cobweb', 'croquet', 'daiquiri', 'duplex', 'dwarves',
            'equip', 'exodus', 'fishhook', 'fixable', 'galaxy',
            'galvanize', 'ivy', 'juicy', 'kilobyte', 'megahertz',
            'oxygen', 'polka', 'quiz', 'rhubarb', 'schizophrenia',
            'unzip', 'uptown', 'vodka', 'whiskey', 'zombie']

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
    '''

    if self.failed_attempts == 1:
      # draw gallows
      figure_turtle.home()
      figure_turtle.pendown()
      figure_turtle.left(90)
      figure_turtle.forward(175)
      figure_turtle.left(90)
      figure_turtle.forward(74)
      figure_turtle.left(90)
      figure_turtle.forward(35)
      figure_turtle.penup()

    if self.failed_attempts == 2:
      # draw head
      figure_turtle.goto(-74, 140)
      figure_turtle.pendown()
      figure_turtle.right(90)
      figure_turtle.circle(15, None, 100)
      figure_turtle.penup()
    elif self.failed_attempts == 3:
      # draw torso
      figure_turtle.goto(-74, 140)
      figure_turtle.pendown()
      figure_turtle.left(90)
      figure_turtle.penup()
      figure_turtle.forward(30)
      figure_turtle.pendown()
      figure_turtle.forward(40)
      figure_turtle.right(180)
      figure_turtle.forward(30)
      figure_turtle.penup()
    elif self.failed_attempts == 4:
      # draw first arm
      figure_turtle.goto(-74, 100)
      figure_turtle.pendown()
      figure_turtle.left(55)
      figure_turtle.forward(45)
      figure_turtle.right(180)
      figure_turtle.forward(45)
      figure_turtle.penup()
    elif self.failed_attempts == 5:
      # draw second arm
      figure_turtle.goto(-74, 100)
      figure_turtle.pendown()
      figure_turtle.left(70)
      figure_turtle.forward(45)
      figure_turtle.right(180)
      figure_turtle.forward(45)
      figure_turtle.penup()
    elif self.failed_attempts == 6:
      # draw first leg
      figure_turtle.goto(-74, 100)
      figure_turtle.pendown()
      figure_turtle.left(55)
      figure_turtle.forward(30)
      figure_turtle.right(30)
      figure_turtle.forward(60)
      figure_turtle.right(180)
      figure_turtle.forward(60)
      figure_turtle.penup()
    elif self.failed_attempts == 7:
      # draw second leg
      figure_turtle.goto(-74, 70)
      figure_turtle.pendown()
      figure_turtle.right(120)
      figure_turtle.forward(60)
      figure_turtle.penup()

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

    # Check if the word is guessed or failed attempts reach 8
    while not self.is_word_guessed() and self.failed_attempts < 8:
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
