import collections

def lenLongestFibSubSeq( A ):
    index = {x:i for i,x in enumerate(A)}
    longest = collections.defaultdict(lambda: 2)

    ans = 0
    for k, z in enumerate(A):
        for j in xrange(k):
            i = index.get(z-A[j], None)
            if i is not None and i < j:
                cand = longest[j,k] = longest[i,j] + 1
                ans = max(ans, cand)
    return ans if ans >= 3 else 0

print lenLongestFibSubSeq( [1, 3, 4, 7, 10, 17, 27, 11])
