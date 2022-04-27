def lomuto_partition(arr):
    start = 0
    end = len(arr)-1
    i = start - 1
    pivot = arr[end]
    for j in range(start,end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i+1

def hoare_partition(arr):
    start = 0
    end = len(arr) - 1
    pivot = arr[start]
    while True:
        while arr[start] < pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        else:
            return end

arr = [12, 9, 4, 6, 15, 5, 7, 8,17,19]
k = hoare_partition(arr)
print(arr, k)
def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    j = len(nums) - 1
    swappedIndex = -1
    next = 0
    for i in range(j,0,-1):
        if nums[i-1] < nums[i]:
            swappedIndex = i - 1
            break

    if swappedIndex == -1:
        nums.reverse()
    else:
        for i in range(j, -1, -1):
            if nums[i] > nums[swappedIndex]:
                next = i
                break
        nums[swappedIndex], nums[next] = nums[next], nums[swappedIndex]
        k = 0
        start = swappedIndex + 1
        end = j
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    return nums

#print(nextPermutation([9, 8, 6, 4, 7, 5, 3, 2]))

def rotateArray1(nums, k):
    # O(nums*k) implemenations
    if k > len(nums):
        k = k - len(nums)
    # 0 1 2 3 4 5 , k = 2
    # 5 0 1 2 3 4
    # 4 5 0 1 2 3
    # index + 2
    tmp = None
    for _ in range(k):
        tmp = nums[0]
        for j in range(1, len(nums)):
            nums[j],tmp = tmp, nums[j]
        nums[0] = tmp
    return nums

def rotateArray(nums, k):
    # O(nums) time implemenations
    # O(k) space implemenation
    if k > len(nums):
        k = k - len(nums)
    # 0 1 2 3 4 5 , k = 2
    # 0 1 1 2 3 4 tmp_list = [2,3,4,5]
    # 0 1 0 1 2 3
    # index + 2
    tmp_list = []
    for i in range(len(nums)-1, len(nums)-(k+1), -1):
        tmp_list.append(nums[i])
    for i in range(len(nums)-1, k-1, -1):
            nums[i] = nums[i-k]
    for i in range(k):
        nums[i] = tmp_list.pop()
    return nums

# Sort all characters
# You have to sort an array of characters containing alphanumeric characters
# along with some other characters - '!', '@', '#', '$', '%', '^', '&', '*',
# '(', ')'. You are given a character array named arr
# Output: Return a character array result, containing characters in sorted
# order of their ASCII values. You can overwrite the existing array
def sort_array(arr):
    def merge_helper(st, end, result):
        # 0 , 3 ==> [0, 1,] [2, 3], [0,0], [1,1], [2,2],[3,3]
        if st == end:
            return
        mid = st + (end - st) // 2
        merge_helper(st, mid,result)
        merge_helper(mid+1, end, result)
        i, j = st, mid+1
        nl = []
        while i <= mid and j <= end:
            if ord(result[i]) < ord(result[j]):
                nl.append(result[i])
                i += 1
            else:
                nl.append(result[j])
                j += 1
        #print(i, mid, j, end)
        #print(nl)
        if i <= mid:
            for k in range(i, mid+1):
                nl.append(result[k])
        #print(nl)
        if j <= end:
            for k in range(j, end+1):
                nl.append(result[k])
        #print(nl)
        result[st:end+1] = nl

    s = 0
    e = len(arr) - 1
    result = [c for c in arr]
    merge_helper(s, e, result)
    return ''.join(result)

#print(sort_array('bcad?ef%'))
# Four Billion
# Given 4 billion of 32 bit integers, return any one that's not among them.
# Assume you have 1 GiB ( 1024 ^ 3 ) bytes of memory
def find_integer(arr):
    pass
# nearest neighbors
# Given a point p, and the other n points in two-dimensional space, find k
# points out of n points which are nearest to p.
def nearest_neighbors(px, py, k, n_points):
    '''
    :param px: x-coordinate of point p
    :param py: y-coordinate of point p
    :param k: return k points
    :param n_points: a list of n points [ (1, 4), (2,7) ]
    :return: a list of k points [ (1,4) ]
    '''
    pass

def sliding_window_control( str, charset ):
    i = 0
    j = 1
    # h e l l o w o r l d
    # key_map = {'w':0, 'r':0, 'l':0}
    key_map = dict()
    for c in charset:
        key_map[c] = 0
    missing = len(charset)
    result = []
    while j < len(str):
        if str[j] in key_map:
            if key_map[str[j]] == 0:
                key_map[str[j]] += 1
                missing -= 1
                if missing == 0:
                    # Now we got our window from i to j
                    while missing == 0:
                        if str[i] in key_map:
                            key_map[str[i]] -= 1
                            if key_map[str[i]] == 0:
                                if len(result):
                                    result.pop()
                                result.append((i, j))
                                missing += 1
                        i += 1
            else:
                key_map[str[j]] += 1
        j += 1
    return result

#res = sliding_window('hardwqke', ['a','d','k'])
#print(res)

def find_longest_palindrome( str ):
    '''
    This is O(n^2) implementation where we look for palindromes from center and look for longest palindrome.
    We have to do two pass as we have to look for both even and odd palindromes.
    :param str:
    :return:
    '''
    def is_palindrome(left, right):
        while left >= 0 and right < len(str) and str[left] == str[right]:
            left -= 1
            right += 1
        return left+1, right-1
    i = 0
    long_pal = 0
    result = []
    while i < len(str):
        left, right = i, i
        rl, rr = is_palindrome(left, right)
        if rr - rl > long_pal:
            long_pal = rr - rl
            if len(result):
                result.pop()
            result.append((rl, rr))
        i += 1
    i = 0
    while i + 1 < len(str):
        left, right = i, i + 1
        rl, rr = is_palindrome(left, right)
        if rr - rl > long_pal:
            long_pal = rr - rl
            if len(result):
                result.pop()
            result.append((rl, rr))
        i += 1
    print( long_pal, result)
    (i,j) = result.pop()
    return str[i:j+1]

print(find_longest_palindrome("hawkwaabkayakba"))
class TrieNode:
    def __init__(self, value,end):
        self.value = value
        self.end = end
        self.children = []

    def insert(self, value, end):
        for node in self.children:
            if node.value == value:
                return node.insert(value,end)
        self.children.append(TrieNode(value,end))


def prefixTrie(str):
    root = TrieNode('/')
    for i,c in enumerate(str):
        end = False
        if i == len(str) - 1:
            end = True
        root.insert(c, end)

#  [ 23, 35, 12, 19, 43, 55]
#   k = 3rd largest
#   [ 23, 12, 19,43,35,55] n = 6, k = 3, index = 2
#   [ 19, 12, 23, 43,35,55] n = 6, k = 3, index = 2 , s = index, e = n