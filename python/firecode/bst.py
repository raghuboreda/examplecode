class TreeNode:
    def __init__(self, data,left_child = None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
          
    def __str__(self):
        return '%s' %self.data

class BinaryTree:
    def __init__(self, root_node = None):
    # Check out Use Me section to find out Node Structure
        self.root = root_node
    # Helper Method    
    def inorder_helper( self, start, k, count ):
        #print k, count, start.data, start.right_child
        if start.right_child:
            node, count = self.inorder_helper(start.right_child, k, count=count)
            #print k, count, start.data, start.right_child.data
            if node != None:
                return node, count

        #print k, count, start.data, start.data
        count = count + 1
        if k == count:
            return start, 0
        if start.left_child:
            node, count = self.inorder_helper(start.left_child, k, count=count)
            if node != None:
                return node, count
        #print 'returning None'
        return None, count

    # insert helper
    def insert_helper( self, start, value ):
        if start.data <= value:
            if start.right_child:
                self.insert_helper(start.right_child, value)
            else:
                start.right_child = TreeNode( value )
        else:
            if start.left_child:
                self.insert_helper( start.left_child, value)
            else:
                start.left_child = TreeNode( value )

    def inorder_print_tree( self, start ):
        if start.right_child:
            self.inorder_print_tree( start.right_child )
        print start.data
        if start.left_child:
            self.inorder_print_tree( start.left_child )
        return

    def print_tree( self ):
        self.inorder_print_tree( self.root )

    def print_tree_iter( self ):
        ns = [ self.root ]
        while( len(ns) != 0 ):
            node = ns.pop()
            if node.right_child:
                ns.append( node.right_child )
            if node.left_child:
                ns.append( node.left_child )
        while( node != None ):
            node = node.left_child
        return True


    def insert( self, value ):
        if self.root == None:
            self.root = TreeNode( value )
        else:
            self.insert_helper( self.root, value )

    # find kth largest
    def find_kth_largest(self,k):
        # Return Element should be of type TreeNode
        root = self.root
        if root == None:
            return None
        if root.right_child == None or root.left_child == None:
            if k == 1:
                return root
        node, _ = self.inorder_helper( self.root, k, count=0 )
        return node

    def validate_Bst_Itr( self ):
        ns = [ self.root ]
        node = ns.pop()
        while( node != None ):
            if node.left_child:
                ns.append( node.left_child )
                if node.data < node.left_child.data:
                    return False
            if node.right_child:
                ns.append( node.right_child )
                if node.data > node.right_child.data:
                    return False
            if len(ns) == 0:
                node = None
            else:
                node = ns.pop()
        return True


def insertTree( tr=None, input_list=None ):
    for element in input_list:
        tr.insert( element )
    return

tree = BinaryTree()
insertTree( tr=tree, input_list=[5,2,9,3,7,11,10,15] )
#tree.print_tree()
#node = tree.find_kth_largest( 2 ) 
#print node
#node = tree.find_kth_largest( 3 ) 
#print node
#node = tree.find_kth_largest( 8 ) 
#print node
print tree.print_tree_iter()

