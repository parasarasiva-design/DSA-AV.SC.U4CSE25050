class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def create(self):
        n = int(input("Enter number of nodes: "))
        for i in range(n):
            data = int(input("Enter element: "))
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                temp = self.head

                while temp.next is not None:
                    temp = temp.next
                temp.next = new_node
                new_node.prev = temp
    def insert_beginning(self):
        data = int(input("Enter element: "))
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    def insert_index(self):
        data = int(input("Enter element: "))
        index = int(input("Enter index: "))
        if index == 0:
            self.insert_beginning()
            return
        temp = self.head
        for i in range(index - 1):
            if temp is None:
                print("Invalid index")
                return
            temp = temp.next
        if temp is None:
            print("Invalid index")
            return
        new_node = Node(data)
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next is not None:
            temp.next.prev = new_node
        temp.next = new_node
    def insert_end(self):
        data = int(input("Enter element: "))
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
    def delete_value(self):
        value = int(input("Enter value to delete: "))
        temp = self.head
        while temp is not None:
            if temp.data == value:
                if temp.prev is not None:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next is not None:
                    temp.next.prev = temp.prev
                print(value, "deleted")
                return
            temp = temp.next
        print("Value not found")
    def delete_first(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.next

            if self.head is not None:
                self.head.prev = None
    def delete_last(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            if temp.prev is None:
                self.head = None
            else:
                temp.prev.next = None
    def count(self):
        count = 0
        temp = self.head
        while temp is not None:
            count = count + 1
            temp = temp.next
        print("Number of nodes:", count)
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            print("Doubly Linked List:")
            while temp is not None:
                print(temp.data, end=" <-> ")
                temp = temp.next
            print("None")
l = DoublyLinkedList()
while True:
    print("\n1. Create linked list")
    print("2. Insert at beginning")
    print("3. Insert at specified index")
    print("4. Insert at end")
    print("5. Delete by value")
    print("6. Delete first node")
    print("7. Delete last node")
    print("8. Count number of nodes")
    print("9. Display / Traverse")
    print("10. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        l.create()
    elif choice == 2:
        l.insert_beginning()
    elif choice == 3:
        l.insert_index()
    elif choice == 4:
        l.insert_end()
    elif choice == 5:
        l.delete_value()
    elif choice == 6:
        l.delete_first()
    elif choice == 7:
        l.delete_last()
    elif choice == 8:
        l.count()
    elif choice == 9:
        l.display()
    elif choice == 10:
        break
    else:
        print("Invalid choice")
