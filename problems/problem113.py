def count():
    inc=[0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 54]
    temp=[0]*(len(inc))

    for i in range(4,10**5):
        for l in range(1,len(temp)):

            temp[l]=sum(inc[:l+1])
        inc=temp[:]
        allk[i]=(sum(inc[:-1])+sum(inc)+allk[i-1]-9) % (10**9+7)


    return True

allk=[0]*(10**5+1)
allk[3]=474
count()

T=int(raw_input().strip())

for _ in range(T):
    k=int(raw_input().strip())
    print allk[k]
