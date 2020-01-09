# BinarySearch delete tree  
This is a simple BST insert and delete with parent node.   
I refered Algorithm book, '관계 중심의 사고법 - 쉽게 배우는 알고리즘(개정판)'.  

## Pseudo Code  
```
DELETE-NODE(r){
    if r.left == NIL and r.right == NIL
        return NIL
    else if r.right == NIL
        return r.left
    else if r.left == NIL
        return r.right
    else
        s = r.right
        while s.left != NIL
            parent = s
            s = s.left
        r.key = s.key
        if s == r.right
            r.right = s.right
        else
            parent.left = s.right
        return r}  

DELETE(node){
    if node == root  
        root = DELETE-NODE(node)  
    else if node == node.parent.left  
        node.parent.left = DELETE-NODE(node)  
    else  
        node.parent.right = DELETE-NODE(node)  
```