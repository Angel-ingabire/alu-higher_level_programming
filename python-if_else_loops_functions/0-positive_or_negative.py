#!/bin/bash
import random

number = random.randint(-10, 10)  # This will assign a random signed number

# Your code starts here
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")


