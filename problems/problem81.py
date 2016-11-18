def findMin(arr):
    for i in range(len(arr)-2,-1,-1):
        arr[len(arr)-1][i]+=arr[len(arr)-1][i+1]
        arr[i][len(arr)-1]+=arr[i+1][len(arr)-1]

    for i in range(len(arr)-2,-1,-1):
        for j in range(len(arr)-2,-1,-1):
            arr[i][j]+=min(arr[i+1][j], arr[i][j+1])
    return arr[0][0]


N=int(raw_input().strip())

arr=[]
for n in range(N):
    arr.append(map(int, raw_input().strip().split(' ')))

print findMin(arr)
