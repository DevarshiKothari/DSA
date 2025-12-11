# Max consecutive 1's


class Solution:
    def longestOnes(self, nums, k):
        left, count, max, ans = 0, 0, 0, 0
        for right in range(len(nums)):
            ans += 1  # expansion
            if nums[right] == 0:
                count += 1
            while count > k:  # contraction
                if nums[left] == 0:
                    count -= 1
                left += 1
                ans -= 1
            if ans > max:  # condition
                max = ans
        return max


sol = Solution()
print(sol.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(sol.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
