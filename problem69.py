primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]

T=int(raw_input().strip())

for _ in range(T):
    N=int(raw_input().strip())
    n=1
    for p in primes:
        n*=p
        if n>=N:
            print n/p
            break
        
