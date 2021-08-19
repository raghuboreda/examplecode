def mergeOneListToAnother(arr1, arr2):
    '''
    :param arr1: sorted list, length n
    :param arr2: sorted list, lenght 2n, last n elements are zero
    :return: arr2 which is sorted list of arr1 and arr2
    Need to do this in constant space
    '''
    n = len(arr1)
    insert_index = 0
    a1 = 0
    a2 = 0
    while (a2 < n):
        arr2[a2+n] = arr2[a2]
        arr2[a2] = 0
        a2 += 1
    a2 = n
    while a1 < n and a2 < 2*n:
        if arr1[a1] < arr2[a2]:
            arr2[insert_index] = arr1[a1]
            a1 += 1
        else:
            arr2[insert_index] = arr2[a2]
            a2 += 1
        insert_index += 1
        print(arr1, arr2, a1, a2, insert_index)
    while a1 < n:
        arr2[insert_index] = arr1[a1]
        a1 += 1
        insert_index += 1
    return arr2

nl = mergeOneListToAnother([13,21], [13,13,0,0])
print(nl)