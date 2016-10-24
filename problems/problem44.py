import math

def isPenta(num, K):
    nk=(num-K)*(3*(num-K)-1)/2
    n=num*(3*num-1)/2
    first=math.ceil(math.sqrt((n-nk)*2./3))
    second=math.ceil(math.sqrt((n+nk)*2./3))
    if first*(3*first-1)==2*(n-nk) or second*(3*second-1)==2*(n+nk):
        return True
    else:
        return False

N,K=raw_input().strip().split(" ")
N=int(N)
K=int(K)
sumi=0
num=K+1
while(num<N):
    if isPenta(num, K):
        print num*(3*num-1)/2
    num+=1
