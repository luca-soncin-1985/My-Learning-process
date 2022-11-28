def well(arr):
    c = 0
    for i in arr:
        for j in i:
            if str(j).casefold() == "good":
                c += 1
    if c > 2:
        return "I smell a series!"
    elif 1 <= c <= 2:
        return "Publish!"
    else:
        return "Fail!"