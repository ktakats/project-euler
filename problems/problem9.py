T=int(raw_input().strip())

def test(N):
    if ((N*N)%2!=0):
        return -1
    for a in range(N/3,0,-1):
        b=(N*(N-2*a))/(2*(N-a))
        c=N-b-a
        if(b<c and a<b and a**2+b**2==c**2):
            return a*b*c
    return -1


for t in range(T):
    N=int(raw_input().strip())
    print test(N)
