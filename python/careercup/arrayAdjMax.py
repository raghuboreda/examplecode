# comparing each element in a sorted array
# comparing elements in array A[i]
# return max( A[i2] - A[i1])
#        where i2 > i1
# O(n^2) implementation
import time
import random

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
          
def arrayFastAdjMax( l, min=0, maxdiff=0 ):
    if( len(l) <= 2 ):
        if len(l) == 1:
            if l[0] < min:
                min = l[0]
            if l[0] - min > maxdiff:
               maxdiff = l[0] - min 
        else:
            if l[0] < l[1]:
                if l[0] < min:
                    min = l[0]
                if l[1] - min > maxdiff:
                    maxdiff = l[1] - min
            else:
                if l[0] - min > maxdiff:
                    maxdiff = l[1] - min
                if l[1] < min:
                    min = l[1]
        maxdiff = maxdiff
        return min, maxdiff

    min, maxdiff = arrayFastAdjMax( l[:len(l)/2],
                          min=min, maxdiff=maxdiff )
    min, maxdiff = arrayFastAdjMax( l[len(l)/2:],
                          min=min, maxdiff=maxdiff )
    return min, maxdiff

def arrayRecursiveAdjMax( l ):
    min, maxdiff = arrayFastAdjMax( l, min=l[0] )
    return maxdiff
             

if __name__ == '__main__':
    assert arrayAdjMax([ 9,2,3,4,6,7,8]) == 6
    b = [ 9,5,7,11,2,3,10]
    assert arrayAdjMax( b ) == 8 
    c = [ 9,1,7,11,2,3,10]
    assert arrayAdjMax( c ) == 10 
    assert arrayRecursiveAdjMax([ 9,2,3,4,6,7,8]) == 6
    d = list()
    for index in range( 1, 1000):
        d.append( random.randrange( 1, 3000 ) )
    stTime = time.time()
    l1 = arrayAdjMax( d )
    endTime = time.time()
    print l1, endTime - stTime
    stTime = time.time()
    l1 = arrayRecursiveAdjMax( d )
    endTime = time.time()
    print l1, endTime - stTime
