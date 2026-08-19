'''def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
arr = []
n = int(input("Enter num of elements: "))
for i in range(n):
    p = int(input("Enter element: "))
    arr.append(p)
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)'''


'''def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr
arr = []
n = int(input("Enter num of elements: "))
for i in range(n):
    p = int(input("Enter element: "))
    arr.append(p)
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)'''


'''def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
arr = []
n = int(input("Enter num of elements: "))
for i in range(n):
    p = int(input("Enter element: "))
    arr.append(p)
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)'''

'''
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return arr
arr = []
n = int(input("Enter num of elements: "))

for i in range(n):
    p = int(input("Enter element: "))
    arr.append(p)

sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)'''

'''def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = []
    right = []
    for i in range(len(arr) - 1):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left) + [pivot] + quick_sort(right)
arr = []
n = int(input("Enter num of elements: "))
for i in range(n):
    p = int(input("Enter element: "))
    arr.append(p)
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)

'''
