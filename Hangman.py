import random
import Hangman_Stages
import Hangman_Words
print("Welcome to Hangman Game")
chosen_word = random.choice(Hangman_Words.word_list)
display = []
for i in range(len(chosen_word)): # Adding the blank spaces which the user need to be filled
    display += '_'
print(display)
life = 6
game_over = False
while not game_over:
    guessed_letter = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guessed_letter == letter:
            display[position] = guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        life -= 1
        if life == 0: # Loosing Condition
            game_over = True
            print("You Lost")
    if '_' not in display: # Winning Condition
            game_over = True
            print("You Won!!!")
    # Showing the Hangman Figure
    print(Hangman_Stages.hangman_stages[life])    
