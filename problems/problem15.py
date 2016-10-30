import math

T=int(raw_input().strip())

for _ in range(T):
    N,M=map(int,raw_input().strip().split(' '))
    print math.factorial(N+M)/(math.factorial(N)*math.factorial(M)) % 1000000007
