def alphabet_position(text):
    a = 'abcdefghijklmnopqrstuvwxyz'
    d = []
    for i in text.casefold():
        if i in a:
            d.append(str(a.index(i) + 1))
    return " ".join(d)