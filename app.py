import random


def start_game():
    user_input_level = input("What level do you want to play?(Easy/Medium/Hard): ")
    while user_input_level.lower() != 'easy' and user_input_level.lower() != 'hard' and user_input_level != 'medium':
        user_input_level = input('You are entering an invalid value, type easy, medium or hard: ')
    if user_input_level.lower() == 'easy':
        start_level(1, 10, 6)
    elif user_input_level.lower() == 'medium':
        start_level(1, 20, 4)
    elif user_input_level.lower() == 'hard':
        start_level(1, 50, 3)


def start_level(start_int, end_int, guess_chance):
    guess_number = random.randrange(start_int, end_int)
    start_count = 1

    while start_count <= guess_chance:
        user_guess = input('Make a guess, between ' + str(start_int) + ' and ' + str(end_int) + ': ')
        while user_guess == '':
            user_guess = input("You can't play the game without making a guess, Make a guess: ")
        if int(user_guess) == guess_number:
            print('You got it right! You won')
            start_game()
        else:
            print('That was wrong')
            print(f'You have {guess_chance - start_count} guess left')
        start_count = start_count + 1
    print('Game Over')


start_game()
