from collections import Counter

cubes=[]
for n in range(5, N):
    cubes.append(''.join(sorted(list(str(n**3)))))

c=Counter(cubes)
out=[]
for key in c.iterkeys():
    if c[key]==K:

        out.append((cubes.index(key)+5)**3)

for i in sorted(out):
    print i
