# 424. Longest Repeating Character Replacement


class Solution:
    def characterReplacement(self, s, k):
        s = s.lower()
        left = 0
        ans = 0
        freq = [0] * 26
        for right in range(len(s)):
            freq[ord(s[right]) - 97] += 1 # expansion
            max_freq = max(freq)
            total_sum = sum(freq)
            d = k - (total_sum - max_freq)

            while d < 0 and left < right: # contraction
                freq[ord(s[left]) - 97] -= 1
                left += 1
                max_freq = max(freq)
                total_sum = sum(freq)
                d = k - (total_sum - max_freq)

            if right - left + 1 > ans: # condition
                ans = right - left + 1
        return ans


sol = Solution()
print(
    sol.characterReplacement(
        "EOEMQLLQTRQDDCOERARHGAAARRBKCCMFTDAQOLOKARBIJBISTGNKBQGKKTALSQNFSABASNOPBMMGDIOETPTDICRBOMBAAHINTFLH",
        7,
    )
)
