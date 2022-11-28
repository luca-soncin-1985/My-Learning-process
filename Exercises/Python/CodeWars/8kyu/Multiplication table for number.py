def multi_table(number):
    s = ""
    for i in range(1, 11):
        s += "{} * {} = {}\n".format(i, number, int(i) * number)
    s = s[:-1]

    return s