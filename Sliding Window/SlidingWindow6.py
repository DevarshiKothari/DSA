# Fruits into baskets
from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, f: List[int]) -> int:
        left = 0
        dc = defaultdict(int)
        maxNum = 0
        for right in range(len(f)):
            dc[f[right]] += 1
            while len(dc) > 2:
                dc[f[left]] -= 1
                if dc[f[left]] == 0:
                    del dc[f[left]]
                left += 1
            if maxNum < right - left + 1:
                maxNum = right - left + 1
        return maxNum


sol = Solution()
print(sol.totalFruit([0, 1, 2, 2 ]))
