class Solution:
    def isPalindrome(self, s: str) -> bool:

        result = ""
        for c in s:
            if c.isalnum():
                result+=c.lower()
        for i in range(len(result)//2):
            if result[i] != result[-i-1]:
                return False
        return True