class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")
def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    return search(root.left, key) or search(root.right, key)
def find_min(root):
    while root.left:
        root = root.left
    return root
def delete(root, key):
    if root is None:
        return None
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    return root
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
def count_leaf_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)
def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))
def display(root):
    print("Inorder Traversal: ", end="")
    inorder(root)
    print()
    print("Preorder Traversal: ", end="")
    preorder(root)
    print()
    print("Postorder Traversal: ", end="")
    postorder(root)
    print()
root = None
while True:
    print("\n1. Insert")
    print("2. Inorder Traversal")
    print("3. Preorder Traversal")
    print("4. Postorder Traversal")
    print("5. Search")
    print("6. Delete")
    print("7. Count Nodes")
    print("8. Count Leaf Nodes")
    print("9. Height")
    print("10. Display")
    print("11. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = int(input("Enter value to insert: "))
        root = insert(root, value)
    elif choice == 2:
        inorder(root)
        print()
    elif choice == 3:
        preorder(root)
        print()
    elif choice == 4:
        postorder(root)
        print()
    elif choice == 5:
        key = int(input("Enter value to search: "))
        if search(root, key):
            print("Element found.")
        else:
            print("Element not found.")
    elif choice == 6:
        key = int(input("Enter value to delete: "))
        root = delete(root, key)
        print("Element deleted if present.")
    elif choice == 7:
        print("Total nodes:", count_nodes(root))
    elif choice == 8:
        print("Leaf nodes:", count_leaf_nodes(root))
    elif choice == 9:
        print("Height:", height(root))
    elif choice == 10:
        display(root)
    elif choice == 11:
        print("Program terminated.")
        break
    else:
        print("Invalid choice.")
