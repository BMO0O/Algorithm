import random
from timeit import default_timer as timer #timeit모듈안에 default_timer사용 timer라는 이름으로


def insertion_sort(A):
    for i in range(1, len(A)):
        loc = i-1
        new_item = A[i]
        while loc>=0 and new_item<A[loc]:
            A[loc+1]=A[loc]
            loc-=1
        A[loc+1]=new_item


def test(A):
    for i in range(1, len(A)):
        if A[i-1]>A[i]:
            return False
    return True

x = random.sample(range(1000), 100)
start = timer()
insertion_sort(x)
print(timer()-start)
print(x)
print(test(x))
