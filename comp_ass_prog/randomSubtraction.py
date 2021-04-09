import random


def random_subtraction():

    num1 = random.randint(50, 100)
    num2 = random.randint(50, 100)

    selection = int(input('press 1 to start subtraction quiz or press 0 to quit : \n '))
    while selection == 1:
        answer = int(input(f'What is {num1}  -  {num2} : '))

        if answer == 0:
            break
        elif answer == num1 - num2:
            print('Well-done, you got it right')

        else:
            print('Incorrect answer, try again')

        while answer != num1 - num2:
            answer = int(input(f'What is {num1}  -  {num2} : '))
            if answer == num1 - num2:
                print('Well-done, you got it right')
            else:
                print('Incorrect answer, try again')


random_subtraction()
