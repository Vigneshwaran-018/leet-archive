

s=["h","e","l"]
o=[]

for i in range(len(s)):
    o.append(s[-1])
    del s[-1]
 
print(o)
