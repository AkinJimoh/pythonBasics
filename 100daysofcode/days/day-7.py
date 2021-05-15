#Hang-Man

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#https://replit.com/@appbrewery/Day-7-Hangman-2-Start
import random
import hangman_art as mx
import hangman_words as hw
print(f"{mx.logo}" )

end_of_game = False
wl = hw.word_list
display = []
picked_words = []
chosen_word = random.choice(wl)
#print(chosen_word)
words = range(len(chosen_word))
lives = 6

for i in words:
    display += "_"

while not end_of_game:
    guess = input("Please choose a letter:\n").lower()

    if guess in display:
        print(f"Hi Anna, you have already chosen the letter {guess}, try something else")

    for i in words:
        if guess == chosen_word[i]:
                display[i] = guess

    if guess not in chosen_word and guess not in picked_words:
        print(f"Sorry, but the letter {guess} is not part of the word")
        lives -= 1
    elif guess not in chosen_word and guess in picked_words:
        print(f"You have picked the letter {guess} already")

    if guess not in chosen_word:
        picked_words += guess


    if "_" not in display:
        end_of_game = True
        print("Congratulations, You win!!!!.")
    elif lives == 0:
        end_of_game = True
        print(f"Game Over, You Lose!!! The word was {chosen_word}")

    print(f"{' '.join(display)}")
    print(mx.stages[lives])





