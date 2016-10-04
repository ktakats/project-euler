T=int(raw_input().strip())

def sumsq(N):
    out=long(0)
    for i in range(1,N+1):
        out+=i**2
    return out

def sqsum(N):
    if(N==1):
        return 1
    if (N%2==0):
        return ((N+1)*N/2)**2
    else:
        return (N*(N-1)/2+N)**2

for i in range(T):
    N=int(raw_input().strip())
    print abs(sumsq(N)-sqsum(N))
