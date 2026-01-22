class Solution:
    def prefixSum(self, nums: list) -> list:
        # if not nums or len(nums) == 1:
        #     return nums

        for i in range(len(nums)):
            if i == 0:
                continue
            nums[i] = nums[i - 1] + nums[i]
        return nums


s = Solution()
print(s.prefixSum([1, 2, 3, 4]))
print(s.prefixSum([3, 1, 2, 10, 1]))
