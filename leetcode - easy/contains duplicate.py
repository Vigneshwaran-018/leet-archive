

nums=[1,2,3,4,0,0,4]


f=False

l=[]

for i in nums:
    l.append(i)

l=sorted(l)
print(l)

for i in range(len(l)):
    if len(nums)==1:
        f=False
    elif l[i-1]==l[i]:
        f=True

if f:
    print("true")
else:
    print("false")


