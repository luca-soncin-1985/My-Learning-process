def two_highest(arg1):
    c = []
    for i in arg1:
        if i not in c:
            c.append(i) # append the i to create array if the value is not in the array already
    c.sort(reverse = True) #sort them
    return c[:2] # get the first 2