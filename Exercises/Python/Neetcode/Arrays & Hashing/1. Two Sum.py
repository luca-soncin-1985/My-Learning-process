class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, j in enumerate(nums):
            z = target - j
            if z in nums and nums.index(z) != i:
                return i, nums.index(z)
