

nums=[9,6,4,2,3,5,7,0,1]

l=len(nums)
o=[]

for i in range(l+1):
    o.append(i)


p=[num for num in o if num not in nums]

for i in p:
    print(i)

