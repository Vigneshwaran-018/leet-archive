
s = "adcb"
m=list(s)z

asc = [ord(char) for char in m]

r=""


if len(s)==1:
    r = "".join(m)
    print(r)

else:
    f=False
    for i in range(len(asc)):
        for j in range(1,len(asc)):
            if abs(asc[i]-asc[j])==1 or abs(asc[i]-asc[j])==25:
                f=True
                break
        del m[i:j+1]                
        if f==True:
            break
        else:
            print(s)
        
    r = "".join(m)
    print(r)




