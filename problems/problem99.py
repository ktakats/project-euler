import math

N=int(raw_input().strip())
inp=[]
for _ in range(N):
    inp.append(map(int, raw_input().strip().split(" ")))
K=int(raw_input().strip())


s=sorted(inp, key=lambda n: math.log10(n[0])*n[1])
print ' '.join([str(i) for i in s[K-1]])
