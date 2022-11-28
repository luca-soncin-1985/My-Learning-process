def move_ten(st):
    d = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    s = ""
    for i in st:
        x = d.index(i)
        s += d[x + 10]
    return s