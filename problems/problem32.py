def ispandigital(string):
    digits=range(1,N+1)
    if len(string)>N:
        False
    else:
        for letter in string:
            if int(letter) in digits:
                digits.remove(int(letter))
        if len(digits)==0:
            return True
    return False

N=int(raw_input().strip())
pandigitals=[]
for i in range(1,10**(N/2-1)):
    for j in range(i, 10**(N/2)):
        if i!=j:
            prod=i*j
            string=str(i)+str(j)+str(prod)
            if len(string)==N:
                if ispandigital(string) and not (prod in pandigitals):
                    pandigitals.append(prod)

print sum(pandigitals)
