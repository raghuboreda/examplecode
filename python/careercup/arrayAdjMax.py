# comparing each element in a sorted array
# comparing elements in array A[i]
# return max( A[i2] - A[i1])
#        where i2 > i1
# O(n^2) implementation
def arrayAdjMax( l ):
    max = 0
    tmax = 0
    p = l[1:]
    p.sort()
    if l[0] < p[0]:
       return(p[len(p)-1] - l[0])
    else:
       i = 0
       while( i < (len(p) -1)):
           index2 = l.index(p[len(p)-1-i])
           j = 0
           while( j < (len(p)-1-i)):
               index1 = l.index(p[j])
               if( index1 < index2 ):
                  tmax = l[ index2 ] - l[ index1 ]
               if ( tmax > max ):
                  max = tmax
               j = j + 1
           i = i + 1
    return max


# O(nlogn) implementation
def arrayFastAdjMax( l ):
    pass

a = [ 9,2,3,4,6,7,8]
print arrayAdjMax( a )
        
b = [ 9,5,7,11,2,3,10]
print arrayAdjMax( b )

c = [ 9,1,7,11,2,3,10]
print arrayAdjMax( c )
