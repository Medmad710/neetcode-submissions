


class Solution:

  def maxArea(self, height: List[int]) -> int:
    res = 0  #[cite: 1]
    l, r = 0, len(height) - 1  #[cite: 1]

    while l < r:  #[cite: 1]
      area = (r - l) * min(height[l], height[r])  #[cite: 1]
      res = max(res, area)  #[cite: 1]

      if height[l] < height[r]:  #[cite: 1]
        l += 1  #[cite: 1]
      else:
        r -= 1  #[cite: 1]

    return res  #[cite: 1]