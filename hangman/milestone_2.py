import random

word_list = ["banana", "strawberry", "pineapple", "raspberry", "mango"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Enter a letter: ")
if len(guess) == 1 and str.isalpha(guess):
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")


