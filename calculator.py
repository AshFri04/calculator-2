"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def calculator():
    print 'To use the caluculator enter the operation in the format: \"operator num1 num2\"'
    user_input = raw_input('>')
    try:
        input_list = user_input.split(" ")
        print "input list: ", input_list
    except:
        print "Hmmm, I didn\'t catch that. Please try again using the valid format: \"operator num1 num2\""
        calculator()
calculator()