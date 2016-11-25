import math
from collections import Counter

def square(N):
    out=[]
    out2={}
    for n in range(int(math.ceil(math.sqrt(10**(N-1)))), int(math.sqrt(10**N))+1):
        if not n**2==10**N:
            m=''.join(sorted(list(str(n**2))))
            if len(m)==N:
                out2[m]=n**2
                out.append(m)

    return out, out2

N=int(raw_input().strip())
squares, keys=square(N)
c=Counter(squares)
mc=c.most_common(5)
#print mc
if mc[0][1]==mc[1][1]:
    a=keys[mc[0][0]]
    b=keys[mc[1][0]]

    if a>b:
        print a
    else:
        print b
else:
    print keys[mc[0][0]]
