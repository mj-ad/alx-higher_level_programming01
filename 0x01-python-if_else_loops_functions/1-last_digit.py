#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_digit = number % 10
    if last_digit > 5:
        print(f'Last digit of {number} is {last_digit} and is greater than 5')
    elif last_digit == 0:
        print(f'Last digit of {number} is {last_digit} and is 0')
    else:
        print(f'Last digit of {number} is {last_digit} and is less than 6 and not 0')
else:
    num = number * -1
    last = num % 10
    last = last * -1
    print(f'Last digit of {number} is {last} and is less than 6 and not 0')
