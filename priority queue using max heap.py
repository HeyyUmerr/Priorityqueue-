# PRIORITY QUEUE USING MAX HEAP 
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def insert(array, newNum):
    array.append(newNum)
    size = len(array)
    for i in range((size // 2) - 1, -1, -1):
            heapify(array, size, i)

def deleteNode(array, num):
    size = len(array)
    for i in range(0, size):
        if num == array[i]:
            break
    array[i], array[size - 1] = array[size - 1], array[i]
    del array[size - 1]
    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)

def rootnode(array):
    print(array[0])


arr = []
insert(arr, 1)
insert(arr, 43)
insert(arr, 4)
insert(arr, 21)
insert(arr, 9)
insert(arr, 29)
insert(arr, 50)
print("max heap",arr)
# deleteNode(arr,9)
# print("After deleting an element: ", arr)
# print("root node is:")
# rootnode(arr)
