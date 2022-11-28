def bubblesort_once(l):
    m = []

    for i in l:
        if len(m) == 0:
            m.append(i)
        else:
            if i < m[-1]:
                m.append(i)
                m[-1], m[-2] = m[-2], m[-1]
            else:
                m.append(i)

    return m