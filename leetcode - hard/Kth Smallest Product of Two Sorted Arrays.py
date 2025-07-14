
nums1=[2,5]
nums2=[3,4]

k=2
l=[]
i=0
while i<len(nums1):
    j=0
    while j<len(nums2):
        l.append(nums1[i]*nums2[j])
        j+=1
    i+=1

l=sorted(l)
print(l[k-1])
