import unittest
from utils.node import Node
from utils.stack import Stack


class test_Node(unittest.TestCase):
    def setUp(self):
        self.A = (5, None)
        self.B = ('a', self.A)

    def test_init(self):
        self.assertEqual((self.A[0], self.A[1]), (5, None))
        self.assertEqual((self.B[0], self.B[1]), ('a', self.A))


class test_Stack(unittest.TestCase):

    def setUp(self):
        self.A = (5, None)
        self.test_data = 'data1'

    def test_init(self):
        self.assertEqual(self.A, (5, None))

    def test_push(self):
        self.assertEqual(self.test_data, 'data1')



if __name__ == '__main__':
    unittest.main()
