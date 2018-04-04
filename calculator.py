"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


def calculator():
    print 'To use the caluculator enter the operation in the format: \"operator num1 num2\"'
    user_input = raw_input('>')
    if user_input == 'q' or user_input == 'Q':
        return
    try:
        input_list = user_input.split(" ")
        operator = input_list[0]
        nums = list(map(lambda x: int(x), input_list[1:]))
        print "Type of nums: ", type(nums[0])
        print "input list: ", input_list
        num1 = float(nums[0])
        num2 = float(nums[1]) or None    
        
        if operator == '+':
            print add(num1, num2)
        elif operator == '-':
            print subtract(num1, num2)
        elif operator == '*':
            print multiply(num1, num2)
        elif operator == '/':
            print divide(num1, num2)
        elif operator == 'square':
            print square(num1)
        elif operator == 'cube':
            print cube(num1)
        elif operator == 'power':
            print power(num1, num2)
        elif operator == 'mod':
            print mod(num1, num2)
        else:
            print "Hmmm, I didn\'t catch that. Please try again using the valid format: \"operator num1 num2\""
            calculator()

    except:
        print "Hmmm, I didn\'t catch that. Please try again using the valid format: \"operator num1 num2\""
        calculator()
calculator()