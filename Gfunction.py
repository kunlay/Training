import random

def GuessGame():
    user = input('Welcome, what is your name? \n')
    result = random.randint(1, 50)
    print(result)
    Max_guesses = 3
    guess_left = Max_guesses
    print('welcome,' + user + ', Guess a number between 1-50.')
    while guess_left:
        print('Guess remaining: ' + str(guess_left))
        guess = int(input('enter a number? \n'))
        if guess == result:
            print('Good Job')
            break
        elif guess < result:
            print('too low, try again')
        elif guess > result:
            print('too high,try again')
        guess_left -= 1
    else:
        print(user + ' Game Over, you are out of guesses!')

def restart():
    while True:
        restart = input('would you like to play again? y/n ').lower()
        if restart == 'n':
            print('BYE')
        else:
            GuessGame()

GuessGame()
restart()