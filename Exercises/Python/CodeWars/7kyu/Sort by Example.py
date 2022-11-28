def example_sort(arr, example_arr):
    l = []
    for j in range(0, len(example_arr)):
        u = example_arr[j]
        for i in range(0, len(arr)):
            if arr[i] == u:
                l.append(arr[i])
    return l
# this damn kata costed me 8 hours >:(