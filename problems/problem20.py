import math
T=int(raw_input().strip())

for _ in range(T):
    N=int(raw_input().strip())
    arr=map(int, str(math.factorial(N)))
    print sum(arr)
