import itertools

primes=[2,3,5,7,11,13,17,19]

def checkprimes(arr):
    for i in range(1, len(arr)-2):
        n=''.join(str(i) for i in arr[i:i+3])
        if int(n) % primes[i-1] !=0:
            return False
    return True

N=int(raw_input().strip())

arr=range(0,N+1)
out=0
long(out)
for num in itertools.permutations(arr):
    if N<=5:
        if checkprimes(num):
            out+=(int(''.join(str(i) for i in num)))
    else:
        if num[3]%2==0 and num[5] % 5 ==0:
            if checkprimes(num):
                out+=(int(''.join(str(i) for i in num)))
print out
