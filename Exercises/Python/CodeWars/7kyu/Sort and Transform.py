def sort_transform(arr):
    a = []
    for i in arr:
        a.append(chr(i))

    d = "".join(a)
    d1 = sorted(a)
    d2 = sorted(a, reverse=True)

    f = "".join(d1)
    g = "".join(d2)

    c = (d[:2] + d[-2:])
    c1 = (f[:2] + f[-2:])
    c2 = (g[:2] + g[-2:])

    zzz = (c + "-" + c1 + "-" + c2 + "-" + c1)

    return zzz