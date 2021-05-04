# Insertion Sort
import random 


def insertionSort(arr):
  
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
        
        
B = []
for x in range(10):
    b = random.randint(-50, 50)
    B.append(b)
    
print("Array B:", B)
print('-'*50)
insertionSort(B)
print("Sorted array:")
for i in range(len(B)):
    print("%d" %B[i])