"""
computes the cartesian product of input iterables

"""
import itertools


A = [1, 2]
# A = list(map(int,input().split()))
B = [3, 4]
# B = list(map(int,input().split()))
C = itertools.product(A, B)
print(*C)
