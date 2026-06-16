import sys
def fun(nums):
    d = {}
    for i in nums:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    return max(d, key=d.get)

nums = [2,2,1,1,1,2,2]
print(fun(nums))