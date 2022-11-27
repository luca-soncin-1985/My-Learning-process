def rotate_left3(nums):
  new_list = []
  for i in range(len(nums)-1):
    new_list.append(nums[i+1])
  new_list.append(nums[0])
  return new_list