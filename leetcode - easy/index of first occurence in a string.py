haystack="sadbutsad"
needle="sad"

p=len(needle)

n=list(haystack)
m=list(needle)

g=[]
k=[]

a=[ord(char) for char in n]
b=[ord(char) for char in m]

for i in range(len(a)-p+1):
    z=a[i:i+p]
    for j in b:
        if z==b:
            d=b
            o=a[i]
            g.append(i)
            break

if g:
    print(g[0])
else:
    print(-1)



'''
class Solution(object):
    def strStr(self, haystack, needle):
        if not haystack:
            return -1
        if needle == "":
            return 0
        if needle in haystack:
            for i in range(len(haystack)):
                if haystack[i:i+len(needle)] == needle:
                    return i
        else:
            return -1

'''
