def string_splosion(str):
  c = ""
  for s in range(len(str)): 
    c += str[:s+1]
  return c
