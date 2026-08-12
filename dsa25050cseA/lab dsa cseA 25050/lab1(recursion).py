'''def count(n):
    print(n)
    if n>0:
        return count(n-1)
    else:
      return 0
n=int(input("Enter a number to start countdown:"))
count(n)
print("LAUNCH----->")'''



'''def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


n = int(input("Enter n value: "))

for i in range(n):
    print(fib(i))'''


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


'''def search_employee(arr, id, index):
    if index == len(arr):
        return -1

    if arr[index] == id:
        return index

    return search_employee(arr, id, index + 1)


employees = [101, 102, 103, 104, 105]

id = int(input("Enter employee ID to search: "))

result = search_employee(employees, id, 0)

if result == -1:
    print("Employee ID not found")
else:
    print("Employee ID found at position", result)'''































