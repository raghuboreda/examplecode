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
    print(input)
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
    print(p)
    if target > input[0] and target <= input[p-1]:
        return bsearch(input[:p-1], target)
    else:
        k = bsearch(input[p:], target)
        if k != -1:
            return p + bsearch(input[p:], target)

def rsearch(input, target, s, e):
    if s > e:
        return -1
    mid = (s+e)//2
    if target == input[mid]:
        return mid
    if input[s] < input[mid]:
        if input[s] <= target < input[mid]:
            return rsearch(input, target, s, mid)
        else:
            return rsearch(input, target, mid+1, e)
    elif input[mid] < input[e]:
        if input[mid] < target <= input[e]:
            return rsearch(input, target, mid+1, e)
        else:
            return rsearch(input, target, s, mid)

def rotated_search(input,target):
    return rsearch(input, target, 0, len(input)-1)

print(rotated_search([12,16,19,21,45,2,5,10], 5))

