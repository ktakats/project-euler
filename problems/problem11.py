M=[]
for i in range(20):
    M.append(map(int, raw_input().strip().split(" ")))

maxi=1
for i in range(20):
    for j in range(20):
        #horizontal
        if j<17:
            h=M[i][j]*M[i][j+1]*M[i][j+2]*M[i][j+3]
        else:
            h=1
        #vertical
        if i<17:
            v=M[i][j]*M[i+1][j]*M[i+2][j]*M[i+3][j]
        else:
            v=1
        #left diagonal
        if i<17 and j>2:
            ld=M[i][j]*M[i+1][j-1]*M[i+2][j-2]*M[i+3][j-3]
        else:
            ld=1
        #right diagonal
        if i<17 and j<17:
            rd=M[i][j]*M[i+1][j+1]*M[i+2][j+2]*M[i+3][j+3]
        else:
            rd=1
        maxi=max(maxi, h, v, ld, rd)
print maxi
