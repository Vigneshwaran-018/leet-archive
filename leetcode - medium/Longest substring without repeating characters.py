



s="bbbb"

s=list(s)
f=False

l=[]

for i in range(len(s)):
    if s[i-1]==s[i]:
        l.append(1)

if len(l)==len(s):
    print("1")
