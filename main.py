#Simple script to guess a number

import random

def pcGuess(x):
	secretNumber = int(input('Enter the secret number: '))
	guess = 0
	low = 1
	high = x
	while guess != secretNumber:
		guess = random.randint(low, high)
		if guess > secretNumber:
			print(f'AI guessed {guess}. Guess too high, guessing again')
			high == high - 1
		elif guess < secretNumber:
			print(f'AI guessed {guess}. Guess too low, guessing again')
			low == low + 1
		else:
			print(f'AI guessed the number {secretNumber}!')
			

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

welcomeMessage = input('Welcome to number guessing game!\nWho is gonna guess?\nComputer with user interact(C)\nComputer without user interact(AI)\n Human(H)\n ').lower()
if welcomeMessage == 'c':
    x = int(input('Chosse the higher number to be guessed: '))
    computerGuess(x)
elif welcomeMessage == 'ai':
   x = int(input('Choose the higher number to be guessed: '))
   pcGuess(x)
   
else:
    x = int(input('Chosse the higher number to be guessed: '))
    guess(x)
