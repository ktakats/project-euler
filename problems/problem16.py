T=int(raw_input().strip())

for _ in range(T):
    N=int(raw_input().strip())

    print sum(map(int, str(2**N)))
