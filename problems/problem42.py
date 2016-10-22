import math

T=int(raw_input().strip())

for _ in range(T):
    N=int(raw_input().strip())
    num=int(math.sqrt(2*N))
    if num*(num+1)==2*N:
        print num
    else:
        print -1
