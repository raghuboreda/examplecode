# Input:  'aaaabbbccc'
# Output: 'a4b3c3'


def compressStr( str ):
    count = 1
    newStr = ''
    for i in range( 1, len(str) ):
        if str[i] == str[i-1]:
            count = count + 1
            if i == len(str) - 1:
               newStr += '%s%d' % (str[i-1], count)
        else:
            if count > 1:
                newStr += '%s%d' % (str[i-1], count)
            else:
                newStr += str[i-1] 
            if i == len(str) - 1:
                newStr += str[i]
            count = 1
    if len(str) < len(newStr):
        return str
    return newStr

if __name__ == '__main__':
    assert compressStr( 'aaaabbbccc' ) == 'a4b3c3'
    assert compressStr( 'helllooo' ) == 'hel3o3'
    assert compressStr( 'helllooob' ) == 'hel3o3b'
    assert compressStr( 'hheelllooob' ) == 'h2e2l3o3b'
            

        
