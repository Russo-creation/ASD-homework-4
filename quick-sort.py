def partition(A, p, r):
    pivot = A[r]
    smaller = p # index of smaller element
    for j in range(p, r):
        if A[j] <= pivot: 
            A[smaller], A[j] = A[j], A[smaller] # Swap A[smaller] and A[r]
            smaller = smaller + 1 # index of smaller element + 1
    A[smaller], A[r] = A[r], A[smaller] # Swap A[smaller] and A[r]
    return (smaller)
    
def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)

#A = [24, 21,1,3,4,80,64,4,3,45,2,67,16,24,51,23,71,24,5,2,1,0,42,4,6,7,5,1,23,34,32,21] #losowa 
#A = [0,1,1,1,2,2,3,3,4,4,4,5,5,6,7,16,21,21,23,23,24,24,24,32,34,42,45,51,64,67,71,80] #posortowana
A = [80,71.67,64,51,45,42,34,32,24,24,24,23,23,21,21,16,7,6,5,5,4,4,4,3,3,2,2,1,1,1,0] #odwrotnie posortowana

n = len(A)
quickSort(A, 0, n-1)

for i in A:
    print(i)

