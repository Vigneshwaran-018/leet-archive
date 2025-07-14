

x=1534236469

if x>2147483647 or x<-2147483648:
    print("0")

else:
    x=str(x)
    x=list(x)

    if '-' in x:
        x.remove('-')
        x=x[::-1]
        x.insert(0,'-')

        x=str(''.join(x))
        x=str(int(x))
        if x>2147483647 or x<-2147483648:
            print("0")
        else:
            print(x)
    else:
        x=x[::-1]
        x=int(''.join(x))
        if x>2147483647 or x<-2147483648:
            print("0")
        else:
            print(x)
