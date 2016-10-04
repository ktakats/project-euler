def ZellerCongruence(y,m,d):
    if m<3:
        m+=12
        y-=1
    K=y%100
    J=y/100
    day=(d+(13*(m+1)/5)+K+(K/4)+J/4+5*J)
    return day % 7

def countSundays(Y1,M1,D1,Y2,M2,D2):
    if D1==1 and ZellerCongruence(Y1,M1,D1)==1:
        sundays=1
    else:
        sundays=0

    while True:
        if Y1==Y2 and M1==M2:
            return sundays
        if M1<12:
            M1+=1
        else:
            Y1+=1
            M1=1

        if ZellerCongruence(Y1,M1,1)==1:
            sundays+=1


T=int(raw_input().strip())

for _ in range(T):
    Y1,M1,D1=map(int,raw_input().strip().split(" "))
    Y2,M2,D2=map(int,raw_input().strip().split(" "))
    print countSundays(Y1,M1,D1,Y2,M2,D2)
