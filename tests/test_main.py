import unittest
from utils.stack import Stack
from utils.queue import Queue
from utils.linked_list import LinkedList
from io import StringIO
from contextlib import redirect_stdout


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


class TestLinked_list(unittest.TestCase):

    def test_print_ll(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})

        out = StringIO()
        with redirect_stdout(out):
            ll.print_ll()
        self.assertEqual(out.getvalue().strip(), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")


    def test_to_list(self):
        ll1 = LinkedList()
        ll1.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll1.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll1.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll1.insert_beginning({'id': 0, 'username': 'serebro'})
        test_list = ll1.to_list()
        self.assertEqual(len(test_list), 4)
        self.assertEqual(test_list[0]['id'], 0)
        self.assertEqual(test_list[1]['id'], 1)
        self.assertEqual(test_list[2]['id'], 2)
        self.assertEqual(test_list[3]['id'], 3)

    def test_get_data_by_id(self):
        ll2 = LinkedList()
        ll2.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll2.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll2.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll2.insert_beginning({'id': 0, 'username': 'serebro'})
        self.assertEqual(ll2.get_data_by_id(0), {'id': 0, 'username': 'serebro'})
        self.assertEqual(ll2.get_data_by_id(1), {'id': 1, 'username': 'lazzy508509'})
        self.assertEqual(ll2.get_data_by_id(2), {'id': 2, 'username': 'mik.roz'})
        self.assertEqual(ll2.get_data_by_id(3), {'id': 3, 'username': 'mosh_s'})
        self.assertRaises(TypeError, ll2.get_data_by_id, 'n')

