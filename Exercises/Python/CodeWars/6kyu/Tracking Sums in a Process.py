def track_sum(arr):
    a = []
    for i in arr:
        a.append(i)

    b = list(set(a))
    b.sort(reverse=True)

    c = []
    for i in range(0, len(b) - 1):
        c.append(b[i] - b[i + 1])

    d = []
    for i in c:
        if i not in d:
            d.append(i)

    return [[sum(a), sum(b), sum(c), sum(d)], d]