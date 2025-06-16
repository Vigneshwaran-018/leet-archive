
nums = [0,1,2,2,3,0,4,2]
val=int(input())

for i in range(len(nums)):
    if val == nums[i]:
        continue
    else:
        print(nums[i])


'''
class Solution(object):
    def removeElement(self, nums, val):
        nums = [0,1,2,2,3,0,4,2]
        val=int(input())
        k=0
        for i in range(len(nums)):
            if val == nums[i]:
                continue
            else:
                nums[k] = nums[i]
                k+=1
        print(k)
'''
