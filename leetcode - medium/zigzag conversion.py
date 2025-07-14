

s="PAYPALISHIRING"
numRows=4

s=list(s)
if numRows==1:
    print(''.join(s))

elif numRows==2:
    m,n=[],[]
    for i in range(len(s)):
        if i%2!=0:
            n.append(s[i])

        if i%2==0:
            m.append(s[i])

    o=m+n
    print(''.join(o))

else:
    n=numRows-3
    p=[]
    print(p)
    for i in range(1,n+1):
        p.append(i)

    ei=set([numRows]+[x+numRows for x in p])

    for i in range(len(s)):
        if i%numRows==0:
            ei.add(i)
            for x in p:
                ei.add(i+x)

    ei={i for i in ei if i<len(s)}
    ei=list(ei)
    ei=ei[ei.index(numRows):]

    r=[char for i,char in enumerate(s) if i not in ei]
    print(r)
        














    
