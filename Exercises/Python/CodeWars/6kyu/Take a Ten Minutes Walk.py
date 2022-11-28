def is_valid_walk(walk):
    w = walk.count("w")
    e = walk.count("e")
    n = walk.count("n")
    s = walk.count("s")
    if (w + e + n + s) == 10 and w == e and s == n:
        return True
    return False