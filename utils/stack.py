from utils.node import Node


class Stack:
    """Класс, реализующий структуру данных, представляющая из себя упорядоченный набор элементов,
    в которой добавление новых элементов и удаление существующих производится с одного конца,
    называемого вершиной стека. Притом первым из стека удаляется элемент, который был помещен туда последним,
    то есть в стеке реализуется стратегия «последним вошел — первым вышел» (last-in, first-out — LIFO).
    """

    def __init__(self):
        self.elements = []
        self.top = None

    def push(self, data):
        """
        Добавляет в стэк элемент в виде узла Node
        """
        if len(self.elements) == 0:
            new_node = Node(data)
        else:
            new_node = Node(data, self.top)
        self.top = new_node
        return self.elements.append(new_node)

