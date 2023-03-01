class Node:
    def __init__(self,data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:

    def __init__(self):
        self.top = Node()

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node


n1 = Node(5, None)
n2 = Node('a', n1)
print(n1.data)
print(n2.data)
print(n1)
print(n2.next_node)

stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')
print(stack.top.data)
print(stack.top.next_node.data)
print(stack.top.next_node.next_node.data)
print(stack.top.next_node.next_node.next_node)
print(stack.top.next_node.next_node.next_node.data)

