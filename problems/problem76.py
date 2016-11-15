#https://en.wikipedia.org/wiki/Partition_%28number_theory%29

import math
def part(lim):
    p=[1]*lim
    p[2]=2
    p[3]=3
    for i in range(4,lim):
        s=0
        k=1
        l=k*(3*k-1)/2
        while l<=i:
            s+=((-1)**(k-1)*p[i-l]) % (10**9+7)
            if k>0:
                k=-k
            else:
                k=-k+1
            l=k*(3*k-1)/2
        p[i]=s
    return p

parts=part(1001)

T=int(raw_input().strip())

for _ in range(T):
    N=int(raw_input().strip())
    print int((parts[N]-1) %  (10**9+7))
