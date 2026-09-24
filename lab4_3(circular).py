class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
    def create(self):
        n = int(input("Enter number of nodes: "))
        for i in range(n):
            data = int(input("Enter element: "))
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                new_node.next = self.head
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = new_node
                new_node.next = self.head
    def insert_beginning(self):
        data = int(input("Enter element: "))
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            self.head = new_node
            temp.next = self.head
    def insert_index(self):
        data = int(input("Enter element: "))
        index = int(input("Enter index: "))
        if index == 0:
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                new_node.next = self.head
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                new_node.next = self.head
                self.head = new_node
                temp.next = self.head
            return
        temp = self.head
        for i in range(index - 1):
            if temp.next == self.head:
                print("Invalid index")
                return
            temp = temp.next
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
    def insert_end(self):
        data = int(input("Enter element: "))
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
    def delete_value(self):
        value = int(input("Enter value to delete: "))
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == value:
            self.delete_first()
            return
        temp = self.head
        while temp.next != self.head:
            if temp.next.data == value:
                temp.next = temp.next.next
                print(value, "deleted")
                return
            temp = temp.next
        print("Value not found")
    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            self.head = self.head.next
            temp.next = self.head
    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            while temp.next.next != self.head:
                temp = temp.next
            temp.next = self.head
    def count(self):
        if self.head is None:
            print("Number of nodes: 0")
            return
        count = 0
        temp = self.head
        while True:
            count = count + 1
            temp = temp.next
            if temp == self.head:
                break
        print("Number of nodes:", count)
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            print("Circular Linked List")
            while True:
                print(temp.data, end=" -> ")
                temp = temp.next
                if temp == self.head:
                    break
            print("(head)")
l = CircularLinkedList()
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
