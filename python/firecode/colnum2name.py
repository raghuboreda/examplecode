s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = dict()
ind = 1
for c in s:
    a[ind] = c
    ind = ind + 1

def colrecurse( colnum ):
    if colnum > 0 and colnum < 27:
        return a[colnum]
    if colnum == 0:
        return a[26]
    mult = 1
    tmp = colnum
    index = 0
    while tmp > 26:
        tmp = tmp/26
        mult = mult * 26
    coldiv = colnum/mult
    colrem = colnum%mult
    colnum = colnum - (mult * coldiv)
    if colrem == 0:
        return a[coldiv-1] + colrecurse( colnum )
    return a[coldiv] + colrecurse( colnum)

def col2name( colnum ):
    s = colrecurse( colnum )
    #print s
    return s

def coliterate( colnum ):
    index = colnum - 1
    output = ''
    while index >= 0:
        character = chr( (index%26) + ord('A') )
        output = output + character
        index = index/26 - 1
    #print output[::-1]
    return output[::-1]


assert coliterate(27) == col2name(27)
assert coliterate(10) == col2name(10)
assert coliterate(57) == col2name(57)
assert coliterate(1077) == col2name(1077)
assert col2name(706) != coliterate(676)

