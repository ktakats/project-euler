def chains(Nm):
    chain=[0]*(Nm+1)
    maxes=[0]*(Nm+1)
    max_so_far=0
    maxindex=0
    for num in range(Nm+1):
        step=1
        n=num
        while(num>1):
            if num<len(chain) and chain[num]!=0:
                step+=chain[num]-1
                num=1
            else:
                if(num%2==0):
                    num/=2
                    step+=1
                else:
                    num=num*3+1
                    step+=1
        chain[n]=step
        if step>=max_so_far:
            max_so_far=step
            maxindex=n
        maxes[n]=maxindex

    return maxes


T=int(raw_input().strip())
ns=[]
for _ in range(T):
    ns.append(int(raw_input().strip()))
Nm=max(ns)
maxes=chains(Nm)
nmax=0
m=0
for n in ns:
    print maxes[n]
