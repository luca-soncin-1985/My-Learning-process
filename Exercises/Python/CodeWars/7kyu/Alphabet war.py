def alphabet_war(fight):
    l = {
        "w" : 4,
        "p" : 3,
        "b" : 2,
        "s" : 1
    }
    r = {
        "m" : 4,
        "q" : 3,
        "d" : 2,
        "z" : 1
    }
    c = 0
    for i in fight:
        if i in r:
            x = r.get(i)
            c += x
        elif i in l:
            x = l.get(i)
            c -= x
    if c > 0:
        return "Right side wins!"
    elif c < 0:
        return "Left side wins!"
    else:
        return "Let's fight again!"