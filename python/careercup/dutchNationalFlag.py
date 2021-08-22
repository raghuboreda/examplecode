def dutchNationalFlag(arr=None):
    g = 'G'
    r = 'R'
    b = 'B'
    rp = 0
    bp = len(arr) - 1
    while rp <= bp and bp > 0:
        while rp < len(arr) and arr[rp] == r:
            rp += 1
        while bp > 0 and (arr[bp] == b or arr[bp]== g):
            bp -= 1
        if rp < bp:
            arr[rp], arr[bp] = arr[bp], arr[rp]
    gp = rp
    bp = len(arr) - 1
    print(gp, bp)
    while gp <= bp and bp > 0:
        while gp < len(arr) and arr[gp] == g:
            gp += 1
        while bp > 0 and arr[bp] == b:
            bp -= 1
        if gp < bp:
            arr[gp], arr[bp] = arr[bp], arr[gp]
    return arr

arr1 = ['B', 'B']
print (dutchNationalFlag(arr1))