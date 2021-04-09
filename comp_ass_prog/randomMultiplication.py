import random


def random_multiplication():

    num1 = random.randint(5, 10)
    num2 = random.randint(5, 10)

    selection = int(input('press 1 to start multiplication quiz or press 0 to quit : \n '))
    while selection == 1:
        answer = int(input(f'What is {num1}  *  {num2} : '))

        if answer == 0:
            break
        elif answer == num1 * num2:
            print('Well-done, you got it right')

        else:
            print('Incorrect answer, try again')

        while answer != num1 * num2:
            answer = int(input(f'What is {num1} * {num2} : '))
            if answer == num1 * num2:
                print('Well-done, you got it right')
            else:
                print('Incorrect answer, try again')


random_multiplication()
