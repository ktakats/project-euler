#https://oeis.org/A046175
def triPlusPenta(num):
    a=[1,20]
    b=0
    i=2
    while b*(b+1)/2<num:
        b=14*a[i-1]-a[i-2]+6
        a.append(b)
        i+=1
    return a[:-1]

#https://oeis.org/A046178/internal
def pentaPlusHexa(num):
    a=[1,165]
    b=0
    i=2
    while b*(3*b-1)/2<num:
        b=194*a[i-1]-a[i-2]-32
        a.append(b)
        i+=1
    return a[:-1]

N, i, j=raw_input().strip().split(" ")
N=int(N)
i=int(i)

if i==3:
    arr=triPlusPenta(N)
    for k in arr:
        print k*(k+1)/2
else:
    arr=pentaPlusHexa(N)
    for k in arr:
        print k*(3*k-1)/2
