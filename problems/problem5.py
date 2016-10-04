T=int(raw_input().strip())

def findnum(N):
    if N==1:
        return 1
    else:
        if (findnum(N-1) % N !=0):
            i=2
            while(N%i!=0 and i<N):
                i+=1
            if(i!=N):
                return findnum(N-1)*i
            else:
                return findnum(N-1)*N
        else:
            return findnum(N-1)


for i in range(T):
    N=int(raw_input().strip())
    print findnum(N)
