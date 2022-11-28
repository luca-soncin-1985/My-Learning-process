def count_salutes(hallway):
    x = 0
    for i in range(0, len(hallway)-1):
        if hallway[i] == ">":
            x += hallway[i+1:].count("<")
    return x*2