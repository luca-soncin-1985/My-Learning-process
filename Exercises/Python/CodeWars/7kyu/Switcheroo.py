def switcheroo(s):
    c = {"a": "b", "b": "a"}
    x = s.maketrans(c)
    return s.translate(x)
    # your code here