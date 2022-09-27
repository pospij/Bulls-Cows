"""Druhy projekt do Engeto online Python Akademie
autor: Jan Pospisil
email: honza@seamaster.cz
discord: Jan P#5449
"""

import random


# generator nahodnych cisel bez duplikatu
def generator():
    while True:
        numbers = random.randint(1000, 9999)
        if bezduplikatu(numbers):
            return numbers


# funkce ktera z cisel dela list cisel
def cislalistu(number_1):
    return [int(i) for i in str(number_1)]


# funkce aby se neopakovala cisla
def bezduplikatu(number_2):
    number_list = cislalistu(number_2)
    if len(number_list) == len(set(number_list)):
        return True
    else:
        return False


# porovnani gen.cisla a hadaneho. pocitani bulls&cows
def bullscows(number_3, guess_1):
    bulls_cows = [0, 0]
    number_list = cislalistu(number_3)
    guess_list = cislalistu(guess_1)
    for x, y in zip(number_list, guess_list):
        if y in number_list:
            if y == x:
                bulls_cows[0] += 1
            else:
                bulls_cows[1] += 1
    return bulls_cows


# beh hry

sep = '-' * 50

print(f'''Hi there!
{sep}
I've generated a random 4 digit number for you.
The number is unique and the number is not repeated.
Let's play a bulls and cows game.
{sep}''')
number = generator()
pokusy = int(input('Enter number of your tries:'))
print(sep)
odehrana_kola = 0
while pokusy > 0:

    guess = int(input('Enter a number:'))

    if not bezduplikatu(guess):
        print('The numbers are repeated. Try it again.')
        print(sep)
        continue
    if guess < 1000 or guess > 9999:
        print('The number is not 4 digits or starts with 0')
        print(sep)
    bull_cow = bullscows(number, guess)
    if bull_cow[0] == 1 and bull_cow[1] == 1:
        print(f'{bull_cow[0]} Bull, {bull_cow[1]} Cow')

    elif bull_cow[0] == 1 and bull_cow[1] > 1:
        print(f'{bull_cow[0]} Bull, {bull_cow[1]} Cows')

    elif bull_cow[0] > 1 and bull_cow[1] == 1:
        print(f'{bull_cow[0]} Bulls, {bull_cow[1]} Cow')

    elif bull_cow[0] == 0 and bull_cow[1] == 0:
        print(f'{bull_cow[0]} Bulls, {bull_cow[1]} Cows')

    elif bull_cow[0] == 1 and bull_cow[1] == 0:
        print(f'{bull_cow[0]} Bull, {bull_cow[1]} Cows')

    elif bull_cow[0] == 0 and bull_cow[1] == 1:
        print(f'{bull_cow[0]} Bulls, {bull_cow[1]} Cow')

    else:
        print(f'{bull_cow[0]} Bulls, {bull_cow[1]} Cows')
    print(sep)
    if bull_cow[0] == 4:
        print(f'''!You win!
You guessed the number in {odehrana_kola} tries''')
        print(sep)
        break
    pokusy -= 1
    odehrana_kola += 1
else:
    print(f'You are out of tries! The number is {number}')
    print(sep)
