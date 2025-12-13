# 424. Longest Repeating Character Replacement


class Solution:
    def characterReplacement(self, s, k):
        s = s.lower()
        left = 0
        max = 0
        d = k
        freq = [0] * 26
        for right in range(len(s)):
            freq[ord(s[right]) - 97] += 1
            if s[left] != s[right]:
                d -= 1
            while d < 0 or (right - left + 1 - freq[left] > k and left != right):
                while s[left] == s[left + 1]:
                    freq[left] -= 1
                    left += 1
                freq[left] -= 1
                left += 1
                d = right - left + 1 - freq[left]
            if right - left + 1 > max:
                max = right - left + 1
        return max


sol = Solution()
print(sol.characterReplacement("ABAB", 2))
print(sol.characterReplacement("AABABBA", 1))
print(sol.characterReplacement("AAAA", 0))
print(sol.characterReplacement("AAAB", 0))
print(sol.characterReplacement("ABAA", 0))
print(sol.characterReplacement("ABCBDBFFFA", 3))
