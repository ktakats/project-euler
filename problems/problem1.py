T=int(raw_input().strip())

def countit(k,n):
    m=(k-1) // n
    return (n*m*(m+1))//2

for i in range(T):
    N=int(raw_input().strip())
    out=0
    out=countit(N,3)+countit(N,5)-countit(N,15)
    print out
