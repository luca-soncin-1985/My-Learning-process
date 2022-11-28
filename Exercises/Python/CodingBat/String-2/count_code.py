def count_code(str):
  a = 0
  for i in range(len(str) - 3):
    if str[i:i+2] + str[i+3] == 'coe':
      a += 1
  return a