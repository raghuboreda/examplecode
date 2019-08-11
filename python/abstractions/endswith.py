def endsWith( string, suffix ):
    n = len(string)
    s = len(suffix)
    if n < s:
        return False
    if string[n-s:] == suffix:
        return True
    return False

def trimString( string ):
    '''
    remove white spaces in begining and end
    '''
    s = ''
    for c in string:
        if c != ' ':
            s += c
    return s

def substr( string, pos, n=-1 ):
    l = len(string)
    if pos > l-1:
        return -1
    s = ''
    i = 0
    if n == -1:
        e = l
    else:
        e = pos + n
    for c in string:
        if i < pos:
            i += 1
            continue
        if i >= e:
            break
        s += c
        i += 1
    return s

def capitalize(string):
    '''
    initial character is capitalized
    all other characters are converted to lower case
    '''
    s = ''
    for i,c in enumerate(string):
        if i == 0:
            if c.islower():
                c = c.upper()
        else:
            if c.isupper():
                c = c.lower()
        s += c
    return s



if __name__ == '__main__':
    assert endsWith( 'Merciful', 'ful') is True
    assert endsWith( 'Awful', 'ful') is True
    assert endsWith( 'Incendiary', 'ary') is True
    assert endsWith( 'Archive', 'ary') is False
    assert endsWith( 'shelf', 'shelf') is True
    assert endsWith( 'Willows', 'ow') is False
    assert trimString( '  cow  ') == 'cow'
    assert trimString( '  plough') == 'plough'
    assert trimString( 'wasted  ') == 'wasted'
    assert substr( 'wasted', 3, 2) == 'te'
    assert substr( 'chrome', 1, 4) == 'hrom'
    assert substr( 'chrome', 3, 4) == 'ome'
    assert substr( 'chrome', 3) == 'ome'
    assert capitalize( 'boolean') == 'Boolean'
    assert capitalize( 'bOoLeAn') == 'Boolean'
    assert capitalize( 'BOoLeAn') == 'Boolean'
