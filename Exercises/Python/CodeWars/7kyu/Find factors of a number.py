def factors(x):
    if type(x) != int:
        return -1
    elif x < 1:
        return -1
    else:
        z = []
        for i in range(1, x + 1):
            if x % i == 0:
                z.append(i)
    z.sort(reverse=True)
    return z 