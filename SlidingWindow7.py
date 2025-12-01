# 567. Permutation in String


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        ans = ""
        finalAns = False
        for right in range(len(s2)):
            ans += s2[right]
            if len(ans) > len(s1):
                left += 1
                ans = ans[left:]
            if len(ans) == len(s1):
                print(ans)
                dummy = s1
                c = 0
                for i in range(len(ans)):
                    if ans[i] not in dummy:
                        break
                    if ans[i] in dummy:
                        dummy = dummy.replace(ans[i], "")
                        print("dummy is ", dummy)
                        c += 1
                if c == len(ans):
                    print(len(ans), "and c is ", c)
                    finalAns = True
                    break
            # if not finalAns:
            #     break
        return finalAns


sol = Solution()
print(sol.checkInclusion("hello", "ooolleoooleh"))
# print(sol.checkInclusion("ab", "eidboaoo"))
# print(sol.checkInclusion("ab", "eidbaooo"))
