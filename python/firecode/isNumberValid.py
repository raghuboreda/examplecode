def isValid( s ):
    """
    valid strings are 525, -535, 52.5, 53e4, 10e-4
    """
    def validateSpaces( s ):
        foundSpace = False
        for i in range(len(s)):
            if s[i] == ' ':
                foundSpace = True
            else:
                if foundSpace:
                    return False
        return True

    if len(s) == 1:
        if s[0] == '.' or s[0] == 'e':
            return False

    dotOreIndex = s.find('.')
    if dotOreIndex == -1:
        dotOreIndex = s.find('e')

    if dotOreIndex == -1:
        try:
            l = int(s)
        except:
            return False
    else:
        if dotOreIndex > 0: 
            l = s[:dotOreIndex]
        if dotOreIndex < len(s)-1: 
            r = s[dotOreIndex+1:]
        try:
            l = int(l)
            r = int(r)
        except:
            return False
        if s[dotOreIndex] == '.':
            if r < 0:
               return False
    return True

assert(isValid('525') == True)
assert(isValid('-535') == True)
assert(isValid('53.5') == True)
assert(isValid('53e5') == True)
assert(isValid('10e-5') == True)
assert(isValid('54a5') == False)
assert(isValid('54.-5') == False)
assert(isValid(' 1') == False)
assert(isValid('1 ') == True)
assert(isValid('1 .5') == False)
assert(isValid('.') == False)
assert(isValid('.5') == True)
assert(isValid('e') == False)
