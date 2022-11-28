def max_diff(lst):
    if len(lst) <= 1:
        return 0
    else:
        return max(lst) - min(lst)