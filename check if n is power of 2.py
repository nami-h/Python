class Solution(object):
    def isPowerOfTwo(self, n):
        while True:
            if n < 1:
                return False
            elif n == 1:
                return True
            elif n%2 != 0:
                return False
            else:
                n = n/2
