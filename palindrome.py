def isPalindrome(self, s: str) -> bool:
        if s==' ':
            return True
        s=s.lower()
        x=s.replace(" ", "")
        l=[]
        for let in x:
            if let.isalnum():
                l.append(let)
        print(l[::-1])
        if l==l[::-1]:
            return True
        else:
            return False
        
