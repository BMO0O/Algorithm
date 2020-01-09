# Matrix_path

This code is solution of matrix path problem.  
### Problem  
- Only can move to right or down  
- Find the path which the sum of the value of current and adjacent space is biggest moving from the upper left side to the lower right side.  
### Pseudo code    
```  
MATRIX-PATH(i, j){  
 if i == 0 or j == 0 :  
   return 0;  
   
 return m[i][j] + max(MATRIX-PATH(i-1, j), MATRIX-PATH(i, j-1));}  
```
