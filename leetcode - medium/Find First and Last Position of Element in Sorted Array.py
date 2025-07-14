class Solution(object):
    def searchRange(self, nums, target,):

        l=[]
        f=False
        for i in range(len(nums)):
            if target in nums:
                f=True
                if nums[i]==target:
                    l.append(i)
            else:
                l=[-1,-1]

        if f:
            k=[l[0],l[-1]]
            print(k)
        


    searchRange(0,[5,7,7,8,8,10],8)
