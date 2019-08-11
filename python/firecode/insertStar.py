a_string = 'abc'
b_string = ''.join(a_string[0])
b_string += b_string.join('*')
b_string += ''.join(a_string[1])
print b_string
