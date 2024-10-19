import random

word_list = ["banana", "strawberry", "pineapple", "raspberry", "mango"]

word = random.choice(word_list)
print(word)

def check_guess(guess):
    '''
    This function is used to check that a guess is in the random word.
    It takes in guess as a parameter
    '''
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    '''
    This function will iteratively check if an input is a valid guess.
    Once a valid input is submitted
    It will then call the check_guess function.
    '''
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and str.isalpha(guess):
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()