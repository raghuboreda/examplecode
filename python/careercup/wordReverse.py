def reverse( a ):
    return a[::-1]

def reverseWords( a=None ):
    """
    space complexity is length of a
    """
    s = a.split()
    l = list()
    for word in s:
        word = reverse( word )
        l.append( word ) 
    s = ' '.join( word for word in l )
    return s 

def reverseInPlaceWords( a=None ):
    """
    space complexity is length of longest word in a
    """
    s = a.split()
    for index in range(len(s)):
        word = s[index]
        i = len(word)
        j = 0
        r = ''
        while( j < len(word) ):
            r += word[ i-1 ]
            j = j + 1
            i = i - 1
        s[index] = r
    s = ' '.join( word for word in s )
    return s 

if __name__ == '__main__':
    assert reverseWords( a='the boy ran') == 'eht yob nar'
    assert reverseWords( a='good heavens') == 'doog snevaeh'
    assert reverseWords( a='star wars') == 'rats sraw'
    assert reverseInPlaceWords( a='the boy ran') == 'eht yob nar'
    assert reverseInPlaceWords( a='good heavens') == 'doog snevaeh'
    assert reverseInPlaceWords( a='star wars') == 'rats sraw'
