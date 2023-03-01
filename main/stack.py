class Stack:

    def __init__(self):
        self.top = Node()

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node