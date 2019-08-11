def removeDups( a ):
    """
    a = [ 'cat', 'dog', 'fish', 'cat' ]
    removeDups(a) == [ 'cat', 'dog', 'fish' ]
    Space : O(n)
    Time : O(n)
    """
    b = list()
    for item in a:
        if item not in b:
            b.append( item )
    return b

def removeDupsInPlace( a ):
    """
    a = [ 'cat', 'dog', 'fish', 'cat' ]
    removeDups(a) == [ 'cat', 'dog', 'fish' ]
    Space : O(1)
    Time : O(n**2)
    """
    indexI = 0
    aLen = len(a)
    while indexI < aLen:
        indexJ = indexI + 1
        while indexJ < aLen:
            if a[indexI] == a[indexJ]:
                del a[indexJ] 
                aLen = aLen - 1
            else:
                indexJ = indexJ + 1
        indexI = indexI + 1
    return a

if __name__ == '__main__':
   assert removeDups( [ 'cat', 'dog', 'fish', 'cat' ]) == [ 'cat', 'dog', 'fish' ]
   assert removeDups( [ 'dog', 'dog', 'fish', 'cat' ]) == [ 'dog', 'fish', 'cat' ]
   assert removeDups( [ 'dog', 'dog', 'dog', 'cat' ]) != [ 'cat', 'dog' ]
   assert removeDups( [ 'dog', 'dog', 'dog', 'cat' ]) == [ 'dog', 'cat' ]
   assert removeDupsInPlace( [ 'cat', 'dog', 'fish', 'cat' ]) == [ 'cat', 'dog', 'fish' ]
   assert removeDupsInPlace( [ 1, 2, 1 , 1, 1, 1, 5, 2, 1, 3 ]) == [ 1, 2, 5, 3 ]
