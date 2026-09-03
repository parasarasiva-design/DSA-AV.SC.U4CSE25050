class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def push(self, item):
        if self.top == self.size - 1:
            print("Stack overflow")
        else:
            self.top = self.top + 1
            self.stack[self.top] = item
            print(item, "pushed into stack")

    def pop(self):
        if self.top == -1:
            print("Stack underflow")
        else:
            item = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            print(item, "popped from stack")

    def peek(self):
        if self.top == -1:
            print("Stack is empty")
            return None
        else:
            print("Top element:", self.stack[self.top])
            return self.stack[self.top]

    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Stack elements:", end=" ")
            for i in range(self.top, -1, -1):
                print(self.stack[i], end=" ")
            print()

# Test the stack with a size of 5
my_stack = Stack(5)
my_stack.push(10)
my_stack.push(30)
my_stack.display()
my_stack.push(20)
my_stack.display()
my_stack.push(40)
my_stack.pop()
my_stack.peek()
my_stack.display()






































    
