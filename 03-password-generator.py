import random

# The string module allows us to avoid writing out 'abcdef...'
import string

# Discuss the basics of functions - i.e. args and return values, as well as default args
# Discuss booleans
def generate_password(length=8, use_lowercase=True, use_uppercase=True, use_numbers=True, use_symbols=True):
    possible_characters = ""
    
    if use_lowercase:
        possible_characters += string.ascii_lowercase
    if use_uppercase:
        possible_characters += string.ascii_uppercase
    if use_numbers:
        possible_characters += string.digits
    if use_symbols:
        # You could use string.punctuation, but that includes some weird ones
        possible_characters += '!@#$%^&*()-+='

    # Discuss the length function
    if len(possible_characters) == 0:
        raise ValueError("No characters selected for password generation. Adjust your criteria.")

    generated_password = ""

    for i in range(length):
        # You can also do random.choice(possible_characters)
        generated_password += possible_characters[random.randint(0, len(possible_characters) - 1)]

    return generated_password

password = generate_password(length=12, use_lowercase=True, use_uppercase=True, use_numbers=True, use_symbols=True)
print(password)