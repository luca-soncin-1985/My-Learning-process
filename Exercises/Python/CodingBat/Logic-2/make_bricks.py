def make_bricks(small, big, goal):
    b = big * 5
    s = small * 1
    r = goal // 5
    m = goal % 5
    if b >= goal:
        if small >= m:
            return True
    elif b < goal:
        if s + b >= goal:
            return True
    return False