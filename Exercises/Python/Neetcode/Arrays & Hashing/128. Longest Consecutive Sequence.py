class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = sorted(nums)
        c = 1
        d = []
        b = {1: 1}
        a = 1
        if not nums:
            return 0
        else:
            for i in range(1, len(nums)):
                if s[i] - s[i - 1] == 1:
                    b[a] += 1
                elif s[i] == s[i - 1]:
                    continue
                else:
                    a += 1
                    b[a] = 1
        z = sorted(b.values())
        return max(z)
