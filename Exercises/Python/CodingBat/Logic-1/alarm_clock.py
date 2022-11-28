def alarm_clock(day, vacation):
  if vacation == True and 1<= day <= 5:
    return "10:00"
  elif vacation == True:
    return "off"
  elif vacation == False and 1 <= day <=5:
    return "7:00"
  else:
    return "10:00"
