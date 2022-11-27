def sum2(nums):
  if len(nums) == 0:
    return 0
  if len(nums) == 1:
    return nums[0]
  else:
    return sum(nums[:2])
