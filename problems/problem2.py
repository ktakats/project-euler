T=int(raw_input().strip())

def fib(N):
    n1=0
    n2=2
    n3=8
    sumit=n1+n2+n3
    while True:
        n1=n2
        n2=n3
        n3=4*n2+n1
        if n3>N:
            break
        else:
            sumit+=n3

    return sumit

for i in range(T):
    N=int(raw_input().strip())
    print fib(N)
