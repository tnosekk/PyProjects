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
    

guess(40)