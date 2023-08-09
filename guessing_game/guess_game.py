import random



def guess(limit):
    r_num = random.randint(1, limit)
    guess = 0
    while guess != r_num:
        guess = int(input(f'Guess a number between 1 and {limit}: ')) 
        if guess == r_num:
            print(f'{guess} was a correct guess, you WIN!')
        elif guess < r_num:
            print(f'{guess} was to low. Try something bigger')
        elif guess > r_num:
            print(f'{guess} was to high. Try something lower')
    
def computer_guess(limit):
    low = 1
    limit = limit
    computer_guess = 0
    count = 0
    my_number = int(input(f'Input a number between 1 and {limit}: '))
    while computer_guess != my_number:
        count += 1
        computer_guess = random.randint(low, limit)
        if computer_guess < my_number:
            print(f'{computer_guess} was to low.')
            low = computer_guess + 1
        elif computer_guess > my_number:
            print(f'{computer_guess} was to high')
            limit = computer_guess - 1
    print(f'The correct answer was {computer_guess}, the computer guessed your number in {count} turns')


computer_guess(100)
