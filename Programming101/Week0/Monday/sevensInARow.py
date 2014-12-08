def sevens_in_a_row(arr, n):
    count = 0
    for item in range(0, len(arr)):
        if arr[item] == 7:
            count += 1
        else:
            count = 0
        if count == n:
            return True
    return False
