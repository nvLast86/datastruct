from utils.node import Node


class Stack:
    """Класс, реализующий структуру данных, представляющая из себя упорядоченный набор элементов,
    в которой добавление новых элементов и удаление существующих производится с одного конца,
    называемого вершиной стека. Притом первым из стека удаляется элемент, который был помещен туда последним,
    то есть в стеке реализуется стратегия «последним вошел — первым вышел» (last-in, first-out — LIFO).
    """

    def __init__(self):
        self.top = None

    def push(self, data):
        """
        Добавляет в стэк элемент в виде узла Node
        """
        next_node = self.top
        new_top = Node(data, next_node)
        self.top = new_top

    def pop(self):
        """
        Удаляет и возвращает верхний элемент стэка
        """
        remove = self.top
        self.top = self.top.next_node
        return remove.data

