def permute_a_palindrome (input):
    s = set(input)
    c = 0
    d = []
    for i in s:
        d.append(input.count(i))
    for i in d:
        if i % 2 == 1:
            c += 1
            if len(input) % 2 == 0:
                if c % 2 != 0:
                    return False
            elif len(input) % 2 == 1:
                if c % 2 != 1:
                    return False
    return True