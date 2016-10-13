#narcissistic numbers
def checksum(num, N):
    arr=map(int, str(num))
    sumit=0
    for n in arr:
        sumit+=n**N
    if sumit==num:
        return True
    return False

N=int(raw_input().strip())
out=[]
for i in range(10, 1000000):
    if checksum(i, N):
        out.append(i)
print sum(out)
