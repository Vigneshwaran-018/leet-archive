words=["leet","code"]
x="e"
r=[]
n = len(words)
for i in range(n):
    if x in words[i]:
        r.append(i)
        print(x)