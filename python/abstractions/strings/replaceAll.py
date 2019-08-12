def replaceAll( string, str1, str2):
    """
    replace all occurences of str1 by str2
    """
    s = ''
    if len(str1) == len(str2) and len(str1) == 1: 
        return replaceAllChar( string, str1, str2 )
    i = 0
    while i < len(string):
        if string[i] == str1[0]:
            if isStringsEqual( string, i, str1):
                # copy str2 here
                s += str2
                i += len(str2)
                continue
        s += string[i]
        i += 1
    return s

def isStringsEqual( string, i , str1 ):
    j = 0
    while j < len(str1):
        if str1[j] != string[i+j]:
            return False
        j += 1
    return True

def replaceAllChar( string, char1, char2 ):
    s = ''
    for c in string:
        if c == char1:
            c = char2
        s += c
    return s

assert replaceAll( 'Anshul', 's', 'd' ) == 'Andhul'
assert replaceAll( 'Workhorse', 'kho', 'twy' ) == 'Wortwyrse'
assert replaceAll( 'In the night knight', 'night', 'time' ) == 'In the time ktime'
# need to fix this.
assert replaceAll( 'HawkTime', 'awk', 'illary' ) == 'HillaryTime'

