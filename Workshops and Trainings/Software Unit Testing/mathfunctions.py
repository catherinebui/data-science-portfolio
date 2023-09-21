import math
import numpy as np


def addNumbers(x1, x2):
    '''
    Function: Add Two Numbers
    Inputs:
        *x1 accepts int or float
        *x2 accepts int or float
    Output:
        return number int if x1 and x2 are int and float otherwise
    '''
    return np.add(x1, x2)

def multiplyNumbers(x_list):
    '''
    Function: Multiply Numbers in a List
    Inputs:
        *x_list - List of Integers
    Output:
        Return Integer
    '''
    output_value = 1
    for x in x_list:
        output_value *= x
    return output_value


def deleteNthvalue(x_list, N):
    '''
    Function: Delete the Nth value of the List and Return a new List
    Inputs:
        *x_list - List of Integers
        *N (integer) - Index value of x_list
    Output:
        Return list of integers
    '''
    return x_list[:N] + x_list[N+1:]