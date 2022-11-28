def xyz_there(str):
  for i in range(0, len(str), 1):
    if str[i] == "x" and str[i+1:i+3] == "yz" and str[i-1] != ".":
      return True
  return False