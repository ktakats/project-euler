from itertools import permutations

def goodie(num, K):
    for k in range(2,K+1):
        n=k*int(''.join(str(i) for i in num))
        narr=list(str(n))
        for i in num:
            if str(i) in narr:
                narr.remove(str(i))
            else:
                return False
        if len(narr)!=0:
            return False
    return True

N,K = raw_input().strip().split(" ")
n=len(N)
N=int(N)
K=int(K)

for i in range(6,n+1):
    arr=range(10)
    for perm in list(permutations(arr, i)):
        out=""
        num=int(''.join(str(k) for k in perm))
        if not perm[0]==0 and num<=N:
            if goodie(perm, K):
                num=int(''.join(str(k) for k in perm))
                for k in range(1,K+1):
                    out+=str(k*num)+ " "
                print out

         
