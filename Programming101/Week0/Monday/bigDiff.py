
def biggest_difference(arr):
    if len(arr) == 0:
        return 0
    min = arr[0]
    max = arr[0]
    for i in range(0, len(arr)):
        if arr[i] < min:
            min = arr[i]
        if arr[i] > max:
            max = arr[i]
    return min - max
