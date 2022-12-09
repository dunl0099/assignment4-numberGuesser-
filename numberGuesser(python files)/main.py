import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    print("Choose a number between 1 and 10. The computer will attempt to guess the number.")
    while True:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f'Yay! The computer guessed your number, {guess}, correctly!')
            break
        else:
            print('\nWrong selection of option. Please try again.\n')


computer_guess(10)