#!/usr/bin/python3
# ascii hangman game
#   - by bryan "zb" zuber

import random

class Game:
  def __init__(self):
    self.difficulty, self.guesses_left, self.guesses_used = 0, 0, 0
    self.end, self.win = False, False
    
    # game title art
    self.title ="""
                                                             +---+
  H    H    AA    NN   N   GGGGG  M     M    AA    NN   N    |   |
  H    H   A  A   N N  N  G       MM   MM   A  A   N N  N    O   |
  HHHHHH  AAAAAA  N  N N  G  GGG  M M M M  AAAAAA  N  N N   /|\  |
  H    H  A    A  N   NN  G    G  M  M  M  A    A  N   NN   / \  |
  H    H  A    A  N    N   GGGG   M     M  A    A  N    N        |
                                                          =========
                                            - by zb"""
    # -- hangman ascii art array--
    self.ascii = ['''

      +---+
      |   |
          |
          |
          |
          |
    =========''', '''

      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''

      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''

      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''

      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''

      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''

      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    # -- end hangman ascii art array --
    
  # set difficulty
  def set_difficulty(self):
    while True:
      print("Select difficulty level:")
      print("1: Easy (States, 6 guesses)")
      print("2: Medium (Countries, 5 guesses")
      print("3: Hard (Capitals, 4 guesses)")

      try: # handle exception
        n = int(input("\r\n> ") )
        if n in range(1,4):
          self.difficulty = n
          break
        else:
          print("Invalid selection.\r\n")
          continue
      except ValueError: # non-int value
        print("Invalid selection.\r\n")
        continue

  # draw hangman picture
  def draw_hangman(self):
    print(self.ascii[6 - self.guesses_left] )
    print()
  
class Word:
  def __init__(self):
    self.states = "texas colorado louisiana kansas oklahoma washington oregon idaho arizona florida illinois".split()
    self.countries = "america canada mexico russia england norway germany spain israel japan libya ukraine taiwan".split()
    self.capitals = "tokyo moscow berlin london paris athens rome kiev madrid amsterdam helsinki dublin nairobi".split()
    self.bank, self.letters_secret, self.letters_tried, self.letters_correct = [], [], [], []
    self.guess = ""
    
  # choose a random word
  def shuffle(self):
    self.secret = random.choice(self.bank)
    self.letters_secret = list(self.secret)
    
  # draw blank spaces and correct letters
  def draw_letters(self):
    for i in self.letters_secret:
      if i in self.letters_correct:
        print(i, end=" ")
      else:
        print("_", end=" ")
    print()

  # draw tried letters
  def draw_tried(self):
    print("Letters tried: ", end="")
    for i in self.letters_tried:
      print(i, end=" ")
      
# ---- end of classes ----

# start a new game
newgame = True

# ---- restart loop ----
while newgame:
  # init objects
  game = Game()
  word = Word()

  # title
  print(game.title)

  # player selects difficulty
  game.set_difficulty()
      
  # set wordbank and guesses
  if game.difficulty == 1:
    game.guesses_left = 7
    word.bank = word.states
  elif game.difficulty == 2:
    game.guesses_left = 6
    word.bank = word.countries
  elif game.difficulty == 3:
    game.guesses_left = 5
    word.bank = word.capitals
    
  # pick secret word
  word.shuffle()

  # ---- main loop ----
  while not game.end:
    
    # check for correct letter
    if word.guess in word.letters_secret:
      for i in word.letters_secret:
        if word.guess is i:
          word.letters_correct.append(i)
    else:
      game.guesses_used += 1
      game.guesses_left -= 1
    
    # check if player has won
    if len(word.letters_correct) == len(word.letters_secret):
      game.win = True
      game.end = True

    # check if player has lost
    if game.guesses_left == 0:
      word.letters_correct = word.letters_secret
      game.end = True
      
    # draw stuff
    word.draw_tried()
    game.draw_hangman()
    word.draw_letters()
    
    # get input if game not over
    if not game.end:
      word.guess = input("\r\n> ")
      word.letters_tried.append(word.guess)
        
  # ---- end main loop ----

  # print results
  print()
  if game.win:
    print("Well done! You win!")
  else:
    print("Sorry! You lose.")
  
  # ask if player wants to play again
  if newgame:
    print()
    print("Play again? (y or n)")
    if input("\r\n> ") in ["y", "yes"]:
      newgame = True
    else:
      newgame = False

# ---- end restart loop ----

# say goodbye
print("Goodbye!")
