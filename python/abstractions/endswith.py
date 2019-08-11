def endsWith( string, suffix ):
    n = len(string)
    s = len(suffix)
    if n < s:
        return False
    if string[n-s:] == suffix:
        return True
    return False

if __name__ == '__main__':
    assert endsWith( 'Merciful', 'ful') is True
    assert endsWith( 'Awful', 'ful') is True
    assert endsWith( 'Incendiary', 'ary') is True
    assert endsWith( 'Archive', 'ary') is False
    assert endsWith( 'shelf', 'shelf') is True
    assert endsWith( 'Willows', 'ow') is False
