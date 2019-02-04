'''
This is a simple python script that will generate a random number between
0 and 100 (integer), and the user will have to guess that number.  The
script will take each guess from the user and reply with a higher/lower
response until the correct number is found.

We add in a feature whereby a colored LED will light with each guess,
red meaning the guess was too low, white meaning the guess was too high
and green meaning correct.
'''

# jimp 01-16-2019

# now use a function to check and compare
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput
       break

# main program starts here
import random

# generate a random number
random.seed()
ran_num = random.random()
# note that this is a float between 0 and 1, and we want an integer
#  between 0 and 100
number = int(ran_num * 100)
print(number)

# first, we need to display output to the screen (print) and accept
#   input from the keyboard

print('I am thinking of a number between 1 and 100, can you guess what it is?')

str_guess = inputNumber('Enter your guess: ')
guess = int ( str_guess )
response = 'Your guess {} is too {}'

# check for larger or smaller
while True:
   if guess == number:
       print('Your guess is correct!')
       break
   if guess > number:
       print(response.format(guess,'high'))
       guess = int ( input('Try again: ') )
   elif guess < number:
       print(response.format(guess,'low'))
       guess = int ( input('Try again: ') )
