import collections
import itertools

LST = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
C = 6
DCT = {6: 55, 4: 40, 18: 60, 5: 45}

L = collections.Counter(LST)
D = collections.Counter(L).items()
K = collections.Counter(L).keys()
V = collections.Counter(L).values()

# D = dict(itertools.zip_longest(*[iter(L)] * 2, fillvalue=""))
print(L)
print(D)
print(K)
print(V)
print(" ")
print()

# X= TOTAL NUMBER OF SHOES
X = 10

# Get the total tally of shoe sizes
line = LST
SIZE = [6, 6, 6, 4, 18, 10]
PRICE = 55, 45, 55, 40, 60, 50
# Read the number of customers
N = 6
# save the earnings
earnings = 0
for _ in range(N):
    S = " ".join(SIZE).split(" ")
    if L[SIZE] > 0:
        earnings += PRICE
        L[SIZE] -= 1

print(earnings)
