def countUniqChar( a ):
    c = [ 0 for i in range(256) ]
    j = 0
    rc = 0
    while( j < len(a) ):
        c[ord(a[j])] = c[ord(a[j])] + 1
        j = j + 1
    for i in range(256):
        if c[i] > 1:
            rc = 1
            break
    if rc:
        print(a, ' is not Unique')
        return
    print(a, ' is Unique')

def uniq_path_helper(i, j, m, n):
    '''
    Top Down Recursive Helper
    :param i:
    :param j:
    :param m:
    :param n:
    :return:
    '''
    cnt = 0
    if i > m or j > n:
        return 0
    if i == m and j == n:
        return 1
    cnt += uniq_path_helper(i, j+1, m, n)
    cnt += uniq_path_helper(i+1, j, m, n)
    return cnt

def unique_paths(m, n):
    return uniq_path_helper(1,1,m,n)

def uniq_paths2_helper(m, n, memo):
    '''
    Top Down Recursive Approach with Memoization
    :param m:
    :param n:
    :param memo:
    :return:
    '''
    key = str(m)+','+str(n)
    if key in memo:
        return memo[key]
    if m == 0 or n == 0:
        memo[key] = 0
        return 0
    if m == 1 and n == 1:
        memo[key] = 1
        return 1
    memo[key] = uniq_paths2_helper(m-1,n, memo) + uniq_paths2_helper(m,n-1, memo)
    return memo[key]

def unique_paths2(m, n):
    memo = dict()
    return uniq_paths2_helper(m,n, memo)

def subset_helper(input, slate, results, curr_element):
    # base case
    if curr_element >= len(input):
        tmp = slate.copy()
        return results.append(tmp)
    #print(curr_element, slate, results)
    subset_helper(input, slate, results, curr_element + 1)
    #print(curr_element, slate, results)
    slate.append(input[curr_element])
    subset_helper(input, slate, results, curr_element + 1)
    slate.remove(input[curr_element])

def all_subsets(arr):
    result = []
    subset_helper(arr, [], result, 0)
    return result

if __name__ == '__main__':
    countUniqChar( a='whoisthat' )
    countUniqChar( a="I'm Unique" )
