def get_subsets(lst):
    if not lst:
        return [[]]
    
    first = lst[0]
    rest_subsets = get_subsets(lst[1:])
    subsets_with_first = [[first] + subset for subset in rest_subsets]
    
    return rest_subsets + subsets_with_first

def product(subset):
    result=1
    for num in subset:
        result*=num
    return result
'''
target=24
nums=[3,1,6,4,8]
'''

l=[]
subsets=get_subsets(nums)

for s in subsets:
    if s:
        n=f"{product(s)}"
        l.append(n)


f=False
for i in range(len(l)):
    if target==i:
        print("true")
        f=True
        break

if not f:
    print("false")




