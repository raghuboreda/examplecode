def subset_str_helper(input, slate, curr_element, results):
    # base case
    if curr_element >= len(input):
        tmp = slate
        return results.append(tmp)
    #print(curr_element, slate, results)
    subset_str_helper(input, slate, curr_element + 1, results)
    #print(curr_element, slate, results)
    slate = slate + input[curr_element]
    subset_str_helper(input, slate, curr_element + 1, results)
    slate = slate[:-1]

def all_str_subsets(arr):
    result = []
    subset_str_helper(arr, '', 0, result)
    return result

#print(all_str_subsets("any"))

def subset_str_dup_helper(input, slate, curr_element, results, subsetMap):
    # base case
    if curr_element >= len(input):
        tmp = slate
        return results.append(tmp)
    key = slate + input[curr_element:] + ',' + str(curr_element)
    if key in subsetMap:
        return
    else:
        subsetMap[key] = True
    #print(curr_element, slate, results)
    subset_str_dup_helper(input, slate, curr_element + 1, results, subsetMap)
    #print(curr_element, slate, results)
    slate = slate + input[curr_element]
    subset_str_dup_helper(input, slate, curr_element + 1, results, subsetMap)
    slate = slate[:-1]

def all_str_dup_subsets(arr):
    result = []
    subsetMap = {}
    subset_str_dup_helper(arr, '', 0, result, subsetMap)
    return result

#print(all_str_dup_subsets('aaab'))

def palindrome_helper(text, slate, offset, result):
    if offset == len(text):
        result.append(slate[1:])
        return
    for i in range(offset+1, len(text)+1):
        prefix = text[offset:i]
        if prefix == prefix[::-1]:
            palindrome_helper(text, slate + '|'+prefix, i, result)

def palindrome_substrings(input):
    result = []
    palindrome_helper(input, '', 0, result)
    return result

def combination_helper(slate, offset, n, k, result):
    if len(slate) == k:
        result.append(slate.copy())
        return
    i = offset
    remaining = k - len(slate)
    while i <= n and remaining <= n - i + 1:
        combination_helper(slate+[i], i + 1, n, k, result)
        i += 1

def combinations(n, k):
    result = []
    combination_helper([], 1, n, k, result)
    return result

print(combinations(4,2))
def permute_helper( slate, numPlaced, result ):
    if numPlaced >= len(slate):
        result.append(slate.copy())
    else:
        for i in range(numPlaced, len(slate)):
            if i != numPlaced:
                slate[i], slate[numPlaced] = slate[numPlaced], slate[i]
            permute_helper(slate, numPlaced+1, result)
            if i != numPlaced:
                slate[i], slate[numPlaced] = slate[numPlaced], slate[i]
            i += 1

def permute_list( arr ):
    result = []
    arr = sorted(arr)
    permute_helper(arr, numPlaced=0, result=result)
    return result

print(permute_list([1,3,5]))

def permute_dup_helper( slate, numPlaced, result ):
    def count_dups(i):
        k = 0
        j = i + 1
        while j < len(slate):
            if slate[j] == slate[i]:
                j += 1
                k += 1
            else:
                break
        return k

    if numPlaced >= len(slate):
        tmp = slate.copy()
        result.append(tmp)
    else:
        i = numPlaced
        while i < len(slate):
            dups = count_dups(i)
            if i != numPlaced:
                slate[i], slate[numPlaced] = slate[numPlaced], slate[i]
            permute_dup_helper(slate, numPlaced+1+dups, result)
            if i != numPlaced:
                slate[i], slate[numPlaced] = slate[numPlaced], slate[i]
            i += 1

def permute_dup_list( arr ):
    result = []
    arr = sorted(arr)
    permute_dup_helper( arr, numPlaced=0, result=result)
    return result

alphmap = {'2':'abc',
           '3':'def',
           '4':'ghi',
           '5':'jkl',
           '6':'mno',
           '7':'pqr',
           '8':'stuv',
           '9':'wxyz'}

def phone_helper(input, slate, offset, result):
    #base case
    if offset >= len(input):
        result.append(slate.copy())
        #result = slate.copy()
        return
    nl = []
    if input[offset] not in ['0','9']:
        for c in alphmap[input[offset]]:
            for substr in slate:
                substr = substr + c
                nl.append(substr)
        slate = nl
    phone_helper(input, slate, offset+1, result)

def phone2_helper(input, slate, offset, result):
    #base case
    if offset >= len(input):
        result.append(slate)
        return

    if input[offset] not in ['0','9']:
        for c in alphmap[input[offset]]:
            phone2_helper(input, slate + c, offset+1, result)

def phone_list(str):
    result = []
    phone2_helper(str, '', 0, result)
    return result

#print(phone_list('2345'))
def combinationSum(candidates, target):
    """
    :param candidates: distinct integers
    :param target: sum of candidates should be same as target
    :return: list of candidates whose sum is same as target
    """
    def cs_helper(slate, target, index, result):
        # base case
        if target == 0:
            result.append(slate.copy())
            return
        if target < 0:
            return
        # recursive case
        for i in range(index, len(candidates)):
            slate = slate + [candidates[i]]
            target = target - candidates[i]
            #cs_helper(slate + [candidates[i]], target - candidates[i], i, result)
            cs_helper(slate, target, i, result)
            slate.pop()
            target = target + candidates[i]
    result = []
    cs_helper([], target, 0, result)
    return result

print(combinationSum([2,5,7,11], 11))

def queen_helper(i,n,slate,result):
    if i >= n:
        return
    for j in range(0, n):
        slate.append((i,j))
        queen_helper(1, n)
        slate.remove((i,j))

#print(phone_list('2345'))
# calculate_power(a, b)
# The problem statement is straight forward. Given a base ‘a’ and an exponent ‘b’.
# Your task is to find a^b. The value could be large enough. So, calculate
# a^b % 1000000007.
def calculate_power(a, b):
    def power_helper(base, exp):
        if exp == 0:
            return 1
        if exp == 1:
            return base % 1000000007
        return power_helper(base*base, exp-1)
    return power_helper(a, b)
# strings from wild card
# You are given string s of length n, having m wildcard characters '?', where
# each wildcard character represents a single character. Write a program which
# returns a list of all possible distinct strings that can be generated by
# replacing each wildcard character in s with either '0' or '1'.
#
# Any string returned must not contain '?' characters, all must be replaced with either '0' or '1'.
def find_all_possibilities(s):
    def possibility_helper(curr, slate, res):
        if curr == len(s):
            res.append(slate)
            return
        if s[curr] == '?':
            possibility_helper(curr+1, slate+'0', res)
            possibility_helper(curr+1, slate+'1', res)
        else:
            possibility_helper(curr+1, slate+s[curr], res)
        return
    result = []
    possibility_helper(0, '', result)
    return result
