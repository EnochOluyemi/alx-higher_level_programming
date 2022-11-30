#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = str(number)
unit = digit[-1:]
unit = int(unit)
if unit > 5:
    print(f"Last digit of {number} is {unit} and is greater than 5")
elif unit < 6 and unit > 0:
    print(f"Last digit of {number} is -{unit} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is 0 and is 0")
