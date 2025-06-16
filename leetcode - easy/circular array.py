

nums=[1,2,4]

nums.append(nums[0])
# [1,2,4,1]

l=[]

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        k=(abs(nums[i]-nums[j]))
        l.append(k)


print(max(l))
