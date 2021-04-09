import random


class ComputerAssistedProgram:

    @staticmethod
    def random_addition(num1, num2):
        num1 = random.randint(50, 100)
        num2 = random.randint(50, 100)

        answer = int(input(f'What is {num1}  +  {num2} : '))
        if answer == num1 + num2:
            print('Well-done, you got it right')
        else:
            print('Incorrect answer, try again')
            while answer != num1 + num2:
                answer = int(input(f'What is {num1}  +  {num2} : '))
                if answer == num1 + num2:
                    print('Well-done, you got it right')
                else:
                    print('Incorrect answer, try again')

    random_addition()

    # @staticmethod
    # def random_subtraction(self):
    #     num1 = random.randint(50, 100)
    #     num2 = random.randint(20, 40)
    #
    #     answer = int(input(f'What is {num1}  -  {num2} : '))
    #     if answer == num1 - num2:
    #         print('Well-done, you got it right')
    #     else:
    #         print('Incorrect answer, try again')
    #         while answer != num1 + num2:
    #             answer = int(input(f'What is {num1}  -  {num2} : '))
    #             if answer == num1 + num2:
    #                 print('Well-done, you got it right')
    #             else:
    #                 print('Incorrect answer, try again')
    #
    # random_subtraction()

