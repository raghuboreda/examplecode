import bisect
from collections import deque
class TreeNode(object):
    def __init__(self, label=None, left_ptr=None, right_ptr=None):
        self.label = label
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr

class bst(object):
    def __init__(self, node):
        self.root = node
    def insertHelper(self, root, node):
        # base case
        if root.left_ptr == None and root.right_ptr == None:
            if node.label > root.label:
                root.right_ptr = node
            else:
                root.left_ptr = node
            return
        # recursive case
        if node.label > root.label:
            if root.right_ptr:
                self.insertHelper(root.right_ptr, node)
            else:
                root.right_ptr = node
        if node.label < root.label:
            if root.left_ptr:
                self.insertHelper(root.left_ptr, node)
            else:
                root.left_ptr = node
        return
    def insert(self, node):
        if self.root == None:
            self.root = node
            return
        self.insertHelper(self.root, node)
        return


def minimum_bst(root):
    node = root
    while node.left_ptr != None:
        node = node.left_ptr
    return node.label

def maximum_bst(root):
    node = root
    while node.right_ptr != None:
        node = node.right_ptr
    return node.label

def inorder_traverse(root):
    if root == None:
        return
    inorder_traverse(root.left_ptr)
    print(root.label)
    inorder_traverse(root.right_ptr)

def isBstIterative(root):
    #  root , root.left, root.right
    stack = []
    prev = None
    node = root
    while node or len(stack):
        while node:
            stack.append(node)
            node = node.left_ptr
        node = stack.pop()
        if prev == None:
            prev = node.label
        elif node.label < prev:
            return False
        else:
            prev = node.label
        node = node.right_ptr
    return True

def next_succesor(root, value):
    node = root
    prev = None
    while node:
        if node.label < value:
            prev = node
            node = node.right_ptr
        elif node.label > value:
            prev = node
            node = node.left_ptr
        elif node.label == value:
            break
    if node == None:
        print("Cannot find the element")
        return -1
    if node.right_ptr:
        return minimum_bst(node.right_ptr)
    elif prev.left_ptr == node:
        return prev.label
    elif prev.left_ptr == node:
        print("Need to get parents parent")
        return -1

def find_index(arr, x):
    i = bisect.bisect_left(arr, x)
    if i != len(arr) and arr[i] == x:
        return i
    return -1

def makeTree(pre, inorder, s, e, offset):
    if s > e:
        return
    if s == e:
        return TreeNode(label=pre[s])
    root_index = find_index(inorder, pre[s])
    node = TreeNode(label=pre[s])
    lcount = root_index - offset
    print('S:', s, e, lcount)
    rcount = e - offset
    print('E:', rcount, e)
    left_offset = offset
    right_offset = root_index + 1
    node.left_ptr = makeTree(pre, inorder, s+1, s+lcount, left_offset)
    node.right_ptr = makeTree(pre, inorder, s+lcount+1, e, right_offset )
    return node

def sorted_list_binary_search_tree(preorder):
    inorder = sorted(preorder)
    print('Inorder:', inorder)
    print('Preorder:', preorder)
    root = makeTree(preorder, inorder, 0, len(inorder)-1, 0)
    return root

def level_order_traverse(root):
    tree_q = deque()
    tree_q.append(root)
    l = len(tree_q)
    result = []
    while l > 0:
        nl = []
        for i in range(0, l):
            node = tree_q.popleft()
            nl.append(node.label)
            if node.left_ptr:
                tree_q.append(node.left_ptr)
            if node.right_ptr:
                tree_q.append(node.right_ptr)
        result.append(nl)
        l = len(tree_q)
    return result

#node = sorted_list_binary_search_tree([50,90,80,85,83])
#result = level_order_traverse(root)
#print(result)
def make_a_balanced_binary_tree():
    root = TreeNode(50)
    bstObj = bst(root)
    arr = [35,25,45,75,65,100]
    for elem in arr:
        bstObj.insert(TreeNode(elem))
    return bstObj.root
root_node = make_a_balanced_binary_tree()
#inorder_traverse(root_node)
#result = level_order_traverse(root_node)
#print(result)
#print(isBstIterative(root_node))
#rint(next_succesor(root_node, 55))

def pb_helper(node, level, result):
    # base-case:
    if node == None:
        return
    if level in result:
        result[level].append(node.label)
    else:
        result[level] = list()
        result[level].append(node.label)  # '0" : [ 6,7 ], '-1': [3,2], '-2':[5,9]

    if node.left_ptr:
        pb_helper(node.left_ptr, level - 1, result)  # 3, -1, { }, 5 , -2,
    if node.right_ptr:
        pb_helper(node.right_ptr, level + 1, result)  # 2, -1,
    return


def print_level_lr(root):
    if root == None:
        return None
    result = {}
    pb_helper(root, 0, result)
    for k in sorted(result.keys()):
        print(result[k], end=' ')

#print_level_lr(root_node)

def is_tree_balanced(root):
    '''
    Tree is balanced if difference in depth between every left and right subtree is 1
    :param root:
    :return: True if balanced else false
    '''
    def tree_depth( node, balanced ):
        left, right = 0, 0
        if node.right_ptr == None and node.left_ptr == None:
            return 0
        if balanced[0] == False:
            return 0
        if node.left_ptr:
            left = tree_depth(node.left_ptr, balanced) + 1
        if node.right_ptr:
            right = tree_depth(node.right_ptr, balanced) + 1
        if abs(right-left) >= 2:
            print(left, right)
            balanced[0] = False
        return max(left, right)

    gr = [True]
    tree_depth(root, gr)
    return gr[0]
#print(is_tree_balanced(root_node))
def is_tree_symmetric(root):
    '''
    Left subtree should be mirror image of right subtree
    check left subtree and right subtree for each node while
    traversing from root to leafs
    :param root:
    :return: True or False
    '''
    def is_symmetric(node1, node2):
        if node1 == None and node2 == None:
            return True
        if node1 and node2:
            return ( node1.label == node2.label and
                     is_symmetric(node1.left, node2.right) and
                     is_symmetric(node1.right, node2.left))
        return False
    if root == None:
        return True
    return is_symmetric(root.left_ptr, root.right_ptr)
def lca(root, node_a, node_b):
    '''
    Lowest common ancestor of any two nodes is the node furthest from the root that is
    an ancestor to both nodes.
    :param root:
    :return: common ancestor Node
    '''
    left, right = None, None
    if root == None:
        return None
    if root.label in (node_a.label, node_b.label):
        return root.label
    if root.left_ptr:
        left = lca(root.left_ptr, node_a, node_b)
    if root.right_ptr:
        right = lca(root.right_ptr, node_a, node_b)
    if left and right:
        return root.label
    else:
        return left or right