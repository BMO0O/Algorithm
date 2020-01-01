# Python3 program to make fibonacci numbers in two different ways
from timeit import default_timer as timer

f = [0,0,0,0,0,0,0,0,0,0,0]

len = int(len(f))-1

# A utility function to make fibonacci numbers in basic way
def FIB(A, n):
    if A[n] != 0:
        return A[n]
    if n == 1  or n == 2:
        A[n] = 1
    else:
        A[n] = FIB(A, n-1) + FIB(A, n-2)
    return A[n]

# A utility function to make fibonacci numbers in advaced way suited for python
def FIB2(A, n):
    A[0], A[1] = 0, 1
    for i in range(n-1):
        A[i+2] = A[i+1]+A[i]
    return A[i+2]
start = timer()
FIB(f, len)
print(timer()-start)
print(f)

start2 = timer()
FIB2(f, len)
print(timer()-start2)
print(f)

    

