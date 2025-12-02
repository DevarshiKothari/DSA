# 567. Permutation in String


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ans = ""
        finalAns = False
        for right in range(len(s2)):
            ans += s2[right]
            if len(ans) > len(s1):
                ans = ans[1:]
            if len(ans) == len(s1):
                dummy = s1
                c = 0
                for i in range(len(ans)):
                    if ans[i] not in dummy:
                        break
                    if ans[i] in dummy:
                        dummy = dummy.replace(ans[i], "", 1)
                        c += 1
                if c == len(ans):
                    finalAns = True
                    break
        return finalAns


sol = Solution()
# print(sol.checkInclusion("hello", "ooolleoooleh"))
# print(sol.checkInclusion("ab", "eidboaoo"))
# print(sol.checkInclusion("ab", "eidbaooo"))
# print(sol.checkInclusion("abc", "bbbca"))
print(sol.checkInclusion("abcdxabcde", "abcdeabcdx"))
