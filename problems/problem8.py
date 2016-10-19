T=int(raw_input().strip())

def count(arr):
    out=1
    for i in arr:
        out*=i
    return out

def prod(n,K):
    current=count(n[:K])
    for i in range(K+1,len(n)+1):
        current=max(count(n[i-K:i]), current)
    return current


for t in range(T):
    N,K=raw_input().strip().split(" ")
    n=map(int,str(raw_input().strip()))
    print prod(n,int(K))
