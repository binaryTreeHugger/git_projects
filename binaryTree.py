
'''            15 
            /     \
          10       25
         /  \     /   \
        6   14   20    60
'''

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, newValue):
    if root is None:
        root = Node(newValue)
        return root

    if newValue < root.data:
        root.left = insert(root.left, newValue)
    else:
        root.right = insert(root.right, newValue)
    return root

def reverseTree(root):
    if root is None:
        return
    reverseTree(root.left)
    reverseTree(root.right)
    root.left,root.right = root.right, root.left

def treeSum(root):
    if root is None:
        return 0
    leftSum = treeSum(root.left)
    rightSum = treeSum(root.right)
    return root.data + leftSum + rightSum

def is_same_tree(u,v):
    if u is None or v is None:
        return u == v
    if u.data != v.data:
        return False
    leftSide = is_same_tree(u.left, v.left)
    rightSide = is_same_tree(u.right, v.right)
    return leftSide and rightSide

def preorder(root):
    if root == None:
        return
    print(root.data,end=' ')
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)


def isSortedTree(root,minVal=float('-inf'),maxVal=float('inf')):
    if root is None:
        return True
    if minVal < root.data < maxVal:
        leftSorted = isSortedTree(root.left,minVal,root.data)
        rightSorted = isSortedTree(root.right,root.data,maxVal)
        return leftSorted and rightSorted
    else:
        return False

#############################################################################
#                                                                           #
#                                                                           #
#############################################################################

root = insert(None, 15)

leaves = [10,25,6,14,20,60]
for l in leaves:
    insert(root,l)

#print('sum of all tree nodes = ',treeSum(root))

print('Is the tree sorted?')
print(isSortedTree(root))

print("\nPrinting values of binary tree in Preorder Traversal")
preorder(root)

print('\nreversing tree...')
reverseTree(root)

print("\nPrinting values of reversed tree in Preorder Traversal")
preorder(root)

print('\nIs the tree sorted?')
print(isSortedTree(root))


'''
print("Printing values of binary search tree in Inorder Traversal")
inorder(root)

print("Printing values of binary search tree in Postorder Traversal")
postorder(root)

if isSortedTree(root):
    print("The tree is sorted")

print(f'changing tree root to 3')
root.data = 3

print("Printing tree nodes in Preorder Traversal")
preorder(root)

if isSortedTree(root):
    print("The tree is sorted")   

else:
    print("This tree is not sorted")

'''










