import random

## getting secret word
def load_word():

    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split( )
    secret_word = random.choice(words_list)
    return secret_word

def get_guessed_word(secret_word, letters_guessed):
    display = [ ]
    for letters_guessed in secret_word:
        if letters_guessed in secret_word:
            display += letters_guessed
        else:
            display += "_"
    return display

## receiving user input
def is_guess_in_word(guess, secret_word):
    guess = input("Guess A Letter: ")
    for guess in secret_word:
        if guess in secret_word:
            return True
        else:
            return False

## testing if secret word has been guessed correctly
def is_word_guessed(secret_word, letters_guessed):
    for letters_guessed in secret_word:
        if letters_guessed == secret_word:
            print("Correct!")
            return True
        else:
            print("Incorrect, Try Again")
            return False

## structure of game
def spaceman(secret_word):
    get_guessed_word = "_" * len(secret_word)
    attempts_left = 7
    letter_guessed = [ ]

    print("Welcome to the Spaceman Game!")
    print("You have 10 attempts to guess my Secret Word. Good Luck!")

    while attempts_left > 0:
        print("\nSecret Word:", get_guessed_word)
        print("Attempts Left: ", attempts_left)
        guess = input("Guess A Letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a Single Letter")
        
        if guess in letter_guessed:
            print("You've previously entered this Guess. Please try again")
        letter_guessed.append(guess)


        if guess in secret_word: 
            print("Correct!")
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    get_guessed_word = get_guessed_word[:i] + guess + get_guessed_word[i + 1:]
        
        else:
            print("Incorrect!")
            attempts_left -= 1
            print(f"Attempts Left: {attempts_left}")
        
        if get_guessed_word == secret_word:
            print("Congrats! You Won. The Secret Word was: ", secret_word)
            return True

        if attempts_left == 0:
            print("You lose! The Secret Word was: ", secret_word)
        
    while attempts_left == 0:
        response = input("Would you like to play again? YES / NO: ")

        if response.lower() == 'yes':
            return spaceman(secret_word)
        else:
            print("Thank you for playing Spaceman!")
            break

## caller function
secret_word = load_word()
spaceman(secret_word)