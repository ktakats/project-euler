#Binet's formula, convergence, golden ratio

import math


def findFib(N):
    return int(math.ceil(((N-1)+math.log10(5)/2)/math.log10(1.61803398875)))

T=int(raw_input().strip())

for _ in range(T):
    N=int(raw_input().strip())
    print findFib(N)
