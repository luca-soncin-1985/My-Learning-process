def is_sorted_and_how(arr):
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return "yes, descending"
        else:
            return "yes, ascending"

    else:
        neg = 0
        pos = 0
        for c in range(0, len(arr) - 1):
            if arr[c] < arr[c + 1]:
                neg += 1
            elif arr[c] > arr[c + 1]:
                pos += 1

        if neg == len(arr) - 1:
            return "yes, ascending"
        elif pos == len(arr) - 1:
            return "yes, descending"
        else:
            return "no"