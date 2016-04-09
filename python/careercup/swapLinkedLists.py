class Node( object ):
    def __init__( self, value, next=None ):
        self.value = value
        self.next = next

NodeH = Node( 'Henry' )
NodeG = Node( 'Gary', next=NodeH )
NodeF = Node( 'Fai', next=NodeG )
NodeE = Node( 'Elmo', next=NodeF )
NodeD = Node( 'Delta', next=NodeE )
NodeC = Node( 'Charlie', next=NodeD )
NodeB = Node( 'Boston', next=NodeC )
NodeA = Node( 'Apple', next=NodeB )

def printLinkListInOrder( ll ):
    while( ll != None ):
        print ll.value
        ll = ll.next

def swapLL( ll ):
    if ll is None or ll.next is None:
       return
    node = ll
    ll = node.next
    prevNode = None
    while( node != None ):
        tmpNode = node.next.next
        node.next.next = node
        if prevNode is not None:
            prevNode.next = node.next
        node.next = tmpNode
        prevNode = node
        node = tmpNode
    return ll

printLinkListInOrder( NodeA )
altNode = swapLL( ll=NodeA )
printLinkListInOrder( altNode )
