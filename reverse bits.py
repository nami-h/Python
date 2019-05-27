class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        num=0
        for k in range(0, 32):
            num*=2
            if (n%2==1):
                num+=1
            n/=2
        return num
            
