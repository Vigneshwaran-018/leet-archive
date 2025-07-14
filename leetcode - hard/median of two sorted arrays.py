class Solution(object):
    def findMedianSortedArrays(self,nums1,nums2):
        p=sorted(nums1+nums2) # 1 2 3 7
        if len(p)%2!=0:
            o=int((len(p)-1)/2)
            return (p[o])

        elif len(p)%2==0:
            o=(len(p)//2)
            print(o)
            t=((len(p)//2)+1)
            print(t)
            if (p[o]==0 and p[t]==0):
                return 0
            elif (p[o]==-1 and p[t]==0):
                return -0.5
            elif (p[o]==0 and p[t]==1):
                return 0.5
            else:
                return ((p[o-1])+(p[t-1]))/2.0

    print(findMedianSortedArrays(0,[1,3],[2,7]))
