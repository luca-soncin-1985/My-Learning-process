def sum67(nums):
  s = True
  sum = 0
  for i in nums:
    if i == 6:
      s = False
    elif s == True and i == 7:
      sum += i
    elif i == 7:
      s = True
    elif s == True:
      sum = sum + i

  return sum
