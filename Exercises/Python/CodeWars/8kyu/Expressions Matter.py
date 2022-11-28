def expression_matter(a, b, c):
    d = (a + b) * c
    e = a * (b + c)
    f = a + b + c
    g = a + b * c
    h = a * b * c
    i = a * b + c
    return max(d,e,f,g,h,i)