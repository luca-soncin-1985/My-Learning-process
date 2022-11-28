def sum_differences_between_products_and_LCMs(pairs):
    if pairs:
        gcd = []
        for x, y in pairs:
            while (y):
                x, y = y, x % y
            gcd.append(x)

        prod = []
        for x, y in pairs:
            prod.append(x * y)

        lcm = []
        for p in range(len(prod)):
            if gcd[p] == 0:
                lcm.append(0)
            else:
                lcm.append(int(prod[p] / gcd[p]))

        result = 0
        for i in range(len(lcm)):
            result += (prod[i] - lcm[i])

        return result
    return 0