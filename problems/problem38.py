def pandigital(num):
    arr=range(1,K+1)
    if len(list(num))!=len(arr):
        return False
    for digit in list(num):
        if int(digit) in arr:
            arr.remove(int(digit))
        else:
            return False
    return True

N,K=raw_input().strip().split(" ")
N=int(N)
K=int(K)

for num in range(1, N):
    sring=""
    for i in range(1,6):
        sring+=str(num*i)
        if len(sring)>K:
            break
        if pandigital(sring):
            print num
            break
           
