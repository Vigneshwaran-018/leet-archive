class Solution(object):
    def isHappy(self, n):

        while n!=1:
            d=[]
            while n>0:
                d.insert(0,n%10)
                n//=10
            n=0
            for i in d:
                n+=i**2
            
    isHappy(0,19)
