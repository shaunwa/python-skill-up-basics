import random

one = """
+-----+
|     |
|  •  |
|     |
+-----+
"""

two = """
+-----+
|•    |
|     |
|    •|
+-----+
"""

three = """
+-----+
|•    |
|  •  |
|    •|
+-----+
"""

four = """
+-----+
|•   •|
|     |
|•   •|
+-----+
"""

five = """
+-----+
|•   •|
|  •  |
|•   •|
+-----+
"""

six = """
+-----+
|•   •|
|•   •|
|•   •|
+-----+
"""

# Discuss how lists are indexed, i.e. they start at 0
die_faces = [
    one,
    two,
    three,
    four,
    five,
    six,
]

user_input = input('How many dice would you like to roll?: ')

# Discuss basic error handling in programs
try:
    number_of_dice = int(user_input)

    # This is how you do things repeatedly.
    # First, show typing this out twice
    for x in range(number_of_dice):
        print(f'Here is die number {x + 1}')
        selected_number = random.randint(0, 5)
        print(die_faces[selected_number])
except ValueError:
    print('Sorry, that is not a valid number. Please try again.')
