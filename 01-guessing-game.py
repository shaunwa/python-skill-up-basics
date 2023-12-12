# What are imports and why are they necessary?
import random

# Save this for later, when you want to make the program configurable
# Challenge for learner - add a question at the beginning that allows the user to select 'easy', 'medium' or 'hard' mode
max_number = 5

# This is one way for our program to communicate with the user
# Also discuss basic string syntax in Python
print('Welcome to the guessing game!')
print(f'I\'m thinking of a number between 1 and {max_number} - try to guess what it is...')

# Discuss variables
# Discuss "integers" vs. "floats"
# This is how we generate random integers in Python - here, from 1 to 10, inclusive.
# You may want to just hard-code the number first
selected_number = random.randint(1, max_number)

# This is how the user can communicate back to the program
users_guess = input('Please enter your guess here: ')

# Discuss if-else statements
# Discuss the "type mismatch" here - i.e. we must convert the user's input into an int
if int(users_guess) == selected_number:
    # This is how we insert values into strings
    print(f'Congratulations, you guessed it! The number was {selected_number}')
else:
    print(f'No, sorry. The number was {selected_number}')