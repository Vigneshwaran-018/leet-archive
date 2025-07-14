
s="aab"
p="c*a*b"

n=[]
m=[]



for i in s:
    n.append(ord(i))

for j in p:
    m.append(ord(j))
    
if len(m)<=1:
    print("false")
'''
elif m[0]==46 and m[1]==42:
    print("true")
'''



