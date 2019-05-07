def getPivot(nums, length):
    l = 0
    r = length - 1
    m = 0
    if nums[r] > nums[l]:
        return l
    while( l < r ):
        m = l + (r-l)/2
        if m == l and m == r - 1:
            if nums[r] < nums[l]:
                return r
            return l
        if nums[m] < nums[l]:
            r = m
        else:
            l = m
    return m

def bsearch(input, target):
    print input
    l = 0
    r = len(input) - 1
    m = 0
#    if input[l] == target:
#        return l
#    if input[r] == target:
#        return r
    while l <= r:
        m = l + (r-l)/2
        if m == l and m == r - 1:
            if input[m] == target:
                return m
            elif input[r] == target:
                return r
            else:
                return -1
        if input[m] == target:
            return m
        elif input[m] > target:
            r = m - 1
        else:
            l = m + 1
    return -1

def search(input, target):
    p = getPivot( input, len(input))
    print p
    if target > input[0] and target <= input[p-1]:
        return bsearch(input[:p-1], target)
    else:
        k = bsearch(input[p:], target)
        if k != -1:
            return p + bsearch(input[p:], target)

print search([5,1,3], 3)
