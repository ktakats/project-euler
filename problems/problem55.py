from collections import Counter

def palindrom(n):
    return str(n)[::-1]==str(n)

N=int(raw_input().strip())

pals=[]
for i in range(1,N+1):
    count=0
    if palindrom(i):
        pals.append(i)
    else:
        num=i
        while(count<60):
            num1=int(str(num)[::-1])+num
            if palindrom(num1):
                pals.append(num1)
                break
            else:
                num=num1
                count+=1

c=Counter(pals)
d=c.most_common(1)[0]
print d[0], d[1]
