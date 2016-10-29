import math

N,K=raw_input().strip().split(" ")
N=int(N)
K=long(K)

def comb(N):
    count=N+1
    n=0
    f=math.factorial(N)/(math.factorial(n)*math.factorial(N-n))
    long(f)
    while f<=K and n<=N/2:
        if n==N/2 and N%2==0:
            count-=1
        else:
            count-=2
        n+=1
        f=math.factorial(N)/(math.factorial(n)*math.factorial(N-n))
    return count

out=0
long(out)

lims=[1,1,9,13,16,20,23,26,30,33,37,40,43,47,50,54,57,60,64]

j=lims[int(math.log10(K))]


for i in range(j,N+1):
   # print i, comb(i)
    out+=comb(i)

print out
    
