

s="abc"
t="abcde"

p=[]
q=[]

for i in s:
    p.append(ord(i))

for i in t:
    q.append(ord(i))


p=sum(p)
q=sum(q)

o=(chr(abs(p-q)))

print(o.lower())
