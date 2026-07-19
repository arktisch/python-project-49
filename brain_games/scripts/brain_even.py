from random import randint
from brain_games import cli

user_name = cli.welcome_user()

def main():
    print('Answer "yes" if the number is even? otherwise answer "no".')
    iteration = 3

    while iteration > 0:
        generate_number = randint (1, 99)
        print(f'Question: {generate_number}')
        user_answer = input('Your answer: ')

        if generate_number % 2 == 0:
            true_answer = 'yes'
        else:
            true_answer = 'no'

        if user_answer == true_answer:
            print('Correct!')
            iteration -= 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{true_answer}'.\nLet's try again, {user_name}!")      
            return
            
            
    if iteration == 0:
        print (f'Congratulations, {user_name}!')
