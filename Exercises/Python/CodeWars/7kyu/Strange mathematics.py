def strange_math(n, k):
    a = []
    for i in range(1, n + 1):
        a.append(str(i))

    a.sort()

    b = a.index(str(k))

    return b + 1

# code's too slow tho. Time: 3385ms
