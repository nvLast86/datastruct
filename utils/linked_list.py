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

    def to_list(self) -> list:
        """
        Возвращает список с данными, содержащимися в
        односвязном списке LinkedList
        """
        output_data = []
        while self.head:
            output_data.append(self.head.data)
            if self.head.next_node:
                self.head = self.head.next_node
            else:
                break
        return output_data

    def get_data_by_id(self, id):
        while self.head:
            if self.head.data['id'] == id:
                return self.head.data
            else:
                self.head = self.head.next_node

ll = LinkedList()

ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
ll.insert_beginning({'id': 0, 'username': 'serebro'})

# lst = ll.to_list()
# for item in lst: print(item)


user_data = ll.get_data_by_id(2)
print(user_data)