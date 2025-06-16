
s="Hello World "
s=s.strip()

s=s[::-1]
l=[]

for i in s:
    if i==" ":
        break
    l.append(i)

print(len(l))
