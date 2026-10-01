class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        r=[0]*(len(s)+1)
        r[0]=1
        i=-1
        while i<len(s) :
            i+=1
            if r[i]==0:
                continue 
            for w in wordDict:
                if w == s[i:i+len(w)]:
                    r[i+len(w)]=1
            
        return r[len(s)]==1
        

