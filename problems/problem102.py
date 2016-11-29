def det(x,y,a,b):
    return x*b-y*a*1.

def inTriangle(x1,y1,x2,y2,x3,y3):
    v1x=x2-x1
    v1y=y2-y1
    v2x=x3-x1
    v2y=y3-y1
    a=(-det(x1,y1,v2x,v2y))/det(v1x,v1y,v2x,v2y)
    b=(det(x1,y1,v1x,v1y))/det(v1x,v1y,v2x,v2y)
   # print a,b
    if a>=0 and b>=0 and a+b<1:
        return True
    else:
        return False

N=int(raw_input().strip())
count=0
for _ in range(N):
    x1,y1,x2,y2,x3,y3=raw_input().strip().split(" ")
    x1,y1,x2,y2,x3,y3=[int(x1),int(y1),int(x2),int(y2),int(x3),int(y3)]
    if inTriangle(x1,y1,x2,y2,x3,y3):
        count+=1
print count
