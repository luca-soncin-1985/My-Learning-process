def find_lowest_int(k):
    if not k:
        return 0
    else:
        k2 = k + 1
        x = 0
        c = 2

        for i in range(1, 1000000):
            n = k * i
            m = k2 * i
            z = sorted(str(n))
            y = sorted(str(m))
            if z == y:
                x = i
                return x