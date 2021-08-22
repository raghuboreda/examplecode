class LinkedListNode(object):
    def __init__(self, value=0):
        self.value = value
        self.next = None

def merge_two_sorted_lists(list1, list2):
    dummy = tail = LinkedListNode()
    while list1 and list2:
        if list1.value < list2.value:
            tail.next, list1 = list1, list1.next
        else:
            tail.next, list2 = list2, list2.next
        tail = tail.next
    if list1 or list2:
        tail.next = list1 or list2
    return dummy.next

def merge_sorted_linked_lists(arr):
    '''
    :param arr: list of sorted linked lists
    :return: single linked list with all lists merged and sorted
    '''
    l1 = arr[0]
    for i in range(1, len(arr)):
        l2 = arr[i]
        l1 = merge_two_sorted_lists(l1, l2)
    return l1

def make_linked_list(arr):
    head = tmp = None
    for i,num in enumerate(arr):
        if i == 0:
            head = LinkedListNode(num)
            prev = head
        else:
            prev.next = LinkedListNode(num)
            prev = prev.next
    return head

def print_linked_list(node):
    tmp = node
    while tmp != None:
        print(tmp.value)
        tmp = tmp.next
    return

arr1 = [1,3,8]
arr2 = [2,5,9]
arr3 = [4,6,12]
head1 = [make_linked_list(arr1), make_linked_list(arr2), make_linked_list(arr3)]
for item in head1:
    print_linked_list(item)
head = merge_sorted_linked_lists(head1)

print_linked_list(head)


