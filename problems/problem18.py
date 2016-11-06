def findMax(arr,i,j):
    if i==0 and j==0:
        return arr[i][j]
    else:
        if j<=len(arr[i])-3 and j>0:
            return arr[i][j]+max(findMax(arr, i-1, j), findMax(arr, i-1, j-1))
        elif j==len(arr[i])-2 and j>0:
            return arr[i][j]+max(findMax(arr, i-1, j), findMax(arr, i-1, j-1))
        elif j>len(arr[i])-2 and j>0:
            return arr[i][j]+max(findMax(arr, i-1, j-1),0)
        else:
            return arr[i][j]+max(findMax(arr, i-1, j),0)

T=int(raw_input().strip())

for _ in range(T):
    N=int(raw_input().strip())
    arr=[]
    for n in range(N):
        arr.append(map(int, raw_input().strip().split(' ')))
    maxi=0
    for item in range(N):
        newvalue=findMax(arr, N-1, item)
        if newvalue>maxi:
            maxi=newvalue

    print maxi
