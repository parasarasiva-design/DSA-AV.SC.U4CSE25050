class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = []
        self.front = -1
        self.rear = -1

    def enqueue(self, x):
        if self.rear == self.size - 1:
            print("Queue Overflow")
        else:
            self.queue.append(x)

            if self.front == -1:
                self.front = 0

            self.rear = self.rear + 1
            print(x, "inserted into queue")

    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow")
        else:
            x = self.queue[self.front]
            self.front = self.front + 1
            print(x, "deleted from queue")

            if self.front > self.rear:
                self.front = -1
                self.rear = -1

    def display(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("Queue elements:")

            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")

            print()


size = int(input("Enter queue size: "))

q = Queue(size)

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
