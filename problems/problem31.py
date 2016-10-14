p=[1,2,5,10,20,50,100,200]

def countvar():
    vals=[0]*(10**5+1)
    vals[0]=1
    for k in range(len(p)):
        for i in range(p[k],10**5):
            vals[i]=(vals[i]+vals[i-p[k]])%(10**9+7)

    return vals


vals=countvar()
T=int(raw_input().strip())
for _ in range(T):
    N=int(raw_input().strip())
    print vals[N]
    
