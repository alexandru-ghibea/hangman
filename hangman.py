import random
from hangman_word import word_list
from hangman_art import logo, stages
from IPython.display import clear_output


chosen_word = random.choice(word_list)
display = []
lives = len(chosen_word) - 1
game_on = True


def replay():
    answer = ["Y", "N"]
    choice = input("Do you want to play again Y or N: ")
    while choice not in answer:
        choice = input("Sorry, please select  Y or N: ")
    if choice == "Y":
        return True
    else:
        return False


for letter in chosen_word:
    display.append("_")

print(logo)
print(f"You have {lives} lives. Then...dead!")

while game_on:
    index = 0
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in chosen_word:
        if guess == position:
            display[index] = position
        index += 1
    print(" ".join(display))
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess. Number of lives remaining {lives}")
    if lives == 0:
        game_on = False
        print("You loose.Word was:", chosen_word)
    if "".join(display) == chosen_word:
        print("You won. Word was:", chosen_word)
        game_on = False
    print(stages[lives])
