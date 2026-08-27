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
    def insert_end(self,data):
        new=Node(data)
        if self.head==None:
            self.head=new
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new
    def insert_at_index(self,index,data):
        if index==0:
            self.insert_begin(data)
            return
        new=Node(data)
        temp=self.head
        for i in range(index-1):
            temp=temp.next
        new.next=temp.next
        temp.next=new
    def cont(self):
        if self.head==None:
            print("there r no items")
        else:
            c=0
            temp=self.head
            while temp.next:
                c=c+1
                temp=temp.next
        print(c)
    def del_begin(self,data):
        if self.head==None:
            return
        else:
            temp=self.head
            self.head=temp.next
    def del_at_end(self,data):
        if self.head is None:
            print('there r no elements')
        temp=self.head
        temp1=temp
        while temp.next:
            temp1=temp
            temp=temp.next
        temp1.next=None
    def del_at_index(self,index,data):
        if index==0:
            self.del_begin(data)
        else:
            temp=self.head
            for i in range(index-1):
                temp=temp.next
        
my_list = LinkedList()
my_list.insert_begin(10)
my_list.insert_begin(20)
my_list.insert_end(30)
my_list.insert_end(40)
my_list.insert_at_index(2,50)
print(my_list)
my_list.cont()
while True:
    print("\n--- operations ---")
    print("1. insert_begin")
    print("2. insert_end")
    print("3. insert_at_index")
    print("4. del_begin")
    print("5. del_at_end")
    print("6. del_at_index")
    print("7. print_list")
    print("8. cont")
    print("9. exit")
    
    choice = int(input("\nEnter choice: "))
    
    if choice == 1:
        data = int(input("Enter data: "))
        my_list.insert_begin(data)
        
    elif choice == 2:
        data = int(input("Enter data: "))
        my_list.insert_end(data)
        
    elif choice == 3:
        index = int(input("Enter index: "))
        data = int(input("Enter data: "))
        my_list.insert_at_index(index, data)
        
    elif choice == 4:
        my_list.del_begin()
        
    elif choice == 5:
        my_list.del_at_end()
        
    elif choice == 6:
        index = int(input("Enter index: "))
        my_list.del_at_index(index)
        
    elif choice == 8:
        my_list.cont()
        
    elif choice == 7:
        my_list.print_list()
        
    elif choice == 9:
        print("exiting...")
        break
        
    else:
        print("invalid choice")


