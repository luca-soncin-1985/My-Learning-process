def save(sizes, hd):
    c = 0

    for i in sizes:
        if i <= hd:
            hd -= i
            c += 1
        elif i > hd:
            break

    return c
