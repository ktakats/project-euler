import math
def runIt():
    n=1
    p=3
    q=2
    while n<N:
        n+=1
        p1=p+2*q
        q1=p+q
       # print n, p1, q1
        if int(math.log10(p1))>int(math.log10(q1)):
            print n
        p=p1
        q=q1

N=int(raw_input().strip())

runIt()
