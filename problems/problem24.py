#factorial number system
import math

def getString(num):
    factsys=[]
    outString=""
    for i in range(1, 14):
        factsys.append(num % i)
        num/=i
    factsys.reverse()
    for i in factsys:
        outString+=string[i]
        string.remove(string[i])
    return outString




T=int(raw_input().strip())

for _ in range(T):
    string=list('abcdefghijklm')
    N=int(raw_input().strip())
    print getString(N-1)
