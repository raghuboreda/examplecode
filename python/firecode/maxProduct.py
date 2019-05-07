def mult( nums ):
    prod = 1
    for i in nums:
        prod *= i
    return prod

def maxP( nums ):
    print nums
    if len(nums) == 1:
        return nums[0]
    negativeIndexes = [ i for i,v in enumerate(nums) if v < 0 ]
    nn = 0
    if len(negativeIndexes) > 0 and len(negativeIndexes)%2 == 1:
        nn = 1

    if nn == 0:
        return mult(nums)

    prod = []
    prod.append(mult(nums[:negativeIndexes[-1]]))
    prod.append(mult(nums[negativeIndexes[0]+1:]))
    return max(prod)

def maxProduct( nums ):
    zeroI = [ i for i,v in enumerate(nums) if v == 0 ]

    if len(nums) == 0:
        return 0
    if len(nums) == 1 or len(zeroI) == 0:
        return maxP( nums )

    if len(zeroI) == 1:
        v = zeroI[0]
        if v == 0:
            return maxP(nums[v+1:])
        elif v == len(nums) - 1:
            return maxP(nums[:v])
        else:
            return max(maxP(nums[:v]), maxP(nums[v+1:]))
    prev = 0
    prod = []
    print zeroI
    for i,v in enumerate(zeroI):
        if i == 0 and v == 0:
            prev = v
        elif i == 0 and v != 0:
            prev = v
            prod.append(maxP(nums[:v]))
        else:
            prod.append(maxP(nums[prev+1:v]))
            prev = v
    v = zeroI[-1]
    if v != len(nums) - 1:
        prod.append(maxP(nums[v+1:]))
    print prod
    return max(max(prod), 0)

a = [0, -1, 4, -4, 5, -2, -1, -1, -2, -3, 0, -3, 0, 1, -1, -4, 4, 6, 2, 3, 0,
        -5, 2, 1, -4, -2, -1, 3, -4, -6, 0, 2, 2, -1, -5, 1, 1, 5, -6, 2, 1, -3,
        -6, -6, -3, 4, 0, -2, 0, 2]
print maxProduct( a )
