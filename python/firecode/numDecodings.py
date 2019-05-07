def numDecodings( s ):
    l = len(s)

    if len(s) == 0:
        return 0
    if len(s) == 1 and s[0] == '0':
        return 0
    if len(s) == 2:
        if int(s[0]) > 2 and s[1] == '0':
           return 0
    record = dict()
    record[0] = 1
    if s[0] in ['1','2']:
        if 0 < int(s[1]) <= 6 :
            record[1] = 1
    else:
        record[1] = 0

    if len(s) > 2:
        for i in range(2, len(s)):
            if int(s[i-1]) > 2 and s[i] == '0':
                return 0
            if s[i-1] in ['1','2']:
                if 0 < int(s[i]) <= 6:
                    record[i] = 1
            else:
                record[i] = 0

    nways = 0
    for v in record.values():
        nways += v
    return nways 

print numDecodings( '12' )
print numDecodings( '10' )
print numDecodings( '50' )
print numDecodings( '123' )
print numDecodings( '1231' )
print numDecodings( '5231' )
print numDecodings( '12301' )

