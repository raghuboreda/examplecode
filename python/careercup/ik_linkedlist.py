class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def has_cycle( root ):
    slownode = root
    if slownode:
        fastnode = root.next
    if not fastnode:
        return False
    while slownode != None and fastnode != None:
        if slownode == fastnode:
            return True
        slownode = slownode.next
        if fastnode.next:
            fastnode = fastnode.next.next
        else:
            fastnode = fastnode.next
    return False

def build_ll( ll_list ):
    hdr = None
    for i in ll_list:
        if hdr == None:
            hdr = Node(i)
            tail = hdr
        else:
            node = Node(i)
            tail.next = node
            tail = tail.next
    return hdr

def build_ll_with_cycles(ll_list, cycle_start, cycle_end):
    '''
    :param ll_list: list of integers to make a linked list
    :param cycle_start: index where you want the cycle to start from
    :param cycle_end: index where you want to end the cycle
    :return: header of linked list with cycles
    example: [1,3,5,7,9,11], 4, 2
    should return a linked list
     1->3->5->7->9
           ^-----| i.e. a node 9 is linked to node 7
    '''
    hdr = build_ll(ll_list)
    if cycle_start <= cycle_end:
        print('Cannot create a linked list with cycles')
        return None

    node_start = None
    node_end = None
    node = hdr
    # 1 3 5 7 9 11 13 15 17
    # cs = 4 ce = 2 node = 1
    # cs = 3, ce = 1 node = 3
    # cs = 2, ce = 0, node = 5 (node_end = 5)
    # cs = 1, ce = -1, node = 7
    # cs = 0, ce = -2, node = 9 (node_start = 9)
    while cycle_start > 0 and node != None:
        if cycle_end == 0:
            node_end = node
        cycle_end -= 1
        cycle_start -= 1
        node = node.next
    node_start = node
    node_start.next = node_end
    return hdr

def print_ll( root ):
    node = root
    while node != None:
        print(node.value)
        node = node.next
    return

#hdr1 = build_ll_with_cycles( [1,3,5,7,9,11,13,15,17,19], 9, 3)
#hdr2 = build_ll( [1,3,5,7,9,11,13,15,17,19])
#cycle1 = has_cycle(hdr1)
#cycle2 = has_cycle(hdr2)
#print('Cycles: ', cycle1, cycle2)

def merge_two_sorted_linked_list(list1, list2):
    al = Node(0)
    tail = al
    node1 = list1
    node2 = list2
    while node1 != None and node2 != None:
        if node1.value < node2.value:
            tail.next = node1
            node1 = node1.next
        else:
            tail.next = node2
            node2 = node2.next
        tail = tail.next
    if node1:
        tail.next = node1
    if node2:
        tail.next = node2
    return al.next

#hdr1 = build_ll( [1,3,5,7,9,11,13,15,17,19])
#hdr2 = build_ll( [2,4,6,10,12,14,20,22,24])
#hdr3 = merge_two_sorted_linked_list(hdr1, hdr2)
#print_ll(hdr3)
import heapq
def merge_n_sorted_linklists( ll_lists ):
    '''
    :param ll_lists: list of n sorted linked lists
    :return: sorted and merged link list
    '''
    h = []
    for i in range(len(ll_lists)):
        heapq.heappush(h, (ll_lists[i].value, ll_lists[i]))
    header = dummy = Node(0)
    while len(h):
        node = heapq.heappop(h)
        dummy.next = node[1]
        if node[1].next:
            heapq.heappush(h, (node[1].next.value, node[1].next))
        dummy = dummy.next
    return header.next
#hdr1 = build_ll( [1,3,5,7,9])
#hdr2 = build_ll( [2,4,6,18])
#hdr3 = build_ll([8,16,22])
#hdr4 = build_ll([10,15,21])
#hdrlist = [hdr1, hdr2, hdr3, hdr4]
#sorted_ll = merge_n_sorted_linklists(hdrlist)
#print_ll(sorted_ll)
def middle_of_ll(header):
    '''
    Given a header to linked list, return middle element of the list
    :param header: head of link list
    :return: node of middle element
    '''
    size = 0
    tmp = header
    while tmp != None:
        size += 1
        tmp = tmp.next
    if size % 2 == 0:
        size = size // 2 - 1
    else:
        size = size // 2
    tmp = header
    while size > 0:
        size -= 1
        tmp = tmp.next
    return tmp

def palindrome_linked_list( header ):
    '''
    Is linked list palindrome
    :param header: linked list header
    :return: True if Palindrome else False
    '''
    # Approach #1
    # Naive approach is reverse the linked list (duplicate )
    # and then compare both the original and reversed lists
    # Time O(n) and Space O(n)
    # How to solve it in O(1)
    # Approach #2
    # Figure out the middle node
    # make two lists l1 -> original list until the middle node
    # l2 -> second list from middle node to end of the list
    # l2 -> reverse of l2
    # compare l2 and l1. Let's code approach #2
    h = t = header
    # Figure out the middle node
    while h.next != None and h.next.next != None:
        h = h.next.next
        t = t.next
    # assign the second list
    l2 = t.next
    # cut off first list from second list
    t.next = None
    l1 = header
    prev = None
    curr = l2
    while curr != None:
        succ = curr.next
        curr.next = prev
        prev = curr
        curr = succ
    l2 = prev
    tail1 = l1
    tail2 = l2
    while tail1 != None and tail2 != None:
        if tail1.value == tail2.value:
            tail1 = tail1.next
            tail2 = tail2.next
        else:
            return False
    return True

