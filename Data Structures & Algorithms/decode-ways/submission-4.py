class Solution:
    def numDecodings(self, s: str) -> int:
        a,b=1,0
        r=0
        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":
                r=0
            else:
                r=a
            if (i+1 < len(s) and (s[i]=="1" or s[i]=="2" and s[i+1] in "0123456")):
                r+=b
            b=a
            a=r
        return r