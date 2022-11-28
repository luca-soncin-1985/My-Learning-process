def remove_smallest(numbers):
    z = numbers.copy()
    if not z:
        return z
    else:
        c = z.index(min(z))
        z.pop(c)
    return z

    # raise NotImplementedError("TODO: remove_smallest")