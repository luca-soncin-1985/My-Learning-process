def reverse3(nums):
  num = []
  for i in range(len(nums)):
    num.append(nums[len(nums) - i - 1])
  return num
