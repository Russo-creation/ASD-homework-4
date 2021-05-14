def max_heapify(A, heap_size, i):
    l = 2 * i + 1
    r = 2 * i + 2
    
    if(l< heap_size and A[l] > A[i]):
        largest = l
    else:
        largest = i
    if (r< heap_size and A[r] > A[largest]):
        largest = r
    if (i!=largest):
        A[largest], A[i] = A[i], A[largest]
        max_heapify(A, heap_size, largest)
  
def build_max_heap(A):
    heap_size = len(A)

    for i in range(heap_size // 2 - 1, -1, -1):
        max_heapify(A, heap_size , i)
        
def heap_sort(A):
    build_max_heap(A)
    heap_size = len(A)
    
    for i in range(heap_size-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        max_heapify(A, i, 0)

#A = [24, 21,1,3,4,80,64,4,3,45,2,67,16,24,51,23,71,24,5,2,1,0,42,4,6,7,5,1,23,34,32,21] #losowa 
#A = [0,1,1,1,2,2,3,3,4,4,4,5,5,6,7,16,21,21,23,23,24,24,24,32,34,42,45,51,64,67,71,80] #posortowana
A = [80,71.67,64,51,45,42,34,32,24,24,24,23,23,21,21,16,7,6,5,5,4,4,4,3,3,2,2,1,1,1,0] #odwrotnie posortowana

heap_sort(A)

for i in A:
    print(i)