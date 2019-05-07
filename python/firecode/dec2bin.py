def dec_to_bin(number):
    s=''
    while number > 0:
        print number
        s += ''.join(str(number&0x1))
        number = number >> 1
    print s[::-1]

dec_to_bin(10)
