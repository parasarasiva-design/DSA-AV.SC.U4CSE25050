size = 10
def separate_chaining():
    table = [[] for i in range(size)]
    n = int(input("Enter number of elements: "))
    for i in range(n):
        key = int(input("Enter value: "))
        index = key % size
        table[index].append(key)
    print("Hash Table using Separate Chaining:")
    for i in range(size):
        print(i, ":", table[i])
def linear_probing():
    table = [None] * size
    n = int(input("Enter number of elements: "))
    for i in range(n):
        key = int(input("Enter value: "))
        index = key % size
        while table[index] is not None:
            index = (index + 1) % size
        table[index] = key
    print("Hash Table using Linear Probing:")
    for i in range(size):
        print(i, ":", table[i])
def quadratic_probing():
    table = [None] * size
    n = int(input("Enter number of elements: "))
    for i in range(n):
        key = int(input("Enter value: "))
        index = key % size
        j = 0
        while table[(index + j * j) % size] is not None and j < size:
            j += 1
        if j < size:
            table[(index + j * j) % size] = key
        else:
            print("Hash table is full")
    print("Hash Table using Quadratic Probing:")
    for i in range(size):
        print(i, ":", table[i])
while True:
    print("\n1. Separate Chaining")
    print("2. Linear Probing")
    print("3. Quadratic Probing")
    print("4. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:       separate_chaining()
    elif choice == 2:
        linear_probing()
    elif choice == 3:
        quadratic_probing()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
