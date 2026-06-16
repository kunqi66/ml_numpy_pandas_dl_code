def fun(nums):
    i,j=1,0
    while i<len(nums):
        if nums[j] == nums[i]:
            i+=1
            continue
        else:
            nums[i],nums[j+1] = nums[j+1],nums[i]
            i+=1
            j+=1
    return j+1

nums = [0,0,1,1,1,2,2,3,3,4]
print(fun(nums))
print(nums)