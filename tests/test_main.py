import unittest
from utils.stack import Stack
from utils.queue import Queue

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

class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        assert queue.head.data == 'data1'
        assert queue.head.next_node.data == 'data2'
        assert queue.tail.data == 'data3'
        assert queue.tail.next_node is None

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        assert queue.dequeue() == 'data1'
        assert queue.dequeue() == 'data2'
        assert queue.dequeue() == 'data3'
        assert queue.dequeue() is None



