class Solution:
    def isPalindrome(self, s: str) -> bool:

        result = "".join( char for char in s if ("a" <= char <= "z" or "A" <= char <= "Z" or "0" <= char <= "9")).lower()
        for i in range(len(result)//2):
            if result[i] != result[-i-1]:
                return False
        return True