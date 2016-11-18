def findMin(arr):
    sol = [0]*len(arr)
    for i in range(len(arr)):
        sol[i]=arr[i][len(arr)-1]

    for i in range(len(arr)-2,-1,-1):
        sol[0]+=arr[0][i]
        for j in range(1,len(arr)):
            sol[j]=min(sol[j-1]+arr[j][i], sol[j]+arr[j][i])

        for j in range(len(arr)-2,-1,-1):
            sol[j]=min(sol[j], sol[j+1]+arr[j][i])


    return min(sol)

N=int(raw_input().strip())

arr=[]
for n in range(N):
    arr.append(map(int, raw_input().strip().split(' ')))

print findMin(arr)


""" My original solution, doesn't pass the test, not sure why.

def findMin(arr):

    for j in range(len(arr)-2,0,-1):
        for i in range(len(arr)-1,-1,-1):
            if i==len(arr)-1:
                arr[i][j]+=min(arr[i][j+1], arr[i-1][j]+arr[i-1][j+1])
            elif i==0:
                arr[i][j]+=min(arr[i][j+1], arr[i+1][j])
            else:
                arr[i][j]+=min(arr[i+1][j], arr[i][j+1], arr[i-1][j]+arr[i-1][j+1])
    j=0
    for i in range(len(arr)-1,-1,-1):
        arr[i][j]+=arr[i][j+1]

    return min([i[0] for i in arr])
"""
