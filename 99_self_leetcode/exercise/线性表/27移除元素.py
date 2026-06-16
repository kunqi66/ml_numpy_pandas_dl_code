def remove(nums, val):
    number = len(nums) - 1
    for i in range(number,-1,-1):
        if nums[i] == val:
            nums[number] , nums[i]= nums[i] , nums[number]
            number-=1
    return number+1



nums = [0,1,2,2,3,0,4,2]
val = 2

print(remove(nums,2))
print(nums)