def fun(nums):
    if len(nums)<=1:
        return len(nums)
    i,j=1,0
    k = 0
    while i<len(nums):
        if nums[j] == nums[i] and k>=1:
            i+=1
            continue
        elif nums[j] != nums[i]:
            k = 0
            nums[i],nums[j+1] = nums[j+1],nums[i]
            i+=1
            j+=1
        else:
            nums[i],nums[j+1] = nums[j+1],nums[i]
            i+=1
            j+=1
            k+=1
    return j+1




nums = [1,2]
print(fun(nums))
print(nums)