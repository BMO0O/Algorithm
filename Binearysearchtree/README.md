# BinarySearch Tree   
This is Binary search tree in python 3.

## Pseudo code  
```
SEARCH(node, key){
    if node == NIL or node.key == key
        return node
    if key < node.key
        return SEARCH(node.left, key)
    else
        return SEARCH(node.right, key) }  


INSERT(node, key){
    if node == NIL
        node.key = key
        node.left = NIL
        node.right = NIL
    else if key < node.key
        node.left = INSERT(node.left, key)
    else
        node.right = INSERT(node.right, key)
    return node }
```
