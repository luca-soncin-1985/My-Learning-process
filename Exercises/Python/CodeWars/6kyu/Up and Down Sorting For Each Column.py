def up_down_col_sort(matrix):
    a = sorted(j for x in matrix for j in x)  # sorting the matrix and store it in a var

    r = len(matrix)  # rows number, to be used as a var
    c = len(matrix[0])  # columns number, to be used as a var

    t = [[0] * c for i in range(r)]  # creates and empty array with the same "matrix" dimensions

    x = 0  # counter
    z = 0  # controller
    rev = True  # switch
    co = 0  # delimiter
    for i in range(0, c + 1):
        co += 1
        if co == c + 1:
            break  # when delimiter reaches the total column value, break
        else:
            for j in range(0, r):
                if rev == True:  # if the switch is True, adds values
                    t[j][i] = a[x]
                    x += 1
                    z += 1
                    if z % r == 0:  # if we reached the end of the rows, change the switch
                        rev = False

                elif rev == False:
                    w = r - 1 - j
                    t[w][i] = a[x]
                    x += 1
                    z += 1
                    if z % r == 0:
                        rev = True

    return t