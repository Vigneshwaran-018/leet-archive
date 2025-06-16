
#Output: [[-1,-1,2],[-1,0,1]]
from itertools import combinations

nums=[-1,0,1,2,-1,-4]
p=len(nums)
k=[list(c) for c in combinations(nums, 3)]

o=[]

f=False
for i in k:
    if sum(i)==0:
        l=sorted(i)
        o.append(l)
        f=True

    if f:
        pass
    else:
        print("[]")

s=set()
u=[]
for i in o:
    t=tuple(i)
    if t not in s:
        s.add(t)
        u.append(i)

print(u)
