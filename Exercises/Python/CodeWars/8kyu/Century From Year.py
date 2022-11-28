import math

def century(year):
    c = str(year)
    d = int(c[:2])
    e = year / 100
    return math.ceil(e)