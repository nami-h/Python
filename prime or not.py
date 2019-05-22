from math import sqrt
class Solution:
    def isPrime(self, A):
        if A==1:
            return 0                   #prime
        elif A==2:
            return 1                   #not prime
        for i in range(2, int(sqrt(A))+1):
            if (A%i==0):
                return 0              #prime
        return 1                       #not prime
