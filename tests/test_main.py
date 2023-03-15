import unittest
from utils.stack import Stack


class test_data(unittest.TestCase):
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')
    stack.pop()


    def test_data(self):
        self.assertEqual(self.stack.top.data, 'data2')
        self.assertEqual(self.stack.top.next_node.data, 'data1')

    def test_pop(self):
        stack = Stack()
        self.assertEqual(stack.pop(), None)
        stack.push('data1')
        stack.push('data2')
        self.assertEqual(stack.pop(), 'data2')



