def end_other(a, b):
  an = a.lower()
  bn = b.lower()
  if an.endswith(bn) == True or bn.endswith(an) == True:
    return True
  return False