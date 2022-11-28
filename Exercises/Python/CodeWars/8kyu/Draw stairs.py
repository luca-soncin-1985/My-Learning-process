def draw_stairs(n):
    c = ""

    for i in range(1, n):
        z = "I\n"
        p = " " * i
        c += z + p
    return c + "I"