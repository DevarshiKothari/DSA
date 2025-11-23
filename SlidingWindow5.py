# Longest Substring With At Most K Distinct Characters
from collections import defaultdict


class SlidingWindow:
    def operation(s: str, k: int) -> int:
        unique = defaultdict(int)
        left, right = 0, 0
        ans = 0
        sub: str = ""

        while right < len(s):
            unique[s[right]] += 1  # expansion
            if len(unique) <= k:
                if right - left + 1 > ans:
                    ans = right - left + 1
                    sub = s[left : right + 1]
            else:
                while len(unique) > k:  # shrink
                    unique[s[left]] -= 1
                    if unique[s[left]] == 0:
                        del unique[s[left]]
                    left += 1
            right += 1
        print(sub)


ans = SlidingWindow
ans.operation("aababbcaacc", 2)
