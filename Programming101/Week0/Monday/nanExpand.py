from countSubstrings import count_substrings


def nan_expand(times):
    nan = '"'
    if times == 0:
        return '""'
    elif times == 1:
        return '"Not a NaN"'
    else:
        for i in range(0, times):
            nan += "Not a "
        nan += 'NaN"'
        return nan


def iterations_of_nan_expand(expanded):
    if expanded == "":
        return 0
    if not count_substrings(expanded, "Not a "):
        return False
    else:
        return count_substrings(expanded, "Not a ")
