def countBits( number ):
    count = 0
    while number:
        if number & 1:
            count += 1
        number = number >> 1

    return count

assert countBits(10) == 2
assert countBits(11) == 3
assert countBits(12) == 2
assert countBits(15) == 4
