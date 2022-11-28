def lone_sum(a, b, c):
    if a == b and a != c:
        return c
    elif a == c and a != b:
        return b
    elif b == c and a != b:
        return a
    elif a == b == c:
        return a - b
    else:
        return a + b + c 