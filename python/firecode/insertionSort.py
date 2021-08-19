def insertionSort( A ):
    j = 1
    while ( j < len(A)):
        i = j - 1
        while ( i >= 0 ):
            if A[i] > A[i+1]:
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp
            i = i - 1
        j = j + 1
    return A

def quicksort(arr, start_index, end_index):
    if start_index >= end_index:
        return
    partition_index = partition(arr, start_index, end_index)
    #print( arr, start_index, partition_index)
    quicksort(arr, start_index, partition_index)
    #print(arr, partition_index+1, end_index)
    quicksort(arr, partition_index+1, end_index)

def partition(arr, s, e):
    pivot = arr[s]
    i = s
    j = e
    while True:
        while j > s and arr[j] >= pivot:
            j -= 1
        while i < e and arr[i] < pivot:
            i += 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            #print('returning', j)
            return j

if __name__ == '__main__':
    assert [3,4,5,7] == insertionSort( [3,5,4,7] )
    assert [3,9,121,129,221,423] == insertionSort( [121,9,129,3,423,221] )
    assert [121,142,225,237,321] == insertionSort( [321,237,225,142,121] )
