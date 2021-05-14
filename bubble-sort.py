def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
  

#A = [24, 21,1,3,4,80,64,4,3,45,2,67,16,24,51,23,71,24,5,2,1,0,42,4,6,7,5,1,23,34,32,21] #losowa 
#A = [0,1,1,1,2,2,3,3,4,4,4,5,5,6,7,16,21,21,23,23,24,24,24,32,34,42,45,51,64,67,71,80] #posortowana
A = [80,71.67,64,51,45,42,34,32,24,24,24,23,23,21,21,16,7,6,5,5,4,4,4,3,3,2,2,1,1,1,0] #odwrotnie posortowana

bubbleSort(A)
  
for i in A:
    print(i)