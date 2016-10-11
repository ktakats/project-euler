"""
d1=(2n+1)^2
d2=(2n+1)^2-2n
d3=(2n+1)^2-2n-2n
d4=(2n+1)^2-3*(2n)

d1+d2+d3+d4=4(2n+1)^2+4*(2n)=16*n^2+4*n+4
sum n=1..N 16*n^2+4*n+4n=16*N(N+1)(2N+1)/6+4*N/2*(N+1)+4N
+1
"""

def diagonalSum(N):
    d=8*N*(N+1)*(2*N+1)/3+2*N*(N+1)+4*N+1
    return d

T=int(raw_input().strip())

for _ in range(T):
    n=int(raw_input().strip())
    print diagonalSum((n-1)/2) % (10**9+7)
