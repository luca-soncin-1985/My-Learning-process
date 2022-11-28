def squirrel_play(temp, is_summer):
  if is_summer == True:
    if 60 <= temp <= 100:
      return True
    return False
  elif is_summer == False and 60 <= temp <= 90:
    return True
  else:
    return False
