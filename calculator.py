"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calculator():
    user_input = raw_input('>')
    if quitting(user_input):
        return
    try: 
        num1, num2, operator = get_nums(user_input)
        do_calculation(num1, num2, operator) 
    except:
        throw_exception()

def init():
    print 'To use the calculator enter the operation in the format: \"operator num1 num2\"'
    calculator()

def throw_exception():
    print "Hmmm, I didn\'t catch that. Please try again using the valid format: \"operator num1 num2\""
    calculator()


def quitting(user_input):
    return (user_input == 'q') or (user_input == 'Q')

def get_nums(user_input):
    input_list = user_input.split(" ")
    operator = input_list[0]
    nums = list(map(lambda x: int(x), input_list[1:]))
    num1 = float(nums[0])
    num2 = float(nums[1]) or None
    return num1, num2, operator   

def do_calculation(num1, num2, operator):
    if operator == '+':
        print add(num1, num2)
    elif operator == '-':
        print subtract(num1, num2)
    elif operator == '*':
        print multiply(num1, num2)
    elif operator == '/':
        print divide(num1, num2)
    elif operator == 'square' and num2 == None:
        print square(num1)
    elif operator == 'cube' and num2 == None:
        print cube(num1)
    elif operator == 'power':
        print power(num1, num2)
    elif operator == 'mod':
        print mod(num1, num2)
    else:
        print "Hmmm, I didn\'t catch that. Please try again using the valid format: \"operator num1 num2\""
    calculator()

init()