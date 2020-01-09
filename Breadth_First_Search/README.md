# Breadth_First_Search_Find_Path  
    This is Python3 program to find a route to the goal point by BFS
    All movement time from one node to another is 1  
## Pseudo code  
```
    BFS(G,S){ 
      for v∈V
       visited[v] = False
    visited[s] = True
    enqueue(Q,s)
  
    while Q≠∅
      u = dequeue(Q)
      
      for v∈𝑳(𝒖)
        if visited[v] == False
          visited[v] = True
          enqueu(Q,v)}
```