import math
def pitTriangles(plim):
    peris=[0]*plim
    q=[(3,4,5)]
    pop=q.pop
    while q:
        a,b,c=pop()
        sumabc=a+b+c
        if sumabc<=plim:
            for i in range(1, plim//sumabc):
                peris[i*sumabc]+=1
            a2, b2, c2, c3 = 2*a, 2*b, 2*c, 3*c
            p1 = (-a+b2+c2, -a2+b+c2, -a2+b2+c3)
            p2 = ( a+b2+c2,  a2+b+c2,  a2+b2+c3)
            p3 = ( a-b2+c2,  a2-b+c2,  a2-b2+c3)
            q += [p1, p2, p3]
    return peris

def findmax(N):
    parimax=[0]*N
    bestindex=0
    bestvalue=0
    for i in range(N):
        if triangles[i]>bestvalue:
            bestvalue=triangles[i]
            bestindex=i
        parimax[i]=bestindex
    return parimax

triangles=pitTriangles(5000000)
maxies=findmax(5000000)

T=int(raw_input().strip())

for _ in range(T):
    N=int(raw_input().strip())
    print maxies[N]
