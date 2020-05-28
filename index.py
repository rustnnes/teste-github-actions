# import unittest

# def fun(x):
#     return x + 1

# class MyTest(unittest.TestCase):
#     def test(self):
#         self.assertEqual(fun(3), 5)

print('test 0')
assert sum([1, 2, 3]) == 6

print('test 1')
assert sum([1, 2, 3]) != 7

print('test 2 - fail')
assert sum([1, 2, 3]) == 8

print('all tests ok')