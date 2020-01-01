import random
from timeit import default_timer as timer

def merge_sort(x):
    if len(x) > 1:
        mid = len(x) // 2
        lx, rx = x[:mid], x[mid:]
        merge_sort(lx)
        merge_sort(rx)
        li, ri, i = 0, 0, 0
        while li<len(lx) and ri<len(rx):
            if lx[li] < rx[ri]:
                x[i] = lx[li]
                li+=1
            else:
                x[i]=rx[ri]
                ri += 1
            i += 1
        x[i:] = lx[li:] if li != len(lx) else rx[ri:]


def test(A):
    for i in range(1, len(A)):
        if A[i-1]>A[i]:
            return False
    return True

x = random.sample(range(10000),100)
start = timer()
merge_sort(x)
print(timer()-start)
print(x)
print(test(x))