class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p=sorted(p.lower())
        s=s.lower()
        l=[]
        j=0
        count=1
        i=0
        
        for num in s:
            x=sorted(s[j:j+(len(p))])
            if x==p:
                l.append(j)
            j=j+1
            
        return l        
            
            
            
        
