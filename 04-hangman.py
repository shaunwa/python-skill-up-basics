import random

def play_hangman():
    # If you want to have more words, use an external module
    words = ['python', 'developer', 'console', 'function', 'variable']
    word = random.choice(words)
    
    guessed = ['_'] * len(word)
    guessed_letters = []

    attempts = 6

    print("Let's play Hangman!")
    
    # This is the main game loop
    while attempts > 0 and ''.join(guessed) != word:
        print(f"{' '.join(guessed)}")
        print(f"You have {attempts} {'attempts' if attempts > 1 else 'attempt'} left.")
        print("Guessed letters:", ", ".join(guessed_letters))

        # This converts it to lowercase
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please guess one letter at a time.")
            continue
        
        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed[index] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! The letter '{guess}' is not in the word.")
    
    if ''.join(guessed) == word:
        print(f"\nCongratulations! You guessed the word '{word}' correctly.")
    else:
        print(f"\nYou're out of attempts! The word was '{word}'.")

play_hangman()