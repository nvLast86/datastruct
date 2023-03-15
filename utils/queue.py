from utils.node import Node


class Queue:
    """
    Класс Queue ("Очередь"), инициализируется двумя аттрибутами: начало и конец очереди
    """
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        """
        Метод для добавления данных в очередь
        """
        new_node = Node(data)
        if self.head = = None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

