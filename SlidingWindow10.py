# LC 76: Minimum Window Substring
# Not solved yet

class Solution:
    def check(self, c, f1, f2):
        if "A" <= c <= "Z":
            return (
                f1[ord(c) - ord("A")] > 0
                and f1[ord(c) - ord("A")] > f2[ord(c) - ord("A")]
            )
        else:
            return (
                f1[26 + ord(c) - ord("a")] > 0
                and f1[26 + ord(c) - ord("a")] > f2[26 + ord(c) - ord("a")]
            )

    def minWindow(self, s: str, t: str) -> str:
        left = 0
        freq1 = [0] * 52
        ans = s.length()
        # newStr = ""
        # freq2 = [0] * 52
        for i in t:
            if "A" <= i <= "Z":
                freq1[ord(i) - ord("A")] += 1
            else:
                freq1[26 + ord(i) - ord("a")] += 1
        print("freq1", freq1)
        freq2 = freq1.copy()
        c1 = t.length()
        c2 = 0

        for right in range(len(s)):
            # newStr += s[right]  # expansion
            if freq2[s[right]] > 0:
                c2 += 1
                freq2[s[right]] -= 1

            if c2 == c1:
                freq2 = freq1.copy()
                if right - left < ans:
                    ans = right - left
                    print(s[left:right])
                if freq2[s[left]] > 0:
                    freq2[s[left]] -= 1
                left += 1
                c2 -= 1
                while freq1[s[left]] == 0:
                    left += 1


d = Solution()
print(d.minWindow("ADOBECODEBANC", "ABC"))
