import random

word_list = ["banana", "strawberry", "pineapple", "raspberry", "mango"]

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    Parameters:
    ----------
    word_list (list) : 
            List of words to be used in the game
    num_lives (int) : 
            Number of lives the player has
        
    Attributes:
    ----------
    word (str) :
            The word to be guessed, picked randomly from the word_list. 
    word_guessed (list) : 
            A list of the letters of the word, with _ for each letter not yet guessed. 
            For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. 
            If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters (int) : 
            The number of UNIQUE letters in the word that have not been guessed yet
    num_lives (int) : 
            The number of lives the player has at the start of the game.
    word_list (list) : 
            A list of words
    list_of_guesses (list) : 
            A list of the guesses that have already been tried.
        
    Methods:
    ----------
    check_guess(guess)
            Checks if the guess is in the word.
    ask_for_input()
            Asks the user to input a letter guess.
    '''
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word.lower()))
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
    

    def check_guess(self, guess):
        '''
        This method is used to check that a guess is in the random word.
        If it is then it replaces the '_' in the word_guessed list with the letter at any points in appears
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter (str) :
            The letter to be checked
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for idx, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[idx] = guess
            self.num_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")
    
    def ask_for_input(self):
        '''
        This method will iteratively ask for an input until the input is a valid guess.
        A valid guess is :
            - a single letter
            - that hasn't already been tried
        Once a valid input is submitted
        It will then call the check_guess method.
        '''
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or str.isalpha(guess) == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")  
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                #forgot to add break in milestone 4
                break 
            

def play_game(wordlist):
    num_lives = 5
    game = Hangman(wordlist, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            print(game.word_guessed)
            game.ask_for_input()
        else:
            print(game.word_guessed)
            print("Congratulations. You won the game!")
            break

play_game(word_list)