from utils.node import Node


class LinkedList:
    """
    Класс, хранящий ссылку на начало и конец связанного списка,
    т.е. первый и последний Node
    """

    def __init__(self, tail=None, head=None):
        self.tail = tail
        self.head = head

    def insert_beginning(self, data):
        """
        Принимает данные и добавляет узел с этими данными в начало связанного списка
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data):
        """
        Принимает данные и добавляет узел с этими данными в конец связанного списка
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def print_ll(self):
        """
        Метод вывода данных из односвязанного списка
        """
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        print(ll_string)


ll = LinkedList()
ll.insert_beginning({'id': 1})
ll.insert_at_end({'id': 2})
ll.insert_at_end({'id': 3})
ll.insert_beginning({'id': 0})
ll.print_ll()





