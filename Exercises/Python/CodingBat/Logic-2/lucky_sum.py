def lucky_sum(a, b, c):
  n = 0
  for l in (a, b, c):
    if l == 13:
      break
    n += l
  return n
