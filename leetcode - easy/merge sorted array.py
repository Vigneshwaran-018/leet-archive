

nums1=[1,2,3,0,0,0]
m=3

nums2=[2,5,6]
n=3

l=[]
k=[]

for i in range(m):
    i=nums1[i]
    l.append(i)
for i in range(n):
    i=nums2[i]
    k.append(i)

s=l+k
print(sorted(s))
