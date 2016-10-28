#fastest - Fast modular exponentiation
def fast_exp(num, n, mod):
    res=1
    while n>0:
        if n % 2 ==1:
            res=(res*num) % mod
        num=(num*num)%mod
        n=n/2
    return res % mod
#faster
def modular_pow(num,n,mod):
    if mod==1:
        return 0
    c=1
    for i in range(1,n+1):
        c=(c*num) % mod
    return c
#slowest
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
sumy=0
for i in range(1,N+1):
    if i%10 ==0:
        sumy+=0
    else:
      #  sumy+=(expSquaring(i,i) % 10000000000)
      #  sumy+=modular_pow(i,i,10000000000)
        sumy+=fast_exp(i,i,10000000000)

print int(''.join(list(str(sumy))[-10:]))
