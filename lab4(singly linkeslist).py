class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_begin(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new
my_list = LinkedList()
my_list.insert_begin(10)
my_list.insert_begin(20)
print(my_list)
