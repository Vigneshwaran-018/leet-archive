


nums=[2,4,4,2,1,1]
l=[]
nums=sorted(nums)
# [1,1,2,2,3,4,4]

for i in range(len(nums)):
    if nums[i-1]!=nums[i]!=nums[i+1]:
        print(nums[i])
