from random import randint

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key 


n = 20
arr = [randint(1,31) for i in range(n)]
print(arr)
insertion_sort(arr)
print(arr)
