class Solution:
    def isHappy(self, n: int) -> bool:
        a=[]
        while n!=1:
            n=sum(int(i)**2 for i in str(n))
            a.append(n)
            if n in a[:-1]:
                return False
        return True
