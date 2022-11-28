def number_of_rectangles(m, n):
    ooo = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            ooo += i * j

    return ooo