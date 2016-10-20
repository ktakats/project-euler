def palindrom(n):
    return str(n)[::-1]==str(n)

def tobase(num, K):
    newbase=[]
    while(num>0):
        newbase.append(num % K)
        num=num/K
    newbase.reverse()
    return int(''.join(str(i) for i in newbase))

N,K=raw_input().strip().split(" ")
N=int(N)
K=int(K)
out=[]
for num in range(1,N):
    if palindrom(num):
        if palindrom(tobase(num, K)):
            out.append(num)
print sum(out)
