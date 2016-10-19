
N=int(raw_input().strip())
total=(N-1)*(N-1)
bases=range(2,N+1)
subt=[]
for base in range(2,N+1):
    i=2
    while(base**i<=N):
        if not (base**i in subt):
            if i==2:
                total-=N/i-1
                subt.append(base**i)
            else:
                total-=N/i-1
                subt.append(base**i)
                for j in range(N/i+1,N+1):
                    for k in range(2,i):
                        if (i*j) % k ==0 and i*j/k<=N:
                            total-=1
                            break

        i+=1
print total
