class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = nums
        for i in range(len(nums)):
            if i == 0:
                continue
            self.nums[i] += self.nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.nums[right]

        return self.nums[right] - self.nums[left - 1]
    
