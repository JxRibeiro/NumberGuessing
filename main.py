#Simple script to guess a number

import random

def guess(x):
    randomNum = random.randint(1,x)
    guess = 0
    while guess != randomNum:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess > randomNum:
            print('Your guess was too high! Try again')
        elif guess < randomNum:
            print('Your guess was too low! Try again')
    print(f'You guessed the number {randomNum}! Congratulations')

def computerGuess(x):
    lowGuess = 1
    highGuess = x
    message = ''
    
    while message != 'c': 
        if lowGuess != highGuess:
            guess = random.randint(lowGuess, highGuess)
        else: 
            guess = lowGuess
        message = input(f'Is the {guess} too high (H), too low (L) or correct (C)?').lower()
        if message == 'h':
            highGuess = guess - 1
        if message == 'l':
            lowGuess = guess + 1
    print(f'AI guessed the number {guess}!') 

welcomeMessage = input('Welcome to number guessing game!\nWho is gonna guess? Computer(C) or Human(H)').lower()
if welcomeMessage == 'c':
    x = int(input('Chosse the higher number to be guessed: '))
    computerGuess(x)
   
else:
    x = int(input('Chosse the higher number to be guessed: '))
    guess(x)
