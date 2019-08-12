def hasSubsequence( t, s ):
    if len(s) > len(t):
        return False
    if len(s) == 1:
        if s[0] in t:
            return True
        return False
    lt = len(t)
    ls = len(s)
    for i in range(lt):
        if s[0] == t[i]:
            return hasSubsequence( t[i+1:], s[1:]) 

    return False

assert hasSubsequence( 'painstaking', 'it') == True
assert hasSubsequence( 'stake', 'ske') == True
assert hasSubsequence( 'spake', 'skt') == False
assert hasSubsequence( 'introspectionary', 'noeioa') == True
assert hasSubsequence( 'rejection', 'iok') == False
assert hasSubsequence( 'quakers', 'krs') == True


