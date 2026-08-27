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
            c=1
            temp=self.head
            while temp.next:
                c=c+1
                temp=temp.next
        print(c)
        
my_list = LinkedList()
my_list.insert_begin(10)
my_list.insert_begin(20)
my_list.insert_end(30)
my_list.insert_end(40)
my_list.insert_at_index(2,50)
print(my_list)
my_list.cont()

