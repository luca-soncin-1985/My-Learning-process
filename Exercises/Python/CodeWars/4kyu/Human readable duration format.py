def format_duration(seconds):
    if seconds == 0:
        return "now"
    else:
        y = (seconds // 31536000)
        d = (seconds // 86400) % 365
        h = (seconds // 3600) % 24
        m = (seconds // 60) % 60
        s = seconds % 60
        yy = ""
        dd = ""
        hh = ""
        mm = ""
        ss = ""

        if y > 0:
            if y == 1:
                yy += "1 year"
            else:
                yy += "{} years".format(y)
        if d > 0:
            if y > 0:
                dd += ", "
            if d == 1:
                dd += "1 day"
            else:
                dd += "{} days".format(d)
        if h > 0:
            if y > 0 and d == 0:
                hh += ", "
            elif d > 0:
                hh += ", "
            if h == 1:
                hh += "1 hour"
            else:
                hh += "{} hours".format(h)
        if m > 0:
            if y > 0 and d == 0 and h == 0:
                mm += ", "
            elif d > 0 and h == 0:
                mm += ", "
            elif h > 0:
                mm += ", "
            if m == 1:
                mm += "1 minute"
            else:
                mm += "{} minutes".format(m)
        if s > 0:
            if y > 0 and d == 0 and h == 0 and m == 0:
                ss += ", "
            elif d > 0 and h == 0 and m == 0:
                ss += ", "
            elif h > 0 and m == 0:
                ss += ", "
            elif m > 0:
                ss += ", "
            if s == 1:
                ss += "1 second"
            else:
                ss += "{} seconds".format(s)
    zz = yy + dd + hh + mm + ss
    f = ' and '.join(zz.rsplit(', ', 1))
    return f