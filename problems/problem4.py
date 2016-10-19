import math

T=int(raw_input().strip())

def palindrom(n):
    return str(n)[::-1]==str(n)

def threedig(n):
    j=int(math.ceil(n/999.9))
    for i in range(j,999,1):
        if(n%i==0):
            return True
    return False

def goodie(N):
    for j in range(N-1,101100,-1):
        if(palindrom(j)):
            if threedig(j):
                return j



for i in range(T):
    N=int(raw_input().strip())
    print goodie(N)
