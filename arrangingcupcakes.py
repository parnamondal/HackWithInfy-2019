# cook your dish here
import math
for i in range(int(input())):
    n= int(input())
    b=[]
    for j in range(1,int(math.sqrt(n))+1):
        k = n/j
        if k -int(k)== 0 :
            b.append(abs(j-int(k)))
    print (min(b))

    