class Solution:
    def romanToInt(self, s: str) -> int:
        mapping={'I':1,'IV':4,'V':5,
                 'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,
                 'CD':400,'D':500,'CM':900,'M':1000}
        n=len(s)
        i=n-1
        res=0
        while i>=0:
            if s[i-1:i+1] in mapping:
                res+=mapping[s[i-1:i+1]]
                i-=2
                #print(s[i:i-2]+" "+mapping[s[i:i-2]])
            elif s[i] in mapping:
                #res+=mapping[s[i]]
                print(s[i]+" "+str(mapping[s[i]]))
                i-=1
            else:
                return -1
        return res

sol=Solution()
print(sol.romanToInt("MCMXCIV"))