# Longest Substring With At Most K Distinct Characters


class SlidingWindow:
    def operation(s: str, k: int) -> int:
        unique = set()
        left, right = 0, 0
        ans = 0
        sub: str = ""

        while right < len(s):
            unique.add(s[right])
            if len(unique) <= k:
                if right - left + 1 > ans:
                    ans = right - left + 1
                    sub = s[left : right + 1]
            else:
                while len(unique) > k:
                    unique.remove(s[left])
                    left += 1
            right += 1
        print(sub)


ans = SlidingWindow
ans.operation("aababbcaacc", 2)
