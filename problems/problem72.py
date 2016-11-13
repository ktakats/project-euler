import math

def divs():
    N=1000000
    phi=range(N+1)
    result = 0;
    results=[0]*(N+1)
    for i in range(2,N+1):
        if phi[i] == i:
            for j in range(i, N+1, i):
                phi[j] = phi[j] / i * (i - 1);

        result+=phi[i]
        results[i]=result
    return results

divis=divs()
T=int(raw_input().strip())

for _ in range(T):
    N=int(raw_input().strip())


    print divis[N]
