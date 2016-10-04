import math

T=int(raw_input().strip())

def checkit(N):
    out=1
    M=math.sqrt(N)
    while(N%2==0):
        N=N/2
    if N==1:
        return 2
    j=3
    while(N>1):
        while(N%j!=0 and j<M):
            j+=2
        if(N%j==0):
            N=N/j
            if N==1:
                return j
        else:
            return N

for i in range(T):
    N=int(raw_input().strip())
    print checkit(N)
