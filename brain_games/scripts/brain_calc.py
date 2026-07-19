from random import randint, choice
from brain_games import cli


def main():
    user_name = cli.welcome_user()
    print('What is the result of the expression?')

    iteration = 3
    calc_lists = ['+', '-', '*']

    while iteration > 0:
        number_one = randint(0, 1000)
        number_two = randint(0, 1000)
        operand = choice(calc_lists)

        print(f'Question: {number_one} {operand} {number_two}')
        user_answer = input('Your answer: ')

        match operand: 
            case '+':
                correct_answer = number_one + number_two
            case '-':
                correct_answer = number_one - number_two
            case '*':
                correct_answer = number_one * number_two

  
        if int(user_answer) == correct_answer:
            print('Correct!')
            iteration -= 1
        else: 
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            return

        
        if iteration == 0:
            print(f'Congratulations, {user_name}')
        