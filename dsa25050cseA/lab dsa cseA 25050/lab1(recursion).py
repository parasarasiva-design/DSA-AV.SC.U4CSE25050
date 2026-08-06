'''def count(n):
    print(n)
    if n>0:
        return count(n-1)
    else:
      return 0
n=int(input("Enter a number to start countdown:"))
count(n)
print("LAUNCH----->")'''



'''def fib_series(n):
    a=0
    b=1
    c=a+b
    for i in range(n):
          a=b
          b=c
          c=a+b
          print(c)
n=int(input("Enter n value:"))
a=0
b=1
c=a+b
print(a)
print(b)
print(c)
fib_series(n)'''


'''def fact(n):
     if n==0:
         return 1
     elif n==1:
         return 1
     else:
        return n*fact(n-1)

n=int(input("Enter a number to start arrangment:"))
a=fact(n)
print(a)'''



'''def power(p,n):
    if n==0:
        return 1
    else:
        return p*power(p,n-1)
    
p=int(input("Enter p number to start calculation:"))
n=int(input("Enter n number to start calculation:"))
a=power(p,n)
print(a)  '''


def search(emp_list,key):
    n=len(emp_list)
    for i in range(n):
        if emp_list[i]==key:
            print(f"key found at {i} position")
        
emp_list=[10,2,9,4,567,69,99]
key=int(input("enter a key to search in the emp id list"))
search(emp_list,key)

def search_empire(emp_list, target, index=0):
      if index == len(emp_list):
    return False

  if emp_list[index] == target:
    return True

  return search_empire(emp_list, target, index + 1)



empires = ["Roman", "Ottoman", "Persian", "Mauryan"]
target_empire = "Persian"

found = search_empire(empires, target_empire)
print(f"\nIs {target_empire} in the list? {found}")































