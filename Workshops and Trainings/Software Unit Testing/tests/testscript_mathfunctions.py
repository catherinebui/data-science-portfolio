import os, sys, inspect
import unittest
import numpy as np
import math
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
currentdir_basename = os.path.basename(currentdir)
parentdir = os.path.dirname(currentdir).replace(os.sep, '/')
sys.path.insert(0, parentdir)
import mathfunctions
# from file_name import class_name

'''
Test Script for User Defined Math Functions
'''
class TestScript_MathFunctions(unittest.TestCase):
    def __init__(self, methodName, *args, **kwargs):
        super(TestScript_MathFunctions, self).__init__(methodName = methodName)
        ## self.study = study
        ## self.df1 = 
        ## self.df2 = 
    def test1_addNumbers(self):
        '''
        Testing the addNumbers function from mathfunctions module
        '''
        ## self.assertEqual(df1.shape[0], df2.shape[0]) ## number of records in df1 and df2
        with self.subTest("Test1a - Check that addNumbers works as expected"):
            self.assertEqual(mathfunctions.addNumbers(5, 10), 15)
        with self.subTest('Test1b- Check that addNumbers works as expected with python in system addition'):
            self.assertEqual(mathfunctions.addNumbers(5, 5), 5 + 5)
        with self.subTest('Test1c- Check that addNumbers works as expected with another addition method'):
            self.assertEqual(mathfunctions.addNumbers(5, 5), sum([5,5]))

    def test2_multiplyNumbers(self):
        '''
        Testing the multiplyNumbers function from mathfunctions module
        '''
        x_list = [5, 2, 10, 20]
        self.assertEqual(mathfunctions.multiplyNumbers(x_list), np.prod(x_list))

    def test3_deleteNthNumbers(self):
        '''
        Testing the deleteNthvalue function from mathfunctions module
        '''
        with self.subTest('Test3a - check that function works as expected'):
            x_list = [4, 5, 2, 3, 2]
            self.assertEqual(mathfunctions.deleteNthvalue(x_list, 2), [4,5,3,2])
        with self.subTest('Test3b - Check function with another method such as list pop'):
            x_list = [4, 5, 2, 3, 2]
            output_from_deleteNthvalue = mathfunctions.deleteNthvalue(x_list, 2)
            x_list.pop(2)
            output_from_pop = x_list
            self.assertEqual(output_from_deleteNthvalue, output_from_pop)
        with self.subTest():
            x_list = [4, 5, 2, 3, 2]
            print(mathfunctions.deleteNthvalue(x_list, -6))          
            self.assertEqual(mathfunctions.deleteNthvalue(x_list, -6), [4,5,2,3,2])


def suite():
    '''
    Adding Tests from TestScript objects into a Collection/Suite of Tests
    '''
    suite = unittest.TestSuite()
    test_loader = unittest.TestLoader()
    testscript1_names = sorted(test_loader.getTestCaseNames(TestScript_MathFunctions), key = lambda x:  int(x.split('_')[0][4:]))
    for test_name in testscript1_names:
        suite.addTest(TestScript_MathFunctions(methodName = test_name))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(suite())
