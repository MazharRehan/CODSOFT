"""
TASK 2: CALCULATOR - CONSOLE
Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result
"""


def calculator():
    try:
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
    except ValueError:
        print('Invalid input. Please enter a number.')
        return

    print('Select operation:')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Modulus')

    choice = input('Enter choice (1/2/3/4/5): ')

    if choice == '1':
        result = num1 + num2
        print(f'Result: {result}')
    elif choice == '2':
        result = num1 - num2
        print(f'Result: {result}')
    elif choice == '3':
        result = num1 * num2
        print(f'Result: {result}')
    elif choice == '4':
        if num2 == 0:
            print('Cannot divide by zero.')
        else:
            result = num1 / num2
            print(f'Result: {result}')
    elif choice == '5':
        if num2 == 0:
            print('Cannot perform modulus by zero.')
        else:
            result = num1 % num2
            print(f'Result: {result}')
    else:
        print('Invalid choice.')


if __name__ == '__main__':
    calculator()
