def isInPlacePalindrome( a=None ):
   for i in range( len(a)/2 ):
       if a[i] != a[len(a) - 1 - i]:
           return False
   return True

def isSlicePalindrome( a=None ):
    b = a[:len(a)/2]
    c = a[-1:-(len(a)/2+1):-1]
    if b != c:
        return False
    return True

def isRecursivePalindrome( a = None ):
    if len(a) <= 1:
        return True
    else:
        return a[0] == a[-1] and isRecursivePalindrome( a[1:-1] )

if __name__ == '__main__':
    assert isInPlacePalindrome( a='HeroreH')
    assert isSlicePalindrome( a='PenneP')
    assert isRecursivePalindrome( a='HeroreH')
    assert isInPlacePalindrome( a='malayalam')
    assert isSlicePalindrome( a='malayalam')
    assert isRecursivePalindrome( a='malayalam')
    assert isInPlacePalindrome( a='whatissitahw')
    assert isRecursivePalindrome( a='whatissitahw')
    assert not isInPlacePalindrome( a='NotPali')
    assert not isInPlacePalindrome( a='YeahReally')
    assert not isRecursivePalindrome( a='YeahReally')
