def string_match(a, b):
  count = 0
  r = min(len(a), len(b))
  for i in range (0, r - 1, 1):
    if a[i:i+2] in b[i:i+2]:
      count += 1
  return count
