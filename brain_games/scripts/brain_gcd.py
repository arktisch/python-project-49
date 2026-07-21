import random
from brain_games import cli


def main():
    user_name = cli.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    
    iteration = 3

    while iteration > 0:
        number_one = random.randint(1, 100)
        number_two = random.randint(1, 100)
        max_gcd = 1

        print(f'Question: {number_one} {number_two}')

        user_answer = input('Your answer: ')

        if number_one < number_two:      #если первое число меньше, то возьмем его за максимальный делитель
            for i in range (1, number_one + 1): # проверить все числа от 1 до максимального делителя
                if number_one % i == 0 and number_two % i == 0: #если оба числа делятся без остатка
                    max_gcd = i

        if number_one > number_two:      #если второе число меньше, то возьмем его за максимальный делитель
            for i in range (1, number_two + 1):
                if number_one % i == 0 and number_two % i == 0:
                    max_gcd = i

        if number_one == number_two:
            max_gcd = number_one

        if max_gcd == int(user_answer):
            print('Correct!')
            iteration -= 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{max_gcd}'.\nLet's try again, {user_name}!")
            return


    if iteration == 0:
        print(f'Congratulations, {user_name}!')
