# Python3 program to demonstrate insert and delete operation
# in binary search tree with parent pointer  
import random
from timeit import default_timer as timer

# A utility function to create a new BST Node
class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        
# A utility function to do insert a new node with given key in BST and save a parent node info
def insert(node, key):

    # If the tree is empty, return a new node
    if node is None: node = Node(key)

    # Otherwise, recur down the tree
    elif key < node.key: 
        node.left = insert(node.left, key)
        node.left.parent = node
    else: 
        node.right = insert(node.right, key)
        node.right.parent = node
    return node

# A utility function to search a node with given key in BST
def search(node, key):
    if node is None or node.key == key : return node
    if key < node.key: return search(node.left, key)
    return search(node.right, key)

# A utility function to delete a node with given key in BST
def delete(node, key):
    if node is None:
        return node

    if node.key < key:
        node.right = delete(node.right, key)
        
    elif node.key > key:
        node.left = delete(node.left, key)
        
    else:
        node = delete_node(node, key)

    return node
 
# A utility function to delete a node and return a new root's of subtree
def delete_node(node, key):

    # If a node doesn't have a left child, return a right child
    if node.left is None:
        temp = node.right
        node = None
        return temp
    # If a node doesn't have a right child, return a left child
    elif node.right is None:
        temp = node.left
        node = None
        return temp
    # If a node doesn't have any child, return nothing
    elif node.left is None and node.right is None:
        return None

    # If a node have both child and a left child of the node's right child doesn't have a left child,
    # duplicate a left child of the node's right child and put into the space of the deleted node
    # If not, find the end of the left child in a tree of a right child of the node, and duplicate it 
    current = node.right
    while current.left != None:
         current = current.left

    node.key = current.key  
    
    if current == node.right:
         node.right = current.right
    else:
         current.parent.left = current.right
    return node        

def inorder(root): 
    if root != None: 
        inorder(root.left) 
        print("Node :", root.key, ", ", end = "")  
        if root.parent == None: 
            print("Parent : NULL")  
        else: 
            print("Parent : ", root.parent.key) 
        inorder(root.right) 
 
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
root = insert(root, 100)
root = insert(root, 10)
root = insert(root, 90)
root = insert(root, 88)
root = insert(root, 110)
root = insert(root, 120)
root = insert(root, 109)
root = insert(root, 108)


inorder(root)
print("----delete test-----")
root = delete(root, 30)
root = delete(root, 100)


inorder(root)
