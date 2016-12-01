def seq(n):
    midnum=[1,1,2,3]
    prev=[0,1,2]
    for i in range(4,n):

        if i%2==1:
            midnum.append((prev[i-2]+midnum[i-1])%715827881)
            prev.append((prev[i-2]+midnum[i-1]-midnum[i/2])%715827881)
        else:
            prev.append((prev[-1]+midnum[i-1])%715827881)
            midnum.append((midnum[i-1]+midnum[i-1])%715827881)
    out=""
    s=0
   # print prev
   # print midnum
    midnum.reverse()
    for i in midnum:
        s=(s+i)%715827881
        out+=str(s)+" "
    out.strip()
    return out


n=int(raw_input().strip())
print seq(n)
