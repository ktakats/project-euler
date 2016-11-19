#http://www.afjarvis.staff.shef.ac.uk/maths/jarvisspec02.pdf

import math

def digits(num, p):
    a=5*num
    b=5
    lim=10**(p+1)
    while b<lim:
        if a>=b:
            a=a-b
            b+=10
        else:
            a=a*100
            b=(b-5)*10+5
    return b

N=int(raw_input().strip())
P=int(raw_input().strip())
sumi=0
for n in range(N+1):
    i=math.sqrt(n)
    if i!=int(i):
        d=digits(n,P)
        s=map(int, list(str(d)))
        sumi+=sum(s[:P+1])
print sumi
