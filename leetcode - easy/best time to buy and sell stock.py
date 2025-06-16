

prices=[7,1,5,3,6,4]

s=sorted(prices)

if s[::-1]==prices:
    print("0")

else:
    a=0

    for i in prices:
        for j in range(len(prices)):
            if i==prices[j]:
                continue
            print(i,j)

            if i<prices[j]:
                a=i
            
            else:
                a=prices[j]

    print(a)

    if prices.index(a)==prices[-1]:
        prices.remove(a)
        print(prices)
        for i in prices:
            for j in range(len(prices)):
                if i==prices[j]:
                    continue

                if i<prices[j]:
                    a=i
            
                else:

                    a=prices[j]
    
                    
        
    o=prices[prices.index(a):]
    for i in o:
        if i==prices[j]:
            continue

        if i>prices[j]:
            a=i
            
        else:
            a=prices[j]



    #print(prices.index(a)+1)




