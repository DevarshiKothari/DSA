# Count K-Length Substrings With No Repeated Characters


class SlidingWindow:
    def operation(s: str, k: int) -> int:
        uniqueChar = set()
        i, start, ans = 0, 0, 0
        l = len(s)
        if l < k:
            return 0

        while i < l - k + 1:
            while len(uniqueChar) < k and i < l - k + 1:
                if s[start] not in uniqueChar:
                    uniqueChar.add(s[start])
                    start += 1
                else:
                    while s[start] in uniqueChar:
                        uniqueChar.remove(s[i])
                        i += 1
                    uniqueChar.add(s[start])
                    start += 1
                # print(uniqueChar, i, start)
            if len(uniqueChar) == k:
                ans += 1
                # print("Ans:", ans)
                uniqueChar.remove(s[i])
                i += 1

        print(ans)


ans = SlidingWindow
ans.operation("abcbac", 3)
