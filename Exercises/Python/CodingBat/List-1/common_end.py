def common_end(a, b):
  if len(a) > 0 and len(b) > 0 and a[0] == b[0] or a[-1] == b[-1]:
    return True
  else:
    return False
