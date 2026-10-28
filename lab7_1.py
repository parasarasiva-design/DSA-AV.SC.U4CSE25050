MAX = 100
tree = [None] * MAX
def insert(value, index=0):
    if index >= MAX:
        print("Tree is full.")
        return
    if tree[index] is None:
        tree[index] = value
        print(value, "inserted.")
        return
    if value < tree[index]:
        insert(value, 2 * index + 1)
    else:
        insert(value, 2 * index + 2)
def inorder(index=0):
    if index >= MAX or tree[index] is None:
        return
    inorder(2 * index + 1)
    print(tree[index], end=" ")
    inorder(2 * index + 2)
def preorder(index=0):
    if index >= MAX or tree[index] is None:
        return
    print(tree[index], end=" ")
    preorder(2 * index + 1)
    preorder(2 * index + 2)
def postorder(index=0):
    if index >= MAX or tree[index] is None:
        return
    postorder(2 * index + 1)
    postorder(2 * index + 2)
    print(tree[index], end=" ")
def search(value, index=0):
    if index >= MAX or tree[index] is None:
        return False

    if tree[index] == value:
        return True

    if value < tree[index]:
        return search(value, 2 * index + 1)
    else:
        return search(value, 2 * index + 2)


def count_nodes(index=0):
    if index >= MAX or tree[index] is None:
        return 0

    return 1 + count_nodes(2 * index + 1) + count_nodes(2 * index + 2)


def count_leaf_nodes(index=0):
    if index >= MAX or tree[index] is None:
        return 0

    if tree[2 * index + 1] is None and tree[2 * index + 2] is None:
        return 1
    return count_leaf_nodes(2 * index + 1) + count_leaf_nodes(2 * index + 2)
def height(index=0):
    if index >= MAX or tree[index] is None:
        return 0
    return 1 + max(height(2 * index + 1), height(2 * index + 2))
def display():
    print("Inorder traversal: ", end="")
    inorder()
    print()
    print("Preorder traversal: ", end="")
    preorder()
    print()
    print("Postorder traversal: ", end="")
    postorder()
    print()
while True:
    print("\n1. Insert")
    print("2. Inorder Traversal")
    print("3. Preorder Traversal")
    print("4. Postorder Traversal")
    print("5. Search")
    print("6. Count Nodes")
    print("7. Count Leaf Nodes")
    print("8. Height")
    print("9. Display")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to insert: "))
        insert(value)
    elif choice == 2:
        inorder()
        print()
    elif choice == 3:
        preorder()
        print()
    elif choice == 4:
        postorder()
        print()
    elif choice == 5:
        value = int(input("Enter value to search: "))
        if search(value):
            print("Element found.")
        else:
            print("Element not found.")
    elif choice == 6:
        print("Total nodes:", count_nodes())
    elif choice == 7:
        print("Leaf nodes:", count_leaf_nodes())
    elif choice == 8:
        print("Height:", height())
    elif choice == 9:
        display()
    elif choice == 10:
        print("Program terminated.")
        break
    else:
        print("Invalid choice.")

