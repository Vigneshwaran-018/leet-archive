

numRows=5



for i in range(numRows):
    o=[[1],[1,1]]
    p=o[-1]
    for j in o[-1]:
        l=[p[0],i+j,p[-1]]
    o.append(l)
    print(o)
