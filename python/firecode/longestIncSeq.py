def lenLongestIncrSubSeq( A ):
    """
    This is not O(n^2) solution
    More of a brute force solution
    as subseq actually keeps track of all sub sequences
    """
    subseq = []
    subseq.append([A[0], 1])
    ans = 0
    for i in range(1,len(A)):
        for j in range(len(subseq)):
            if A[i] > subseq[j][0]:
                rc = subseq[j][1]
                rc += 1
                elem = []
                elem.append(A[i]) 
                elem.append(rc) 
                if elem not in subseq:
                    subseq.append(elem)
                ans = max(ans, rc)
            else:
                if [A[i],1] not in subseq:
                    subseq.append([A[i],1])
    return ans


assert lenLongestIncrSubSeq( [3, 9, 1, 2, 8, 7, 10, 11]) == 5
assert lenLongestIncrSubSeq( [9, 8, 4, 6, 7, 11]) == 4
assert lenLongestIncrSubSeq( [50, 95, 25, 40, 30, 11]) == 2
assert lenLongestIncrSubSeq( [90, 80, 75, 6, 7, 11]) == 3
assert lenLongestIncrSubSeq( [50, 95, 25, 40, 30, 11, 45,60,75]) == 5
assert lenLongestIncrSubSeq( [10, 95, 25, 100, 125] ) == 4
assert lenLongestIncrSubSeq( [ 25, 10, 40, 30, 22, 26, 28, 12, 13, 14, 15, 16, 17] ) == 7
