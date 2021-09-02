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

def permute_list( arr ):
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

def target_helper(input, slate, offset, result, target):
    if offset >= len(input):
        return
    if target == input[offset]:
        #print(slate, input[offset])
        slate.append(input[offset])
        result.append(slate.copy())
        return
    elif target < input[offset]:
        return
    slate = slate + [input[offset]]
    print("tv", slate, offset + 1 , target)
    target_helper(input, slate, offset+1, result, target-input[offset])
    slate.remove(input[offset])
    idx = offset + 1
    count = 0
    while idx < len(input) and input[offset] == input[idx]:
        count += 1
        idx += 1
    print(slate, offset+1+count, target)
    target_helper(input, slate, offset + 1 + count, result, target)

def target_sum(input, target):
    result = []
    input.sort(reverse=True)
    print(input)
    target_helper(input, [], 0, result, target)
    return result

def queen_helper(i,n,slate,result):
    if i >= n:
        return
    for j in range(0, n):
        slate.append((i,j))
        queen_helper(1, n)
        slate.remove((i,j))


#print(all_str_dup_subsets('aaab'))
#print(phone_list('2345'))
print(target_sum([1,2,3,3],3))