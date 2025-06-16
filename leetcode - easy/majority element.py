
nums=[2,2,2,2,3,2]

count=0

for i in nums:
    if i in nums:
        count+=1
    else:
        count=0

count=[nums.count(x) for x in nums]


i=count.index(max(count))

print(nums[i])
