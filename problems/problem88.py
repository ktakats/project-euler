#still too slow
#http://www.mathblog.dk/project-euler-88-minimal-product-sum-numbers/

import math

def mins(maxK):
    maxNumber = 2 * maxK;

    numFactors=int(math.log10(maxNumber) / math.log10(2))
    factors = [0]*numFactors;

    k=[x*2 for x in range(0,maxK+1)]
    k[1] = 0;

    factors[0] = 1
    curMaxFactor = 1
    j = 0

    while True:
        if j == 0:
            #at first factor
            if curMaxFactor == numFactors:
                #Used all the factos we can
                break

            if factors[0] < factors[1]:
                #can increment
                factors[0]+=1
            else:
                #add another factor
                curMaxFactor+=1
                factors[curMaxFactor - 1] =2
                factors[0] = 2;


            j+=1
            factors[1] = factors[0]-1;
        elif j == curMaxFactor-1:
            #At the max factor
            factors[j]+=1
            sumi = 0;
            prod = 1;
            for i in range(0,curMaxFactor):
                prod *= factors[i]
                sumi += factors[i]


            if prod > maxNumber:
                #Exceed the limit so go back
                j-=1
            else:
                #Check the result
                pk = prod - sumi + curMaxFactor
                if pk <= maxK and prod < k[pk]:
                    k[pk] = prod


        elif factors[j] < factors[j + 1]:
            #increment the reset the next factor
            #and go up
            factors[j]+=1
            factors[j+1] = factors[j]-1
            j+=1
        elif factors[j] >= factors[j + 1]:
            #Need to go further back
            j-=1


    return sum(list(set(k)))

N=int(raw_input().strip())
#a=mins(N)
#print a
print mins(N)
