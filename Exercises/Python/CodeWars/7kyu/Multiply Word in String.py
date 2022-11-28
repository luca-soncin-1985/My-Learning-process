def modify_multiply(st, loc, num):
    x = st.split()
    y = x[loc]
    z = ""
    for i in range(num):
        z += y
        z += "-"
    return z[:-1]