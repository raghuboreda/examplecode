class Node( object ):
    def __init__( self, value, next=None ):
        self.value = value
        self.next = next

    def insert( self, node ):
        if self.next == None:
            self.next = node
        else:
            self.next.insert( node )

    def search( self, key ):
        tmp = self
        while( tmp.next is not None ):
            if key == tmp.value:
                return tmp
            tmp = tmp.next
        # check last element
        if tmp.value == key:
            return tmp
        return None

class LinkedList( object ):
    def __init__( self ):
        self.root = None

    def insert( self, node ):
        if self.root == None:
            self.root = node
        else:
            self.root.insert( node )

    def search( self, key ):
        rc = self.root.search( key )
        return rc

nodeList = [ 'Apple', 'Boston', 'Charlie', 'Delta', 'Elmo', 'Fai', 'Gary', 'Henry']
secnodeList = [ 'Junior', 'Kelp', 'Larry', 'Munro', 'Nathan', 'Olivia', 'Peter', 'Queer']

head = LinkedList()

for val in nodeList + secnodeList:
    node = Node( val )
    head.insert( node )

def printLinkListInOrder( linkedlist=None ):
    head = linkedlist.root
    tmp = head
    while( tmp != None ):
        print tmp.value
        tmp = tmp.next

def swapLL( ll=None ):
    head = ll.root
    if head is None or head.next is None:
       return
    node = head 
    head = node.next
    prevNode = None
    while( node != None ):
        tmpNode = node.next.next
        node.next.next = node
        if prevNode is not None:
            prevNode.next = node.next
        node.next = tmpNode
        prevNode = node
        node = tmpNode
    ll.root = head
    return

printLinkListInOrder( linkedlist=head )
swapLL( ll=head )
printLinkListInOrder( linkedlist=head )
node = head.search( 'Delta' )
print node.next.value
