import math
N=int(raw_input().strip())

for n in range(int(math.ceil((10**(N-1))**(1./N))), int((10**N)**(1./N))+1):
    i=n**N
    if i>10**(N-1) and i<10**N:
        print n**N
