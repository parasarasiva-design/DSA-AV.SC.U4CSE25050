class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, x):
        new_node = Node(x)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(x, "inserted into queue")
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
        else:
            x = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            print(x, "deleted from queue")
    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp = self.front
            print("Queue elements:")
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()
q = Queue()
while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        x = int(input("Enter element: "))
        q.enqueue(x)
    elif choice == 2:
        q.dequeue()
    elif choice == 3:
        q.display()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
