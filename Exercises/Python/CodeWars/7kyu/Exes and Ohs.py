def xo(s):
    if not xo:
        return False
    else:
        if not s:
            return True
        else:
            a = s.lower()
            for i in a:
                if a.count("x") == a.count("o"):
                    return True
                elif a.count("x") == 0 and a.count("o") == 0:
                    return True
                else:
                    False
            return False