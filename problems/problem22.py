def points(name):
    letters=list('.ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    point=0
    for char in name:
        point+=letters.index(char)
    return point

N=int(raw_input().strip())
names=[]


for _ in range(N):
    names.append(raw_input().strip())
    names.sort()

Q=int(raw_input().strip())
for _ in range(Q):
    name=raw_input().strip()
    point=points(name)
    print point*(names.index(name)+1) 
