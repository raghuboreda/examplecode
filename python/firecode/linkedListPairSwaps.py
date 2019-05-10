#class Node( object ):
#    def __init__( self, val ):
#        self.x = val
#        self.next = None
#
def swapPairs(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    def swapHelper(head, node, prev):
        if node == None or node.next == None:
            return head
        tmp = node.next
        node.next = tmp.next
        tmp.next = node
        node = node.next
        if prev == head:
            head = tmp
        else:
            prev.next = tmp
            prev = tmp.next
        return swapHelper(head,node,prev)
    return swapHelper(head, head, head)
