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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        """
        Удаляет из очереди крайний левый элемент (первый добавленный)
        :return: Удаленный экземпляр класса Node
        """
        if self.head is None:
            return None
        else:
            deleted_node_object = self.head.data
            self.head = self.head.next_node
            return deleted_node_object

