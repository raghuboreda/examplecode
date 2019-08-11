def dec_to_bin(number):
    s=''
    while number > 0:
        s += ''.join(str(number&0x1))
        number = number >> 1
    return '0b'+ s[::-1]

def strToDecimal( str ):
    s = str[::-1]
    num = 0
    prod = 1
    for c in s:
        num += (ord(c) - ord('0')) * prod
        prod *= 10
    return num


print dec_to_bin(10)
print dec_to_bin(15)
print strToDecimal('15')
print strToDecimal('150')
print strToDecimal('1504')
print strToDecimal('10505')
