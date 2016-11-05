def numtoWord(num):
    ones=["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    tens=["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    teens=["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    levels=["Hundred", "Thousand", "Million", "Billion", "Trillion"]

    out=""

    if num>=10**12:
        lev=levels[4]
        div=10**12
    elif num>=10**9:
        lev=levels[3]
        div=10**9
    elif num>=10**6:
        lev=levels[2]
        div=10**6
    elif num>=1000:
        lev=levels[1]
        div=1000
    elif num>=100:
        lev=levels[0]
        div=100

    if num>=100:
        out+=numtoWord(num/div) + lev + " "
        if num-num/div*div>0:
            out+=numtoWord(num-num/div*div)
    elif num>=20 and num<100:
        out+=tens[num/10] + " "
        if num-num/10*10>0:
            out+=numtoWord(num-num/10*10)
    elif num>=10 and num<20:
        out+=teens[num-10] + " "
    elif num<10 and num>0:
        out+=ones[num] + " "
    elif num==0:
        out+=ones[num]
    return out

T=int(raw_input().strip())


for _ in range(T):
    N=int(raw_input().strip())
    print numtoWord(N)
