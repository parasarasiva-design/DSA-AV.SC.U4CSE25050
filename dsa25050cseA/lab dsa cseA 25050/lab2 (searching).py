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
 
'''def binary_search (arr, k) :
   low=0;
   high=len (arr)-1;
   while low <= high:
       mid=(low+high) //2
       if k == arr [mid] :
          return mid;
       elif k <arr[mid] :
          high=mid-1;
       else:
           low=mid+1;
   return-1;
n=int(input("enter the no of elements:"))
arr=[];
for i in range(n) :
   arr.append (int (input ("enter the element:") ))
k=int (input ("enter the search element:"))
print (binary_search (arr, k) )
'''
