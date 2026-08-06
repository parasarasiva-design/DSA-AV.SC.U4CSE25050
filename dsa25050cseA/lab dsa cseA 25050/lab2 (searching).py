'''def lin_search(num,key):
    for i in range(n):
        if num[i]==key:
            return i
    return -1
num=[]
n=int(input("enter num of elements in list"))
for i in range(n):
    p=int(input())
    num.append(p)
key=int(input("enter key to find in list"))
result=lin_search(num,key)
if result==-1:
    print("Element not found in list")
else:
    print(f"element found at {result}")
'''