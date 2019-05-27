class Solution(object):
    def plusOne(self, digits):
        s=[str(i) for i in digits]
        r=int("".join(s))
        r+=1
        return [int(i) for i in str(r)]
        
