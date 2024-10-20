import random

word_list = ["banana", "strawberry", "pineapple", "raspberry", "mango"]

class Hangman:
    def __init__(self, word_list, num_lives=5):
        '''
        Attributes:
            word (str) : The word to be guessed, picked randomly from the word_list. 
            word_guessed (list) : A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
            num_letters (int) : The number of UNIQUE letters in the word that have not been guessed yet
            num_lives (int) : The number of lives the player has at the start of the game.
            word_list (list) : A list of words
            list_of_guesses (list) : A list of the guesses that have already been tried. Set this to an empty list initially
        '''
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word.lower()))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    

    def check_guess(self, guess):
        '''
        This method is used to check that a guess is in the random word.
        It takes in guess as a parameter
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for idx, letter in enumerate(self.word):
                print(idx, letter)
                if guess == letter:
                    self.word_guessed[idx] = guess
            self.num_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")
    
    def ask_for_input(self):
        print(self.word)
        '''
        This method will iteratively check if an input is a valid guess.
        Once a valid input is submitted
        It will then call the check_guess function.
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

hangman = Hangman(word_list)
hangman.ask_for_input()
