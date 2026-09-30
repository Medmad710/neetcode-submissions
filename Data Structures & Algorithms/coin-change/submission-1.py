class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        r=[-1]*(amount+1)
        r[0]=0
        for i in range(1,amount+1):
            r[i] = 1+min([r[i-c] for c in coins if i >= c and r[i-c] >= 0], default=-2)
        return r[amount]