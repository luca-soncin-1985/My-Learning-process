def sort_my_string(s):
    e = ""
    o = ""

    for i in range(0, len(s)):
        if i % 2 == 0:
            e += s[i]
        else:
            o += s[i]

    return e + " " + o
