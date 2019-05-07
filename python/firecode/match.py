def match(first, second):
    if len(first) == 1:
        if len(second) == 1 and first[0] == second[0]:
            return True
        else:
            return False

    if first[0] == '*':
        l = len(first[1:])
        print second, second[-l:]
        return match(first[1:], second[-l:])
    elif first[0] == '?':
        return match(first[1:], second[1:])
    else:
        if first[0] == second[0]:
            return match( first[1:], second[1:] )
        else:
            return False
    print 'Never Reached'
    return True

print match( 'a*er', 'after' )
