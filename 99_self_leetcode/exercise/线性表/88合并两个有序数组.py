def fun(num1,num2,n,m):
    i,j,s = n-1,m-1,m+n-1
    while s>=0:
        print(i,j,s)
        print(num1)
        if i<0:
            num1[s] = num2[j]
            s-=1
            j-=1
            continue
        elif j<0:
            num1[s] = num1[i]
            s-=1
            i-=1
            continue
        if num1[i] > num2[j]:
            num1[s] = num1[i]
            s-=1
            i-=1
        else:
            num1[s] = num2[j]
            s-=1
            j-=1
    return s
num1 = [4,5,6,0,0,0]
num2 = [1,2,3]
n = 3
m = 3

print(fun(num1,num2,n,m))
print(num1)