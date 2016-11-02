def expSquaring(num, n):
    if n<0:
        return expSquaring(1/num, -n)
    elif n==0:
        return 1
    elif n==1:
        return num
    elif n % 2==0:
        return expSquaring(num*num, n/2)
    elif n % 2!=0:
        return num*expSquaring(num*num, (n-1)/2)

N=int(raw_input().strip())

m=0
out=0
for i in range(1, N):
    if i%10!=0:
        for j in range(1, N):
            arr=list(str(expSquaring(i,j)))
            n=sum(int(k) for k in arr)
            if n>m:
                m=n

print m
