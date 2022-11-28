def flatten_and_sort(array):
    c = []

    for x in array:
        for y in x:
            c.append(y)  # when you done appending
        c.sort()  # sort it

    return c