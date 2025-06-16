digits=[9,9]

l=[]
m=int(''.join(map(str,digits)))
m=m+1
m=str(m)

n=''.join(m)
print(list(n))

for j in m:
    l.append(int(j))

print(l)