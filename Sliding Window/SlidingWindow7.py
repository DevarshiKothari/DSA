# 567. Permutation in String


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0

        freqA1 = [0] * 26
        freqA2 = [0] * 26

        for c in s1:
            freqA1[ord(c) - 97] += 1  # frequency array for s1

        for right in range(len(s2)):
            freqA2[ord(s2[right]) - 97] += 1  # expansion

            if (right - left + 1) > len(s1):  # contraction
                freqA2[ord(s2[left]) - 97] -= 1
                left += 1

            if freqA1 == freqA2:  # condition
                # print(freqA1)
                return True

        return False


sol = Solution()
print(sol.checkInclusion("hello", "ooolleoooleh"))
print(sol.checkInclusion("ab", "eidboaoo"))
print(sol.checkInclusion("ab", "eidbaooo"))
print(sol.checkInclusion("abc", "bbbca"))
print(sol.checkInclusion("abcdxabcde", "abcdeabcdx"))
