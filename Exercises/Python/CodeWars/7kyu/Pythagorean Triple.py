def pythagorean_triple(integers):
    a = integers[0]
    b = integers[1]
    c = integers[2]

    if a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b:
        return True
    return False