# PRIORITY QUEUE USING MIN HEAP 

def heapify(arr,n,i):
    min = i
    l = (2*i)+1
    r = (2*i)+2
    if (l<n and arr[i]>arr[l]):
        min = l
    if (r<n and arr[min]>arr[r]):
        min = r
    if min !=i :
        arr[min], arr[i] = arr[i], arr[min]
        heapify(arr,n, min)
    
def insert(arr,val):
    arr.append(val)
    n = len(arr)
    for i in range((n // 2) - 1, -1, -1):
        heapify(arr, n, i)

def deleteNode(arr,val):
    n = len(arr)
    for i in range(0,n):
        if arr[i] == val:
            break
    arr[i] , arr[n-1] = arr[n-1], arr[i]
    del arr[n - 1]
    for i in range((len(arr) // 2) - 1, -1, -1):
        heapify(arr, len(arr), i)

def rootnode(arr):
    print(arr[0])

arr = []
insert(arr, 2)
insert(arr, 4)
insert(arr, 21)
insert(arr, 3)
insert(arr, 7)
insert(arr, 21)
insert(arr, 34)
insert(arr, 23)
insert(arr, 39)
insert(arr, 93)
insert(arr, 43)
insert(arr, 1)
print("min heap",arr)
deleteNode(arr,9)
deleteNode(arr,4)
print("min heap",arr)
print("After deleting an element: ", arr)
print("root node is:")
rootnode(arr)
