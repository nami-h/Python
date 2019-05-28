class Solution(object):
    def checkPerfectNumber(self, num):
        l=[]
        for i in range(1, num):
            if num%i==0:
                l.append(i)
        sum=0      
        for i in l:
            sum+=i
            
        if sum==num:
            return True
        else:
            return False
