# LC 76: Minimum Window Substring


class Solution:
    def check(self, c, s):
        if c in s:
            return 1
        else:
            return 0

    def minWindow(self, s: str, t: str) -> str:
        left = 0
        freq1 = [0] * 52
        freq2 = [0] * 52
        ans = 0
        for i in t:
            if "A" <= i <= "Z":
                freq1[ord(i) - ord("A")] += 1
            else:
                freq1[26 + ord(i) - ord("a")] += 1

        for right in range(len(s)):
            d = self.check(s[right], t)
            if d == 1:
                if "A" <= s[right] <= "Z":
                    freq2[ord(s[right]) - ord("A")] += 1
                else:
                    freq2[26 + ord(s[right]) - ord("a")] += 1

            while freq1 == freq2:
                if right - left + 1 > ans:
                    ans = right - left + 1
                    print(s[left : right + 1])
                    # res = s[left : right + 1]
                see = True
                while see:
                    print(left, s[left], t)
                    left += 1
                    d = self.check(s[left], t)
                    print("ans", d)
                    if d == 1:
                        see = False


d = Solution()
print(d.minWindow("ADOBECODEBANC", "ABC"))
