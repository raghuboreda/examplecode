def simpleBinaryAdd( a1, b1, c1=None):
    """
    carry is '1' or None
    """
    if c1 is None:
        if a1 == '1' and  b1 == '1':
           return ('0','1')
        elif a1 == '0' and b1 == '1':
           return ('1', None)
        elif a1 == '1' and b1 == '0':
           return ('1', None)
        elif a1 == '0' and b1 == '0':
           return ('0', None)
    else:
        # assuming carry is always '1'
        if a1 == '1' and  b1 == '1':
           return ('1','1')
        elif a1 == '0' and b1 == '1':
           return ('0', '1')
        elif a1 == '1' and b1 == '0':
           return ('0', '1')
        elif a1 == '0' and b1 == '0':
           return ('1', None)
    

def binaryAdd( a, b ):
    """
    add two binary strings
         '1011' + '1101' == '11000'
    """
    la = len(a)
    lb = len(b)
    
    if( la < lb ):
        binaryAdd( b, a )
    i = la-1
    j = lb-1
    carry = None 
    binResult = ''
    while( i >= 0 ):
        if( j < 0 ):
            break
        res, carry = simpleBinaryAdd( a[i], b[j], carry ) 
        binResult += res 
        i = i - 1
        j = j - 1
    if( i < 0 and j < 0 ):
        if carry is not None:
            binResult += carry
    else:
        if( i >= 0 ):
            if carry is not None:
                while( i >= 0 ):
                    res, carry = simpleBinaryAdd( a[i], carry, None )
                    if carry is None:
                        carry = '0'
                    binResult += res
                    i = i - 1
                if carry == '1':
                    binResult += carry
            else:
                binResult += a[:i+1]
      
    print binResult[::-1]

binaryAdd( '1011', '1101' )
binaryAdd( '111110000', '1000' )
binaryAdd( '111110000', '11000' )
        
