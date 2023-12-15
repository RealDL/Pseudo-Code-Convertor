# Python to Pseudocode convertor.

This script turns regular python code into OCR A-Level pseudocode. It is not exactly like the OCR pseudocode, however, it does successfully translate python into pseudocode. Your welcome. Need any help hit me up on discord @realdl

# How to use

1. Firstly, do not worry about modules, no external or internal python modules are used.
2. Copy out your python code and put it in `MyPythonFile.txt`. Do not put anything important in `pseudocode.txt` because that gets written over each time the program runs.
3. Copy your pseudocode from `pseudocode.txt` and your done!

# Example
Below will be an example of how program works

# Python
```py
import random

def get_interesting_fact(number):
    # You can create your own dictionary of facts associated with numbers
    facts = {
        1: "One is the loneliest number.",
        2: "The number 2 is the only even prime number.",
        3: "Three is the number of primary colors.",
        # Add more facts as desired...
    }
    return facts.get(number, "Sorry, I don't have a fact for this number.")

def random_number_fact():
    user_name = input("Hello there! What's your name? ")
    print(f"Hello, {user_name}!")

    # Generating a random number between 1 and 10 for example
    random_number = random.randint(1, 10)

    print(f"Your random number is: {random_number}")
    print("Here's an interesting fact about your number:")
    print(get_interesting_fact(random_number))

# Run the program
random_number_fact()
```

# Pseudocode
```
// Created by RealDL - @realdl on discord.

import random

function get_interesting_fact(number)
    // You can create your own dictionary of facts associated with numbers
    facts = {
        1: "One is the loneliest number.",
        2: "The number 2 is the only even prime number.",
        3: "Three is the number of primary colors.",
        // Add more facts as desired...
    }
    return facts.get(number, "Sorry, I don't have a fact for this number.")
endfunction

procedure random_number_fact()
    user_name = new input("Hello there! What's your name? ")
    print(f"Hello, {user_name}!")
    // Generating a random number between 1 and 10 for example
    random_number = new random.randint(1, 10)
    print(f"Your random number is: {random_number}")
    print("Here's an interesting fact about your number:")
    print(get_interesting_fact(random_number))
endprocedure

// Run the program
random_number_fact()
// Created by RealDL - @realdl on discord.
```
