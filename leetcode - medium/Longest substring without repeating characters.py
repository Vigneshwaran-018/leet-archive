



s="abcabcbbmnopq"

s=list(s)
l=[]

for i in s:
    l.append(i)
    #print(l)
    if i in l:
        del l[0:l.index(i)]

    print(l)
