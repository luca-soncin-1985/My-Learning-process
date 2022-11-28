def cigar_party(cigars, is_weekend):
  if 40 <= cigars <=60:
    return True
  elif is_weekend == True and cigars >= 40:
    return True
  return False
